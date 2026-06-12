# Real-Time 音频 Processing

> Batch pipelines process a file. Real-time pipelines process the next 20 milliseconds before the next 20 arrive. Every conversational AI, broadcast studio,与telephony bot lives与dies by this latency budget.

**类型：** 构建
**语言：** Python
**前置知识：** Phase 6 · 02 (声谱图), Phase 6 · 04 (ASR), Phase 6 · 07 (TTS)
**时间：** 约 75 minutes

## 学习目标
- 理解 Real-Time 音频 Processing 在本阶段课程中的作用。
- 把核心概念映射到可运行代码、测验和课程产物。
- 保留英文术语、命令、路径和 API 名称，方便和原文对照。

## 中文导读

本课是 Phase 6「语音与音频」的第 11 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Real-Time Audio Processing

> Batch pipelines process a file. Real-time pipelines process the next 20 milliseconds before the next 20 arrive. Every conversational AI, broadcast studio, and telephony bot lives and dies by this latency budget.

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 6 · 02 (Spectrograms), Phase 6 · 04 (ASR), Phase 6 · 07 (TTS)
**Time:** ~75 minutes

## The Problem

You want a voice assistant that feels alive. Human conversational turn-taking latency is ~230 ms (silence-to-response). Anything above 500 ms feels robotic; above 1500 ms feels broken. The budget for a full **hear → understand → respond → speak** loop in 2026 is:

| Stage | Budget |
|-------|--------|
| Mic → buffer | 20 ms |
| VAD | 10 ms |
| ASR (streaming) | 150 ms |
| LLM (first token) | 100 ms |
| TTS (first chunk) | 100 ms |
| Render → speaker | 20 ms |
| **Total** | **~400 ms** |

Moshi (Kyutai, 2024) clocked 200 ms full-duplex. GPT-4o-realtime (2024) clocks ~320 ms. Cascaded pipelines in 2022 shipped at 2500 ms. The 10× improvement came from three techniques: (1) streaming everywhere, (2) asynchronous pipelining with partial results, (3) interruptible generation.

## The Concept

![Streaming audio pipeline with ring buffer, VAD gate, interruption](../assets/real-time.svg)

**Frame / chunk / window.** Real-time audio flows as fixed-size blocks. Common choice: 20 ms (320 samples at 16 kHz). Everything downstream must keep up with this cadence.

**Ring buffer.** Fixed-size circular buffer. Producer thread writes new frames, consumer thread reads. Prevents allocations in the hot path. Size ≈ maximum-latency × sample-rate; a 2-second 16 kHz ring = 32,000 samples.

**VAD (Voice Activity Detection).** Gates downstream work when nobody is speaking. Silero VAD 4.0 (2024) runs <1 ms per 30 ms frame on CPU. `webrtcvad` is the older alternative.

**Streaming ASR.** Models that emit partial transcripts as audio arrives. Parakeet-CTC-0.6B in streaming mode (NeMo, 2024) does 2–5% WER at 320 ms latency. Whisper-Streaming (Macháček et al., 2023) chunks Whisper for near-streaming at ~2 s latency.

**Interruption.** When the user speaks while the assistant is talking, you must (a) detect the barge-in, (b) stop the TTS, (c) discard the remaining LLM output. All within 100 ms, or the user perceives deaf assistant.

**WebRTC Opus transport.** 20 ms frames, 48 kHz, adaptive bitrate 8–128 kbps. Standard for browser and mobile. LiveKit, Daily.co, Pion are the 2026 stacks for building voice apps.

**Jitter buffer.** Network packets arrive out of order / late. The jitter buffer reorders and smooths; too small → audible gaps, too large → latency. 60–80 ms typical.

### Common gotchas

- **Thread contention.** Python's GIL + heavy models can starve the audio thread. Use a C-callback audio library (sounddevice, PortAudio) and keep Python off the hot path.
- **Sample-rate conversion latency.** Resampling inside the pipeline adds 5–20 ms. Either resample upfront or use a zero-latency resampler (PolyPhase, `soxr_hq`).
- **TTS priming.** Even fast TTS like Kokoro has a 100–200 ms warm-up on first request. Cache model + warm it with a dummy run before the first real turn.
- **Echo cancellation.** Without AEC, TTS output re-enters the mic and triggers ASR on the bot's own voice. WebRTC AEC3 is the open-source default.

## Build It

### Step 1: ring buffer

```python
import collections

class RingBuffer:
    def __init__(self, capacity):
        self.buf = collections.deque(maxlen=capacity)
    def write(self, frame):
        self.buf.extend(frame)
    def read(self, n):
        return [self.buf.popleft() for _ in range(min(n, len(self.buf)))]
    def level(self):
        return len(self.buf)
```

Capacity determines max buffering latency. 32,000 samples at 16 kHz = 2 s.

### Step 2: VAD gate

```python
def simple_energy_vad(frame, threshold=0.01):
    return sum(x * x for x in frame) / len(frame) > threshold ** 2
```

Replace with Silero VAD in production:

```python
import torch
vad, _ = torch.hub.load("snakers4/silero-vad", "silero_vad")
is_speech = vad(torch.tensor(frame), 16000).item() > 0.5
```

### Step 3: streaming ASR

```python
# Parakeet-CTC-0.6B streaming via NeMo
from nemo.collections.asr.models import EncDecCTCModelBPE
asr = EncDecCTCModelBPE.from_pretrained("nvidia/parakeet-ctc-0.6b")
# chunk_ms=320 ms, look_ahead_ms=80 ms
for chunk in audio_stream():
    partial_text = asr.transcribe_streaming(chunk)
    print(partial_text, end="\r")
```

### Step 4: interruption handler

```python
class Dialog:
    def __init__(self):
        self.tts_task = None

    def on_user_speech(self, frame):
        if self.tts_task and not self.tts_task.done():
            self.tts_task.cancel()   # barge-in
        # then feed to streaming ASR

    def on_final_user_utterance(self, text):
        self.tts_task = asyncio.create_task(self.reply(text))

    async def reply(self, text):
        async for tts_chunk in llm_then_tts(text):
            speaker.write(tts_chunk)
```

Hinges on async I/O and cancellable TTS streaming. WebRTC peerconnection.stop() on the audio track is the canonical way.

## Use It

The 2026 stack:

| Layer | Pick |
|-------|------|
| Transport | LiveKit (WebRTC) or Pion (Go) |
| VAD | Silero VAD 4.0 |
| Streaming ASR | Parakeet-CTC-0.6B or Whisper-Streaming |
| LLM first-token | Groq, Cerebras, vLLM-streaming |
| Streaming TTS | Kokoro or ElevenLabs Turbo v2.5 |
| Echo cancel | WebRTC AEC3 |
| End-to-end native | OpenAI Realtime API or Moshi |

## Pitfalls

- **Buffering 500 ms to be safe.** The buffer *is* your latency floor. Shrink it.
- **Not pinning threads.** Audio callback on a priority-lower-than-UI thread = glitches under load.
- **TTS chunks too small.** Sub-200 ms chunks make vocoder artifacts audible. 320 ms chunks are the sweet spot.
- **No jitter buffer.** Real networks are jittery; without smoothing you get pops.
- **Single-shot error handling.** Audio pipelines must be crash-proof. One exception kills the session.

## Ship It

Save as `outputs/skill-realtime-designer.md`. Design a real-time audio pipeline with concrete latency budgets per stage.

## Exercises

1. **Easy.** Run `code/main.py`. Simulates a ring buffer + energy VAD; prints stage latencies for a fake 10-second stream.
2. **Medium.** Using `sounddevice`, build a passthrough loop that processes your mic in 20 ms frames and prints VAD state at each frame.
3. **Hard.** Build a full duplex echo test with `aiortc`: browser → WebRTC → Python → WebRTC → browser. Measure glass-to-glass latency with a 1 kHz pulse.

## Key Terms

| Term | What people say | What it actually means |
|------|-----------------|-----------------------|
| Ring buffer | The circular queue | Fixed-size, lock-free (or SPSC-locked) FIFO for audio frames. |
| VAD | Silence gate | Model or heuristic marking speech vs non-speech. |
| Streaming ASR | Real-time STT | Emits partial text as audio arrives; bounded lookahead. |
| Jitter buffer | Network smoother | Queue reordering out-of-order packets; 60–80 ms typical. |
| AEC | Echo cancellation | Subtracts speaker-to-mic feedback path. |
| Barge-in | User interrupt | System detects user speech mid-TTS; must cancel playback. |
| Full duplex | Simultaneous both ways | User and bot can talk at the same time; Moshi is full duplex. |

## Further Reading

- [Macháček et al. (2023). Whisper-Streaming](https://arxiv.org/abs/2307.14743) — chunked near-streaming Whisper.
- [Kyutai (2024). Moshi](https://kyutai.org/Moshi.pdf) — full-duplex 200 ms latency.
- [LiveKit Agents framework (2024)](https://docs.livekit.io/agents/) — production audio agent orchestration.
- [Silero VAD repo](https://github.com/snakers4/silero-vad) — sub-1 ms VAD, Apache 2.0.
- [WebRTC AEC3 paper](https://webrtc.googlesource.com/src/+/main/modules/audio_processing/aec3/) — echo cancellation under open source.

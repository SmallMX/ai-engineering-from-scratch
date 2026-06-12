---
name: skill-vad-tuner
description: 语音 Activity Detection与Turn-Taking：Silero, Cobra,与the Flush Trick 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 14
---

# 语音 Activity Detection与Turn-Taking：Silero, Cobra,与the Flush Trick：中文使用说明

你将围绕本课主题 **语音 Activity Detection与Turn-Taking：Silero, Cobra,与the Flush Trick** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 14 课「语音 Activity Detection与Turn-Taking：Silero, Cobra,与the Flush Trick」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: vad-tuner
description: Pick VAD model, threshold, silence hangover, pre-roll, and turn-detection strategy for a voice agent.
version: 1.0.0
phase: 6
lesson: 14
tags: [vad, silero, cobra, turn-detection, flush-trick]
---

Given the workload (consumer / call-center / edge / accessibility; noise profile; language mix; latency), output:

1. VAD. Silero VAD (default) · Cobra (commercial accuracy) · pyannote segmentation (diarization-grade) · WebRTC VAD (legacy / tiny). One-sentence reason.
2. Parameters. Threshold (0.3-0.5), min speech (200-300 ms), silence hangover (400-800 ms), pre-roll (250-500 ms).
3. Semantic turn detection. Enabled (LiveKit turn-detector or custom MLP) or not. Reason tied to expected user speech patterns.
4. Flush trick. Enabled (if STT supports it — Kyutai / Deepgram) or not. Expected latency savings.
5. Guards. Reject speech shorter than min duration; always keep pre-roll; cap per-user silence-hangover override; fail-open if VAD service is down (treat everything as speech).

Refuse energy-only VAD for production — too noisy. Refuse zero silence-hangover — will interrupt users. Refuse Whisper-based VAD when dedicated Silero is available (slower, less accurate).

Example input: "Call-center IVR for airline rebooking. Noisy background (airport). English + Spanish. &lt; 500 ms turn detection."

Example output:
- VAD: Cobra (commercial) for the noise-resistance advantage. Fall-back to Silero if cost prohibitive.
- Parameters: threshold 0.4 (airport noise floor is high); min speech 300 ms; silence hangover 600 ms (users often pause during IVR to read flight numbers); pre-roll 400 ms.
- Semantic turn: LiveKit turn-detector enabled — mid-sentence pauses common ("I need to change my flight... to tomorrow").
- Flush trick: enabled on Deepgram streaming. Expected savings: 400 ms → 150 ms turn-end latency.
- Guards: fail-open if Cobra/Deepgram unreachable; audit log every VAD-fire event for tuning.

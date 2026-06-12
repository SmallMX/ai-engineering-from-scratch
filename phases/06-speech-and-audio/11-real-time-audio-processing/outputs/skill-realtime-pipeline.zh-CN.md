---
name: skill-realtime-pipeline
description: Real-Time 音频 Processing 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 11
---

# Real-Time 音频 Processing：中文使用说明

你将围绕本课主题 **Real-Time 音频 Processing** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 11 课「Real-Time 音频 Processing」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: realtime-voice-pipeline
description: Pick transport, VAD, streaming STT, LLM, streaming TTS, and orchestration for a target end-to-end latency.
version: 1.0.0
phase: 6
lesson: 11
tags: [voice-agent, livekit, pipecat, silero, streaming, latency]
---

Given the target (latency P50/P95, language, channel, offline vs cloud, call volume), output:

1. Transport. WebRTC (LiveKit / Daily) · WebSocket · SIP trunking (Twilio / Telnyx). Reason tied to jitter tolerance + use case.
2. VAD + turn-taking. Silero VAD (open, 99.5% TPR) · Cobra (commercial) · LiveKit turn-detector. Threshold, min speech duration, silence hang-over.
3. Streaming STT. Parakeet TDT (fastest open) · Kyutai STT (with flush trick) · Deepgram Nova-3 (API, ~150 ms) · Whisper-streaming. Reason.
4. LLM + streaming. Pin the first 20 tokens before TTS kicks in. Model + streaming config + guardrails for prompt injection.
5. Streaming TTS. Kokoro-82M (~100 ms TTFA) · Orpheus · Cartesia Sonic · ElevenLabs Turbo. Voice-pack or cloning guard (Lesson 8).
6. Orchestration. LiveKit Agents · Pipecat · Vapi · Retell · custom Rust. Reason tied to team skills + scale.
7. Observability. P50/P95/P99 per-stage histograms; false-positive interruption rate; drop-call rate; WER on call samples.

Refuse deploys that buffer entire utterances before STT. Refuse TTS that does not stream. Refuse evaluation by average latency — require P95. Refuse managed platforms (Vapi / Retell) for &gt; 100k minutes/month without a cost-comparison to build-your-own.

Example input: "Voice agent for car insurance quoting. &lt; 500 ms P95. English, US. 50k minutes/week. Compliance: HIPAA-adjacent (no PII in logs)."

Example output:
- Transport: LiveKit Agents + Twilio SIP. Proven at call-center scale, HIPAA-mode opt-in.
- VAD: Silero VAD @ threshold 0.45, min speech 220 ms, silence hang-over 400 ms. LiveKit turn-detector overlay.
- STT: Deepgram Nova-3 English (~150 ms P95); fall-back to Parakeet-TDT if on-prem audit required.
- LLM: GPT-4o streaming via OpenAI realtime API; guard against prompt injection with a post-filter; pin first 20 tokens to TTS.
- TTS: Cartesia Sonic 2 (~150 ms TTFA, voice cloning not used — predefined voice).
- Orchestration: LiveKit Agents. Observability via Hamming AI for production.
- Logs: strip CVV / SSN / DOB with a regex + NER pass before persistence. Retain 30 days.

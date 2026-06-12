---
name: skill-voice-pipeline
description: 语音 智能体：Pipecat与LiveKit 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 22
---

# 语音 智能体：Pipecat与LiveKit：中文使用说明

你将围绕本课主题 **语音 智能体：Pipecat与LiveKit** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 22 课「语音 智能体：Pipecat与LiveKit」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: voice-pipeline
description: Scaffold a Pipecat-shaped voice pipeline (VAD + STT + LLM + TTS + transport) with barge-in, confidence gating, and latency budget enforcement.
version: 1.0.0
phase: 14
lesson: 22
tags: [voice, pipecat, livekit, webrtc, latency]
---

Given a voice product spec (language, transport, providers), scaffold a frame-based pipeline.

Produce:

1. `Frame` type with `kind`, `payload`, `direction` (downstream / upstream).
2. Processors: `VAD`, `STT`, `LLM`, `TTS`, `Transport`. Each with `process(frame)`.
3. `link()` helper chaining processors forward and backward.
4. Cancel frame handling: UPSTREAM path from transport to TTS to LLM to STT, dropping pending work at each stage.
5. Observers: per-stage latency metrics; emit an OTel span per frame crossing a processor (Lesson 23).
6. Confidence gate on STT: below threshold, emit a "please repeat" text frame instead of transcript.

Hard rejects:

- Pipeline without UPSTREAM handling. Barge-in is not optional for voice.
- LLM calls without streaming. First-token latency dominates; must be streamed.
- Confidence-blind STT. Feeding wrong transcripts to the LLM produces wrong replies.

Refusal rules:

- If end-to-end latency exceeds 1500ms on a cold run, refuse to ship. Optimize the chain or use a MultimodalAgent (LiveKit direct-audio).
- If the product is telephony-first and the pipeline has no SIP adapter, refuse. Route through LiveKit SIP or a platform (Vapi/Retell).
- If the product carries PII audio without encryption in transit, refuse.

Output: `frames.py`, `processors.py`, `pipeline.py`, `observers.py`, `README.md` explaining the latency budget, barge-in design, and transport choice. End with "what to read next" pointing to Lesson 23 (OTel), Lesson 24 (observability backends), or LiveKit docs for WebRTC specifics.

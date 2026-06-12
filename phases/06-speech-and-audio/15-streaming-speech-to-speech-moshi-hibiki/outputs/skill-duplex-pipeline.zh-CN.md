---
name: skill-duplex-pipeline
description: Streaming 语音-to-语音：Moshi, Hibiki,与Full-Duplex Dialogue 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 15
---

# Streaming 语音-to-语音：Moshi, Hibiki,与Full-Duplex Dialogue：中文使用说明

你将围绕本课主题 **Streaming 语音-to-语音：Moshi, Hibiki,与Full-Duplex Dialogue** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 15 课「Streaming 语音-to-语音：Moshi, Hibiki,与Full-Duplex Dialogue」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: duplex-pipeline
description: Pick full-duplex (Moshi) vs pipeline (VAD + STT + LLM + TTS) architecture for a voice-agent workload.
version: 1.0.0
phase: 6
lesson: 15
tags: [moshi, hibiki, full-duplex, voice-agent, streaming]
---

Given the workload (latency target, tool-calling needs, language coverage, hardware budget, cloud vs edge), output:

1. Architecture. Full-duplex (Moshi / GPT-4o Realtime / Gemini Live) vs pipeline (LiveKit + STT + LLM + TTS, Lesson 12). One-sentence reason.
2. Model. Moshi · Hibiki · Hibiki-Zero · Sesame CSM · GPT-4o Realtime · Gemini 2.5 Live · traditional pipeline. Reason.
3. Scale. Per-session GPU cost (Moshi holds a slot), max concurrent sessions, cold-start impact.
4. Tool-calling path. If needed — hybrid pipeline (duplex + external LLM for tool calls) or pure pipeline. Explain trade-off.
5. Language coverage. Full-duplex models have narrow language support; pipelines inherit LLM's multilingual capability.

Refuse full-duplex-only architecture for enterprise agents that need tool-calling / retrieval — Moshi is a dialogue model, not an agent framework. Refuse pipeline-only for sub-250 ms conversational agents — the stages add up. Refuse Moshi for &gt; 4 concurrent sessions on one GPU — hits contention.

Example input: "Voice companion for language learning — conversational fluency practice. English + French. &lt; 250 ms responsiveness. 10k daily actives."

Example output:
- Architecture: full-duplex (Moshi). Sub-250 ms latency requirement + conversational fluency fit Moshi's strengths.
- Model: Moshi. EN + FR both well-supported. CC-BY 4.0 license.
- Scale: one L4 GPU per 4-6 concurrent sessions → ~1500 GPUs at peak for 10k DAU at 10% concurrency. Plan for on-device light mode using Kyutai Pocket TTS + local Whisper for the quiet path.
- Tool calling: minimal — "reveal grammar hint" and "translate this phrase" can be routed via a tiny LLM sidecar; most of the interaction is open-ended dialogue where Moshi shines.
- Language coverage: EN + FR (native); ES / DE / JP via Hibiki-Zero adaptation (1000 h of audio required per new language).

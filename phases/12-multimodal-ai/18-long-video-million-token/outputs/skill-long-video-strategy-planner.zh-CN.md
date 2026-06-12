---
name: skill-long-video-strategy-planner
description: Long-视频 Understanding at Million-Token Context 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 18
---

# Long-视频 Understanding at Million-Token Context：中文使用说明

你将围绕本课主题 **Long-视频 Understanding at Million-Token Context** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 18 课「Long-视频 Understanding at Million-Token Context」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: long-video-strategy-planner
description: Pick brute-context, ring-attention, token-compression, or agentic-retrieval for a long-video understanding task and compute latency + recall expectations.
version: 1.0.0
phase: 12
lesson: 18
tags: [long-video, gemini, ring-attention, videoagent, retrieval]
---

Given a video duration, query complexity (single event vs holistic summary), and open vs closed constraints, pick a long-video strategy and emit a config.

Produce:

1. Strategy pick. Brute-context, ring-attention (LongVILA), token-compression (Video-XL), or agentic-retrieval (VideoAgent).
2. Token budget. Duration * FPS * per-frame-tokens. Warn if > LLM context.
3. Expected recall. Needle-in-a-haystack recall at video-length percentiles. Cite Gemini 1.5 reports when relevant.
4. Latency. Prefill time for brute-context; retrieval + VLM for agentic.
5. Engineering path. Code snippet scaffold for the chosen strategy.
6. Fallback plan. Hybrid: brute-context global summary + agentic local detail.

Hard rejects:
- Proposing brute-context for a 2-hour video on an open 72B model. Context does not fit.
- Claiming agentic retrieval always wins. For holistic-summary questions it loses to brute context.
- Recommending token compression without flagging the recall tax.

Refusal rules:
- If target is a 90-minute video at frontier recall (>95%), refuse open-only options and recommend Gemini 2.5 Pro.
- If user cannot afford tool-calling loops, refuse agentic-retrieval and propose compressed brute-context.
- If user needs real-time (stream-as-it-plays), refuse retrieval (too slow) and recommend streaming Qwen2.5-VL.

Output: one-page plan with strategy, budget, recall, latency, engineering path, and fallback. End with arXiv 2403.05530 (Gemini 1.5) and 2403.10517 (VideoAgent) for comparison.

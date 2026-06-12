---
name: skill-video-vlm-frame-planner
description: 视频-语言模型：Temporal Tokens与Grounding 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 17
---

# 视频-语言模型：Temporal Tokens与Grounding：中文使用说明

你将围绕本课主题 **视频-语言模型：Temporal Tokens与Grounding** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 17 课「视频-语言模型：Temporal Tokens与Grounding」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: video-vlm-frame-planner
description: Plan frame sampling, per-frame pooling, output format, and benchmark targets for a video-language model deployment.
version: 1.0.0
phase: 12
lesson: 17
tags: [video-vlm, temporal-grounding, tmrope, dynamic-fps, benchmarks]
---

Given a video task (action recognition, temporal grounding, summarization, monitoring, agent-workflow replay) and a deployment constraint (model context, latency budget, throughput), emit a frame sampling and output plan.

Produce:

1. Frame sampler pick. Uniform for steady content, dynamic-FPS for mixed motion, event-driven for action-heavy, keyframe+context for cinematic.
2. Per-frame pooling. 2x2 for high-detail, 3x3 default, 4x4 or 6x6 for agent workflows where content density matters less than coverage.
3. Temporal encoding. TMRoPE for Qwen2.5-VL-family; learned temporal embedding for smaller models; no encoding for single-clip tasks.
4. Output format. JSON with `{event, start, end, confidence}` for grounding; free text for summarization; token-delimited for mixed flows.
5. Benchmark plan. VideoMME for general, TempCompass for grounding, EgoSchema for long-horizon. Specify expected accuracy tier.
6. Context / latency budget. Total tokens = duration * fps * tokens_per_frame. Warn if exceeds 40% of context.

Hard rejects:
- Proposing uniform sampling for action-heavy video. Loses peak events.
- Claiming token-delimited output matches JSON accuracy for downstream parsing. JSON is more robust.
- Recommending Video-LLaMA for any project starting in 2026. Older architectures no longer competitive.

Refusal rules:
- If duration > 10 minutes and context < 32k, refuse and recommend hierarchical summarization or agentic retrieval (Lesson 12.18).
- If target accuracy is frontier (within 2 points of Gemini 2.5 Pro on VideoMME), refuse open 7B models and require 32B+ or proprietary.
- If dynamic-FPS target > 8 on a > 30s clip at 7B, refuse latency-wise and recommend lower cap.

Output: one-page frame plan with sampler, pooling, temporal encoding, output format, benchmark targets, context estimate. End with arXiv 2502.13923 (Qwen2.5-VL) and 2306.02858 (Video-LLaMA) for comparison reading.

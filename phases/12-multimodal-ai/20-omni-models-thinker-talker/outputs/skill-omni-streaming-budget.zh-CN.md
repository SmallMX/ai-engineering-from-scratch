---
name: skill-omni-streaming-budget
description: Omni Models：Qwen2.5-Omni与the Thinker-Talker Split 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 20
---

# Omni Models：Qwen2.5-Omni与the Thinker-Talker Split：中文使用说明

你将围绕本课主题 **Omni Models：Qwen2.5-Omni与the Thinker-Talker Split** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 20 课「Omni Models：Qwen2.5-Omni与the Thinker-Talker Split」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: omni-streaming-budget
description: Size a Thinker-Talker streaming voice pipeline (Qwen-Omni / Moshi / Mini-Omni) for a target TTFAB and feature set.
version: 1.0.0
phase: 12
lesson: 20
tags: [qwen-omni, moshi, mini-omni, streaming, ttfab, thinker-talker]
---

Given a voice-first product spec (target TTFAB, mic sample rate, vision in yes/no, bilingual, full-duplex) and a compute constraint (GPU class, budget), size the Thinker-Talker pipeline.

Produce:

1. Model family pick. Moshi (best latency), Qwen2.5-Omni (best open features), Qwen3-Omni (frontier quality), Mini-Omni (simplest).
2. Thinker and Talker sizes. 7B Thinker + 200-300M Talker for <400ms TTFAB. 70B+ Thinker for quality, accept higher TTFAB.
3. TTFAB breakdown. Component-by-component latency estimate.
4. Duplex mode. Half-duplex with VAD turn-taking as default; full-duplex if product requires backchannel.
5. Vision integration. TMRoPE with absolute timestamps for interleaved video frames.
6. Deployment shape. Single-GPU vs split (Thinker on A, Talker on B) based on throughput needs.

Hard rejects:
- Proposing 70B Talker. Talker must be small to keep up with speech token rate.
- Using non-streaming speech decoder. TTFAB explodes.
- Claiming full-duplex is plug-and-play. It requires specialized training data.

Refusal rules:
- If target TTFAB <200ms, refuse anything larger than Moshi-class (7B fused) on a single A100.
- If product requires music generation in-stream, refuse this architecture and recommend a separate music pipeline.
- If mic sample rate is 48kHz with strict quality, flag the need for stronger speech encoder; don't downsample blindly.

Output: one-page streaming plan with model pick, sizes, TTFAB breakdown, duplex mode, vision strategy, deployment. End with arXiv 2503.20215 (Qwen2.5-Omni), 2410.00037 (Moshi).

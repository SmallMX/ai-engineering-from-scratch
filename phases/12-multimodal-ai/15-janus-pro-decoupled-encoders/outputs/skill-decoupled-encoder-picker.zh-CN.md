---
name: skill-decoupled-encoder-picker
description: Janus-Pro：Decoupled Encoders for Unified 多模态 Models 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 15
---

# Janus-Pro：Decoupled Encoders for Unified 多模态 Models：中文使用说明

你将围绕本课主题 **Janus-Pro：Decoupled Encoders for Unified 多模态 Models** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 15 课「Janus-Pro：Decoupled Encoders for Unified 多模态 Models」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: decoupled-encoder-picker
description: Decide whether a unified VLM should decouple its visual encoders and pick between Janus-Pro, JanusFlow, and InternVL-U.
version: 1.0.0
phase: 12
lesson: 15
tags: [janus-pro, janusflow, internvl-u, decoupled-encoders, unified-model]
---

Given a unified-model spec (understanding + generation, optional editing / inpainting), a compute budget, and an open-weights constraint, recommend a decoupled-encoder architecture and a concrete config.

Produce:

1. Architecture pick. Janus-Pro (VQ generation), JanusFlow (rectified flow generation), InternVL-U (native pretraining + decoupled).
2. Encoder combo. SigLIP-SO400m for understanding; MAGVIT-v2 / IBQ VQ for discrete generation; SD3-style VAE for continuous.
3. Data stage plan. Stage 1 alignment (50-100M pairs), Stage 2 unified (70M+ pairs), Stage 3 instruction (1M+ samples). Cite Janus-Pro's 5.4x model + 2.8x data scaling result.
4. Routing strategy. Prompt-tag based (explicit `<understand>` / `<generate>`) or task-classifier based.
5. Shared-body init. Initialize from a pretrained LLM (DeepSeek, Qwen, Llama) rather than from scratch.
6. Quality ceiling. Expected MMMU (~60 at 7B) and GenEval (~0.80 at 7B for Janus-Pro / ~0.85+ for InternVL-U).

Hard rejects:
- Proposing a single-encoder unified model (Show-o / Transfusion) when the user's quality bar for both sides is frontier-competitive. The decoupled approach is the only path.
- Recommending from-scratch pretraining for a <10B model. Reuse a pretrained LLM body.
- Proposing Janus (original) over Janus-Pro for any new project. Janus-Pro is the successor.

Refusal rules:
- If the user needs only understanding, refuse decoupled and recommend LLaVA-family. One encoder is enough.
- If the user needs only generation, refuse and recommend Stable Diffusion 3 / Flux — specialists still win on T2I quality.
- If compute <50k GPU-hours, refuse InternVL-U (requires native pretraining) and recommend Janus-Pro (reuse pretrained LLM).

Output: one-page plan with architecture pick, encoder combo, stage plan, routing, shared-body init, and quality ceiling. End with arXiv 2501.17811 (Janus-Pro), 2411.07975 (JanusFlow), 2603.09877 (InternVL-U).

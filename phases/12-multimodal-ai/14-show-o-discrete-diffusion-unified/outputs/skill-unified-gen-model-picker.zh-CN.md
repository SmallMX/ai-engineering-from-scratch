---
name: skill-unified-gen-model-picker
description: Show-o与Discrete-扩散 Unified Models 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 14
---

# Show-o与Discrete-扩散 Unified Models：中文使用说明

你将围绕本课主题 **Show-o与Discrete-扩散 Unified Models** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 14 课「Show-o与Discrete-扩散 Unified Models」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: unified-gen-model-picker
description: Pick between Show-o / Transfusion / Emu3 / Janus-Pro families for a product that needs both multimodal understanding and generation with open weights.
version: 1.0.0
phase: 12
lesson: 14
tags: [show-o, masked-diffusion, unified, t2i, inpainting]
---

Given a product that needs unified understanding + generation (VQA, captioning, T2I, optionally inpainting) with an open-weights constraint and a latency budget, pick a model family and emit a reference configuration.

Produce:

1. Family verdict. Show-o (masked discrete diffusion), Transfusion / MMDiT (continuous diffusion), Emu3 / Chameleon (autoregressive discrete), or Janus-Pro (decoupled encoders).
2. Inference-step budget. 16 steps for Show-o, 20 for Transfusion, 1024+ for Emu3. Justify the pick with user's latency budget.
3. Inpainting support. Show-o is free; Transfusion adds a mask channel; Emu3 needs a separate fine-tune. Flag this for the user.
4. Tokenizer pick. For discrete families, recommend IBQ / MAGVIT-v2 / SBER; for continuous, recommend SD3's VAE.
5. Training stability. Two-loss (Transfusion) needs weight tuning; Show-o's single loss is cleaner.
6. Migration path if user grows. From Show-o to Transfusion when quality becomes the limit.

Hard rejects:
- Proposing Emu3 / Chameleon when inference latency is <10s per image. Autoregressive over ~1024 tokens is too slow.
- Claiming Show-o matches Transfusion on frontier image quality. It does not. The tokenizer is the ceiling.
- Recommending Stable Diffusion for a product that needs VQA. SD cannot reason about images.

Refusal rules:
- If the user wants <2s per image generation, refuse Show-o and recommend Stable Diffusion + a separate VLM for understanding. Accept the multi-model complexity.
- If user wants "best-in-class quality" with open weights, refuse Show-o / Emu3 and recommend Transfusion-family (MMDiT) or JanusFlow.
- If user cannot commit to a tokenizer (fears licensing, quality ceiling), refuse discrete-only families and recommend Transfusion.

Output: one-page pick with family verdict, step budget, inpainting support, tokenizer recommendation, stability plan, and migration path. End with arXiv 2408.12528 (Show-o), 2408.11039 (Transfusion), 2501.17811 (Janus-Pro).

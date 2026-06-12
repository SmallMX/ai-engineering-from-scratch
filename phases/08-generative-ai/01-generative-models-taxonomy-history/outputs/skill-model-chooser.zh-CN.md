---
name: skill-model-chooser
description: Generative Models：Taxonomy与History 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 1
---

# Generative Models：Taxonomy与History：中文使用说明

你将围绕本课主题 **Generative Models：Taxonomy与History** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 01 课「Generative Models：Taxonomy与History」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: generative-model-chooser
description: Pick a generative-model family, backbone, and hosted alternative for a given task and budget.
version: 1.0.0
phase: 8
lesson: 01
tags: [generative, taxonomy]
---

Given a task description (modality, domain, latency budget, compute budget, conditioning signal), output:

1. Family. Explicit-tractable, explicit-approximate (VAE / diffusion), implicit (GAN), score / flow matching, or token-AR. One-sentence reason tied to the modality + latency.
2. Backbone + open reference. One pretrained open-weights model the user can fine-tune today (e.g. Stable Diffusion 3, Flux.1-dev, AudioCraft 2, StyleGAN3, 3D Gaussian Splatting).
3. Hosted alternatives. Three production APIs ranked by quality / cost / latency trade-off (fal.ai, Replicate, Stability, Runway, Veo, Kling, ElevenLabs, etc.).
4. Failure mode. The known pathology for the chosen family (mode collapse, exposure bias, sampler drift, tokenizer artifacts, CLIP-score gaming).
5. Budget. Rough training hours on a single A100, inference cost per sample, VRAM floor.

Refuse to recommend a GAN when the task requires likelihood scoring. Refuse to recommend autoregressive-over-pixels for high-resolution real-time use. Flag any recommendation to "train from scratch" if the listed open backbone already covers the domain.

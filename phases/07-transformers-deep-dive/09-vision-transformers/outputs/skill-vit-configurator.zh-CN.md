---
name: skill-vit-configurator
description: 视觉 Transformer (ViT) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 9
---

# 视觉 Transformer (ViT)：中文使用说明

你将围绕本课主题 **视觉 Transformer (ViT)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 09 课「视觉 Transformer (ViT)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: vit-configurator
description: Pick a ViT variant, patch size, and pretraining source for a new vision task.
version: 1.0.0
phase: 7
lesson: 9
tags: [transformers, vit, vision]
---

Given a vision task (classification / segmentation / detection / retrieval), image resolution, dataset size (labeled + unlabeled), and deployment target, output:

1. Backbone. One of: DINOv2 ViT-L/14 (default for retrieval/classification), SAM 3 encoder (segmentation), SigLIP (vision-language), ConvNeXt (latency-critical). One-sentence reason.
2. Patch size. 16 for standard classification at 224, 14 for DINOv2, 8 for dense prediction at high res. Flag sequence length `(H/P)^2 + 1` and attention cost `O(N^2)`.
3. Pretraining source. Checkpoint name. For small labeled sets (<10k): DINOv2 features frozen + linear probe. For >100k: fine-tune last blocks. State why.
4. Training recipe. Optimizer (AdamW), lr, augmentations (RandAug, MixUp, Random Erasing), label smoothing (0.1 typical), EMA.
5. Risk note. Data regime risk (too little data for full fine-tune), resolution mismatch (pretrain 224 → deploy 1024 without position interpolation), register-token absence (may hurt DINOv2 features).

Refuse to recommend training a ViT from scratch on less than 1M images — CNN baselines will win. Refuse to recommend patch size that yields sequence length > 4096 without explicit discussion of Flash Attention + hierarchical variants (Swin). Flag any deployment that changes input resolution without interpolating positional embeddings.

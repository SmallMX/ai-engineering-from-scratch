---
name: skill-img2img-chooser
description: Conditional GAN与Pix2Pix 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 4
---

# Conditional GAN与Pix2Pix：中文使用说明

你将围绕本课主题 **Conditional GAN与Pix2Pix** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 04 课「Conditional GAN与Pix2Pix」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: img2img-chooser
description: Pick an image-to-image approach given paired vs unpaired data, domain specificity, and latency budget.
version: 1.0.0
phase: 8
lesson: 04
tags: [pix2pix, img2img, conditional]
---

Given a task description (source domain, target domain, data availability - paired/unpaired/N samples, latency budget, quality bar), output:

1. Approach. Pix2Pix (paired, narrow), Pix2PixHD (paired, high-res), CycleGAN (unpaired), SPADE (seg-to-image), or ControlNet variant over SD3 / Flux.1 (general, open-domain).
2. Training data spec. Minimum pair count, resolution, augmentations, license considerations.
3. Architecture. G (U-Net depth, channel width), D (PatchGAN receptive field, spectral norm), loss weights (adv, L1, VGG-perceptual).
4. Inference latency. Target ms/image on a single consumer GPU (RTX 4090, M3 Max), resolution trade-off.
5. Eval. LPIPS against held-out paired data, FID on 5k samples, task-specific metrics (mIoU for seg tasks, PSNR for super-resolution), human preference.

Refuse to recommend Pix2Pix when data is unpaired - prescribe CycleGAN or ControlNet instead. Refuse to train a paired model with fewer than 500 pairs without augmentation / pretraining advice. Flag any request that says "arbitrary text prompt" - those need diffusion + ControlNet, not a paired GAN.

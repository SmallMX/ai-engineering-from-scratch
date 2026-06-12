---
name: skill-diffusion-trainer
description: 扩散模型：DDPM 从零实现 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 6
---

# 扩散模型：DDPM 从零实现：中文使用说明

你将围绕本课主题 **扩散模型：DDPM 从零实现** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 06 课「扩散模型：DDPM 从零实现」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: diffusion-trainer
description: Configure a diffusion training run: schedule, prediction target, sampler, and eval plan.
version: 1.0.0
phase: 8
lesson: 06
tags: [diffusion, ddpm, training]
---

Given a dataset profile (modality, resolution, dataset size), compute budget (GPU hours, VRAM floor), and quality bar (FID target or downstream use), output:

1. Schedule. Linear, cosine (Nichol), or sigmoid. Number of steps T (1000 for DDPM baseline; 256 for faster variants).
2. Prediction target. epsilon, v-prediction, or x_0. Reason tied to resolution and signal-to-noise across the schedule.
3. Architecture. U-Net depth + channel width for pixel diffusion, DiT for latent diffusion, or 3D U-Net / DiT for video. Include time embedding scheme (sinusoidal + MLP, FiLM, or AdaLN).
4. Sampler. DDIM (20-50 steps), DPM-Solver++ (10-20), Euler-A (creative), or distilled 1-4-step. Include guidance scale (CFG w) recommendation.
5. Eval plan. FID / KID / CLIP-score / human-preference, with sample counts (>=10k for FID), sweep protocol for CFG w.

Refuse to recommend training pixel-space diffusion at &gt;=256x256 when latent diffusion achieves the same quality at 1/16th the FLOPs. Refuse to ship a model without CFG for conditional generation - zero-shot unconditional samples from a conditional model are usually degenerate. Flag any schedule with beta_T &gt; 0.1 as likely to produce saturated or unstable training.

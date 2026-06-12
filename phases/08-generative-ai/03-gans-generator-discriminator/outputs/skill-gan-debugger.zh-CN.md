---
name: skill-gan-debugger
description: GAN：Generator vs Discriminator 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 3
---

# GAN：Generator vs Discriminator：中文使用说明

你将围绕本课主题 **GAN：Generator vs Discriminator** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 03 课「GAN：Generator vs Discriminator」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: gan-debugger
description: Diagnose failing GAN training from loss curves and sample grids; prescribe one-line fixes.
version: 1.0.0
phase: 8
lesson: 03
tags: [gan, adversarial, debugging]
---

Given a failing GAN run (D and G loss curves, sample grid, dataset size, optimizer config), output:

1. Diagnosis. One root cause from: mode collapse, D too strong, D too weak, vanishing gradient, batch-norm leakage, overfit D, learning-rate mismatch, bad init.
2. Evidence. Pointer to the telltale in the loss curves or samples (e.g. "D(fake) &lt; 0.05 by step 500 = D too strong").
3. Fix. One concrete change. Examples: `lr_D = lr_G / 2`, replace BN with IN, add spectral norm to D, switch to WGAN-GP with lambda=10, cut batch size by 2, add 0.1 Gaussian noise to D inputs.
4. Rerun protocol. Seeds to try, number of steps before re-evaluation, acceptance criterion (e.g. "FID drops below baseline by step 20k").
5. Fallback. If the fix doesn't land in one rerun, what to try next. Usually: switch architecture (StyleGAN, R3GAN) or switch paradigm (diffusion, flow matching) if dataset is too diverse.

Refuse to recommend increasing G learning rate when D is already saturated. Refuse to add regularization to G when the real failure is D - fix D first. Flag any run that shows training collapse within 100 steps as likely bad init or lr blowup, not a deep algorithmic issue.

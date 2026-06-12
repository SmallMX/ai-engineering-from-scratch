---
name: skill-vae-trainer
description: 自编码器与Variational 自编码器 (VAE) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 2
---

# 自编码器与Variational 自编码器 (VAE)：中文使用说明

你将围绕本课主题 **自编码器与Variational 自编码器 (VAE)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 02 课「自编码器与Variational 自编码器 (VAE)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: vae-trainer
description: Specify VAE architecture, latent size, beta schedule, and eval plan for a given dataset and downstream use.
version: 1.0.0
phase: 8
lesson: 02
tags: [vae, latent, generative]
---

Given a dataset profile (modality, resolution, dataset size) and the downstream use (reconstruction only, sampling, or input-encoder for a latent-diffusion or token-AR model), output:

1. Variant. Plain VAE, beta-VAE, VQ-VAE, RVQ (residual), or NVAE. One-sentence reason tied to modality and downstream use.
2. Architecture. Encoder / decoder topology (conv downsample factor, channel width, hidden dim, attention blocks). Mention public reference weights (`sd-vae-ft-ema`, Encodec, DAC, WAN-VAE) when applicable.
3. Latent dim. Spatial and channel dims. Total bits per sample. Compression ratio vs the raw data.
4. Beta schedule. Warmup ramp, final value, and free-bits threshold if used.
5. Eval plan. Reconstruction MSE / SSIM / PSNR, KL per dim, active-dim count, posterior-collapse alarm threshold, Frechet distance between `q(z|x)` and prior.

Refuse to ship a VAE with beta > 0.5 at training start (posterior collapse). Refuse to use a plain Gaussian VAE as the final generator for images - it will be blurry; use it as a latent encoder for a diffusion or flow-matching model instead. Flag any VQ-VAE with codebook usage under 20% as a misconfigured codebook reset policy.

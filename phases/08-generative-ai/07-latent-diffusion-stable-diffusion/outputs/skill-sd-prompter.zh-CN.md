---
name: skill-sd-prompter
description: Latent 扩散与Stable 扩散 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 7
---

# Latent 扩散与Stable 扩散：中文使用说明

你将围绕本课主题 **Latent 扩散与Stable 扩散** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 07 课「Latent 扩散与Stable 扩散」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: sd-prompter
description: Configure Stable Diffusion / Flux inference for a given prompt, style, and quality bar.
version: 1.0.0
phase: 8
lesson: 07
tags: [stable-diffusion, flux, latent-diffusion]
---

Given a prompt, target style, and quality bar (fast preview / portfolio quality / print-ready), output:

1. Model + checkpoint. SD 1.5 (legacy tools), SDXL-base + refiner, SDXL-Turbo (fast), SD3.5-Large, Flux.1-dev (best open), Flux.1-schnell (fast open), or a hosted API (DALL-E 3, Imagen 4, Midjourney v7). One-sentence reason.
2. Sampler. Euler A (creative), DPM-Solver++ 2M Karras (stable), LCM (fast), or flow-matching sampler (SD3/Flux). Include step count.
3. CFG scale. 0 for turbo / LCM, 3-4 for Flux, 5-7 for SDXL, 7-10 for SD1.5. Document the trade-off.
4. Add-ons. ControlNet (pose, depth, canny, seg), IP-Adapter (reference image), LoRA (style or subject), T5 toggle for SD3+.
5. Negative prompt. Explicit empty string vs filled content (artifacts, low quality, wrong anatomy) matters; specify both.

Refuse CFG &gt; 10 for SDXL+ (saturated outputs). Refuse &gt; 50 sampler steps on non-legacy checkpoints (quality plateaus by 30). Refuse to mix LoRAs trained on different base models (SD 1.5 LoRA on SDXL is silently broken). Flag any request for photorealistic humans without a reminder about NSFW, deepfake, and copyright policy.

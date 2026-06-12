---
name: skill-token-gen-cost-analyzer
description: Emu3：Next-Token Prediction for 图像与视频 Generation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 12
---

# Emu3：Next-Token Prediction for 图像与视频 Generation：中文使用说明

你将围绕本课主题 **Emu3：Next-Token Prediction for 图像与视频 Generation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 12 课「Emu3：Next-Token Prediction for 图像与视频 Generation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: token-gen-cost-analyzer
description: Compute token counts, inference latency, and quality ceiling for Emu3-style next-token generation and pick between Emu3-family and diffusion.
version: 1.0.0
phase: 12
lesson: 12
tags: [emu3, next-token-prediction, video-gen, diffusion, cfg]
---

Given a generation product spec (image or video, target resolution, quality tier, throughput requirement), compute token counts for Emu3-style next-token generation, estimate inference cost, and pick between Emu3-family and diffusion.

Produce:

1. Token count. Per-image tokens at chosen tokenizer reduction (typically 8x per dim for image). Per-video tokens with 3D VQ (typically 4x4x4 spatiotemporal).
2. Inference latency. Tokens / throughput (tokens-per-second) for Emu3-family; denoise-steps * step-time for diffusion. Cite concrete A100 / H100 ranges.
3. Quality ceiling. Tokenizer reconstruction PSNR (30-32 dB for IBQ-class), FID expectations on MJHQ-30K, FVD for video.
4. CFG configuration. Recommended guidance weight (gamma) per task; typical 3.0 for standard gen, 5-7 for strong prompt adherence.
5. Pick. Emu3-family if product needs unified understanding + generation or any-modality flexibility; diffusion (SDXL / SD3 / Flux) if product is image-gen-only with strict latency.

Hard rejects:
- Claiming Emu3 is faster than diffusion at inference. It is not; the autoregressive decode over thousands of image tokens is the standing cost.
- Recommending Emu3-family without specifying CFG weight. Quality collapses without it.
- Proposing Emu3 for strict 4K image generation. Token count at 2048+ resolution blows KV cache and takes minutes.

Refusal rules:
- If latency budget is <5s per image, refuse Emu3 and recommend SDXL or SD3.
- If product must emit images AND describe them AND reason about third-party images, recommend Emu3-family (the unified loss is the point); diffusion cannot do this without a separate VLM.
- If user wants open weights with permissive license for commercial use, refuse Emu3 — check its license first; some versions are research-only.

Output: one-page analysis with token counts, latency estimates, quality ceiling, CFG config, and a pick with justification. End with arXiv 2409.18869 (Emu3) and 2408.11039 (Transfusion) for the alternative.

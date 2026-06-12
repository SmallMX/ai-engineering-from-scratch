---
name: skill-resolution-budget-planner
description: Any-Resolution 视觉：Patch-n'-Pack与NaFlex 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 6
---

# Any-Resolution 视觉：Patch-n'-Pack与NaFlex：中文使用说明

你将围绕本课主题 **Any-Resolution 视觉：Patch-n'-Pack与NaFlex** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 06 课「Any-Resolution 视觉：Patch-n'-Pack与NaFlex」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: resolution-budget-planner
description: Pick between square-resize, AnyRes, M-RoPE, and NaFlex for a mixed-aspect-ratio VLM workload and emit a per-task token budget plan.
version: 1.0.0
phase: 12
lesson: 06
tags: [vlm, patch-n-pack, naflex, anyres, m-rope, token-budget]
---

Given a workload — a description of the images the VLM will see (OCR documents, charts, UI screenshots, natural photos, video frames) and a total per-request token budget — pick one resolution strategy per image class and produce a runnable configuration.

Produce:

1. Per-image-class strategy. For each declared class (OCR, chart, UI, photo, video-frame), pick one of {square-resize, AnyRes, M-RoPE, NaFlex}. Justify in one sentence citing the task's resolution sensitivity.
2. Token budget per image. Include min_pixels, max_pixels (Qwen2.5-VL style), and the expected sequence length at the chosen strategy. Flag if any single image exceeds 40% of the LLM context.
3. Batch packing plan. If requests are batched, specify whether to use `cu_seqlens` (FlashAttn varlen), a dense block-diagonal mask, or unbatched single-image inference. Note the FLOP savings of varlen when batch aspect ratios vary by > 2x.
4. Encoder recommendation. SigLIP 2 NaFlex for mixed workloads; Qwen2.5-VL native for agent UIs; CLIP-336 + AnyRes for frozen-encoder deployments; a raw ViT at 224 for photo-only paths.
5. Failure-mode alarms. Tokens-per-image at the chosen config; latency cost at 30 tok/s prefill; context-fill percentage; expected accuracy delta vs square-resize on typical OCR benchmarks.

Hard rejects:
- Recommending square-resize for OCR or chart tasks without citing which benchmark number the user will lose.
- Proposing a strategy that produces more tokens than the LLM context allows. Always budget against the declared context window.
- Treating AnyRes as the universal answer — its multiplicative tile overhead can exceed the LLM context before one image finishes encoding.

Refusal rules:
- If the user's declared token budget is below 256 tokens per image, refuse for anything other than a photo-only semantic task — no amount of pooling recovers OCR accuracy at that budget.
- If the user wants dense-prediction outputs (segmentation, depth) without ViT register tokens in the encoder, refuse and point to DINOv2 / SigLIP 2 with registers enabled.
- If the user's LLM context is < 8k and the workload includes documents or screenshots, refuse and recommend a larger context or an OCR-first pipeline.

Output: a one-page budget plan with a per-class strategy table, a batch-packing plan, encoder recommendation, and an alarm list. End with the relevant arXiv paper for follow-up — 2307.06304 for NaViT, 2502.14786 for SigLIP 2 / NaFlex, 2502.13923 for Qwen2.5-VL.

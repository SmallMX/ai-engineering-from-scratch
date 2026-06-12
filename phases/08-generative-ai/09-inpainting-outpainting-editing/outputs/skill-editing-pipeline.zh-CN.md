---
name: skill-editing-pipeline
description: Inpainting, Outpainting与图像 Editing 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 9
---

# Inpainting, Outpainting与图像 Editing：中文使用说明

你将围绕本课主题 **Inpainting, Outpainting与图像 Editing** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 09 课「Inpainting, Outpainting与图像 Editing」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: editing-pipeline
description: Plan an image-editing pipeline from source + edit description to a ready-to-ship output.
version: 1.0.0
phase: 8
lesson: 09
tags: [inpaint, outpaint, edit, sam]
---

Given source image, target edit (remove X, replace Y with Z, extend canvas, restyle region, change season / time-of-day), and quality bar (draft / portfolio / print), output:

1. Mask strategy. Explicit brush mask, SAM 2 click / box prompt, Grounded-SAM on a text phrase, or RMBG (for background removal). One-sentence reason.
2. Base model + mode. SD-Inpaint / SDXL-Inpaint / Flux-Fill / Flux-Kontext for instruction edits, or SDEdit noise-level (0.3 / 0.6 / 0.9) if no mask.
3. Prompt scaffolding. Describe the whole image after edit, not only the new content. Include negative prompt.
4. CFG + strength + feather. Mask feather 8-16 px; CFG ~5-7 for SDXL-inpaint, 3-4 for Flux. Strength 0.8-1.0 for full regenerate, 0.3-0.5 for preserve.
5. Guardrails. NSFW / deepfake / trademark detection hook, face-swap policy gate, reversibility (save the mask + seed).

Refuse to ship identity edits on a recognizable public figure without explicit policy check. Refuse to outpaint an image without at least 30% of the original canvas as the anchor (too little context makes the model hallucinate). Flag any SDEdit run with t/T &gt; 0.7 and fidelity target "preserve subject" as a likely mismatch.

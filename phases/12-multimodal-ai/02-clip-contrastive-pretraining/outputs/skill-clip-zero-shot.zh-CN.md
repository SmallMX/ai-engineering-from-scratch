---
name: skill-clip-zero-shot
description: CLIP与Contrastive 视觉-Language Pretraining 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 2
---

# CLIP与Contrastive 视觉-Language Pretraining：中文使用说明

你将围绕本课主题 **CLIP与Contrastive 视觉-Language Pretraining** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 02 课「CLIP与Contrastive 视觉-Language Pretraining」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: clip-zero-shot
description: Run zero-shot image classification with a CLIP / SigLIP checkpoint, producing ranked predictions with similarity scores.
version: 1.0.0
phase: 12
lesson: 02
tags: [clip, siglip, zero-shot, vision-language]
---

Given a list of images (file paths or URLs) and a list of candidate class names, produce a ranked zero-shot classification using a declared CLIP or SigLIP checkpoint. The skill is pure-prediction; it does not train or finetune.

Produce:

1. Prompt construction. For each class, form N text templates (default: `a photo of a {class}`, `a picture of a {class}`, `an image of a {class}`). Embed each prompt with the text encoder and average to form the class prototype.
2. Image embedding. Embed each input image with the stated vision encoder. Normalize both sides to unit length.
3. Ranked predictions. Compute cosine similarity between each image embedding and each class prototype. Return top-1 and top-5 with scores.
4. Checkpoint metadata. Name the exact Hugging Face checkpoint used (e.g., `openai/clip-vit-large-patch14` or `google/siglip2-so400m-patch14-384`) and the resolution it expects.
5. Honesty notice. State that zero-shot on classes outside the pretraining distribution is unreliable; surface top-1 score as a confidence proxy and warn when it is below 0.2.

Hard rejects:
- Any use that frames the output as a definitive label for classes not in the caller's provided list.
- Claims about scores across different checkpoints being comparable; SigLIP and CLIP score on different scales.
- Running on images known to contain people without a downstream consent policy.

Refusal rules:
- If the caller asks to classify into medical, legal, or safety-critical categories (diagnosis, identity, protected attributes), refuse and redirect to supervised models with audit trails.
- If the caller provides a single class name (one-way classification with no alternatives), refuse — zero-shot needs at least two candidates to be meaningful.
- If the checkpoint is unspecified, refuse and ask which of (CLIP, OpenCLIP, SigLIP, SigLIP 2) plus which scale.

Output: a ranked list of top-5 predictions per image with cosine similarity scores, checkpoint name, prompt templates used, and a confidence flag. End with a "what to read next" paragraph pointing to Lesson 12.06 for NaFlex (handling variable aspect ratios) or the SigLIP 2 paper for a deeper dive.

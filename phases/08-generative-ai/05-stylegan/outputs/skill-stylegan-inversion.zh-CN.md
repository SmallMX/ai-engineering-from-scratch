---
name: skill-stylegan-inversion
description: StyleGAN 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 5
---

# StyleGAN：中文使用说明

你将围绕本课主题 **StyleGAN** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 05 课「StyleGAN」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: stylegan-inversion
description: Choose an inversion and editing pipeline for a pretrained StyleGAN over a real photo.
version: 1.0.0
phase: 8
lesson: 05
tags: [stylegan, inversion, editing]
---

Given a real photo + pretrained StyleGAN checkpoint (FFHQ-1024, StyleGAN-XL, a custom fine-tune) and target edit (age, smile, pose, hair, identity preservation), output:

1. Inversion method. e4e (fast, low fidelity), ReStyle (iterative encoder), HyperStyle (hypernet), PTI (pivotal tuning), or direct W-optimization. One-sentence reason tied to fidelity vs speed.
2. Target space. W, W+, or StyleSpace. Trade-offs: W = most disentangled but lowest fidelity, W+ = per-layer w, StyleSpace = channel-level.
3. Editing direction. Named direction source: InterFaceGAN (SVM-based), StyleSpace channels, GANSpace PCA, or a learned classifier.
4. Fidelity budget. LPIPS threshold before identity drift; rollback heuristic.
5. Eval. ID similarity (ArcFace cosine), LPIPS to original, edit strength (target attribute classifier score).

Refuse any pipeline that edits directly in Z (entangled). Refuse large edits (&gt;1.5 sigma in W) without identity checks. Flag requests that need open-domain editing (e.g. "make him a cartoon") - those require diffusion + IP-Adapter, not StyleGAN.

---
name: skill-document-ai-stack-picker
description: Document与Diagram Understanding 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 22
---

# Document与Diagram Understanding：中文使用说明

你将围绕本课主题 **Document与Diagram Understanding** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 22 课「Document与Diagram Understanding」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: document-ai-stack-picker
description: Pick between OCR pipeline, OCR-free specialist, and VLM-native for a document-AI project based on domain, scale, and regulatory needs.
version: 1.0.0
phase: 12
lesson: 22
tags: [document-ai, ocr, donut, nougat, paligemma, vlm-native]
---

Given a document-AI project (domain: invoices / scientific papers / forms / mixed; scale: pages per day; quality bar; regulatory needs), pick a stack and produce a reference config.

Produce:

1. Stack pick. Era 1 (OCR pipeline + LayoutLMv3), Era 2 (Donut / Nougat OCR-free), Era 3 (VLM-native), or hybrid.
2. Per-page cost estimate. Token count and latency at the chosen stack.
3. Accuracy expectation. DocVQA + ChartQA + domain-specific benchmarks.
4. Handwriting strategy. VLM-native for cost-insensitive; dedicated TrOCR + routing for scale.
5. Math / LaTeX output. Nougat for scientific papers; VLM for other.
6. Regulatory fallback. Hybrid with cross-check audit log.

Hard rejects:
- Proposing VLM-native for >1M pages/day without cost analysis. Token cost at 2576px per page is significant.
- Recommending single-model solutions for regulated workflows without audit paths.
- Claiming Nougat handles scanned invoices. It does not — it is scientific-paper specialist.

Refusal rules:
- If scale is >10M pages/day, refuse Era 3 and recommend Era 1 with Era 3 as sampling validator.
- If domain is handwritten-heavy, refuse OCR pipeline and recommend VLM-native + handwriting specialist (TrOCR).
- If LaTeX fidelity is required for equations, require Nougat in the loop.

Output: one-page plan with stack, cost, accuracy, handwriting, math, regulatory. End with arXiv 2308.13418 (Nougat), 2204.08387 (LayoutLMv3), 2111.15664 (Donut).

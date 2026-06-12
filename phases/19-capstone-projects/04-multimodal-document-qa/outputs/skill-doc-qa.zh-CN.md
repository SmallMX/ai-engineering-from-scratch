---
name: skill-doc-qa
description: 毕业项目 04：多模态 Document QA (视觉-First PDF, Tables, Charts) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 4
---

# 毕业项目 04：多模态 Document QA (视觉-First PDF, Tables, Charts)：中文使用说明

你将围绕本课主题 **毕业项目 04：多模态 Document QA (视觉-First PDF, Tables, Charts)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 04 课「毕业项目 04：多模态 Document QA (视觉-First PDF, Tables, Charts)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: doc-qa
description: Build a vision-first multimodal document QA system on 10k pages with late-interaction retrieval and evidence-region citations.
version: 1.0.0
phase: 19
lesson: 04
tags: [capstone, multimodal, rag, colpali, colqwen, late-interaction, pdf]
---

Given a corpus of PDFs (10-Ks, scientific papers, scanned documents), build a pipeline that indexes pages as images using ColPali-style late interaction and answers questions with page-level evidence regions.

Build plan:

1. Render every PDF page to a 1536x2048 PNG with PyMuPDF at 180 DPI.
2. Embed every page with ColQwen2.5-v0.2 or ColQwen3-omni. Store multi-vector patch embeddings in Vespa, Qdrant multi-vector, or AstraDB.
3. Apply DocPruner-style 50% patch pruning. Verify accuracy drop stays under 0.5% on ViDoRe v3.
4. At query time: embed query tokens; compute MaxSim against every page's patches; rank top-k.
5. Synthesize with Qwen3-VL-30B or Gemini 2.5 Pro passing the query plus top-5 page images. Require cited `(doc_id, page, region)` anchors.
6. For equation- or table-heavy pages, run Nougat or dots.ocr as an optional text channel and feed it alongside the image.
7. Build a Next.js 15 viewer that overlays evidence regions as bounding boxes on the source page.
8. Evaluate on ViDoRe v3 and M3DocVQA. Produce a content-class × approach matrix comparing vision-first vs OCR-then-text on plain text, tables, charts, handwriting, and equations.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | ViDoRe v3 / M3DocVQA accuracy | Benchmark vs OCR-then-text baseline on matched pages |
| 20 | Evidence-region grounding | Fraction of cited regions that contain the answer span |
| 20 | Storage and latency engineering | DocPruner compression, index p95, answer p95 under 2s |
| 20 | Multi-page reasoning | Accuracy on a hand-labeled 100-question multi-page set |
| 15 | Source-inspection UX | Overlay fidelity, comparison tools, page-by-page explorer |

Hard rejects:

- OCR-first pipelines pitched as "vision-first" by retrofitting OCR text into a single-vector embed.
- Any system that drops patch-level bounding boxes and therefore cannot render evidence overlays.
- Storage numbers reported without documenting DocPruner settings.

Refusal rules:

- Refuse to index scanned legal contracts without a dedicated redaction policy. ColQwen embeddings leak content.
- Refuse to serve queries against a corpus the user has not disclosed. Audit trail is mandatory for regulated domains.
- Refuse to compare to OCR-then-text without running both pipelines on the same corpus.

Output: a repo containing the ingestion pipeline, the Vespa (or Qdrant multi-vector) config, the 100-question multi-page eval set, the viewer UI, and a write-up with the content-class x approach matrix and a concrete recommendation for which content classes still favor OCR-then-text in 2026.

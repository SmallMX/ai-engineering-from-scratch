---
name: skill-vision-rag-designer
description: ColPali与视觉-Native Document RAG 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 23
---

# ColPali与视觉-Native Document RAG：中文使用说明

你将围绕本课主题 **ColPali与视觉-Native Document RAG** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 23 课「ColPali与视觉-Native Document RAG」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: vision-rag-designer
description: Design a vision-native document RAG using ColPali / ColQwen2 / VisRAG, with storage estimate and generator-pick.
version: 1.0.0
phase: 12
lesson: 23
tags: [colpali, colqwen2, visrag, late-interaction, vidore]
---

Given a document RAG project (corpus size, query latency target, storage budget, per-query cost), emit a vision-native RAG config.

Produce:

1. Retriever pick. ColPali (PaliGemma base), ColQwen2 (Qwen2-VL base, better quality), ColSmol (1B for edge), or VisRAG (bi-encoder, cheaper storage).
2. Storage estimate. N_docs * N_p_per_doc * D * 4 bytes raw; divide by 8 for PQ.
3. Latency estimate.
   - Retrieval SLA: ~10ms query embed + top-k retrieval (MaxSim or ANN), index-size dependent.
   - Full-answer SLA: retrieval latency + 200-500ms generator (model and hardware dependent).
4. Generator pick. Qwen2.5-VL-72B for open, Claude Opus 4.7 for frontier.
5. Compression plan. PQ / OPQ ratio target 8-16x; HNSW index for fast ANN.
6. Migration path from text-RAG. How to A/B, when to fully cutover.

Hard rejects:
- Using ColPali without PQ compression on corpora >10k pages. Storage explodes.
- Claiming bi-encoder retrieval matches ColBERT MaxSim on document recall. It does not on ViDoRe.
- Recommending text-RAG for charts + tables workloads. Text-RAG loses most of the signal.

Refusal rules:
- If corpus is pure-text (wiki, chat logs), refuse vision-native RAG and recommend standard text-RAG.
- If retrieval SLA <100ms, prefer VisRAG (bi-encoder) over ColPali MaxSim.
- If full-answer SLA <100ms, refuse generative RAG entirely and recommend retrieval-only UX or cached answers.
- If storage budget is <1 GB and corpus is >100k pages, refuse full-fidelity ColPali; propose aggressive PQ or VisRAG.

Output: one-page RAG design with retriever pick, storage estimate, latency, generator, compression, migration. End with arXiv 2407.01449 (ColPali), 2410.10594 (VisRAG).

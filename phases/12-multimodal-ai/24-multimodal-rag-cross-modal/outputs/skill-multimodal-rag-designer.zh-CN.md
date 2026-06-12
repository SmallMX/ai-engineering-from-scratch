---
name: skill-multimodal-rag-designer
description: 多模态 RAG与Cross-Modal 检索 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 24
---

# 多模态 RAG与Cross-Modal 检索：中文使用说明

你将围绕本课主题 **多模态 RAG与Cross-Modal 检索** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 24 课「多模态 RAG与Cross-Modal 检索」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: multimodal-rag-designer
description: Design a production multimodal RAG across text, images, audio, video with retrievers, fusion strategy, and grounded generator.
version: 1.0.0
phase: 12
lesson: 24
tags: [multimodal-rag, cross-modal-retrieval, fusion, grounded-generation]
---

Given a multimodal product query flow (which modalities in the query, which in the corpus), design retrievers, fusion, and generation.

Produce:

1. Per-modality retrievers. CLIP / SigLIP 2 for text+image, CLAP for text+audio, VLM hidden states for anything else.
2. Fusion pick. Score fusion default; MoE fusion if per-query routing is needed; attention fusion at scale.
3. Grounded generator. Qwen2.5-VL or Claude 4.7 with training on source-tagged outputs.
4. Evaluation. Recall@k per modality + fused top-k accuracy + human-judged end-to-end.
5. Agentic multi-hop. When to re-query; confidence threshold to trigger.
6. Storage estimate. Per-modality vector counts and compression.

Hard rejects:
- Using bi-encoder retrieval across modalities without a shared space (CLIP / CLAP). Scores are meaningless.
- Proposing MoE fusion without training data. MoE needs supervision to route correctly.
- Claiming score-fusion weights transfer across domains. They do not.

Refusal rules:
- If the corpus has no image-caption pair data for training retrievers, refuse custom fine-tune and recommend off-the-shelf CLIP / SigLIP 2.
- If the query latency budget is <200ms and multi-hop is required, refuse; propose single-shot with better retrievers.
- If grounded citations are a regulatory requirement and no generator supports them, refuse and propose Anthropic / OpenAI citation APIs or an explicit post-processing citation layer.

Output: one-page RAG design with retrievers, fusion, generator, evaluation, agentic strategy, storage. End with arXiv 2502.08826, 2504.08748, 2503.18016.

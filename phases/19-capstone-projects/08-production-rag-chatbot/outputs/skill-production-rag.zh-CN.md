---
name: skill-production-rag
description: 毕业项目 08：生产 RAG Chatbot for a Regulated Vertical 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 8
---

# 毕业项目 08：生产 RAG Chatbot for a Regulated Vertical：中文使用说明

你将围绕本课主题 **毕业项目 08：生产 RAG Chatbot for a Regulated Vertical** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 08 课「毕业项目 08：生产 RAG Chatbot for a Regulated Vertical」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: production-rag
description: Deploy a regulated-domain RAG chatbot with role + jurisdiction filtering, prompt caching, guardrails, and live drift monitoring.
version: 1.0.0
phase: 19
lesson: 08
tags: [capstone, rag, chatbot, regulated, llama-guard, nemo-guardrails, ragas, langfuse]
---

Given a regulated-domain corpus (legal contracts, clinical trial protocols, insurance policies, or similar), deploy a chatbot that answers with verifiable citations, respects role and jurisdiction access policies, and is monitored for drift.

Build plan:

1. Parse the corpus with docling or Unstructured; route visually rich documents through ColPali. Emit chunks with role and jurisdiction labels.
2. Index dense (Voyage-3 or Nomic-embed-v2) into pgvector + pgvectorscale; sparse BM25 via Tantivy.
3. Wire LangGraph conversational agent: retrieve (filter by role + jurisdiction, hybrid dense+BM25, reciprocal rank fusion), rerank (bge-reranker-v2-gemma-2b or Voyage rerank-2), synth (Claude Sonnet 4.7 with prompt caching).
4. Assemble prompts with stable prefixes: system preamble -> policy block -> reranked context -> user query. Target 60-80% prompt-cache hit rate.
5. Guardrails: Llama Guard 4 on input and output, NeMo Guardrails v0.12 rails for off-domain and policy-forbidden questions, Presidio PII scrub on output, citation enforcement post-filter.
6. Build a 200-question expert-labeled golden set with (answer, citations). Score on exact-citation match, answer correctness, RAGAS faithfulness.
7. Build a 50-prompt red team (PAIR, TAP, PII extraction, off-domain, cross-jurisdiction probes).
8. Arize Phoenix drift dashboard tracking retrieval nDCG and citation faithfulness weekly; alert on 5% drop.
9. Langfuse cost report: prompt-cache hit rate, tokens per query, $/query by stage.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | RAGAS faithfulness + answer relevance | Online scores on the 200-question golden set |
| 20 | Citation correctness | Fraction of answers with verifiable source anchors |
| 20 | Guardrail coverage | Llama Guard 4 pass rate + jailbreak suite result |
| 20 | Cost / latency engineering | Prompt-cache hit rate, p95 latency, $/query |
| 15 | Drift monitoring dashboard | Live Phoenix dashboard with weekly retrieval-quality trend |

Hard rejects:

- Any chatbot that leaks cross-jurisdiction data. Role+jurisdiction filtering must be enforced before retrieval, not after.
- Synthesis prompts that break cache prefixes (reordering policy between system and context). Will destroy the cache economics.
- Guardrail configurations without logged red-team runs.
- Answers without citations; citations without verifiable anchors.

Refusal rules:

- Refuse to deploy in a regulated domain without jurisdiction tags on every chunk.
- Refuse to train retrieval on expert-labeled golden set questions. Contamination destroys eval credibility.
- Refuse to claim "compliant" without an explicit SOC2/HIPAA/GDPR applicability matrix in the README.

Output: a repo containing the ingestion pipeline, the LangGraph conversational agent, the 200-question golden set, the 50-prompt red team, the Phoenix drift dashboard, the Langfuse cost dashboard, and a write-up naming the top three citation-breakage patterns you observed and the retrieval or prompt fix for each.

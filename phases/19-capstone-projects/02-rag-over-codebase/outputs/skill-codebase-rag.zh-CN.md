---
name: skill-codebase-rag
description: 毕业项目 02：RAG over Codebase (Cross-Repo Semantic 搜索) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 2
---

# 毕业项目 02：RAG over Codebase (Cross-Repo Semantic 搜索)：中文使用说明

你将围绕本课主题 **毕业项目 02：RAG over Codebase (Cross-Repo Semantic 搜索)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 02 课「毕业项目 02：RAG over Codebase (Cross-Repo Semantic 搜索)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: codebase-rag
description: Build a cross-repo semantic search system with AST-aware chunking, hybrid retrieval, incremental re-index, and cited answers.
version: 1.0.0
phase: 19
lesson: 02
tags: [capstone, rag, code-search, tree-sitter, qdrant, bm25, hybrid-retrieval]
---

Given 10+ repositories totaling at least 2M lines of code, build an ingestion pipeline, a hybrid index, and a citation-enforced query agent that answers cross-repo questions with verifiable file:line anchors.

Build plan:

1. Parse every file with tree-sitter. Chunk at function and class node boundaries. Store `{repo, path, start_line, end_line, symbol, body}`.
2. Summarize every chunk with Claude Haiku 4.5 or Gemini 2.5 Flash using prompt-cached system prompts. Store the one-sentence summary next to the chunk.
3. Index into three structures: Qdrant (dense, Voyage-code-3 or nomic-embed-code), Tantivy (BM25 with field weights), and kuzu (symbol graph edges for imports, calls, inheritance).
4. Build a LangGraph query agent with three nodes: retrieve (dense parallel BM25), rerank (Cohere rerank-3 or bge-reranker-v2-gemma-2b), synth (Claude Sonnet 4.7 with prompt caching and file:line citation requirement).
5. Post-filter: reject any claim without a verifiable `(repo/path:start-end)` anchor; re-ask or drop.
6. Wire a git push webhook that computes a symbol-level diff and re-embeds only the changed chunks. Target: 50-file commit searchable in under 60s on a 2M-LOC fleet.
7. Evaluate with a 100-question held-out set. Report MRR@10, nDCG@10, citation faithfulness, and latency percentiles.
8. Run a weekly drift job that re-executes the eval and alerts on MRR@10 drop > 5%.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Retrieval quality | MRR@10 and nDCG@10 on a 100-question held-out set |
| 20 | Citation faithfulness | Fraction of answer claims with verifiable file:line anchors |
| 20 | Latency and scale | p95 query latency at 10k QPS on the indexed corpus size |
| 20 | Incremental indexing correctness | Time from git push to searchable on a 50-file commit |
| 15 | UX and answer formatting | Citation clickability, snippet previews, follow-up affordance |

Hard rejects:

- Fixed-size token chunking instead of AST-aware chunking. Will poison generated-code-heavy corpora.
- Cosine-only retrieval without BM25 or rerank. Known to fail on exact-symbol-name queries.
- Answers without mandatory file:line citations.
- Full-corpus re-embedding on every git push; must be incremental.

Refusal rules:

- Refuse to index repos without reading their license. Some forbid embedding in third-party vector stores.
- Refuse to answer queries that claim to cite files the index never saw; always verify the anchor before returning.
- Refuse to serve an answer at p95 above 4s; return a partial result with a follow-up handle instead.

Output: a repo containing the ingestion pipeline, the LangGraph query agent, the 100-question labeled eval set, a Langfuse dashboard link, and a write-up naming the three retrieval failure modes you fixed (generated-code poisoning, long-tail symbol recall, cross-repo symbol resolution) and the exact change that fixed each.

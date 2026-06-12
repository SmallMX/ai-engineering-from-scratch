# Hybrid 记忆：Vector + Graph + KV (Mem0)

> Mem0 (Chhikara et al., 2025) treats memory as three stores in parallel：vector for semantic similarity, KV for fast fact lookup, graph for entity-relationship reasoning. A scoring layer fuses the three on retrieval. This is the 2026 production standard for external memory.

**类型：** 构建
**语言：** Python (stdlib)
**前置知识：** Phase 14 · 07 (MemGPT), Phase 14 · 08 (Letta Blocks)
**时间：** 约 75 minutes

## 学习目标
- Explain why a single store (vector only, graph only, KV only) is insufficient for agent memory.
- Name Mem0's three parallel stores与what each one optimizes for.
- Describe Mem0's fusion scoring：relevance, importance, recency —与why it is a weighted sum, not a hierarchy.
- Implement a toy three-store memory in stdlib with an `add()` that writes to all three与a `search()` that fuses results.

## 中文导读

本课是 Phase 14「智能体工程」的第 09 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Hybrid Memory: Vector + Graph + KV (Mem0)

> Mem0 (Chhikara et al., 2025) treats memory as three stores in parallel — vector for semantic similarity, KV for fast fact lookup, graph for entity-relationship reasoning. A scoring layer fuses the three on retrieval. This is the 2026 production standard for external memory.

**Type:** Build
**Languages:** Python (stdlib)
**Prerequisites:** Phase 14 · 07 (MemGPT), Phase 14 · 08 (Letta Blocks)
**Time:** ~75 minutes

## Learning Objectives

- Explain why a single store (vector only, graph only, KV only) is insufficient for agent memory.
- Name Mem0's three parallel stores and what each one optimizes for.
- Describe Mem0's fusion scoring — relevance, importance, recency — and why it is a weighted sum, not a hierarchy.
- Implement a toy three-store memory in stdlib with an `add()` that writes to all three and a `search()` that fuses results.

## The Problem

One store is wrong for one of three query classes:

- **Semantic similarity** — "what did we discuss about agent drift last week?" Vector wins; KV and graph miss.
- **Fact lookup** — "what is the user's phone number?" KV wins; vector is wasteful, graph is overkill.
- **Relationship reasoning** — "which customers share the same billing entity?" Graph wins; vector and KV cannot answer.

Production agents issue all three in one session. A single-store memory is always wrong for two of them. Mem0's contribution is wiring all three behind a single `add`/`search` surface with a scoring function that fuses them.

## The Concept

### Three stores in parallel

Mem0 (arXiv:2504.19413, April 2025) on `add(text, user_id, metadata)`:

1. Extract candidate facts from the text (an LLM-driven step).
2. Write each fact to the vector store (embedding) for semantic search.
3. Write each fact to the KV store keyed on (user_id, fact_type, entity) for O(1) lookup.
4. Write each fact to the graph store (Mem0g) as typed edges for relationship queries.

On `search(query, user_id)`:

1. Vector store returns top-k by embedding cosine.
2. KV store returns direct hits keyed on query-derived (user_id, type, entity).
3. Graph store returns subgraph reachable from query entities.
4. A scoring layer fuses the three.

### Fusion scoring

```
score = w_relevance * relevance(q, record)
      + w_importance * importance(record)
      + w_recency * recency(record)
```

- **Relevance** — vector cosine, KV exact match, graph path weight.
- **Importance** — tagged at write time or learned (some facts matter more: names, IDs, policies).
- **Recency** — exponential decay over time since last write or read.

Weights are tuned per product. Higher `w_recency` for chat agents; higher `w_importance` for compliance agents; higher `w_relevance` for retrieval agents.

### Mem0g and temporal reasoning

Mem0g adds a conflict detector. When a new fact contradicts an existing edge, the existing edge is marked invalid but not deleted. Temporal queries ("what was the user's city in March?") traverse the valid-at-time subgraph.

This is the compliance-grade behavior Letta's invalidation pattern generalizes.

### Benchmark numbers

The Mem0 paper reports (2025):

- **LoCoMo** (long-form conversation memory): 91.6
- **LongMemEval** (long-horizon episodic memory): 93.4
- **BEAM 1M** (1M-token memory benchmark): 64.1

Comparison baselines (full-context 128k LLM, flat vector store, flat KV) all lose by 10+ points. Benchmarks alone don't justify choice — operational shape does — but the numbers show the fusion design is not a rounding error.

### Scope taxonomy

Mem0 splits memory by scope:

- **User memory** — persists across sessions, keyed on `user_id`.
- **Session memory** — persists within one thread.
- **Agent memory** — per-agent instance state.

Every write picks one scope. Retrieval can query across scopes with per-scope weights. Mixing scopes without thought is how you get "the assistant told Alice about Bob's project" incidents.

### Where this pattern goes wrong

- **Embedding drift.** Vector results that look right on the first hundred queries degrade as the corpus grows. Add periodic re-embedding of the top-N-used records.
- **KV schema creep.** `(user_id, type, entity)` looks simple until every team adds their own `type`. Audit the type set quarterly.
- **Graph explosion.** One noisy extractor adds 50 edges per message. Cap graph writes per `add` call; drop low-confidence edges.

## Build It

`code/main.py` implements the three-store pattern in stdlib:

- `VectorStore` — naive token-overlap similarity as an embedding stand-in.
- `KVStore` — dict keyed on `(user_id, fact_type, entity)`.
- `GraphStore` — typed edges (subject, relation, object, valid).
- `Mem0` — top-level facade with `add()`, `search()`, fusion scoring, and scope-aware retrieval.
- A worked trace on a multi-user, multi-session conversation.

Run it:

```
python3 code/main.py
```

The output shows three separate recall paths plus the fused top-k. Flip the scoring weights at the top of `main()` and watch the ranking change.

## Use It

- **Mem0 (Apache 2.0)** — production-ready. Self-host with Postgres + Qdrant + Neo4j, or use the managed cloud.
- **Letta** — three-tier core/recall/archival; bring your own vector and graph backends.
- **Zep** — commercial alternative with temporal KG and fact extraction.
- **Custom builds** — when you need exact control over the extractor (compliance) or fusion weights (voice agents where recency dominates).

## Ship It

`outputs/skill-hybrid-memory.md` generates a three-store memory scaffold with a fusion scorer, scope taxonomy, and temporal invalidation wired in.

## Exercises

1. Replace the toy vector similarity with a real embedding model (sentence-transformers, Ollama, OpenAI embeddings). Measure recall@10 on a synthetic long conversation. Does the ranking drift over 1000 writes?
2. Add a temporal query: `search(query, as_of=timestamp)`. Return only records valid at or before that time. Which store needs the most work?
3. Implement a conflict detector: if an incoming fact contradicts a graph edge, invalidate the old edge and log both. Test on "user lives in Berlin" -> "user lives in Lisbon."
4. Port the fusion scorer to include a `user_feedback` dimension (thumbs-up on retrieved records). How do you prevent gaming (the agent only returns records it already liked)?
5. Read the Mem0 docs (`docs.mem0.ai`). Port the toy to `mem0` client calls. Compare retrieval quality on the same 20 test queries.

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| Hybrid memory | "Vector plus graph plus KV" | Three stores written in parallel, fused on retrieval |
| Fact extraction | "Memory ingestion" | LLM step that breaks text into (entity, relation, fact) tuples |
| Fusion scoring | "Relevance ranking" | Weighted sum of relevance, importance, recency |
| Scope | "Memory namespace" | user / session / agent — determines who sees what |
| Mem0g | "Memory graph" | Typed edges with temporal validity for relationship queries |
| Temporal invalidation | "Soft delete" | Mark contradicted edges invalid; never delete |
| Embedding drift | "Retrieval rot" | Vector quality degrades as corpus grows; re-embed periodically |

## Further Reading

- [Chhikara et al., Mem0 (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413) — the original paper
- [Mem0 docs](https://docs.mem0.ai/platform/overview) — production API, SDKs, managed cloud
- [Packer et al., MemGPT (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560) — the virtual-context predecessor
- [Letta, Memory Blocks blog](https://www.letta.com/blog/memory-blocks) — the three-tier sibling design

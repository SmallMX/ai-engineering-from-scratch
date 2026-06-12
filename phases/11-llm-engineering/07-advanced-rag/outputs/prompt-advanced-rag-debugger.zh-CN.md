---
name: prompt-advanced-rag-debugger
description: 进阶 RAG (Chunking, Reranking, Hybrid 搜索) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 11
lesson: 7
---

# 进阶 RAG (Chunking, Reranking, Hybrid 搜索)：中文使用说明

你将围绕本课主题 **进阶 RAG (Chunking, Reranking, Hybrid 搜索)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 11「LLM 工程」
- 课程：第 07 课「进阶 RAG (Chunking, Reranking, Hybrid 搜索)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: prompt-advanced-rag-debugger
description: Diagnose and fix RAG quality issues across retrieval, generation, and evaluation
phase: 11
lesson: 7
---

You are a RAG system debugger. Given a description of RAG failures or poor quality, diagnose the root cause and prescribe specific fixes.

Gather these diagnostics:

1. **Sample failing query**: the exact question that produced a bad result
2. **Retrieved chunks**: what was actually retrieved (top-k results with scores)
3. **Generated answer**: what the LLM produced
4. **Expected answer**: what the correct answer should have been
5. **Retrieval method**: vector only, BM25 only, or hybrid
6. **Chunk size and overlap**: current configuration

Diagnose using this decision tree:

**Is the correct chunk in the vector store at all?**
- No: the document was not indexed, or was chunked in a way that split the answer across chunk boundaries. Fix: re-chunk with overlap, or use smaller chunks.
- Yes: proceed to next check.

**Is the correct chunk in the top-50 retrieval results?**
- No: embedding mismatch. The query and document use different vocabulary. Fixes:
  - Add hybrid search (BM25 catches exact term matches)
  - Try HyDE to bridge the query-document gap
  - Rephrase the query using an LLM before searching
- Yes: proceed to next check.

**Is the correct chunk in the top-k (final results)?**
- No, but it's in top-50: the chunk is being retrieved but ranked too low. Fix:
  - Add a reranker (cross-encoder) to re-score the top-50
  - Increase k to include more candidates
  - Tune RRF fusion weights
- Yes: proceed to next check.

**Is the LLM ignoring the retrieved context?**
- Yes: the prompt template is weak. Fixes:
  - Add explicit instructions: "Answer ONLY based on the provided context"
  - Set temperature to 0
  - Place the retrieved context before the question (primacy effect)
  - Add "If the context does not contain the answer, say so"
- No: proceed to next check.

**Is the LLM hallucinating facts not in the context?**
- Yes: faithfulness failure. Fixes:
  - Lower temperature
  - Shorten the context (too much irrelevant context confuses the model)
  - Add a faithfulness check: ask a second LLM call to verify claims
  - Use chain-of-thought: "First, identify the relevant passage. Then, answer."

**Common failure patterns and fixes:**

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Wrong source retrieved | Vocabulary mismatch | Add BM25, try HyDE |
| Right source, low rank | Imprecise embeddings | Add reranker |
| Answer contradicts context | Hallucination | Lower temp, add faithfulness check |
| Answer too vague | Context too broad | Smaller chunks, parent-child strategy |
| Misses multi-part questions | Single retrieval pass | Decompose query into sub-queries |
| Stale information returned | Index not updated | Re-index changed documents |
| Same chunk retrieved for everything | Chunk too generic | Improve chunking, add metadata filters |

For each diagnosis, provide:
- The specific root cause
- The recommended fix with implementation details
- How to verify the fix worked (a test to run)

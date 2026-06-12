---
name: skill-rag-pipeline
description: RAG (检索-Augmented Generation) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 11
lesson: 6
---

# RAG (检索-Augmented Generation)：中文使用说明

你将围绕本课主题 **RAG (检索-Augmented Generation)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 11「LLM 工程」
- 课程：第 06 课「RAG (检索-Augmented Generation)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-rag-pipeline
description: Build and debug RAG pipelines from first principles
version: 1.0.0
phase: 11
lesson: 6
tags: [rag, retrieval, embeddings, vector-search, llm-engineering]
---

# RAG Pipeline Pattern

Every RAG system follows this pattern:

```
documents -> chunk -> embed -> store
query -> embed -> search(top_k) -> build_prompt -> generate
```

Indexing happens once per document. Querying happens on every user request.

## When to use RAG

- The LLM needs access to private or recent documents
- Fine-tuning is too expensive or too slow to update
- You need to cite sources for answers
- The knowledge base changes frequently

## When NOT to use RAG

- The answer is general knowledge the LLM already has
- The task is creative (writing, brainstorming) not factual
- You need the model to adopt a specific reasoning style (use fine-tuning)

## Implementation checklist

1. Chunk documents into 256-512 token segments with 50-token overlap
2. Embed each chunk using a consistent embedding model
3. Store embeddings in a vector database with the original text
4. At query time, embed the user's question with the same model
5. Retrieve top-k (5-10) most similar chunks via cosine similarity
6. Build a prompt: system instruction + retrieved context + user question
7. Generate the answer, grounding it in the retrieved context
8. Return the answer with source references

## Common mistakes

- Using different embedding models for indexing and querying (vectors are incompatible)
- Chunks too small (lose context) or too large (dilute relevance)
- Not including overlap between chunks (splits sentences at boundaries)
- Forgetting to re-index when documents change
- Returning retrieved chunks to the user without generating a coherent answer
- Not setting temperature=0 for factual RAG queries (higher temperature = more hallucination)

## Debugging retrieval

If the right chunks are not being retrieved:
1. Print the query embedding and verify it's non-zero
2. Check cosine similarities manually for a known-relevant chunk
3. Try rephrasing the query to match document vocabulary
4. Verify the embedding model matches between index and query time
5. Check if the relevant content was lost during chunking

## Production parameters

- Chunk size: 256-512 tokens
- Overlap: 50 tokens (10-20% of chunk size)
- Top-k: 5-10 for most use cases
- Temperature: 0 for factual answers
- Embedding model: text-embedding-3-small (cost effective) or text-embedding-3-large (higher accuracy)

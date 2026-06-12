---
name: skill-context-engineering
description: 上下文工程：Windows, Budgets, 记忆,与检索 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 11
lesson: 5
---

# 上下文工程：Windows, Budgets, 记忆,与检索：中文使用说明

你将围绕本课主题 **上下文工程：Windows, Budgets, 记忆,与检索** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 11「LLM 工程」
- 课程：第 05 课「上下文工程：Windows, Budgets, 记忆,与检索」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-context-engineering
description: Decision framework for designing context assembly pipelines based on task type, window size, and latency budget
version: 1.0.0
phase: 11
lesson: 05
tags: [context-engineering, context-window, rag, memory, tool-selection, lost-in-the-middle]
---

# Context Engineering

When building an LLM application, apply this framework to design the context assembly pipeline.

## Core principles

1. **Context is scarce.** A 128K window sounds large but fills fast. Budget every component explicitly.
2. **Attention is uneven.** Models attend more to the start and end. Put critical information there. The middle is the dead zone.
3. **Dynamic beats static.** Different queries need different context. Assemble per query, not once at startup.
4. **Less is more.** A curated 10K context outperforms a dumped 100K context. Signal-to-noise ratio matters more than total information.
5. **Measure everything.** You cannot optimize what you do not measure. Count tokens per component on every request.

## Context budget guidelines

| Component | Typical Range | Priority | Compression Strategy |
|-----------|-------------|----------|---------------------|
| System prompt | 200-1,000 tokens | Fixed, high | Write tight, remove redundancy |
| Tool definitions | 500-3,000 tokens | Dynamic, medium | Prune by query intent |
| Retrieved context | 1,000-5,000 tokens | Dynamic, high | Rerank + threshold + deduplicate |
| Conversation history | 500-5,000 tokens | Dynamic, medium | Summarize old turns |
| Few-shot examples | 500-2,000 tokens | Dynamic, high | Select by task similarity |
| User query | 50-500 tokens | Fixed, highest | N/A |
| Generation reserve | 2,000-8,000 tokens | Fixed | Adjust by expected output length |

## When to use each memory type

**Short-term (conversation history):** The current session. Managed by summarization. Compress turns older than 5-10 exchanges. Keep the last 3-4 turns verbatim.

**Long-term (facts database):** Preferences and project facts that persist across sessions. Retrieve on session start. Examples: "user prefers Python", "project uses PostgreSQL", "team follows trunk-based development". Store in CLAUDE.md, a database, or a structured memory system.

**Episodic (past interactions):** Specific past conversations relevant to the current task. Store as embeddings, retrieve by similarity. "Last week we debugged a similar auth issue" is episodic memory.

## Tool selection strategy

Do not include all tools in every request. This wastes tokens and confuses the model.

1. Classify the query intent (code, email, calendar, research, data)
2. Map intents to tool categories
3. Include only matching tools
4. If intent is ambiguous, include tools from the top 2 categories
5. Always include a "general" tool (like web search) as fallback

Expected savings: 60-80% of tool definition tokens on queries with clear intent.

## Retrieval best practices

- **Rerank after retrieval.** Vector similarity is a rough filter. A reranker (cross-encoder or LLM-based) improves precision significantly.
- **Set a relevance threshold.** Do not include chunks below 0.3 cosine similarity. They add noise.
- **Deduplicate.** If two chunks share 80%+ content, keep only the higher-scored one.
- **Apply lost-in-the-middle ordering.** Place the most relevant chunks first and last.
- **Limit total retrieval tokens.** 3-5 highly relevant chunks beat 15 mediocre ones.

## History management

- Keep the last 3-4 turns verbatim (the model needs recent context)
- Summarize older turns into a digest ("We discussed X, decided Y, and blocked on Z")
- Drop system-generated turns that add no information (tool invocations with no user-facing content)
- Trigger compression when history exceeds 30% of the available budget

## Red flags

- System prompt exceeds 2,000 tokens: probably includes information that should be dynamic
- All tools included on every request: implement intent-based selection
- No relevance filtering on retrieval: you are dumping noise into the window
- History grows unbounded: summarization is not implemented
- No generation reserve: the model truncates its responses
- Same information in 3 places (system prompt, retrieved doc, history): deduplicate
- Context utilization over 60%: you are leaving too little room for the model to "think"

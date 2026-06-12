---
name: skill-virtual-memory
description: 记忆：Virtual Context与MemGPT 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 7
---

# 记忆：Virtual Context与MemGPT：中文使用说明

你将围绕本课主题 **记忆：Virtual Context与MemGPT** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 07 课「记忆：Virtual Context与MemGPT」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: virtual-memory
description: Scaffold a MemGPT-shaped two-tier memory system (main context + archival store + memory tools) for any target runtime with correct eviction, citation, and untrusted-input handling.
version: 1.0.0
phase: 14
lesson: 07
tags: [memory, memgpt, virtual-context, archival, citations]
---

Given a target runtime (Python, Node, Rust), a model provider (Anthropic, OpenAI, local), and a storage backend (in-memory, SQLite, vector DB, KV, graph), produce a correct MemGPT-shaped memory system.

Produce:

1. A `MainContext` type with a `core` dict (named persistent sections) and a `messages` list (FIFO). Auto-evict on size cap; evicted turns remain retrievable by `conversation_search`.
2. An `ArchivalStore` with insert and search. Records MUST carry `id`, `text`, `tags`, `session_id`, `turn_id`, `created_at`. Every write returns the stored id for citation.
3. Five memory tools matching the MemGPT surface: `core_memory_append`, `core_memory_replace`, `archival_memory_insert`, `archival_memory_search`, `conversation_search`. Present them to the model with `description` text that tells the model when to use each.
4. A citation contract: every archival retrieval MUST return record ids alongside text, and the agent MUST cite them in final answers. Answers without citations are a soft failure.
5. A consolidation hook (can be a no-op in v1) so Lesson 08 sleep-time agents can plug in without re-plumbing. Expose `list_records_since(timestamp)` and `delete(id)`.

Hard rejects:

- Searching archival with full-prompt LLM scoring. Use a proper retrieval backend (BM25, vector similarity). LLM re-ranking is allowed on the top-k shortlist, not the full corpus.
- Main context with no eviction policy. Unbounded main context silently grows past the window.
- Storing retrieved content as if it were user instructions. All archival content is untrusted text (Lesson 27). Pass it to the model as observation, not as system prompt.
- Writing a `core_memory_clear` tool that wipes all sections. Core is load-bearing; clearing is a foot-gun. Support `replace` not `clear`.

Refusal rules:

- If the user asks for "no citations, just answers," refuse for any domain where source attribution matters (medical, legal, policy, financial). Offer a compromise: citations rendered as footnotes rather than inline.
- If the user asks for "write all retrieved content back to archival without filtering," refuse and point to Lesson 27. Retrieved content is attacker-reachable; blanket write-back is memory poisoning.
- If the runtime has no persistence layer, refuse to ship an agent described as having "long-term memory." Downgrade the product description, not the implementation.

Output: one file per component (`main_context.*`, `archival_store.*`, `memory_tools.*`, `agent.*`) plus a `README.md` explaining the eviction policy, citation contract, and where to plug in Lesson 08 (sleep-time consolidation) and Lesson 09 (Mem0 fusion). End with "what to read next" pointing to Lesson 08 if the agent needs three tiers or async consolidation, or Lesson 09 if the agent needs vector+KV+graph fusion.

---
name: skill-memory-blocks
description: 记忆 Blocks与Sleep-Time Compute (Letta) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 8
---

# 记忆 Blocks与Sleep-Time Compute (Letta)：中文使用说明

你将围绕本课主题 **记忆 Blocks与Sleep-Time Compute (Letta)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 08 课「记忆 Blocks与Sleep-Time Compute (Letta)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: memory-blocks
description: Generate a Letta-shaped three-tier memory system (core blocks, recall, archival) with a sleep-time consolidation agent off the critical path.
version: 1.0.0
phase: 14
lesson: 08
tags: [memory, letta, blocks, sleep-time, consolidation]
---

Given a target runtime, a primary model, and a (possibly stronger) sleep-time model, produce a three-tier memory system with explicit block types and async consolidation.

Produce:

1. `Block` type with `label`, `value`, `limit`, `description`, `version`, `history`. Every write bumps version and records the old value. Expose `near_limit(threshold=0.8)`.
2. A `BlockStore` with at minimum three default blocks: `human` (facts about the user), `persona` (agent self-concept), and `task` (current scope). Allow user-defined blocks.
3. A `Recall` store — turn log paginated by session. Auto-write every turn. Tail evicts on cap but remains retrievable.
4. An `Archival` store — at least two backends (vector, KV). Insert returns record id. Invalidate rather than delete on contradiction.
5. A `PrimaryAgent` that handles turns and only issues raw writes. No summarization on the critical path.
6. A `SleepTimeAgent` that runs between turns: summarize blocks over threshold, invalidate contradicted archival records, write `learned_context` into shared blocks.

Hard rejects:

- Any memory op that runs synchronously during a user-facing turn except a direct lookup. Summarization, consolidation, invalidation belong to the sleep-time pass.
- Deleting archival records on contradiction. Invalidate so history remains auditable.
- Writing to the Persona or Safety block without a review step. These blocks shape behavior globally; silent writes mask bugs.

Refusal rules:

- If the runtime cannot persist blocks across sessions, refuse to ship a product described as "memory." Downgrade the claim.
- If the sleep-time agent has no trace output, refuse. Silent consolidation is a debugging dead-zone.
- If the user asks for "no invalidation, always trust latest write," refuse for any domain where historical claims matter (compliance, medical, legal).

Output: one file per component plus a `README.md` that names the default blocks, the sleep-time cadence, and the contradiction resolution policy. End with "what to read next" pointing to Lesson 09 if the agent needs graph reasoning over memory, or Lesson 23 if the product needs OTel spans on memory ops.

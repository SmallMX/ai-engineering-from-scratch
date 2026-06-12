---
name: skill-task-store-designer
description: Async Tasks (SEP-1686)：Call-Now, Fetch-Later for Long-Running Work 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 13
---

# Async Tasks (SEP-1686)：Call-Now, Fetch-Later for Long-Running Work：中文使用说明

你将围绕本课主题 **Async Tasks (SEP-1686)：Call-Now, Fetch-Later for Long-Running Work** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 13 课「Async Tasks (SEP-1686)：Call-Now, Fetch-Later for Long-Running Work」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: task-store-designer
description: Design the task store for a long-running MCP tool: state shape, ttl, durability, cancellation, crash recovery.
version: 1.0.0
phase: 13
lesson: 13
tags: [mcp, tasks, durable-store, long-running, sep-1686]
---

Given a long-running tool (research, build, export, report generation), design the task store that backs SEP-1686 task augmentation.

Produce:

1. State shape. Minimum fields: `id`, `state`, `progress`, `result`, `error`, `ttl`, `created_at`. Optional: `request_meta`, `parent_task_id` (for future subtasks).
2. Durability choice. Filesystem for toy; SQLite for single-process; Redis for multi-replica. Justify.
3. taskSupport flag. `forbidden`, `optional`, or `required` per tool; one-line justification.
4. Cancellation plan. How the worker checks a cancel signal; what happens on partial progress.
5. Crash recovery. Boot-time reload rule; what `CRASH_RECOVERY` failures look like to the client.

Hard rejects:
- Any store that loses completed results within ttl.
- Any task state without explicit terminal states (`completed`, `failed`, `cancelled`).
- Any cancellation that is not idempotent.

Refusal rules:
- If the tool runs under 5 seconds, refuse to promote to a task. Synchronous is simpler.
- If the task would generate more than 10 MB of result, refuse and recommend streaming content blocks.
- If the server does not have a process capable of persisting state (stateless edge function), refuse and recommend moving to a durable runtime.

Output: a one-page store design with state shape, durability choice, taskSupport flag, cancellation plan, and crash-recovery rule. End with one-line advice on whether SEP-1686 subtasks will affect this design when they ship.

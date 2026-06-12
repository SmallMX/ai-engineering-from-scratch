---
name: skill-runtime-shape
description: 生产 Runtimes：Queue, Event, Cron 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 29
---

# 生产 Runtimes：Queue, Event, Cron：中文使用说明

你将围绕本课主题 **生产 Runtimes：Queue, Event, Cron** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 29 课「生产 Runtimes：Queue, Event, Cron」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: runtime-shape
description: Pick a production runtime shape (request-response, streaming, queue, event, cron, durable) and wire observability.
version: 1.0.0
phase: 14
lesson: 29
tags: [production, runtime, queue, event, durable, observability]
---

Given a task class (expected duration, step count, trigger type, latency budget), pick the runtime shape.

Decision:

1. < 30s, user waits -> **request-response**.
2. Progressive UX or voice -> **streaming**.
3. Minutes to hours, user doesn't wait -> **queue-based**.
4. Reactive to external events -> **event-driven**.
5. Periodic housekeeping -> **cron**.
6. Any of the above where restart cost is high -> add **durable execution**.

Produce:

1. The shape scaffold in your stack.
2. Observability: OTel GenAI spans (Lesson 23), backend wired (Lesson 24).
3. For queue: DLQ + retry policy + queue depth metric.
4. For event: explicit subscriber registry + replay path.
5. For cron: lock file or distributed lock to prevent overlapping runs.
6. For durable: checkpointer backend + resume semantics.

Hard rejects:

- Synchronous HTTP for a 5-minute task. Users hang up; workers pile up.
- Queue-based without DLQ. Failed jobs vanish.
- Background work without trace export. Failures invisible until users complain.
- "No durable state, we'll just retry." Long horizons must checkpoint.

Refusal rules:

- If the product has SLA + replay requirements, refuse swarm topology + non-durable runtime.
- If the task is compliance-bound, refuse event-driven without audit trail.
- If the user wants cron + no lock, refuse. Overlapping cron runs are duplicate work at best, data corruption at worst.

Output: runtime scaffold + observability hooks + README with SLA, retry policy, checkpointer choice. End with "what to read next" pointing to Lesson 23 (OTel), Lesson 24 (observability), or Lesson 17 (Managed Agents for hosted long-running).

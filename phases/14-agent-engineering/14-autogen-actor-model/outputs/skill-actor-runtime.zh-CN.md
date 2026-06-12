---
name: skill-actor-runtime
description: AutoGen v0.4：Actor Model与智能体 框架 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 14
---

# AutoGen v0.4：Actor Model与智能体 框架：中文使用说明

你将围绕本课主题 **AutoGen v0.4：Actor Model与智能体 框架** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 14 课「AutoGen v0.4：Actor Model与智能体 框架」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: actor-runtime
description: Build an AutoGen v0.4-shaped actor runtime with private state, inbox-per-actor, message-only IPC, fault isolation, and a dead-letter queue.
version: 1.0.0
phase: 14
lesson: 14
tags: [autogen, actor-model, messaging, fault-isolation, dead-letter]
---

Given a multi-agent task, produce an actor runtime and the agent actors needed.

Produce:

1. A `Message` type with `sender`, `recipient`, `topic`, `body`, `mid`.
2. An `Actor` base class with `receive(message, runtime)`. Actor state is private.
3. A `Runtime` with a shared queue, `send()`, `run_until_idle()`, and a dead-letter queue. Exceptions in handlers go to DLQ; do not propagate.
4. One topology helper: RoundRobin (fixed rotation), Selector (LLM picks next), or custom broadcast.
5. Observability hooks per message: emit OTel spans with `gen_ai.agent.name` and `gen_ai.operation.name` per Lesson 23.

Hard rejects:

- Synchronous message passing that blocks the sender until the recipient returns. That is the v0.2 model; it breaks fault isolation.
- Shared mutable state across actors. Actors read state via messages or not at all.
- A runtime that propagates handler exceptions. Failures belong in the DLQ; let other actors keep running.

Refusal rules:

- If the task has only two actors with a fixed back-and-forth, refuse the actor framing and suggest a prompt chain (Lesson 12). Actors earn cost when there are >=3 actors or async concurrency.
- If the user wants "synchronous mode" for "easier debugging," refuse. Suggest logging + tracing (Lesson 23) instead.
- If the domain is strictly request/response with a single specialist, suggest routing (Lesson 12) instead of an actor team.

Output: `message.py`, `actor.py`, `runtime.py`, `teams.py`, `README.md` explaining DLQ policy, the topology choice, and how OTel spans are wired. End with "what to read next" pointing to Lesson 25 (multi-agent debate) if actors negotiate, Lesson 23 (OTel) if tracing is required, or Microsoft Agent Framework if you want the forward-looking runtime.

---
name: skill-state-graph
description: LangGraph：Stateful Graphs与Durable Execution 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 13
---

# LangGraph：Stateful Graphs与Durable Execution：中文使用说明

你将围绕本课主题 **LangGraph：Stateful Graphs与Durable Execution** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 13 课「LangGraph：Stateful Graphs与Durable Execution」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: state-graph
description: Build a LangGraph-shaped state machine with typed state, conditional edges, per-node checkpointing, and durable resume.
version: 1.0.0
phase: 14
lesson: 13
tags: [langgraph, state-machine, durable, checkpointing, human-in-the-loop]
---

Given a target runtime, a state shape, a set of node functions, and a checkpointer backend, produce a stateful agent graph.

Produce:

1. A typed `State` (dict or Pydantic). Document every field. Nodes read state; they return updates.
2. A `StateGraph` with `add_node`, `add_edge`, `add_conditional_edges`, `set_entry`, plus `START`/`END` sentinels.
3. A `Checkpointer` interface with `save(session_id, node, state)` and `load_latest(session_id)`. Default to SQLite; allow Postgres/Redis/custom.
4. A `Runner` that steps through the graph, serializes state after every node, catches `PausedAtNode` for human-in-the-loop, and supports `resume_from` with optional `state_override`.
5. Three topology helpers: supervisor (central router), swarm (shared-tool handoffs), hierarchical (subgraphs).

Hard rejects:

- Non-deterministic nodes without explicit random-seed or wall-clock capture. Resume assumes node output is reproducible given input state.
- A checkpointer that only saves "summary" state. Serialize the full state or resume breaks.
- Graphs where every edge is conditional. Prefer linear chains with occasional branches.

Refusal rules:

- If the user asks for a state graph without persistence, refuse. The whole point is durable resume; if you don't need resume, use the workflow patterns in Lesson 12.
- If the user asks to "checkpoint only on success," refuse. Failures need state too — that's where debugging starts.
- If the graph has more than ~30 nodes, refuse flat layout and require nested subgraphs. Flat 30-node graphs are unreviewable.

Output: `state.py`, `graph.py`, `checkpointer.py`, `runner.py`, `README.md` explaining the state schema, checkpointer choice, and resume semantics. End with "what to read next" pointing to Lesson 14 for actor-model alternative, Lesson 16 for handoffs/guardrails layer, or Lesson 23 for OTel spans on graph steps.

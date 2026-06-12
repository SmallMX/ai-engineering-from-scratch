---
name: skill-swarm-fit
description: Parallel / Swarm / Networked Architectures 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 9
---

# Parallel / Swarm / Networked Architectures：中文使用说明

你将围绕本课主题 **Parallel / Swarm / Networked Architectures** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 09 课「Parallel / Swarm / Networked Architectures」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: swarm-fit
description: Decide whether a task fits a swarm (decentralized) architecture or a supervisor (centralized) one.
version: 1.0.0
phase: 16
lesson: 09
tags: [multi-agent, swarm, decentralized, langgraph, matrix]
---

Given a task and its throughput / determinism requirements, recommend swarm or supervisor and list the specific queue and guardrail choices.

Produce:

1. **Task independence check.** Are subtasks independent or do they depend on each other? Swarm only fits when independence is high.
2. **Duration distribution.** Uniform vs variable. Swarm wins mostly on variable-duration workloads.
3. **Ordering requirement.** Strict, relaxed, or none. Swarm does not preserve order; supervisor does.
4. **Debuggability need.** High (finance, medical) → supervisor. Medium → swarm with per-task trace IDs.
5. **Queue choice.** In-memory (`queue.Queue`) for demos; Kafka / Redis Streams / NATS / durable DB-backed for production.
6. **Worker design requirements.** Must be idempotent; must emit per-task trace; must handle back-pressure.
7. **Anti-starvation plan.** Priority aging, worker specialization, bounded queue.
8. **Observability plan.** Per-task IDs, start/end events, result pool schema.

Hard rejects:

- Swarm recommendation for tasks with hard ordering requirements.
- Swarm without idempotent workers.
- Swarm without durable queue in production.

Refusal rules:

- If the task has fewer than 10 independent units per second, refuse swarm and recommend supervisor. Swarm overhead is not justified at low throughput.
- If observability requirements need a single coherent trace (audit, compliance), refuse swarm and recommend LangGraph deterministic graph instead.

Output: a one-page architectural brief. Open with the fit verdict, close with the specific message broker recommendation for the target throughput.

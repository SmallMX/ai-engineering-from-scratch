---
name: skill-handoff-designer
description: Handoffs与Routines：Stateless Orchestration 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 11
---

# Handoffs与Routines：Stateless Orchestration：中文使用说明

你将围绕本课主题 **Handoffs与Routines：Stateless Orchestration** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 11 课「Handoffs与Routines：Stateless Orchestration」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: handoff-designer
description: Design a handoff topology for a Swarm/Agents-SDK-style system: which agents exist, which handoffs they can call, what context transfers.
version: 1.0.0
phase: 16
lesson: 11
tags: [multi-agent, swarm, handoff, openai-agents-sdk]
---

Given a user-facing task (often triage or skill-based routing), produce a handoff topology ready to map onto OpenAI Swarm or the OpenAI Agents SDK.

Produce:

1. **Agent roster.** Each agent: name, one-sentence purpose, tools, and which other agents it can hand off to.
2. **Handoff functions.** The tool signatures per agent. Each handoff function returns a target Agent.
3. **Context transfer policy.** On each handoff edge: full history, last N messages, or summarized snapshot. Justify.
4. **Guardrails.** Input validation per agent (what prompts are allowed to trigger handoffs to sensitive specialists), authentication on handoff where needed.
5. **Loop detection.** Rule to detect ping-pong (e.g., "A handed off to B; B handed off back to A" occurring more than once in a row).
6. **Fallback behavior.** If a handoff target is missing (removed agent, auth failure), which agent handles the session.
7. **Session / memory plan.** Whether to use Agents SDK sessions, caller-managed memory, or no memory at all.

Hard rejects:

- Any handoff design without loop detection.
- Handoff functions that pass full history to specialists with different tool permissions (security risk).
- Designs that assume Swarm's stateless behavior but then require multi-turn memory — use Agents SDK sessions instead.

Refusal rules:

- If the task needs parallel execution, refuse Swarm and recommend supervisor (Lesson 05) instead.
- If the task needs deterministic audit/replay, refuse and recommend LangGraph static graph.
- If the task is a simple DAG of stages (research → code → review), recommend CrewAI Sequential instead.

Output: a one-page handoff brief. Close with a security note on how prompt injection could trigger unwanted handoffs and what guardrails block it.

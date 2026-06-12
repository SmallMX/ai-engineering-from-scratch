---
name: skill-framework-picker
description: 智能体 框架 Tradeoffs：LangGraph vs CrewAI vs AutoGen vs Agno 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 11
lesson: 17
---

# 智能体 框架 Tradeoffs：LangGraph vs CrewAI vs AutoGen vs Agno：中文使用说明

你将围绕本课主题 **智能体 框架 Tradeoffs：LangGraph vs CrewAI vs AutoGen vs Agno** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 11「LLM 工程」
- 课程：第 17 课「智能体 框架 Tradeoffs：LangGraph vs CrewAI vs AutoGen vs Agno」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: framework-picker
description: Pick LangGraph, CrewAI, AutoGen, Agno, or plain Python for an agent task by matching abstraction to problem shape.
version: 1.0.0
phase: 11
lesson: 17
tags: [langgraph, crewai, autogen, agno, agent-framework, orchestration, decision-matrix]
---

Given the task description (problem shape, total LLM calls per run, branching pattern, durability and resume needs, human-in-the-loop checkpoints, parallel fanout, session memory, expected daily run volume), output:

1. Shape match. One sentence naming the abstraction that fits: graph (typed state, named transitions), org chart (specialist roles, manager-routed handoffs), chat (agents talk until done), single agent with tools. If you cannot pick one, the task is not agent-shaped yet; stop and decompose.
2. Branching authority. Who picks the next step: developer (explicit edges), manager LLM (CrewAI hierarchical), conversational emergent (AutoGen GroupChat), tool-call self-routed (Agno). Cite the per-turn token cost of LLM-selected routing if applicable.
3. State budget. Confirm whether resume-after-restart, time-travel, or human interrupts are required. If yes, LangGraph wins on state-first abstractions; Agno covers session-scoped memory only.
4. Framework choice. Output one of langgraph, crewai, autogen, agno, plain_python. Include the one-sentence justification that maps the shape and state answers onto the framework's core abstraction.
5. Escape hatch. If the daily run volume is over 10_000 or the task is two or fewer LLM calls without state, recommend plain Python with the provider SDK instead. No framework is the fastest framework when the task is small.

Refuse to recommend AutoGen for deterministic workflows with a known DAG; the GroupChatManager spends tokens picking speakers that the developer could have wired statically. CrewAI does support structured task outputs via `output_pydantic` / `output_json` (see [docs.crewai.com/en/concepts/tasks](https://docs.crewai.com/en/concepts/tasks)), but its `context` channel still flows through the next task's prompt string. Push back on CrewAI when the workflow relies on raw `context` to carry structured state across tasks without one of those output schemas wired up. Push back on LangGraph for a two-call summarizer; the StateGraph overhead is pure tax. Push back on Agno when the task fans out across more than 4 parallel sub-workers with reducer semantics; Agno ships a `Parallel` block whose outputs join into a dict keyed by step name (see [docs-v1.agno.com/workflows_2/overview](https://docs-v1.agno.com/workflows_2/overview) and [docs.agno.com/workflows/access-previous-steps](https://docs.agno.com/workflows/access-previous-steps)), but it does not expose a Send-style fanout-and-reduce API comparable to LangGraph's.

Example input: "Long-running research workflow: plan, fan out to three retrievers, synthesize, human approves brief, write report, cite sources. Must resume after crash. Production-bound to 50 runs per day."

Example output:
- Shape: graph. Typed plan, three parallel retrievers, named transitions between synthesize and write.
- Branching: developer-decided via conditional edges. No per-turn manager LLM.
- State: requires resume and human interrupt. LangGraph mandatory.
- Framework: langgraph. State, Send fanout, interrupt_before, and PostgresSaver are all first-class.
- Escape hatch: not applicable. 50 runs per day is well below the plain-Python threshold and the workflow is too stateful to leave unframeworked.

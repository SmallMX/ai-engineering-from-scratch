---
name: skill-orchestration-picker
description: Orchestration Patterns：Supervisor, Swarm, Hierarchical 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 28
---

# Orchestration Patterns：Supervisor, Swarm, Hierarchical：中文使用说明

你将围绕本课主题 **Orchestration Patterns：Supervisor, Swarm, Hierarchical** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 28 课「Orchestration Patterns：Supervisor, Swarm, Hierarchical」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: orchestration-picker
description: Pick an orchestration topology (supervisor, swarm, hierarchical, debate, or none) for a given problem and implement it minimally.
version: 1.0.0
phase: 14
lesson: 28
tags: [orchestration, supervisor, swarm, hierarchical, debate]
---

Given a product domain and a task class, pick the minimal topology.

Decision:

1. 1 agent + workflow patterns (Lesson 12) suffice? -> don't use topology at all.
2. 2-4 specialists with distinct responsibilities? -> **supervisor-worker**.
3. Latency-critical and specialists can cleanly hand off? -> **swarm**.
4. 10+ specialists, supervisor context budget failing? -> **hierarchical**.
5. Accuracy matters more than cost, multi-proposer + critique helps? -> **debate** (Lesson 25).

Produce:

1. The chosen topology scaffold.
2. Hop counter on swarm; nesting depth limit on hierarchical; round cap on debate.
3. Observability hooks per handoff or per step (OTel GenAI spans, Lesson 23).
4. A "why this, not that" README section.

Hard rejects:

- Calling 3 LLM calls in sequence "multi-agent." That's a prompt chain.
- Swarm without hop counter. Bouncing is a certainty.
- Hierarchical that bottoms out at 1 specialist per branch. Flatten.

Refusal rules:

- If the user wants multi-agent for a task that a single ReAct loop handles, refuse and suggest Lesson 01.
- If the user wants supervisor for a 2-step task, refuse and suggest prompt chaining (Lesson 12).
- If the domain has compliance / audit requirements, refuse swarm and suggest supervisor or hierarchical.

Output: topology scaffold + README with decision rationale. End with "what to read next" pointing to Lesson 13 (LangGraph) for supervisor implementation, Lesson 16 (OpenAI Agents SDK) for handoffs-as-tools, or Lesson 25 for debate specifics.

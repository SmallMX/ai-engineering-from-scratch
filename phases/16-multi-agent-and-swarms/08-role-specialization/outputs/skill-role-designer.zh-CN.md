---
name: skill-role-designer
description: Role Specialization：Planner, Critic, Executor, Verifier 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 8
---

# Role Specialization：Planner, Critic, Executor, Verifier：中文使用说明

你将围绕本课主题 **Role Specialization：Planner, Critic, Executor, Verifier** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 08 课「Role Specialization：Planner, Critic, Executor, Verifier」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: role-designer
description: Produce a role roster for a multi-agent system, naming the planner/executor/critic/verifier for a given task with explicit I/O schemas.
version: 1.0.0
phase: 16
lesson: 08
tags: [multi-agent, role-specialization, metagpt, chatdev, verification]
---

Given a task, produce a specialized role roster with I/O schemas and a deterministic verifier. Ready to map onto CrewAI, LangGraph, AutoGen, or custom loops.

Produce:

1. **Role roster.** 3-5 roles. Name each. At minimum: planner, executor, verifier. Critic optional.
2. **I/O schema per role.** For each role: what it consumes (from upstream role) and what it produces (schema, not prose). Use dataclass-style notation.
3. **Verifier specification.** Name the deterministic check: test suite, type checker, schema validator, linter. Describe pass/fail criteria.
4. **Critic specification (optional).** If included, name what subjective quality it judges. Concrete checklist, not "good code."
5. **Communicative dehallucination rules.** Name the questions each downstream role is allowed to send upstream when a detail is missing, so they do not invent.
6. **Revision loop budget.** Max rounds before escalation to human. Default 2.
7. **Framework mapping.** One-line each: how to express this roster in CrewAI, LangGraph, AutoGen.

Hard rejects:

- Any roster without a deterministic verifier. All-LLM rosters fail the MAST check.
- Fuzzy I/O ("the executor returns output"). Always state the schema.
- Critic and verifier conflated. They catch different bugs; both must exist if both are warranted.

Refusal rules:

- If the task has no deterministic correctness check (pure generative work, creative writing), refuse and recommend either a human reviewer loop or a multi-agent debate (Lesson 07) instead.
- If the task is too small for 3+ roles (under 10 minutes of human work), refuse and recommend single-agent.

Output: a one-page role-design brief. Close with the MAST failure-gap check: confirm at least one deterministic verifier exists.

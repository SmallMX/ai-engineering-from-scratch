---
name: skill-primitive-mapper
description: The 多智能体 Primitive Model 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 4
---

# The 多智能体 Primitive Model：中文使用说明

你将围绕本课主题 **The 多智能体 Primitive Model** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 04 课「The 多智能体 Primitive Model」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: primitive-mapper
description: Map any multi-agent framework or codebase to the four primitive axes (agent, handoff, shared state, orchestrator).
version: 1.0.0
phase: 16
lesson: 04
tags: [multi-agent, primitives, framework-comparison, architecture]
---

Given a multi-agent framework (or a codebase that uses one), produce the four-primitive mapping so the reader can understand the framework in one paragraph.

Produce:

1. **Agent definition.** How is an agent constructed? What parameters? What state does it carry? Name the exact class or factory.
2. **Handoff mechanism.** Which of the three handoff patterns does it use — function return, graph edge, or speaker selection? If a hybrid, which is primary? Show the minimum code that triggers one handoff.
3. **Shared state model.** Full message pool or projected view? In-memory or durable (checkpointed)? Is it thread-safe for concurrent writers? Who reconciles conflicts?
4. **Orchestrator type.** Static, LLM-selected, handoff-driven, or queue-driven? If LLM-selected, which model by default? If static, is the graph cyclic or DAG?
5. **Cross-axis tradeoffs.** One sentence each on: determinism, scalability ceiling, debuggability, typical failure mode.

Hard rejects:

- Any mapping that claims an abstraction is "new" without showing it does not collapse to one of the four primitives. If you cannot reduce it, name the gap precisely rather than inventing a fifth primitive.
- Framework comparisons that only cite marketing docs. Always cite a concrete code example from the framework's repository or official cookbook.
- Statements like "Framework X is better for agents" without specifying which primitive the framework optimizes.

Refusal rules:

- If the framework is closed-source and the public docs do not expose the agent-handoff-state-orchestrator surface, state that mapping is not possible without internals.
- If the user supplies a codebase but no framework (hand-rolled agents), map the custom implementation instead and flag which primitive is under-designed.
- If the framework is older than 2024 (original AutoGen v0.2, pre-Swarm) and no longer maintained, include a one-line note on whether its successor preserves the mapping.

Output: a one-page framework brief. Start with a single-sentence summary ("Framework X fixes handoff as graph edge and exposes shared state via a reducer."), then the five sections above, then a closing paragraph naming which production project this framework's primitives fit best.

---
name: skill-a2a-agent-spec
description: A2A：智能体-to-智能体 协议 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 19
---

# A2A：智能体-to-智能体 协议：中文使用说明

你将围绕本课主题 **A2A：智能体-to-智能体 协议** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 19 课「A2A：智能体-to-智能体 协议」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: a2a-agent-spec
description: Produce the Agent Card and skills schema for an agent that should be callable over A2A.
version: 1.0.0
phase: 13
lesson: 18
tags: [a2a, agent-card, task-lifecycle, delegation]
---

Given an agent's capabilities and intended collaborators, produce its A2A Agent Card and skill definitions.

Produce:

1. Agent Card. `name`, `description`, `url`, `version`, `schemaVersion`, `capabilities` (streaming, pushNotifications), `skills[]`.
2. Skills list. Each with `id`, `name`, `description`, `inputModes`, `outputModes`. Use the "Use when X. Do not use for Y." pattern in descriptions.
3. Task-state plan. For each skill, expected state transitions and the input_required paths.
4. Signing plan. Whether to sign the card via AP2 (recommended for externally-callable agents).
5. Transport. JSON-RPC over HTTP (default) or gRPC. Note backward-compat with v1.0.

Hard rejects:
- Any Agent Card without a stable URL. Breaks discovery.
- Any skill without input and output modes declared. Callers cannot reason about compatibility.
- Any externally-callable agent without an AP2 signing plan. Impersonation vector.

Refusal rules:
- If the agent's use case is a single tool call, refuse to scaffold A2A; recommend MCP.
- If the agent exposes internals it should not (tool call traces, chain-of-thought), refuse and mandate opacity.
- If the agent needs A2A for payments (AP2 use case), confirm the AP2 extension version and flag that AP2 is separate from core A2A.

Output: a one-page Agent Card JSON, a skills schema for each operation, state-transition plan, signing and transport choices. End with the minimum v1.0 backward-compat guarantee the agent promises.

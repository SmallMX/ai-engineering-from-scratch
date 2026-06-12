---
name: skill-a2a-integrator
description: A2A：The 智能体-to-智能体 协议 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 12
---

# A2A：The 智能体-to-智能体 协议：中文使用说明

你将围绕本课主题 **A2A：The 智能体-to-智能体 协议** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 12 课「A2A：The 智能体-to-智能体 协议」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: a2a-integrator
description: Design an A2A integration between two agents — Agent Card, task schemas, auth, streaming or polling.
version: 1.0.0
phase: 16
lesson: 12
tags: [multi-agent, a2a, protocol, interoperability, google]
---

Given two agent systems that need to interoperate, produce the A2A integration plan: Agent Card contents, task schemas, auth, transport mode.

Produce:

1. **Agent Card.** Name, version, skills, endpoints, supported modalities (text, structured, image, audio, video), protocol_version, auth declaration.
2. **Task schemas per skill.** Input JSON schema + artifact JSON schema. Be explicit — clients will validate.
3. **Auth choice.** Bearer token (OAuth2 or opaque), mTLS, or signed requests. Justify given the threat model (public internet, VPC, mixed).
4. **Transport mode.** Polling vs SSE streaming vs webhook callbacks. Streaming for long-running or progress-heavy tasks; polling for short tasks.
5. **Rate limits.** Per-client and per-task limits. Protection from abuse.
6. **Idempotency.** Strategy for duplicate `POST /tasks` requests (client-side task-key, server-side deduplication).
7. **Failure handling.** Task states beyond `failed` (retriable vs fatal), dead-letter policy, error artifact schema.
8. **MCP vs A2A split.** If the remote agent uses MCP internally, note which tools are exposed vs kept internal.

Hard rejects:

- Agent Cards without a declared protocol version.
- Task schemas that are free-form text when the use case warrants structure.
- Auth=none on public-internet deployments.

Refusal rules:

- If both agents run in the same process, refuse A2A and recommend direct Python/JS calls. A2A is for cross-system boundaries.
- If latency requirements are sub-100ms round-trip, refuse A2A and recommend direct RPC with a shared schema.
- If the remote agent does not declare an Agent Card, refuse integration and recommend publishing one first.

Output: a one-page integration brief. Close with the Agent Card JSON pasted inline so engineering can drop it into `/.well-known/agent.json`.

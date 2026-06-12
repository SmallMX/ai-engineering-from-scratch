---
name: skill-gateway-bootstrap
description: MCP 网关与Registries：Enterprise Control Planes 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 17
---

# MCP 网关与Registries：Enterprise Control Planes：中文使用说明

你将围绕本课主题 **MCP 网关与Registries：Enterprise Control Planes** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 17 课「MCP 网关与Registries：Enterprise Control Planes」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: gateway-bootstrap
description: Produce a gateway configuration spec given users, backends, and compliance constraints.
version: 1.0.0
phase: 13
lesson: 17
tags: [mcp, gateway, rbac, audit, policy]
---

Given an enterprise MCP plan (users, backends, compliance constraints), produce the gateway configuration spec.

Produce:

1. Backend list. Each with its registry (Official / Glama / custom), canonical name (reverse-DNS), pinned description hashes.
2. User list. Each with a role and allowed-tool set.
3. RBAC matrix. One row per user x backend-tool, with allow/deny.
4. Rate limits. Per-user burst and sustained limits; per-tool limits for expensive tools.
5. Audit plan. Log destination (file, OpenTelemetry, SIEM), retention, fields captured.

Hard rejects:
- Any backend not in the Official Registry without explicit admin approval.
- Any RBAC rule allowing all users all tools. Privilege explosion.
- Any audit plan without immutable storage. Compliance fail.

Refusal rules:
- If a developer population exceeds 100 without any roles defined, refuse to bootstrap and require at least three roles.
- If the plan does not identify an OAuth 2.1 identity provider, refuse and recommend adopting Keycloak or Auth0 first.
- If any backend uses stdio, refuse to proxy it through the HTTP gateway; stdio servers run per-developer locally.

Output: a one-page config document with backend list, user list, RBAC matrix, rate limits, and audit plan. End with the single policy rule the team should implement first.

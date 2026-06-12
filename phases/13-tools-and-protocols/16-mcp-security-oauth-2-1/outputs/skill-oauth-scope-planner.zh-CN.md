---
name: skill-oauth-scope-planner
description: MCP 安全 II：OAuth 2.1, Resource Indicators, Incremental Scopes 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 16
---

# MCP 安全 II：OAuth 2.1, Resource Indicators, Incremental Scopes：中文使用说明

你将围绕本课主题 **MCP 安全 II：OAuth 2.1, Resource Indicators, Incremental Scopes** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 16 课「MCP 安全 II：OAuth 2.1, Resource Indicators, Incremental Scopes」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: oauth-scope-planner
description: Design the OAuth 2.1 scope set, pinning rules, and step-up policy for a remote MCP server.
version: 1.0.0
phase: 13
lesson: 16
tags: [oauth, pkce, resource-indicators, step-up, sep-835]
---

Given a remote MCP server with a tool list, design the authorization model.

Produce:

1. Scope hierarchy. Graduated scope set (e.g. `read` -> `write` -> `delete` -> `admin`). One scope per operation class; do not explode the scope set.
2. Scope-to-tool mapping. Each tool annotated with its required scope. Flag any tool that needs more than one scope.
3. Step-up policy. Which operations require step-up rather than an initial consent. Typical: destructive operations require step-up.
4. Resource indicator value. The canonical URL used in the `resource` parameter. Ensure the URL matches the `.well-known/oauth-protected-resource` resource field.
5. Protected-resource metadata. Draft `.well-known/oauth-protected-resource` JSON with `authorization_servers`, `scopes_supported`, and `resource`.

Hard rejects:
- Any tool that requires admin scope but is invoked without an explicit confirmation dialog. Needs step-up.
- Any scope that covers more than one operation class. Privilege creep.
- Any server that skips audience validation. Confused-deputy vulnerability.

Refusal rules:
- If the server is local (stdio), refuse OAuth and state that stdio inherits parent trust.
- If the server depends on a legacy OAuth 2.0 implicit flow, refuse and mandate migration to 2.1 + PKCE.
- If the user asks for passwordless "API key only" auth, refuse for remote servers; require OAuth 2.1 authorization code + PKCE with resource indicators for user-authorized access. Client credentials is only appropriate for machine-to-machine scenarios without user delegation.

Output: a one-page authorization plan with the scope hierarchy, scope-to-tool mapping, step-up policy, resource indicator, and the protected-resource metadata JSON. End with the step-up operation most likely to surprise users on first encounter.

---
name: skill-mcp-transport-migrator
description: MCP Transports：stdio vs Streamable HTTP vs SSE Migration 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 9
---

# MCP Transports：stdio vs Streamable HTTP vs SSE Migration：中文使用说明

你将围绕本课主题 **MCP Transports：stdio vs Streamable HTTP vs SSE Migration** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 09 课「MCP Transports：stdio vs Streamable HTTP vs SSE Migration」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mcp-transport-migrator
description: Produce a migration plan from legacy HTTP+SSE to Streamable HTTP with session id continuity and Origin validation.
version: 1.0.0
phase: 13
lesson: 09
tags: [mcp, streamable-http, sse-migration, session-id, origin]
---

Given an existing HTTP+SSE (legacy) MCP server, produce a migration plan to single-endpoint Streamable HTTP.

Produce:

1. Endpoint rewrite. Merge `/messages` and `/sse` into one `/mcp`. Map POST to request handling, GET to SSE stream, DELETE to session termination.
2. Session continuity. Generate new `Mcp-Session-Id` on first POST. Reject client-supplied ids. Retain bridging logic if the client first sends a legacy session cookie.
3. Origin validation. Allowlist explicit production origins (`https://app.company.com`, `https://claude.ai`, localhost variants). Reject all others with 403.
4. Last-event-id replay. Keep a ring buffer of recent events per session so reconnects can resume.
5. Deprecation window. Document the cut-over date and a 60-day grace period where the legacy endpoints 301 to the new one with a warning header.

Hard rejects:
- Any plan that keeps both endpoints alive indefinitely. Legacy SSE is being removed in 2026.
- Any plan where session ids are client-generated. Breaks the cryptographic-randomness requirement.
- Any plan without Origin validation. DNS-rebinding vulnerability.

Refusal rules:
- If the server is local-only (stdio), refuse to migrate to HTTP; stdio is correct for local.
- If the server does not yet ship OAuth, complete Phase 13 · 16 before exposing it publicly.
- If the hosting target does not support long-lived HTTP (e.g. Vercel free tier), refuse and recommend Cloudflare Workers.

Output: a migration runbook with the endpoint changes, Origin allowlist, session-id plan, deprecation schedule, and a test checklist covering initialize, tools/list, streaming notifications, reconnect with last-event-id, and explicit DELETE.

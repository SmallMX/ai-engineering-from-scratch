---
name: skill-mcp-server
description: 毕业项目 13：MCP Server with Registry与治理 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 13
---

# 毕业项目 13：MCP Server with Registry与治理：中文使用说明

你将围绕本课主题 **毕业项目 13：MCP Server with Registry与治理** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 13 课「毕业项目 13：MCP Server with Registry与治理」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mcp-server-platform
description: Deploy a production MCP server with StreamableHTTP, OAuth 2.1 scopes, OPA policy, human-approval gate for destructive tools, and a registry for discovery.
version: 1.0.0
phase: 19
lesson: 13
tags: [capstone, mcp, fastmcp, streamablehttp, oauth, opa, registry, governance]
---

Given an enterprise environment, ship an MCP server with 10 internal tools, a registry service for discovery, and a governance layer that gates destructive tools via Slack approval.

Build plan:

1. FastMCP server exposing 10 read-only tools (Postgres, S3, Jira, Linear, Datadog, PagerDuty, GitHub, Notion, Slack, Salesforce), each with typed schema and required scope.
2. StreamableHTTP transport, stateless behind a load balancer.
3. OAuth 2.1 token introspection middleware; workload identity via SPIFFE / SPIRE.
4. OPA / Rego policy decisions on every tool call: scope enforcement, PII redaction, payload size caps.
5. Destructive tools (Jira create, Linear create, Postgres write) on a separate MCP server requiring scope `approved:by:human` elevated via Slack card within 15 minutes.
6. Registry service that polls `.well-known/mcp-capabilities` from each server, validates with JSON Schema, and exposes a list/search/validate/enable UI.
7. Per-tenant JSONL audit log with Presidio PII redaction before write.
8. 100-client load test demonstrating horizontal scale; pass MCP conformance suite.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Spec conformance | StreamableHTTP + capability manifest passes MCP conformance tests |
| 20 | Security | Scope enforcement, OPA coverage across every tool, secret hygiene |
| 20 | Observability | Per-tool-call audit log with PII redaction on write |
| 20 | Scale | 100-client load test with horizontal scale demonstration |
| 15 | Registry UX | Discover / validate / enable-disable workflow exercised |

Hard rejects:

- Servers that require stateful sessions (violates 2026 StreamableHTTP stateless contract).
- Single-server topology where destructive tools share the same auth surface as read-only.
- Audit logs that persist raw PII.
- Ignoring the capability manifest; registry integration is a hard requirement.

Refusal rules:

- Refuse to deploy without OAuth; anonymous access is disqualifying.
- Refuse to ship destructive tools without the Slack approval flow.
- Refuse to expose a tool whose scope or description is not in the capability manifest.

Output: a repo containing the two MCP servers (read-only + destructive), the registry service, the Slack approval integration, the OPA policies, the 100-client load-test harness, conformance-test results, and a write-up describing which tools you considered exposing but did not (and why) plus the top three OPA rules that caught near-misses during dry-run.

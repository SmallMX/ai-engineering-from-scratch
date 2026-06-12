---
name: skill-mcp-server-scaffolder
description: Building an MCP Server：Python + TypeScript SDKs 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 7
---

# Building an MCP Server：Python + TypeScript SDKs：中文使用说明

你将围绕本课主题 **Building an MCP Server：Python + TypeScript SDKs** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 07 课「Building an MCP Server：Python + TypeScript SDKs」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mcp-server-scaffolder
description: Scaffold a domain-specific MCP server with the right tools/resources/prompts split and SDK graduation path.
version: 1.0.0
phase: 13
lesson: 07
tags: [mcp, server, fastmcp, scaffold]
---

Given a domain (notes, tickets, files, database, whatever), produce an MCP server plan: which capabilities to expose as tools, which as resources, which as prompts, plus a graduation path to the Python or TypeScript SDK.

Produce:

1. Tools list. Atomic operations the user explicitly asks to perform. Include name, description (Use-when pattern), input schema, and annotation hints.
2. Resources list. Data the user wants to read. URI scheme, mime type, and whether to enable `resources/subscribe`.
3. Prompts list. Reusable templates the host should expose as slash-commands. Argument list.
4. Capability declaration. The exact `capabilities` object the server returns in `initialize`.
5. Graduation notes. FastMCP (Python) or TypeScript SDK equivalents for each piece. Name one SDK feature (e.g. `lifespan`, `context`) that replaces a hand-rolled stdlib pattern from the scaffold.

Hard rejects:
- Any "database query" exposed only as a tool and not as a resource. The correct split is resource for `/list` and `/read`, tool for `/query` with parameters.
- Any server that mixes user-input tools with privileged ones in the same namespace without annotations.
- Any server scaffold that claims `resources/subscribe` capability without a durable notification mechanism.

Refusal rules:
- If the domain has no read-only surface, refuse to scaffold resources; recommend a tool-only server.
- If the domain has no natural slash-command templates, refuse to scaffold prompts.
- If the user asks for an auth scheme, refuse and route to Phase 13 · 16 (OAuth 2.1).

Output: a one-page server plan with the three primitive lists, the capability object, and a 10-line sample `@app.tool()` decorator-style graduation snippet. End with the single most important annotation flag the server should set.

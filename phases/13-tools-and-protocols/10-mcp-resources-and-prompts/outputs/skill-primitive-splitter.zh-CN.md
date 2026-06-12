---
name: skill-primitive-splitter
description: MCP Resources与Prompts：Context Exposure Beyond 工具 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 10
---

# MCP Resources与Prompts：Context Exposure Beyond 工具：中文使用说明

你将围绕本课主题 **MCP Resources与Prompts：Context Exposure Beyond 工具** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 10 课「MCP Resources与Prompts：Context Exposure Beyond 工具」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: primitive-splitter
description: Categorize each capability in an MCP server draft as tool, resource, or prompt with rationale.
version: 1.0.0
phase: 13
lesson: 10
tags: [mcp, primitives, resources, prompts]
---

Given a proposed MCP server's capabilities (as plain English or a draft tool list), categorize each one as tool, resource, or prompt with a one-sentence rationale.

Produce:

1. Per-capability categorization. For each item, return `{name, primitive: tool | resource | prompt, rationale}`.
2. Resource URI scheme. If any capabilities become resources, propose a URI scheme (`notes://`, `gh://`, `db://`) and a template pattern.
3. Prompt argument skeletons. If any capabilities become prompts, propose the argument list and required/optional flags.
4. Subscription candidates. Flag resources that change often and would benefit from `resources/subscribe`.
5. Anti-pattern flags. Call out cases where an old design wrapped a read in a tool (e.g. `notes_read(id)`) when a resource would serve better.

Hard rejects:
- Any capability categorized as "both tool and resource" without a split. Pick one or scaffold a pair.
- Any prompt without required arguments identified. Surfacing in slash-command UIs needs argument schemas.
- Any resource URI scheme not addressable (free-form strings, not URIs).

Refusal rules:
- If all capabilities land as tools, refuse and ask whether the server has read-only data that could be a resource.
- If no capability fits prompts, that is fine; prompts are optional. Do not invent them.
- If the server's domain is better served by A2A (agent-to-agent collaboration, opaque state), refuse and redirect to Phase 13 · 19.

Output: a one-page decision report with the categorization table, a URI scheme proposal, prompt skeletons, and subscription flags. End with the single most impactful tool -> resource conversion for this server.

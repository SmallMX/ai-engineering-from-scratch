---
name: skill-mcp-handshake-tracer
description: MCP 基础：Primitives, Lifecycle, JSON-RPC Base 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 6
---

# MCP 基础：Primitives, Lifecycle, JSON-RPC Base：中文使用说明

你将围绕本课主题 **MCP 基础：Primitives, Lifecycle, JSON-RPC Base** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 06 课「MCP 基础：Primitives, Lifecycle, JSON-RPC Base」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mcp-handshake-tracer
description: Given a pcap-style transcript of an MCP client-server conversation, annotate every message with its primitive, lifecycle phase, and capability dependency.
version: 1.0.0
phase: 13
lesson: 06
tags: [mcp, json-rpc, lifecycle, capabilities]
---

Given a sequence of JSON-RPC 2.0 envelopes captured from an MCP session, produce a walk-through that names each message's primitive, lifecycle phase, and underlying capability flag.

Produce:

1. Per-message annotation. For each `{request, response, notification}`, state: direction (client-to-server or server-to-client), primitive (tools / resources / prompts / roots / sampling / elicitation / lifecycle), lifecycle phase, and the capability flag that had to be negotiated for this message to be valid.
2. Capability check. Reconstruct the `initialize` exchange from the transcript and list all negotiated capabilities. Flag any message that would violate an absent capability.
3. Error diagnostics. For every JSON-RPC error, name the code and the most likely cause given the surrounding context.
4. Completeness audit. Flag a transcript that is missing one of: `initialize`, `initialized` notification, at least one `tools/list` or equivalent, graceful shutdown.
5. Spec compliance. Check each request's params against the 2025-11-25 spec's minimum field set. Flag omissions.

Hard rejects:
- Any message that uses a method outside the spec's allowed set without an `x-` prefix.
- Any `sampling/createMessage` message when the client did not declare the `sampling` capability.
- Any invocation before `notifications/initialized` arrived.

Refusal rules:
- If asked to audit a transcript from a non-MCP protocol, refuse and point at the A2A spec (Phase 13 · 19) as the alternative.
- If asked to "fix" the transcript, refuse. This skill annotates; it does not rewrite. Route corrections through the implementing SDK.

Output: one annotated line per message in arrival order: `[phase/primitive/capability] <method or result shape>`. End with a three-line summary naming any capability violations and any missing lifecycle steps.

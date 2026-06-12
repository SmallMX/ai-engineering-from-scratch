---
name: skill-claude-agent-scaffold
description: Claude 智能体 SDK：Subagents与Session Store 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 17
---

# Claude 智能体 SDK：Subagents与Session Store：中文使用说明

你将围绕本课主题 **Claude 智能体 SDK：Subagents与Session Store** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 17 课「Claude 智能体 SDK：Subagents与Session Store」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: claude-agent-scaffold
description: Scaffold a Claude Agent SDK app with subagents, lifecycle hooks, session store, MCP server attachment, and W3C trace propagation.
version: 1.0.0
phase: 14
lesson: 17
tags: [claude-agent-sdk, subagents, hooks, session-store, mcp]
---

Given a product domain and a list of MCP servers, scaffold a Claude Agent SDK app.

Produce:

1. A main agent definition with instructions, built-in tool access (read_file, write_file, shell, grep, glob, web fetch), and custom function tools.
2. Subagent spawner for parallelization and context isolation. Use when the orchestrator would otherwise blow its context budget.
3. Lifecycle hooks registered: PreToolUse + PostToolUse for audit, SessionStart for setup, SessionEnd for teardown, UserPromptSubmit for rule enforcement (see pro-workflow patterns).
4. Session store (SQLite default) with `list_subkeys` wired to render a subagent tree.
5. MCP server attachment for external tool/resource surfaces.
6. W3C trace context propagation so OTel spans from the caller continue through the CLI.

Hard rejects:

- Spawning a subagent for a single-tool task. Subagents are for parallelization or context isolation; not for "one read_file call."
- Hooks with synchronous expensive work. Hooks should be microseconds to milliseconds. Long work belongs in a subagent.
- Session stores without a cascade-delete policy. Orphaned subagent sessions bloat storage.

Refusal rules:

- If the product needs long-running async work (hours-to-days), refuse the self-hosted SDK and route to Claude Managed Agents.
- If the user asks for `--session-mirror` to a shared location, refuse. Session transcripts carry PII; mirror to per-user encrypted storage.
- If the agent depends on raw LLM streaming for UX without tool use, refuse the Agent SDK and recommend the Client SDK directly.

Output: `agent.py`, `tools.py`, `hooks.py`, `session.py`, `README.md` explaining the subagent policy, hook registry, session backend, MCP attachments, and OTel wiring. End with "what to read next" pointing to Lesson 22 for voice handoffs, Lesson 23 for OTel span attribution, or Lesson 18 if product needs production runtime shape.

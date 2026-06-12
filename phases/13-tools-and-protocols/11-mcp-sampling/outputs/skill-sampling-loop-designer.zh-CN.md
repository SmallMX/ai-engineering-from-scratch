---
name: skill-sampling-loop-designer
description: MCP Sampling：Server-Requested LLM Completions与智能体 Loops 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 11
---

# MCP Sampling：Server-Requested LLM Completions与智能体 Loops：中文使用说明

你将围绕本课主题 **MCP Sampling：Server-Requested LLM Completions与智能体 Loops** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 11 课「MCP Sampling：Server-Requested LLM Completions与智能体 Loops」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: sampling-loop-designer
description: Design a server-hosted agent loop using MCP sampling with the right modelPreferences, rate limits, and safety confirmations.
version: 1.0.0
phase: 13
lesson: 11
tags: [mcp, sampling, agent-loop, model-preferences]
---

Given a server-side algorithm that needs LLM reasoning (research, summarization, planning, triage), design an MCP sampling-based implementation.

Produce:

1. Loop structure. Number each sampling round, state the prompt shape, and the expected output type.
2. `modelPreferences` per round. Weight cost / speed / intelligence (sum 1.0) per round. A "pick files" round leans cost; a "synthesize" round leans intelligence.
3. Rate limit. Set `max_samples_per_tool` per invocation; justify the number.
4. Safety hooks. State where the client should show a confirmation dialog and what the refusal path does.
5. SEP-1577 inclusion. Decide whether to use tools inside sampling; if yes, flag drift risk and specify the tool list.

Hard rejects:
- Any loop without a rate limit. Loop bombs and resource theft risk.
- Any loop that sets `includeContext: "allServers"`. Cross-server leakage.
- Any loop where the server asks the client to generate content that is then fed back as a tool input without user confirmation. Confused-deputy vector.

Refusal rules:
- If the server has its own LLM credentials, ask whether sampling is actually needed; direct calls may be simpler.
- If the use case is a single one-shot tool call, refuse to design a sampling loop; sampling is for multi-round reasoning.
- If the user asks for a sampling loop that hides its intent from the end user, refuse categorically (covert sampling).

Output: a one-page design with the loop steps, modelPreferences per round, rate limit, and safety checklist. End with a note flagging any SEP-1577 (tools-in-sampling) drift risk relevant to the design.

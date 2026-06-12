---
name: skill-agents-sdk-scaffold
description: OpenAI 智能体 SDK：Handoffs, Guardrails, Tracing 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 16
---

# OpenAI 智能体 SDK：Handoffs, Guardrails, Tracing：中文使用说明

你将围绕本课主题 **OpenAI 智能体 SDK：Handoffs, Guardrails, Tracing** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 16 课「OpenAI 智能体 SDK：Handoffs, Guardrails, Tracing」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: agents-sdk-scaffold
description: Scaffold an OpenAI Agents SDK app with a triage agent, handoffs, input/output/tool guardrails, session store, and a trace processor.
version: 1.0.0
phase: 14
lesson: 16
tags: [openai, agents-sdk, handoffs, guardrails, tracing, session]
---

Given a product domain and a list of specialist agents, scaffold an OpenAI Agents SDK app.

Produce:

1. `Agent` per specialist plus one `triage` agent that only has handoffs (no domain tools).
2. `FunctionTool` per domain tool with typed input schema, clear description (tells the model when to use it), and execution sandbox.
3. `Handoff` from triage to each specialist. Verify tool names follow `transfer_to_<agent>` convention.
4. `InputGuardrail` for PII, policy, scope. Default to parallel mode unless the guardrail LLM is large relative to the main model — then use blocking.
5. `OutputGuardrail` for length, PII, policy. Always blocking on prod for safety-critical outputs.
6. Per-tool guardrails on function tools that touch network or filesystem.
7. `Session` store (SQLite default; Redis for prod).
8. `add_trace_processor` wiring spans to your backend alongside OpenAI's trace UI.

Hard rejects:

- Triage agents with domain tools. Triage handoffs only; mixing dilutes the router's decision.
- Guardrails that mutate the input/output. Guardrails approve or reject — they do not rewrite.
- Silent handoff loops. Require a hop counter (default max 3).

Refusal rules:

- If the user wants "no guardrails, just move fast," refuse for any product that hits paying users or PII.
- If the product has only 2 specialists, suggest routing via `Agents` with a direct classifier (Lesson 12) instead of triage+handoffs — less token cost.
- If tracing is disabled in prod, refuse to ship. Multi-step failures are un-debuggable without traces.

Output: `agents.py`, `tools.py`, `guardrails.py`, `app.py`, `README.md` with the triage-agent rationale, guardrail modes, trace processor, and session backend. End with "what to read next" pointing to Lesson 23 (OTel GenAI), Lesson 24 (observability backends), or Lesson 17 for Claude Agent SDK translation.

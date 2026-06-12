---
name: skill-otel-genai-instrumentation
description: OpenTelemetry GenAI：Tracing Tool Calls End-to-End 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 20
---

# OpenTelemetry GenAI：Tracing Tool Calls End-to-End：中文使用说明

你将围绕本课主题 **OpenTelemetry GenAI：Tracing Tool Calls End-to-End** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 20 课「OpenTelemetry GenAI：Tracing Tool Calls End-to-End」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: otel-genai-instrumentation
description: Produce an instrumentation plan for an agent codebase to emit OTel GenAI spans end-to-end.
version: 1.0.0
phase: 13
lesson: 19
tags: [otel, observability, gen-ai, tracing]
---

Given an agent codebase (LLM calls, tool dispatch, MCP client, sub-agents), produce an OTel GenAI instrumentation plan.

Produce:

1. Span hierarchy. Root `agent.invoke_agent` (INTERNAL) and children: `llm.chat` (CLIENT), `tool.execute` (INTERNAL), `mcp.call` (CLIENT), `subagent.invoke` (INTERNAL).
2. Attribute checklist per span. `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model`, `gen_ai.response.model`, `gen_ai.usage.*`, `gen_ai.tool.name`, `gen_ai.agent.name`.
3. Propagation rule. Inject W3C traceparent on every remote call; for MCP stdio use `_meta.traceparent` as an interim field.
4. Content capture policy. Off by default; document which env var enables; name PII risks.
5. Exporter choice. Jaeger / Tempo / Langfuse / Phoenix / Datadog / Honeycomb; OTLP as the wire.

Hard rejects:
- Any plan missing trace propagation across MCP or sub-agent boundaries.
- Any plan with content capture on by default. Leaks prompts and PII.
- Any plan that emits arbitrary custom attributes without the `gen_ai.` or explicit vendor prefix.

Refusal rules:
- If the codebase uses a framework with built-in OTel auto-instrumentation (Pydantic AI, LangGraph, AgentOps), recommend the framework hook first.
- If the exporter backend is on-prem and the team has no SRE support, recommend a managed backend.
- If the user asks to capture content for debugging prod, refuse without a typed consent policy and PII redaction pipeline.

Output: a one-page plan with span hierarchy, attribute checklist per span, propagation rule, content capture policy, and exporter choice. End with the top metric to alert on (typically p95 `gen_ai.client.operation.duration`).

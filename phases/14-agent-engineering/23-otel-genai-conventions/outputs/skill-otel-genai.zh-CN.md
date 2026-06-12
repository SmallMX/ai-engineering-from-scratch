---
name: skill-otel-genai
description: OpenTelemetry GenAI Semantic Conventions 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 23
---

# OpenTelemetry GenAI Semantic Conventions：中文使用说明

你将围绕本课主题 **OpenTelemetry GenAI Semantic Conventions** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 23 课「OpenTelemetry GenAI Semantic Conventions」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: otel-genai
description: Instrument an agent with OpenTelemetry GenAI semantic conventions — invoke_agent, chat, tool_call spans with correct attributes and opt-in content capture.
version: 1.0.0
phase: 14
lesson: 23
tags: [opentelemetry, genai, observability, tracing, semantic-conventions]
---

Given an agent runtime, wire OTel GenAI semantic conventions.

Produce:

1. `invoke_agent` span per agent run. Kind CLIENT for remote agent services, INTERNAL for in-process. Name: `invoke_agent {gen_ai.agent.name}`.
2. `chat` span per LLM call with `gen_ai.operation.name=chat`, `gen_ai.provider.name`, `gen_ai.request.model`, `gen_ai.response.model`.
3. `tool_call` span per tool invocation with `gen_ai.tool.name` and, when applicable, `gen_ai.data_source.id` (RAG corpus / memory store).
4. Opt-in content capture: default OFF; when ON, store inputs/outputs externally and record `*.reference_id` on spans.
5. Context propagation: use W3C trace context headers so multi-process runs (Claude Agent SDK CLI subprocess) stitch into one trace.

Hard rejects:

- Capturing full prompts/outputs inline by default. PII and secret leakage risk; also violates the spec.
- Missing `gen_ai.provider.name`. Multi-provider dashboards break.
- Orphan tool spans. Always set parent-child relation via active context.

Refusal rules:

- If the runtime cannot propagate context across process boundaries, refuse. Multi-process trace stitching is required for Claude Agent SDK + CLI users.
- If the product has regulatory constraints (HIPAA, GDPR), refuse inline content capture. External store with access control only.
- If the backend does not set `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental`, warn: attribute names may change on collector upgrade.

Output: `tracer.py`, `attributes.py`, `content_store.py`, `README.md` explaining span structure, stability opt-in, and content-capture policy. End with "what to read next" pointing to Lesson 24 (backends: Langfuse, Phoenix, Opik) or Lesson 17 for Claude Agent SDK trace-context propagation.

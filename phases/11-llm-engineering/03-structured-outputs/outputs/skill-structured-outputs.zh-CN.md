---
name: skill-structured-outputs
description: 结构化输出：JSON, Schema Validation, Constrained Decoding 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 11
lesson: 3
---

# 结构化输出：JSON, Schema Validation, Constrained Decoding：中文使用说明

你将围绕本课主题 **结构化输出：JSON, Schema Validation, Constrained Decoding** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 11「LLM 工程」
- 课程：第 03 课「结构化输出：JSON, Schema Validation, Constrained Decoding」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-structured-outputs
description: Decision framework for choosing the right structured output strategy based on provider, reliability, and complexity
version: 1.0.0
phase: 11
lesson: 03
tags: [structured-output, json, schema, constrained-decoding, pydantic, function-calling]
---

# Structured Output Strategy

When building an LLM application that requires structured data, apply this decision framework.

## When to use each approach

**Prompt-based ("Return JSON"):** Prototyping only. Acceptable for internal tools where occasional parse failures are tolerable. Add a try/except with retry. Never use in production pipelines.

**JSON mode (API flag):** You need guaranteed valid JSON but the schema is simple or flexible. Works when you validate the shape on the application side. Available: OpenAI, Anthropic (via tool use), Google.

**Schema mode (constrained decoding):** Production systems where every output must match a specific schema. Zero parse failures. Zero schema violations. Use this by default for any production extraction or classification task. Available: OpenAI structured outputs, Outlines, Guidance.

**Function calling / tool use:** The model needs to choose which function to call, not just fill parameters. You have multiple schemas and the model selects the appropriate one. Also use when integrating with existing tool/function infrastructure.

**Instructor library:** You want Pydantic validation with automatic retry across any provider. Best DX for Python projects. Wraps OpenAI, Anthropic, Google, and open-source models.

## Provider-specific guidance

**OpenAI:** Use `response_format` with `json_schema` type. Constrained decoding is built in. Pydantic models work directly. Most reliable structured output implementation.

**Anthropic:** Use tool use for structured output. Define a single tool with the desired schema. The model returns tool call arguments matching the schema. Reliable but requires the tool use API pattern.

**Open-source models (vLLM, Ollama):** Use Outlines or Guidance for constrained decoding. These libraries compile JSON Schemas into finite state machines that mask invalid tokens during generation. Requires running inference locally.

## Schema design guidelines

1. Keep schemas flat when possible. Nested objects beyond 2 levels increase extraction errors.
2. Use enums for categorical fields. Do not rely on the model inventing the right string.
3. Make ambiguous fields required with explicit null support rather than optional. Forces the model to make a decision.
4. Add descriptions to schema properties. The model reads these as instructions.
5. Avoid union types (oneOf/anyOf) unless necessary. They increase decoding complexity.
6. Set minimum/maximum on numbers. Catches hallucinated extreme values.
7. Use minItems/maxItems on arrays to prevent empty or unbounded outputs.

## Common failure patterns and fixes

- **Model wraps JSON in markdown fences**: switch from prompt-based to JSON mode or schema mode
- **Schema-valid but factually wrong**: add an LLM-as-judge validation step after extraction
- **Inconsistent enum values**: switch to constrained decoding or add post-processing normalization
- **Missing optional fields**: make them required or add default values in application code
- **Very slow extraction**: constrained decoding adds 5-15% latency, reduce schema complexity if latency-sensitive
- **Large arrays with varied items**: chunk the input and extract per-chunk, then merge results

## Reliability ladder

| Approach | Parse Success | Schema Match | Setup Effort |
|----------|-------------|-------------|-------------|
| Prompt-based | ~90% | ~80% | 1 minute |
| JSON mode | 100% | ~90% | 5 minutes |
| Schema mode | 100% | ~99% | 15 minutes |
| Constrained decoding | 100% | 100% | 30 minutes |
| Instructor + retry | 100% | ~99.5% | 10 minutes |

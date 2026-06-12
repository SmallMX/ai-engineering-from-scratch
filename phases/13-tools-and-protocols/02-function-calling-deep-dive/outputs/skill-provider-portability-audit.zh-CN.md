---
name: skill-provider-portability-audit
description: 函数调用 深入解析：OpenAI, Anthropic, Gemini 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 2
---

# 函数调用 深入解析：OpenAI, Anthropic, Gemini：中文使用说明

你将围绕本课主题 **函数调用 深入解析：OpenAI, Anthropic, Gemini** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 02 课「函数调用 深入解析：OpenAI, Anthropic, Gemini」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: provider-portability-audit
description: Audit a function-calling integration against one provider for what breaks when ported to the other two.
version: 1.0.0
phase: 13
lesson: 02
tags: [function-calling, openai, anthropic, gemini, portability]
---

Given a function-calling integration on one provider (OpenAI, Anthropic, or Gemini), produce a portability audit listing every field rename, behavior difference, and hard-limit collision that appears when the same logic is shipped on the other two providers.

Produce:

1. Declaration diff. For each tool in the integration, show the envelope / field rename / schema translation required for each of the other two providers. Flag any JSON Schema construct the target provider does not support (Gemini: OpenAPI 3.0 subset; OpenAI strict: no `$ref`, no ambiguous `oneOf`).
2. Response diff. Document where the tool call lives in each provider's response shape (`tool_calls[]` vs `content[]` block vs `parts[]` entry) and who is responsible for parsing `arguments` (string on OpenAI, object on Anthropic and Gemini).
3. `tool_choice` diff. Map the integration's current choice setting (auto / forbid / force / required) to the target provider shape; flag missing modes.
4. Limit collisions. Report tool-count (128 / 64 / 64), schema depth (5 / 10 / effectively unbounded), and per-argument length caps. Raise block-severity on any integration that exceeds a target provider's limits.
5. Strict-mode mapping. State whether strict-mode semantics are preserved on the target. OpenAI `strict: true` has no exact equivalent on Anthropic; Gemini `responseSchema` approximates but is at the request level.

Hard rejects:
- Any integration that assumes `arguments` is a string on the non-OpenAI targets. Will silently produce wrong results.
- Any integration whose tool count exceeds 64 when porting to Anthropic or Gemini without a router.
- Any integration that uses `$ref` in the schema when the target is OpenAI strict mode.

Refusal rules:
- If asked to port an integration that depends on a provider-specific feature with no analog (e.g. OpenAI Responses API stateful turns, Anthropic computer-use blocks), refuse and explain which feature has no target equivalent.
- If asked to pick a winner, refuse. The choice depends on the host's strict-mode needs, cost profile, and parallel-call requirements.

Output: a one-page audit with a per-tool diff table, a limits table, and a final "port verdict" per target provider (ship / needs-router / blocked-by-feature). End with one sentence naming the highest-leverage migration change.

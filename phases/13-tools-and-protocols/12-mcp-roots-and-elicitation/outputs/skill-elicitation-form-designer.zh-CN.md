---
name: skill-elicitation-form-designer
description: Roots与Elicitation：Scoping与Mid-Flight User Input 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 12
---

# Roots与Elicitation：Scoping与Mid-Flight User Input：中文使用说明

你将围绕本课主题 **Roots与Elicitation：Scoping与Mid-Flight User Input** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 12 课「Roots与Elicitation：Scoping与Mid-Flight User Input」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: elicitation-form-designer
description: Design the elicitation form schema and message template for a tool that needs mid-call user confirmation or disambiguation.
version: 1.0.0
phase: 13
lesson: 12
tags: [mcp, elicitation, user-input, forms]
---

Given a tool whose behavior may require mid-call user input, design the elicitation schema and message.

Produce:

1. Trigger condition. State the exact input or ambiguity that should cause the tool to call `elicitation/create`.
2. Message template. One sentence the host shows the user. Plain, specific, free of jargon.
3. Schema. Flat JSON Schema with typed properties and the `enum` list (for disambiguation) or `boolean` (for confirmation). Do not nest.
4. Branch handling. Map `accept` / `decline` / `cancel` to tool behaviors.
5. Rate-limit rule. Cap elicitations per tool invocation; never elicit inside a loop.

Hard rejects:
- Any schema that nests objects. Elicitation v1 is flat.
- Any elicitation used to pad a missing argument the LLM could have asked for in prose.
- Any high-frequency elicitation (more than once per tool call).

Refusal rules:
- If the tool is read-only and low-risk, refuse to elicit and just return the result.
- If the tool is destructive and the host supports `destructiveHint` annotations, suggest using annotations and letting the client handle confirmation natively.
- If the need is an OAuth sign-in, recommend URL-mode elicitation and flag the SEP-1036 drift risk.

Output: a one-page design with trigger condition, message template, schema, branch handling, rate-limit rule, and a note on whether form mode or URL mode fits better.

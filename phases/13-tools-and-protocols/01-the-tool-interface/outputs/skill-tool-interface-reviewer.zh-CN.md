---
name: skill-tool-interface-reviewer
description: The Tool Interface：Why 智能体 Need Structured I/O 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 1
---

# The Tool Interface：Why 智能体 Need Structured I/O：中文使用说明

你将围绕本课主题 **The Tool Interface：Why 智能体 Need Structured I/O** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 01 课「The Tool Interface：Why 智能体 Need Structured I/O」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: tool-interface-reviewer
description: Audit a tool definition (name + description + JSON Schema + executor outline) for loop fitness before it ships to an LLM.
version: 1.0.0
phase: 13
lesson: 01
tags: [tool-calling, function-calling, json-schema, tool-design]
---

Given a proposed tool definition, review it against the four-step loop (describe, decide, execute, observe) and flag loop-breaking defects before the tool reaches a model.

Produce:

1. Name audit. Is the name `snake_case`, stable across versions, and unambiguous? Flag names that collide with built-ins, contain tense ("was_", "will_"), or embed arguments.
2. Description audit. Does the description read as a complete usage brief? Require the two-sentence shape: "Use when X. Do not use for Y." Flag descriptions under 40 characters, marketing prose, or anything that does not teach selection.
3. Schema audit. Is the schema valid JSON Schema 2020-12? Every field typed? `required` list explicit? Enums used for closed value sets? Flag open-ended string fields that should be enums, missing types, and `additionalProperties` left undeclared on input objects.
4. Executor audit. Is the executor deterministic given arguments? Does it handle failure with a typed error (not a raised exception that escapes the host)? If it is consequential (mutates state, spends money, touches user data), is it flagged as such and gated behind a confirmation?
5. Classification. State whether the tool is pure or consequential and why. A consequential tool without a gate is an immediate reject.

Hard rejects:
- Any tool whose description says only what it does and not when to use it. The model needs the "when" for step two.
- Any schema with an untyped field. The validator cannot do its job.
- Any tool that combines all three of: accepts untrusted input, reads sensitive data, and takes consequential action. Violates Meta's Rule of Two.
- Any tool whose executor raises unhandled exceptions on bad input. The host should not need a try/except around every call.

Refusal rules:
- If the tool definition is missing a schema, refuse. Route to Phase 13 · 04 first.
- If the tool is pure but the description says "use sparingly," refuse and ask why. Pure tools should be cheap to re-run.
- If the reviewer is asked to approve a tool that talks to a production database without a read-only guard, refuse and direct to Phase 13 · 17 (gateways and policy).

Output: a one-page audit listing name, description, schema, and executor findings with severity (block / warn / nit) and a final verdict of ship / revise / reject. End with a one-line rewrite suggestion for any reject, if feasible.

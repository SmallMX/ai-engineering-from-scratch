---
name: skill-constitutional-rules-engine
description: 毕业项目 86：Constitutional Rules Engine 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 86
---

# 毕业项目 86：Constitutional Rules Engine：中文使用说明

你将围绕本课主题 **毕业项目 86：Constitutional Rules Engine** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 86 课「毕业项目 86：Constitutional Rules Engine」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-constitutional-rules-engine
description: Declarative YAML rules engine for output constraints with severity, explanation, fixer operations, and structured diff
version: 1.0.0
phase: 19
lesson: 86
tags: [safety, rules, constitutional]
---

# Constitutional Rules Engine

A constitution is a YAML file. Each rule has `name`, `severity` (low | medium | high), `applies_when` (predicate), `must` (predicate), `explanation`, and optional `fix`.

## Predicates

Atomic:

- `contains_regex` / `not_contains_regex`
- `starts_with_regex` / `ends_with_regex`
- `max_words` / `min_words`

Compositional:

- `all_of: [...predicates]`
- `any_of: [...predicates]`
- `not_: predicate`

## Fix operations

- `append_if_missing: <suffix>`
- `prepend_if_missing: <prefix>`
- `replace_regex: { pattern: <regex>, replacement: <text> }`

## Engine output

`Engine.evaluate(text) -> EngineReport` returns one `RuleResult` per rule with `status` in `pass`, `violation`, `not_applicable`. `report.violations()` filters to violations and `report.max_severity()` returns the worst severity present.

## Artifact

`outputs/rules_report.json` carries draft, revised, and structured diff per case.

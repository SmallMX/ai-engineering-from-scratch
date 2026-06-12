---
name: skill-rule-set-builder
description: 智能体 Instructions as Executable Constraints 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 33
---

# 智能体 Instructions as Executable Constraints：中文使用说明

你将围绕本课主题 **智能体 Instructions as Executable Constraints** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 33 课「智能体 Instructions as Executable Constraints」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: rule-set-builder
description: Interview a project owner, classify their existing prose instructions into five operational categories, and emit a versioned agent-rules.md plus a Python checker stub.
version: 1.0.0
phase: 14
lesson: 33
tags: [rules, instructions, constraints, checker, workbench]
---

Given a repo and any existing prose instructions (`AGENTS.md`, `CONTRIBUTING.md`, onboarding docs), produce a five-category rule set the workbench can execute.

The five categories:

1. `startup` — what must be true before work begins.
2. `forbidden` — what must never happen.
3. `definition_of_done` — what proves the task is complete.
4. `uncertainty` — what the agent does when not sure.
5. `approval` — what requires human sign-off.

Produce:

1. `docs/agent-rules.md` with one `##` heading per rule. Each rule carries `category`, `check`, and a one-line description.
2. `tools/rule_checker.py` with a `RuleChecker` class exposing one method per `check`. Each method takes a `TurnTrace` dataclass and returns `bool`.
3. `tools/rule_report.py` runner that loads rules, runs the checker on a trace, emits a `rule_report.json`.
4. A migration notes file: which prose lines became which rule, which were dropped as aspirational, why.

Hard rejects:

- Rules without a `check` field. Aspirational-only rules belong in onboarding docs, not in the workbench rule set.
- A single "be careful" rule. Specify a category and a check or remove it.
- Checks that require LLM calls. Rule checks must be deterministic and cheap so they can run every turn.
- Rule files over 200 lines. Split by category into `agent-rules.{startup,forbidden,done,uncertainty,approval}.md` and route from a parent index.

Refusal rules:

- If the agent product cannot supply a `TurnTrace` (no instrumentation), refuse to wire the checker until at least `read_state_file`, `edited_files`, and `tests_exit_code` are recorded.
- If existing instructions are mostly aspirational (>50%), surface that finding before emitting rules. The rule set will look thin; that is correct.
- If a rule is added because of a single past incident, attach the incident id so future review can decide if it is still needed.

Output structure:

```
<repo>/
├── docs/
│   └── agent-rules.md
├── tools/
│   ├── rule_checker.py
│   └── rule_report.py
└── docs/migration-notes.md
```

End with "what to read next" pointing to:

- Lesson 36 for per-task scope contracts that extend the forbidden category.
- Lesson 38 for verification gates that consume the rule report.
- Lesson 39 for the reviewer agent that scores rule compliance.

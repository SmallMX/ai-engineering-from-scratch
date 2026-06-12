---
name: skill-scope-contract
description: Scope Contracts与Task Boundaries 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 36
---

# Scope Contracts与Task Boundaries：中文使用说明

你将围绕本课主题 **Scope Contracts与Task Boundaries** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 36 课「Scope Contracts与Task Boundaries」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: scope-contract
description: Generate per-task scope contracts with allowed/forbidden globs, acceptance criteria, and rollback plan, plus a CI-ready glob-aware checker that runs on every agent diff.
version: 1.0.0
phase: 14
lesson: 36
tags: [scope, contract, globs, diff-check, ci]
---

Given a task description and a repo layout, produce a scope contract and a diff-aware checker.

Produce:

1. `scope_contract.json` for the task with fields: `task_id`, `goal`, `allowed_files` (globs), `forbidden_files` (globs), `acceptance_criteria`, `rollback_plan`, `approvals_required`.
2. `tools/scope_check.py` that takes a contract path and a list of touched files and returns a `ScopeReport` plus a non-zero exit on any violation.
3. CI step (`.github/workflows/scope-check.yml` or equivalent) that runs the checker against the merge diff.
4. `outputs/scope/closed/<task_id>.json` archival convention so contracts ship with the change history.

Hard rejects:

- A contract without `forbidden_files`. Negative space is part of the contract.
- A contract that lists raw paths instead of globs for code directories. Refactors invalidate raw paths overnight.
- A `rollback_plan` field that is empty or "see runbook." Spell it out.
- Approvals listed as "case by case." Approval boundaries must be enumerable.

Refusal rules:

- If the task description does not constrain a region of the repo, refuse to author `allowed_files` from the description alone. Ask for the directory the task lives in.
- If the repo has no test command, refuse to add `acceptance_criteria` until one is supplied or stubbed. A contract that cannot be verified is a wish.
- If the agent runtime cannot honor approval boundaries (no human-in-the-loop), surface the gap before shipping; scope creep into approval-required actions will be the dominant failure.

Output structure:

```
<repo>/
├── scope_contract.json
├── outputs/scope/closed/
│   └── T-XXX.json
├── tools/
│   └── scope_check.py
└── .github/
    └── workflows/
        └── scope-check.yml
```

End with "what to read next" pointing to:

- Lesson 37 for runtime feedback that links commands run back to the contract.
- Lesson 38 for the verification gate that consumes the scope report.
- Lesson 39 for the reviewer agent that audits the closed contract archive.

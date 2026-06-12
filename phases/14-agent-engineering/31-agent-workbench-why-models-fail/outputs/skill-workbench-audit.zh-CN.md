---
name: skill-workbench-audit
description: 智能体 Workbench 工程：Why Capable Models Still Fail 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 31
---

# 智能体 Workbench 工程：Why Capable Models Still Fail：中文使用说明

你将围绕本课主题 **智能体 Workbench 工程：Why Capable Models Still Fail** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 31 课「智能体 Workbench 工程：Why Capable Models Still Fail」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: workbench-audit
description: Audit a repo for the seven agent workbench surfaces and report which are missing, partial, or healthy before any agent work begins.
version: 1.0.0
phase: 14
lesson: 31
tags: [workbench, audit, reliability, agent-engineering]
---

Given a repository path and the agent product that will run inside it, audit the seven workbench surfaces and produce a readiness report.

The seven surfaces:

1. Instructions: a root file the agent reads first (e.g. `AGENTS.md`), short, that routes to deeper rules.
2. State: a durable, machine-readable file that records task, touched files, blockers, next action.
3. Scope: a contract per task listing allowed files, forbidden files, acceptance criteria, rollback plan.
4. Feedback: a runner that captures command, stdout, stderr, exit code, and feeds the result back into the loop.
5. Verification: a gate that runs tests, lint, type-check, smoke run, and confirms acceptance criteria.
6. Review: a second pass with a different role, builder cannot mark its own work.
7. Handoff: an artifact that summarizes what changed, why, what is left, and the next best action.

Produce:

- A score per surface: 0 missing, 1 partial, 2 healthy. Tie each score to a file or process you observed.
- Three priorities ordered by leverage: which missing surface, if added first, removes the most failure modes.
- A `workbench_audit.json` machine-readable report plus a `workbench_audit.md` human-readable summary.
- A starter patch for the weakest surface: the smallest file change that moves the score from 0 to 1.

Hard rejects:

- "Healthy" scores without a file path or process reference. Audits without evidence rot.
- A single combined "agent config" surface. Combining surfaces hides which one failed when a task breaks.
- Skipping verification because tests are slow. If verification is not on the workbench, builders mark their own homework.

Refusal rules:

- If the repo has no test command at all, refuse the verification score and surface it as a blocking finding.
- If the repo has no version control history, refuse the handoff score and surface it as a blocking finding.
- If the agent product runs as root or with unrestricted file access, refuse the scope score until a sandbox or write list is defined.

Output structure:

```
workbench-audit/
├── workbench_audit.json
├── workbench_audit.md
├── patches/
│   └── <weakest-surface>.patch
└── README.md
```

End with "what to read next" pointing to:

- Lesson 32 for the minimal repo layout.
- Lesson 33 for the instructions surface in depth.
- Lesson 38 for the verification gate.

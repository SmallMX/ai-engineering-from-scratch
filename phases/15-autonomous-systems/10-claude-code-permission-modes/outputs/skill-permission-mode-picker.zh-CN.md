---
name: skill-permission-mode-picker
description: Claude Code as an 自主 智能体：Permission Modes与Auto Mode 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 10
---

# Claude Code as an 自主 智能体：Permission Modes与Auto Mode：中文使用说明

你将围绕本课主题 **Claude Code as an 自主 智能体：Permission Modes与Auto Mode** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 10 课「Claude Code as an 自主 智能体：Permission Modes与Auto Mode」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: permission-mode-picker
description: Match a Claude Code task to the correct permission mode, budget caps, and required isolation before starting a run.
version: 1.0.0
phase: 15
lesson: 10
tags: [claude-code, permission-modes, auto-mode, budgets, isolation]
---

Given a proposed Claude Code task, pick the permission mode, set budgets, and specify the minimum isolation required before the agent is allowed to start.

Produce:

1. **Task profile.** One sentence on what the task does, one sentence on the blast radius if it goes wrong.
2. **Mode recommendation.** One of: `plan`, `default`, `acceptEdits`, `acceptExec`, `autoMode`, `yolo`, `bypassPermissions`. Justify with a single sentence referencing the blast radius.
3. **Budget numbers.** Concrete values for `max_turns`, `max_budget_usd`, and any per-tool caps. For unattended runs over an hour, specify a dollar cap equal to or below what you would pay for a human mistake you cannot roll back.
4. **Isolation requirements.** File-system scope (project directory only, scratch directory, ephemeral container). Network policy (no egress, allowlist only, full). Credential surface (none, scoped token, broad token). For `bypassPermissions` or `yolo`, the run must be inside an ephemeral container with no production credentials mounted.
5. **Trajectory audit plan.** How will a human review the trajectory after the run? Required for `autoMode`, `yolo`, and anything over a 30-minute horizon.

Hard rejects:
- `bypassPermissions` against a repository with uncommitted changes.
- `autoMode` with no budget cap.
- Any mode above `acceptEdits` with broad credentials in the environment (AWS, GCP, GitHub PAT with repo scope).
- Unattended runs longer than one hour with no trajectory audit scheduled.
- Claims that the Auto Mode classifier alone is sufficient for a novel task distribution.

Refusal rules:
- If the user cannot name the blast radius of a failure, refuse and require an explicit worst-case sentence before starting.
- If the user requests `autoMode` in a workspace with production database credentials reachable, refuse and require scoped credentials or an ephemeral container first.
- If the proposed budget cap exceeds what the user is willing to lose on a bad run, refuse and require a lower cap.

Output format:

Return a one-page run card with:
- **Task summary** (one sentence)
- **Blast radius** (one sentence, worst case)
- **Mode** (explicit)
- **Budgets** (`max_turns`, `max_budget_usd`, per-tool caps)
- **Isolation** (fs scope, network policy, credential surface)
- **Audit plan** (who reviews the trajectory, when, against what rubric)

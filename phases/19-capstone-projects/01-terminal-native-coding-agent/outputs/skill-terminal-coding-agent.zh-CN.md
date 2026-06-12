---
name: skill-terminal-coding-agent
description: 毕业项目 01：Terminal-Native Coding 智能体 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 1
---

# 毕业项目 01：Terminal-Native Coding 智能体：中文使用说明

你将围绕本课主题 **毕业项目 01：Terminal-Native Coding 智能体** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 01 课「毕业项目 01：Terminal-Native Coding 智能体」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: terminal-coding-agent
description: Build and evaluate a terminal-native coding agent against SWE-bench Pro with bounded cost, sandboxed tools, and full 2026 hook surface.
version: 1.0.0
phase: 19
lesson: 01
tags: [capstone, coding-agent, claude-code, swe-bench, mcp, hooks, sandbox]
---

Given a target repository and a natural-language task, build a harness that plans, executes in a sandbox, and opens a pull request. Match or beat the mini-swe-agent baseline on a 30-task SWE-bench Pro subset while staying under a $5-per-task budget.

Build plan:

1. Stand up a Bun + Ink TUI harness with a plan pane, a tool-call stream, and a live token/dollar budget.
2. Define six tools (read_file, edit_file, ripgrep, tree_sitter_symbols, run_shell, git) over Model Context Protocol StreamableHTTP. Every call returns at most 4k tokens.
3. Run every tool call inside an E2B or Daytona sandbox on a fresh `git worktree add` branch. Never touch the host filesystem.
4. Wire all eight 2026 hook events: SessionStart, SessionEnd, PreToolUse, PostToolUse, UserPromptSubmit, Notification, Stop, PreCompact. Ship at least four user-authored hooks (destructive-command guard, token accounting, OTel span emitter, trace bundle writer).
5. Enforce three budgets: 50 turns, 200k tokens, $5 dollars. PreCompact fires at 150k and summarizes older turns.
6. Emit OpenTelemetry spans with GenAI semantic conventions to a self-hosted Langfuse.
7. On success, push the branch and open a PR with the plan and trace bundle in the body.
8. Evaluate against mini-swe-agent on a 30-issue SWE-bench Pro Python subset and record pass@1, turns, tokens, and dollars per task.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | SWE-bench Pro pass@1 | Matched 30-task subset vs mini-swe-agent baseline |
| 20 | Architecture clarity | Plan/act/observe separation, hook surface, tool schema readability |
| 20 | Safety | Sandbox escape red-team + destructive-command guard audit |
| 20 | Observability | 100% of tool calls spanned, token accounting per turn |
| 15 | Developer UX | Cold-start under 2s, crash recovery, Ctrl-C cancel semantics |

Hard rejects:

- Harness that shells out to git on the host filesystem instead of inside the sandbox.
- Any agent that can write outside the worktree or curl external URLs without an explicit allowlist hook.
- Eval numbers reported without a matched baseline run on the same 30 issues.
- "Pass rate" claims that depend on `git reset --hard` between retries; SWE-bench Pro is pass@1.

Refusal rules:

- Refuse to push directly to main under any configuration. PR branches only.
- Refuse to disable the destructive-command guard. It is a hard requirement of the rubric.
- Refuse to run without a budget ceiling. Open-ended runs contaminate the eval comparison.

Output: a repo containing the harness, a fixed 30-task SWE-bench Pro eval harness with matched mini-swe-agent baseline run, an OpenTelemetry trace archive for at least 5 full runs, and a write-up naming which tasks the harness solves that the baseline does not and vice versa. End with a section on the top three failure modes you observed and the hook change that fixed each.

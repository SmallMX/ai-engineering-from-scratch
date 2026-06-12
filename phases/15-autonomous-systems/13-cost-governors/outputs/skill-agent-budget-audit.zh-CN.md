---
name: skill-agent-budget-audit
description: Action Budgets, Iteration Caps,与Cost Governors 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 13
---

# Action Budgets, Iteration Caps,与Cost Governors：中文使用说明

你将围绕本课主题 **Action Budgets, Iteration Caps,与Cost Governors** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 13 课「Action Budgets, Iteration Caps,与Cost Governors」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: agent-budget-audit
description: Audit an agent deployment's cost-governor stack and flag missing layers before enabling unattended runs.
version: 1.0.0
phase: 15
lesson: 13
tags: [cost-governors, denial-of-wallet, budgets, claude-code-sdk, agent-governance]
---

Given a proposed agent deployment, audit its cost-governor stack against the twelve-layer reference and flag which layers are missing, under-tuned, or over-tuned.

Produce:

1. **Layer inventory.** For each of the twelve reference layers (per-request cap, per-task token budget, per-task dollar budget, per-tool cap, iteration cap, per-minute/hour/day/month rolling caps, velocity limit, tiered routing, prompt caching, context windowing, HITL checkpoints, kill switch), state whether it is configured, and at what value.
2. **Failure-mode mapping.** For each time-scale failure (runaway loop, slow leak, bad release, legitimate surge), name the specific layer that catches it and how fast.
3. **Tool-specific caps.** List every tool the agent can call. For each, name a per-session cap and a reason. Any tool without an explicit cap is an open loop.
4. **Alert thresholds.** Separate from caps: at what spend rate does a human get paged? The observed e-commerce case ($1,200 → $4,800) was a week-over-week growth problem, not a monthly cap problem.
5. **Kill-switch path.** When a cap fires, what happens? Clean abort, rollback, alert, re-enable procedure. Confirm the kill switch is external to the agent (the agent cannot edit its own cap).

Hard rejects:
- Any autonomous deployment without a per-task dollar budget.
- Any unattended long-horizon run without a velocity limit.
- Tool surfaces with no per-tool cap on a new (<30 days) tool addition.
- Kill switches the agent itself can modify.
- Monthly cap as the only cap (every other time scale is unguarded).

Refusal rules:
- If the user cannot price a worst-case run on today's model prices, refuse and require a costed estimate.
- If the proposed budget exceeds the organization's acceptable loss on a single mistake, refuse and require a lower cap.
- If the user treats the Auto Mode classifier (Lesson 10) as a replacement for budgets, refuse. The classifier is orthogonal to cost; both layers are required.

Output format:

Return a cost-governor audit with:
- **Layer table** (layer name, configured y/n, value)
- **Failure-mode coverage** (4 rows: loop / leak / release / surge)
- **Per-tool caps** (tool, cap, reason)
- **Alert thresholds** (rate, owner, channel)
- **Kill-switch path** (trigger, action, re-enable procedure)
- **Readiness** (production / staging / research-only)

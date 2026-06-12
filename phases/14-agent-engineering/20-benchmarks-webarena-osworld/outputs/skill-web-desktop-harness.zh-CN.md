---
name: skill-web-desktop-harness
description: 基准：WebArena与OSWorld 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 20
---

# 基准：WebArena与OSWorld：中文使用说明

你将围绕本课主题 **基准：WebArena与OSWorld** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 20 课「基准：WebArena与OSWorld」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: web-desktop-harness
description: Build a WebArena/OSWorld-style harness with execution-based evaluation and trajectory-efficiency metrics.
version: 1.0.0
phase: 14
lesson: 20
tags: [webarena, osworld, harness, trajectory-efficiency]
---

Given a target app (web or desktop) and a list of tasks with gold trajectories, build an eval harness.

Produce:

1. Task definitions: `(tid, description, gold_steps, success_predicate, state_reset)`.
2. Runner: runs the agent, captures every action, records step count + elapsed time + success state.
3. Trajectory-efficiency metric: `agent_steps / gold_steps`. Report per-task and aggregate.
4. State reset between tasks — never run one task on state dirtied by another.
5. Failure-mode classifier: for each failure, tag whether it's a grounding miss (wrong element) or a planning miss (wrong action).

Hard rejects:

- No state reset between tasks. Cross-task contamination invalidates all scores.
- Success-rate-only reporting. Trajectory efficiency is the 2026 standard.
- Screenshots-only harness without DOM parity. Some agents use DOM+vision; give both unless specifically constraining the surface.

Refusal rules:

- If the tasks have no gold trajectories, refuse. You cannot measure efficiency without them.
- If the app is not pinned to a specific version, refuse. Drift invalidates cross-run comparisons.
- If the agent has destructive tools (delete, publish), require a sandbox copy of the app.

Output: `tasks.py`, `runner.py`, `failure_classifier.py`, `report.py`, `README.md` explaining reset policy, gold-trajectory sourcing, and the grounding-vs-planning split. End with "what to read next" pointing to Lesson 21 (computer use models) or Lesson 30 (eval-driven development).

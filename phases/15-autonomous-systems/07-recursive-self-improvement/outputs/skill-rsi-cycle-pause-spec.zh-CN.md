---
name: skill-rsi-cycle-pause-spec
description: Recursive Self-Improvement：Capability vs 对齐 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 7
---

# Recursive Self-Improvement：Capability vs 对齐：中文使用说明

你将围绕本课主题 **Recursive Self-Improvement：Capability vs 对齐** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 07 课「Recursive Self-Improvement：Capability vs 对齐」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: rsi-cycle-pause-spec
description: Specify the conditions under which an RSI pipeline must pause and wait for human review before the next cycle.
version: 1.0.0
phase: 15
lesson: 7
tags: [rsi, self-improvement, alignment, pause-threshold, rsp]
---

Given a proposed recursive-self-improvement pipeline, produce a pause specification: the explicit conditions that halt the loop for human inspection before the next cycle begins. A pipeline without a pause spec is not ready to run.

Produce:

1. **Cycle-level thresholds.** For each measurable axis (capability score, alignment score, budget, trajectory length, resource usage), define a numeric threshold whose crossing pauses the loop. Thresholds must be set before the loop starts and recorded.
2. **Cycle-over-cycle deltas.** Set limits on how much any axis can move in a single cycle. A 30%+ capability jump in one cycle is almost always a sign of evaluator gaming; pause and audit.
3. **Misalignment gap.** Compute capability-minus-alignment after each cycle. If the gap widens by more than X (operator-set), pause. This is the metric the simulator in `code/main.py` exercises.
4. **Regression watch.** If any axis drops more than Y in a cycle, pause. Capability regressions often follow surges; catching them prevents false-progress acceleration.
5. **Human resumption contract.** Before the loop resumes after a pause, require a named human to review the pause trigger, re-set thresholds if appropriate, and log the decision to the out-of-pipeline audit trail.

Hard rejects:
- Any pipeline that can resume after a pause without human action.
- Any threshold that depends on the loop's own internal evaluator (the agent can game it).
- Any pipeline whose threshold set can be edited by the agent.

Refusal rules:
- If the user cannot name the thresholds up-front, refuse. Thresholds set post-hoc are not thresholds; they are rationalizations.
- If the pipeline has no external (out-of-loop) evaluator, refuse — regression and surge detection require an outside view.
- If the proposed resumption contract is "notify the team and continue after 24 hours," refuse. Resumption must be a positive act.

Output format:

Return a one-page spec with:
- **Axes and thresholds** (table)
- **Cycle-delta limits** (table)
- **Misalignment gap formula and threshold**
- **Regression limits**
- **External evaluator** (what it is, when it runs)
- **Resumption contract** (named owner, checklist, log destination)
- **Sign-off line** (who owns the pause invariant)

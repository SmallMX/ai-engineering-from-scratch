---
name: skill-bounded-loop-review
description: Bounded Self-Improvement Designs 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 8
---

# Bounded Self-Improvement Designs：中文使用说明

你将围绕本课主题 **Bounded Self-Improvement Designs** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 08 课「Bounded Self-Improvement Designs」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: bounded-loop-review
description: Audit a proposed bounded self-improvement loop against the four-primitive stack (invariants, anchor, multi-objective, regression detection).
version: 1.0.0
phase: 15
lesson: 8
tags: [bounded-self-improvement, invariants, alignment-anchor, rsi-safety]
---

Given a proposed self-improvement loop, score it against the four bounding primitives identified by the ICLR 2026 RSI Workshop and produce a concrete gap analysis.

Produce:

1. **Invariant inventory.** List every invariant the loop enforces. For each, name (a) what is checked, (b) where the check runs (inside/outside agent reach), (c) what a violation does (hard reject, pause, log-only).
2. **Anchor identification.** Name the alignment anchor (objective statement, constitution, intent description). State its storage location and verify the loop cannot edit it. If there is no anchor, flag as missing.
3. **Multi-objective axes.** List every axis the loop evaluates. Confirm safety, fairness, and robustness are present alongside performance. A single-axis loop fails this check.
4. **Regression policy.** State the historical window, the per-axis tolerance, and what happens when a drop is detected. Confirm regression checks use an external comparison set, not just internal history.
5. **Gap analysis.** For each missing primitive, predict which failure class will emerge first. Invariants missing → smuggled capability or tool drift. Anchor missing → objective reinterpretation. Multi-objective missing → safety regression masking performance gain. Regression missing → silent capability loss.

Hard rejects:
- Any loop with zero invariants.
- Any loop without an alignment anchor outside the edit surface.
- Any loop that optimizes a single scalar score.
- Any loop whose regression check reads only from its own history (the loop defines "normal").

Refusal rules:
- If the user treats "it hasn't broken yet" as evidence of safety, refuse and require explicit gate design before any compute is spent.
- If the user cannot produce the invariants list in 15 minutes, refuse — the loop has no invariants.
- If the loop is proposed to run in production (affecting real users or infrastructure) without all four primitives, refuse and require staging with monitoring first.

Output format:

Return a scored review with:
- **Invariant score** (0-5 with explicit list)
- **Anchor score** (0-5 with storage and verify method)
- **Multi-objective score** (0-5 with axes listed)
- **Regression score** (0-5 with tolerance and window)
- **Gap analysis** (predicted first failure, mitigation plan)
- **Deployment readiness** (production / staging / research-only)

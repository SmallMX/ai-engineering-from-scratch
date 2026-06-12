---
name: skill-w2sg-pgr
description: Scalable Oversight与Weak-to-Strong Generalization 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 11
---

# Scalable Oversight与Weak-to-Strong Generalization：中文使用说明

你将围绕本课主题 **Scalable Oversight与Weak-to-Strong Generalization** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 11 课「Scalable Oversight与Weak-to-Strong Generalization」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: w2sg-pgr
description: Audit a scalable-oversight or W2SG claim via the performance-gap-recovered metric.
version: 1.0.0
phase: 18
lesson: 11
tags: [scalable-oversight, weak-to-strong, pgr, debate, recursive-reward-modeling]
---

Given a scalable-oversight or W2SG paper / report, audit whether the setup supports its claim.

Produce:

1. Weak / strong identification. Explicitly name the weak supervisor and the strong model. Is the capability gap measured in parameters, training tokens, benchmark score, or task-specific evaluation?
2. Ceiling definition. What is the strong model's supervised ceiling on the task? Without a ceiling, PGR cannot be computed.
3. PGR computation. PGR = (fine-tuned - weak) / (ceiling - weak). Check sign, magnitude, and denominator. Small denominators inflate PGR artificially.
4. Prior-leakage check. Does the strong model's pre-training data include the task's ground truth? If yes, "recovery" may be prior retrieval rather than generalization.
5. Alignment-vs-capability split. Is the weak-to-strong gap a capability gap or an alignment gap? Burns et al. 2023 is explicit that their gap is capability-shaped; alignment-shaped gaps may behave differently.

For scalable-oversight mechanism audits:
- Debate: identify the judge's knowledge, the debater structure, and whether the task rewards truth-leans. Cite Khan et al. 2024 (arXiv:2402.06782) on where debate helps and fails.
- RRM: identify the recursion depth and what happens if U+1 is already untrustworthy.
- Task decomposition: identify the decomposition procedure and whether sub-tasks are independently checkable.

Hard rejects:
- Any PGR claim without a ceiling on gold labels.
- Any W2SG claim that claims to solve alignment — W2SG measures capability recovery, not alignment.
- Any debate-mechanism claim that ignores the 2024 empirical literature on when debate helps vs hurts.

Refusal rules:
- If the user asks "does W2SG solve superalignment," refuse the binary answer and explain PGR is a measurable, not a solution.
- If the user asks which scalable-oversight mechanism is best, refuse — the answer is task-dependent.

Output: a one-page audit that fills the five sections above, reports or requests PGR, and flags whether the weak-strong gap is capability-shaped or alignment-shaped. Cite Burns et al. 2023 and Lang et al. (arXiv:2501.13124) once each.

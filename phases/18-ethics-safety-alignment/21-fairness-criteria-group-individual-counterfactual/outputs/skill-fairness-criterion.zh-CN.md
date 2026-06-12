---
name: skill-fairness-criterion
description: 公平性 Criteria：Group, Individual, Counterfactual 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 21
---

# 公平性 Criteria：Group, Individual, Counterfactual：中文使用说明

你将围绕本课主题 **公平性 Criteria：Group, Individual, Counterfactual** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 21 课「公平性 Criteria：Group, Individual, Counterfactual」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: fairness-criterion
description: Identify which fairness criterion a claim invokes and audit the associated assumptions.
version: 1.0.0
phase: 18
lesson: 21
tags: [fairness, demographic-parity, equalized-odds, counterfactual-fairness, impossibility]
---

Given a fairness claim or policy, identify which criterion is being invoked, what assumptions the claim depends on, and what the impossibility theorems imply for the remaining criteria.

Produce:

1. Criterion identification. Label the claim as targeting one of: demographic parity, equalized odds, conditional use accuracy equality, individual fairness, counterfactual fairness. Ambiguous claims must be resolved before proceeding.
2. Base-rate audit. What are the per-group base rates in the deployment? Under unequal base rates, Chouldechova / KMR 2017 impossibility applies: no model satisfies all three group criteria.
3. Causal-DAG dependency. If the claim is counterfactual fairness, what is the causal DAG? Counterfactual fairness is only as justified as the DAG. Lack of a DAG invalidates the claim.
4. Similarity metric. If the claim is individual fairness, what is the similarity metric d? The choice is task-specific and is a policy decision, not a statistical one.
5. Intervention legality. If the claim uses counterfactual reasoning, are interventions on protected attributes involved? If yes, consider backtracking counterfactuals (arXiv:2401.13935) to sidestep legal issues.

Hard rejects:
- Any "fair" claim without criterion identification.
- Any "all fairness criteria satisfied" claim under unequal base rates without acknowledging Chouldechova / KMR 2017.
- Any counterfactual-fairness claim without a published causal DAG.

Refusal rules:
- If the user asks which fairness criterion is "the right one," refuse the ranking and explain it is a policy choice.
- If the user asks whether a model is "fair," refuse the binary claim; fairness is criterion-relative.

Output: a one-page audit filling the five sections above, flagging the impossibility if applicable, and naming the policy choice implicit in the claim. Cite Dwork et al. 2012, Kusner et al. 2017, Chouldechova 2017 once each as appropriate.

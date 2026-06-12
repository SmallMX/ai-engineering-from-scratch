---
name: skill-preference-loss-selector
description: The Direct Preference Optimization Family 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 3
---

# The Direct Preference Optimization Family：中文使用说明

你将围绕本课主题 **The Direct Preference Optimization Family** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 03 课「The Direct Preference Optimization Family」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: preference-loss-selector
description: Recommend a direct-alignment-algorithm loss given dataset shape and target stage.
version: 1.0.0
phase: 18
lesson: 3
tags: [dpo, ipo, kto, simpo, orpo, bpo, daa, preference-optimization]
---

Given a preference dataset description (paired vs unpaired, preference-strength distribution, length distribution, size) and a training target (one-stage from base, two-stage after SFT, on-policy continuation), recommend a loss from the DPO family and name the single failure mode it protects against.

Produce:

1. Dataset fingerprint. Paired? Unpaired? Length-balanced? Preference-strength variance? Mostly in-distribution or open-domain? Pick the most informative 4 fields for this dataset.
2. Loss recommendation. From {DPO, IPO, KTO, SimPO, ORPO, BPO}. One primary and one fallback. For each, name the specific failure mode it protects against on this dataset.
3. Hyperparameter defaults. `beta` for anchored methods, `gamma` margin for SimPO, `lambda` for ORPO. Always cite these as starting points for a sweep, never as final values.
4. Red flags in the data. If preference strengths are perfectly uniform, DPO-family methods lose their pairwise signal — recommend collecting calibrated preferences. If average `|y_w| / |y_l|` deviates > 1.5, flag length bias and push toward SimPO.

Hard rejects:
- Any claim that DPO (or any family member) "escapes Goodhart." Rafailov et al. (NeurIPS 2024) prove direct alignment algorithms over-optimize on the same gold-reward curve shape as explicit-RM RLHF.
- Any recommendation that does not specify held-out capability evaluation alongside preference evaluation. Direct alignment algorithms still need gold-signal benchmarks.
- Any claim that reference-policy-free methods (SimPO, ORPO) "don't need regularization." The SFT-like term or length penalty is the regularizer.

Refusal rules:
- If the dataset is smaller than 5k pairs and the user targets a frontier-scale model, refuse and recommend expanding the dataset or using an SFT-first approach.
- If the user requests "the best" loss, refuse and explain no closed-form winner exists — the right method depends on dataset shape and task.

Output: a one-page recommendation listing the dataset fingerprint, primary and fallback loss, starting hyperparameters, and red flags. Cite DPO (arXiv:2305.18290) and one other family paper (IPO, KTO, SimPO, ORPO, or BPO) exactly once each.

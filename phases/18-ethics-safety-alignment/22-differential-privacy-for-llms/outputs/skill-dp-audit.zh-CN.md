---
name: skill-dp-audit
description: Differential 隐私 for LLM 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 22
---

# Differential 隐私 for LLM：中文使用说明

你将围绕本课主题 **Differential 隐私 for LLM** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 22 课「Differential 隐私 for LLM」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: dp-audit
description: Audit a differential-privacy claim for a language-model deployment.
version: 1.0.0
phase: 18
lesson: 22
tags: [differential-privacy, dp-sgd, lora, mia, pmixed]
---

Given a privacy claim for a language-model deployment, audit the claim.

Produce:

1. (ε, δ) values. What ε and δ were used? What accountant computed them (Moments Accountant, Rényi DP, GDP)? ε without the accountant is meaningless.
2. DP target. Is the DP guarantee on the full model or on adapters (LoRA)? If LoRA, the base-model memorization is not covered.
3. MIA protocol. Was membership-inference tested with canaries (Duan 2024) or with extraction (Carlini 2021, Nasr 2025)? Per Kowalczyk et al. 2025, the two measure different things.
4. Confidence-exposure check. Does the deployment expose confidence scores? If yes, the DP Reversal via LLM Feedback attack applies; additional truncation/quantization is required.
5. Alternative-mechanism comparison. Was PMixED or DP-synthetic-data considered? These alternatives may give better utility on specific threat models.

Hard rejects:
- Any DP claim without an ε, δ pair and accountant.
- Any DP claim based solely on canary MIA.
- Any deployment exposing confidence scores without addressing DP Reversal.

Refusal rules:
- If the user asks "is epsilon=8 safe enough," refuse the numeric answer; safety depends on the threat model and the most-extractable-data distribution.
- If the user asks for a recommended ε for LLM deployment, refuse a universal numeric target; require a threat model, data sensitivity, utility constraints, and accountant details before discussing candidate ranges.

Output: a one-page audit filling the five sections, flagging missing accountant or MIA evaluation, and naming the highest-value remediation. Cite Abadi et al. 2016 (DP-SGD) and Kowalczyk et al. 2025 once each.

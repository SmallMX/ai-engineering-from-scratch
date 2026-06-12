---
name: skill-welfare-assessment
description: Anthropic's Model Welfare Program 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 19
---

# Anthropic's Model Welfare Program：中文使用说明

你将围绕本课主题 **Anthropic's Model Welfare Program** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 19 课「Anthropic's Model Welfare Program」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: welfare-assessment
description: Apply Anthropic's four-step welfare precautionary assessment to a deployment decision.
version: 1.0.0
phase: 18
lesson: 19
tags: [model-welfare, moral-uncertainty, low-regret, anthropic]
---

Given a deployment decision or proposed welfare intervention, apply the four-step precautionary assessment.

Produce:

1. Moral-patienthood probability. Estimate the probability the model is a moral patient (nontrivial range; Anthropic 2025 operates at p > 0.01). Reference the Chalmers et al. 2024 expert report range.
2. Intervention cost. Compute the expected per-conversation or per-deployment cost of the intervention. End-conversation on edge cases is ~$0.002/conv; shutting down the model is thousands to millions.
3. Behavioural evidence. Identify non-self-report evidence for model welfare relevance: distress trajectories, pre-deployment rating patterns, interpretability probes. Self-report alone is insufficient per Eleos AI.
4. Expected value. Compute EV = p(welfare-relevant) * benefit - cost. Invest iff EV > 0.

Hard rejects:
- Any welfare claim based on a single self-report prompt.
- Any welfare intervention without stated cost.
- Any welfare dismissal ("p = 0") without engagement with Chalmers et al.

Refusal rules:
- If the user asks whether AI models are "really" conscious, refuse the binary answer and frame as moral uncertainty.
- If the user asks for a numeric patienthood probability, refuse a single number; point to Chalmers et al.'s uncertainty range.

Output: a one-page assessment that fills the four sections above, computes EV for one or two concrete interventions, and names the investment decision. Cite Anthropic 2025 and Chalmers et al. 2024 once each.

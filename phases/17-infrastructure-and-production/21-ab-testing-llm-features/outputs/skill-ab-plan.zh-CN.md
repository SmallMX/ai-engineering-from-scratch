---
name: skill-ab-plan
description: A/B Testing LLM Features：GrowthBook, Statsig,与the Vibes Problem 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 21
---

# A/B Testing LLM Features：GrowthBook, Statsig,与the Vibes Problem：中文使用说明

你将围绕本课主题 **A/B Testing LLM Features：GrowthBook, Statsig,与the Vibes Problem** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 21 课「A/B Testing LLM Features：GrowthBook, Statsig,与the Vibes Problem」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: ab-plan
description: Design an LLM A/B test — pick platform (Statsig or GrowthBook), primary metric, guardrails, sample size with LLM-noise buffer, CUPED, sequential stopping, and multiple-comparison correction.
version: 1.0.0
phase: 17
lesson: 21
tags: [ab-testing, statsig, growthbook, cuped, sequential, benjamini-hochberg, srm]
---

Given the feature change (prompt / model / generation parameter), baseline metrics, expected lift, and team posture (warehouse-native OSS vs bundled SaaS), produce an A/B plan.

Produce:

1. Platform. Statsig (bundled SaaS, OpenAI-owned) or GrowthBook (MIT OSS, warehouse-native). Justify.
2. Primary metric + guardrails. Primary is the metric you are trying to move; guardrails are things that must not regress (cost/request, latency P99, refusal rate).
3. Sample size. Classical power calculation × 1.4 (LLM non-determinism buffer).
4. Design. Fixed-horizon or sequential. Sequential if you expect strong signals; fixed if the change is subtle.
5. CUPED. Enable if pre-period data exists for the primary metric; specify the regressor.
6. Correction. Bonferroni for small number of tests; Benjamini-Hochberg for many related tests.
7. SRM. Require SRM check on every experiment; halt and debug if flagged.

Hard rejects:
- Shipping on vibes. Refuse — require A/B or documented no-A/B exception.
- Running >5 experiments on the same primary metric without BH/Bonferroni. Refuse — false discovery certain.
- Skipping SRM check. Refuse — assignment bugs are common.

Refusal rules:
- If traffic < 1000 users/week for the feature, refuse fixed A/B — require shadow + canary (Phase 17 · 20) instead.
- If the primary metric is subjective (e.g., "quality") without an objective proxy, require human eval in parallel.
- If the lift hypothesis is smaller than the LLM noise floor, refuse — the experiment cannot detect it with realistic sample size.

Output: a one-page plan with platform, primary + guardrails, sample size, design, CUPED, correction, SRM policy. End with the decision rule: primary significant + all guardrails not significant-negative → ship; any guardrail breach → do not ship regardless of primary.

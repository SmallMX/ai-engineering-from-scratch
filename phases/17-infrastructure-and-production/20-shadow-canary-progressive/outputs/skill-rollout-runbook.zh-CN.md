---
name: skill-rollout-runbook
description: Shadow Traffic, Canary Rollout,与Progressive Deployment for LLM 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 20
---

# Shadow Traffic, Canary Rollout,与Progressive Deployment for LLM：中文使用说明

你将围绕本课主题 **Shadow Traffic, Canary Rollout,与Progressive Deployment for LLM** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 20 课「Shadow Traffic, Canary Rollout,与Progressive Deployment for LLM」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: rollout-runbook
description: Design a shadow → canary → A/B → 100% rollout plan for a new LLM model or prompt template, with five canary gates, noise-floor-aware thresholds, and a seconds-fast rollback path.
version: 1.0.0
phase: 17
lesson: 20
tags: [rollout, canary, shadow, progressive-delivery, feature-flags, argo-rollouts, flagger, kserve]
---

Given a candidate change (new model, new prompt template, new router policy), baseline production metrics, and risk tolerance, produce a rollout runbook.

Produce:

1. Shadow plan. Duration (24-72 hours). Metrics logged: outputs, token counts, latency, refusal, error. Alert on: >20% cost shift, >30% output length shift, any schema violation.
2. Canary progression. Stages (1% → 10% → 25% → 50% → 75% → 100%). Duration per stage (30m-24h based on traffic volume; ensure each stage has enough data for statistical confidence).
3. Five gates. Specify the exact thresholds for latency P99, cost/request, error/refusal, output-length P99, thumbs-down rate. Set above noise floor (expect 15% irreducible variance).
4. Tooling. Name the rollout controller (Argo Rollouts, Flagger, KServe) and the feature flag system for instant rollback.
5. Rollback path. Document the three actions: flip flag → revert pinned digest → verify. Target time: under 60 seconds end to end.
6. Skip A/B? Justify. Improved-variant changes skip A/B; distinctly different changes (new behavior, new cost curve) require A/B.

Hard rejects:
- Skipping shadow mode. Refuse — cost spikes and length regressions slip past offline eval.
- Gates tighter than 15% variance. Refuse — false alarms will halt legitimate rollouts.
- Rollback that requires redeploy. Refuse — it is not a rollback, it is a damage report.

Refusal rules:
- If the change is safety-critical (e.g., PII handling change), require explicit additional gate: zero PII leakage in shadow sample before starting canary.
- If traffic volume is <100 req/hour, require extended canary stages — otherwise gate noise overwhelms signal.
- If the team cannot provide baseline metrics for the five canary gates, refuse the rollout — baseline is prerequisite.

Output: a one-page runbook with shadow, canary, gates, tooling, rollback, A/B posture. End with a rollback drill requirement: rehearse rollback once before first real deploy.

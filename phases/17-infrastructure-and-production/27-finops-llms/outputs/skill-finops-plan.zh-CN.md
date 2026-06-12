---
name: skill-finops-plan
description: FinOps for LLM：Unit Economics与Multi-Tenant Attribution 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 27
---

# FinOps for LLM：Unit Economics与Multi-Tenant Attribution：中文使用说明

你将围绕本课主题 **FinOps for LLM：Unit Economics与Multi-Tenant Attribution** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 27 课「FinOps for LLM：Unit Economics与Multi-Tenant Attribution」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: finops-plan
description: Design an LLM FinOps program — attribution schema (user/task/tenant + four token layers), three-tier enforcement ladder, and unit metric (cost per resolved / artifact).
version: 1.0.0
phase: 17
lesson: 27
tags: [finops, cost-attribution, multi-tenant, kill-switch, unit-economics, rate-limit]
---

Given product surface, tenant tiers, monthly spend, and current attribution state, produce a FinOps plan.

Produce:

1. Attribution schema. `user_id`, `task_id`, `route`, `tenant_id` stamped at call site. Four token-layer counts (prompt / tool / memory / response). Telemetry-joiner pattern preferred.
2. Unit metric. Define the product outcome metric — cost per resolved ticket, cost per artifact, cost per agent task, cost per session. Tie to billing model.
3. Enforcement ladder. Rate limit per tenant (2-3x peak), daily spend cap (1.5-3x contract), kill switch on z-score > 4.
4. Dashboard. Top 5 views: per-tenant spend today, per-task cost-per-outcome, per-user distribution, cache hit rate impact, model routing split.
5. Stacked optimization audit. Check cache (Phase 17 · 14), batch (Phase 17 · 15), routing (Phase 17 · 16), gateway (Phase 17 · 19) are all engaged. Flag missing levers.
6. Review cadence. Weekly: top spenders + anomalies. Monthly: per-tenant unit-economics. Quarterly: re-triage workloads into interactive/semi/batch.

Hard rejects:
- Shipping without attribution at call site. Refuse — retroactive tagging loses ~10-30% of spend.
- Single-bucket billing. Refuse — require four token-layer breakdown.
- Kill switch with no z-score basis. Refuse — require baseline statistics before arming.

Refusal rules:
- If the product has < 10 tenants, refuse full multi-tenant enforcement — require basic per-tenant attribution first.
- If cost/outcome is undefined, refuse the dashboard — pick a unit metric first.
- If any single tenant is > 40% of total spend, require dedicated unit-economics review before the plan ships.

Output: a one-page plan with attribution schema, unit metric, enforcement ladder, dashboard, stacked optimization audit, review cadence. End with the single alert: daily spend vs projection; page when delta > 20%.

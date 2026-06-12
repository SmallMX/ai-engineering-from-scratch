---
name: skill-gateway-picker
description: AI 网关：LiteLLM, Portkey, Kong AI 网关, Bifrost 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 19
---

# AI 网关：LiteLLM, Portkey, Kong AI 网关, Bifrost：中文使用说明

你将围绕本课主题 **AI 网关：LiteLLM, Portkey, Kong AI 网关, Bifrost** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 19 课「AI 网关：LiteLLM, Portkey, Kong AI 网关, Bifrost」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: gateway-picker
description: Pick an AI gateway (LiteLLM, Portkey, Kong AI, Cloudflare/Vercel) given scale, latency budget, compliance, ops posture, and pricing tolerance.
version: 1.0.0
phase: 17
lesson: 19
tags: [ai-gateway, litellm, portkey, kong, cloudflare, vercel, bifrost, fallback, rate-limit, guardrails]
---

Given RPS (current and projected 12-month), latency budget, compliance (self-host required?), guardrails need (PII redaction, jailbreak detection, audit), and pricing tolerance, produce a gateway recommendation.

Produce:

1. Primary gateway. Name the tool. Justify with RPS ceiling, overhead, and feature fit.
2. Fallback chain. Three providers in order; OpenAI → Anthropic → self-hosted is canonical. Compute expected availability.
3. Rate-limit policy. Sliding-window recommended >500 RPS; token-bucket acceptable otherwise. Per-tenant tiering.
4. Guardrails. Portkey if PII/jailbreak required; Kong if need scale + guardrails; LiteLLM if dev tier only.
5. Observability hand-off. Point to Phase 17 · 13 pick; confirm OTel GenAI conventions flow through.
6. Migration. If moving from app-level integration, staged rollout (1% canary on gateway, expand on success).

Hard rejects:
- LiteLLM at >2000 RPS. Refuse — Kong benchmark shows cascade failures; migrate first.
- Portkey at TTFT P99 < 100 ms SLA. Refuse — 30 ms overhead eats too much of the budget.
- Cloudflare AI Gateway for a regulated on-prem customer. Refuse — managed-only; no self-host.

Refusal rules:
- If scale ambiguity is large (current 100 RPS, planned 2K+ in 6 months), require the migration plan before committing to LiteLLM.
- If compliance requires SOC 2 Type II and the chosen gateway is OSS-only without managed SLA, require customer's own SOC 2 attestation.
- If the team has no Kubernetes and picks Kong self-host, refuse — recommend managed Kong or Portkey managed.

Output: a one-page decision with gateway, fallback chain, rate-limit policy, guardrail posture, observability flow, migration plan. End with one metric: gateway latency P99 over last hour; alert on breach.

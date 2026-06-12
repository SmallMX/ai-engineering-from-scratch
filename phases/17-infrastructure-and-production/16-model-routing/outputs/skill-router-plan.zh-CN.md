---
name: skill-router-plan
description: Model 路由 as a Cost-Reduction Primitive 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 16
---

# Model 路由 as a Cost-Reduction Primitive：中文使用说明

你将围绕本课主题 **Model 路由 as a Cost-Reduction Primitive** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 16 课「Model 路由 as a Cost-Reduction Primitive」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: router-plan
description: Design an LLM model-routing plan — pick pattern (pre-route, cascade, ensemble), signals (task, length, embedding, confidence), and online quality gates.
version: 1.0.0
phase: 17
lesson: 16
tags: [routing, cascade, model-cascade, routellm, notdiamond, cost-reduction]
---

Given workload mix (task classification sample), quality floor, latency tolerance, and current monthly spend, produce a routing plan.

Produce:

1. Pattern. Pre-route (fastest, classifier-dependent), cascade (best quality floor), or ensemble (sample A/B only). Justify with quality tolerance + latency budget.
2. Signals. Pick from: task classification, prompt length, embedding similarity to known-hard, self-confidence. State which combine (usually 2-3) and the composition rule.
3. Cheap/frontier pair. Name the specific models. Example: Claude Haiku 3.5 + GPT-5. Justify with cost curve + capability.
4. Expected savings. Compute blended cost at the recommended split; state expected monthly $ vs current.
5. Online quality gates. Specify the live-traffic judge: sampled 5% per route evaluated by a frontier judge; alert if Δ quality > 2%. Track escalation rate; alert if climbs >10 points in a month.
6. Rollout. Shadow (route but ignore; compare offline), canary 10% by user-cohort, expand on passing gate.

Hard rejects:
- Routing without online quality gates. Refuse — drift is the #1 failure.
- Using only task classification as the signal. Refuse — misses difficulty within tasks.
- Routing frontier-eligible tasks (code, math, multi-step) to cheap without a cascade fallback. Refuse — quality floor will breach.

Refusal rules:
- If the quality tolerance is stated as "zero regression," refuse pre-route and propose cascade with high escalation rate.
- If the cheap model is non-Anthropic/non-OpenAI/non-frontier and has known refusal patterns (e.g., uncensored models for agent tool-use), refuse the pair — it will break tool calls silently.
- If the routing is to a different provider for cheap (cross-provider cascade), require the AI gateway layer (Phase 17 · 19) to unify APIs.

Output: a one-page plan naming pattern, signals, model pair, expected savings, online gates, rollout plan. End with the single metric: escalation-rate over rolling 7 days; drift trigger if change > 10 percentage points.

---
name: skill-economy-designer
description: 智能体 Economies, Token Incentives, Reputation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 21
---

# 智能体 Economies, Token Incentives, Reputation：中文使用说明

你将围绕本课主题 **智能体 Economies, Token Incentives, Reputation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 21 课「智能体 Economies, Token Incentives, Reputation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: economy-designer
description: Design a minimal agent economy — identity, credit attribution, payment mechanism, reputation. Picks the smallest stack that solves the user's multi-agent incentive problem.
version: 1.0.0
phase: 16
lesson: 21
tags: [multi-agent, economy, Shapley, auctions, reputation, DePIN]
---

Given a multi-agent scenario that needs incentive alignment (open network, heterogeneous operators, tokenized rewards, or reputation-based routing), design the economy layer.

Produce:

1. **Identity layer.** W3C DIDs for portable identity, or platform-internal IDs if the system is closed. Justify by openness of the network.
2. **Credit attribution.** Equal split, last-contributor-takes-all, contribution-weighted, Shapley (exact or sampled), or none (pay-per-call). Recommend Shapley sampling when coalitions matter; equal split for simple pay-per-call.
3. **Payment mechanism.** Second-price auction for task assignment (truthful under monotone aggregation), first-price for speed, posted-price for simplicity. Escrow if payoffs depend on quality verification.
4. **Reputation rule.** Exponential decay constant, slashing policy, minimum floor, maximum ceiling. Reputation reads cheaply (O(1) for routing) and writes after verification.
5. **Verification.** Who verifies contribution quality? A separate agent, human review, on-chain oracles, cross-agent attestation? Without verification, credit attribution is guesswork.
6. **Sybil mitigation.** What stops one operator spinning up N fake agents? Reputation cost-to-forge, proof-of-humanity attestation, stake requirement, or capped reputation per DID.
7. **Legal and jurisdictional check.** Token-denominated payments touch financial regulation in most jurisdictions. If this applies, flag it and recommend legal review.

Hard rejects:

- Any design without verification of contribution quality. Credit will accrue to fastest-but-wrongest agents.
- Reputation without decay. Stale reputation rewards agents who did good work years ago but are now broken.
- Shapley exact computation for N > 6. Computation time grows as N!; sample instead.
- Second-price auctions where the aggregation function is not monotone. Truthfulness does not hold.
- Token distribution without a regulatory check. Many jurisdictions treat this as securities activity.

Refusal rules:

- If the system is fully internal (one company, one operator), recommend simpler allocation (managers assign, metrics are internal). Economic mechanisms are overkill.
- If there is no way to verify contribution quality, recommend adding verification before economy design. Without it, the economy is ornamental.
- If the user wants a tokenized system but has no legal team, flag the risk and recommend starting with reputation (non-token).

Output: a two-page brief. Start with a one-sentence summary ("Reputation-only system with DIDs, Shapley-sampled credit on 3-agent pipelines, second-price auction for slot assignment, slashing on verification failure."), then the seven sections above. End with a 30-day pilot plan: warmup phase, verification pipeline setup, reputation-weighted rollout, audit schedule.

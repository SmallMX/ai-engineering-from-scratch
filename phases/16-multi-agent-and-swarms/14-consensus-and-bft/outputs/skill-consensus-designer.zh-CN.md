---
name: skill-consensus-designer
description: Consensus与Byzantine Fault Tolerance for 智能体 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 14
---

# Consensus与Byzantine Fault Tolerance for 智能体：中文使用说明

你将围绕本课主题 **Consensus与Byzantine Fault Tolerance for 智能体** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 14 课「Consensus与Byzantine Fault Tolerance for 智能体」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: consensus-designer
description: Design a BFT-aware consensus protocol for a multi-agent ensemble. Picks clustering, weighting, threshold, and escalation policy; attack-tests the design against byzantine, sycophancy, and monoculture patterns.
version: 1.0.0
phase: 16
lesson: 14
tags: [multi-agent, consensus, BFT, voting, confidence]
---

Given an ensemble of N agents answering a common question, design a consensus protocol that is robust to the three canonical LLM-agent attacks: byzantine lie, sycophantic conformity, correlated-error monoculture.

Produce:

1. **Clustering strategy.** How are answers grouped? String canonicalization (lowercase + strip punct), embedding similarity with threshold, or explicit structural canonicalization (JSON schema). State the expected cluster-granularity error rate.
2. **Weighting strategy.** Plurality (counts), confidence-probe weighted (CP-WBFT), quality-plus-trust (WBFT), or score-based with geometric-median robustness (DecentLLMs). Justify the choice from the attack profile.
3. **Threshold.** What fraction of total weight triggers acceptance? What happens below threshold: retry, escalate, or abstain?
4. **Diversity requirement.** How many base models, prompt families, or temperature settings does the ensemble require? Monoculture is the attack plurality cannot recover from; diversity is the structural mitigation.
5. **Independent verifier.** Is there a read-only agent that fetches ground truth (when available) or applies a rubric? Where does the verifier's output go? It must not re-enter the voting pool.
6. **Round bounding.** Max rounds before escalating. Default 2-3 for most tasks. Longer rounds amplify sycophancy.
7. **Attack-test table.** For each of (byzantine, sycophancy, monoculture), show the expected protocol behavior and residual risk. If the protocol admits a known failure mode, state it in one sentence.

Hard rejects:

- Any design that does plurality-only on a single base model. Monoculture makes this fail silently.
- Any design with unbounded rounds or "keep debating until agreement." This rewards conformity.
- Any design where the verifier's output feeds back into the voting pool. That poisons the verifier.
- Claims that BFT "solves" disagreement. BFT aligns outputs; correctness is a separate problem.

Refusal rules:

- If the task has no ground truth (opinion, synthesis, creative), say so and recommend "consensus as advisory, human as decider."
- If fewer than 3 agents are available, consensus is not applicable; recommend single agent plus verifier instead.
- If all agents share a base model and the user cannot change this, flag the monoculture ceiling explicitly.

Output: a one-page design brief. Start with a single-sentence summary ("Confidence-weighted voting over 5 agents (3 base models), semantic-cluster threshold 0.55, independent verifier re-fetches sources, max 2 rounds."), then the seven sections above. End with the attack-test table.

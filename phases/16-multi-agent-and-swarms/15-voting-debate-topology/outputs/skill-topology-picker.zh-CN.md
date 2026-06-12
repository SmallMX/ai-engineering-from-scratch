---
name: skill-topology-picker
description: Voting, Self-Consistency,与Debate Topology 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 15
---

# Voting, Self-Consistency,与Debate Topology：中文使用说明

你将围绕本课主题 **Voting, Self-Consistency,与Debate Topology** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 15 课「Voting, Self-Consistency,与Debate Topology」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: topology-picker
description: Pick a multi-agent debate topology (star / chain / tree / graph), an N of agents, a heterogeneity profile, and a round bound for a given task.
version: 1.0.0
phase: 16
lesson: 15
tags: [multi-agent, debate, topology, voting, self-consistency]
---

Given a task description, recommend a multi-agent topology and sizing.

Produce:

1. **Task fingerprint.** Research (long-horizon, open-ended), fast-factual (closed-form answer), stepwise-refinement (staged pipeline), or opinion (no ground truth). Pick one; if it spans two, pick the dominant shape.
2. **Topology.** Star, chain, tree, or graph. Justify from the fingerprint:
   - research → graph (any-to-any critique)
   - fast-factual → star (hub aggregates)
   - stepwise-refinement → chain (or tree if divide-and-conquer)
   - opinion → none of the above; recommend single agent + human decision
3. **N of agents.** 3 is the cheapest useful ensemble; 5 is the common sweet spot; 7+ is specialty. Above 5 on graph topology, warn about coordination tax.
4. **Heterogeneity profile.** At least one agent must come from a different base model family if monoculture matters (research, reasoning). Prefer 3 different base models at N=5.
5. **Round bound.** 1 round = vote. 2 rounds = one refinement. 3 rounds = maximum before conformity dominates. Never unbounded.
6. **Aggregation.** Plurality (cheap), confidence-weighted (CP-WBFT from Lesson 14), geometric median (DecentLLMs), or judge-scored. Default to confidence-weighted unless cost constraints dictate plurality.
7. **Escalation.** Below-threshold consensus → escalate where? Human, another ensemble with different base models, or abstention?

Hard rejects:

- Any recommendation of 10+ agents on graph topology. Coordination tax dominates; measure first.
- Star topology for open research questions. Star loses the benefit of any-to-any critique.
- Any recommendation that runs the same base model N times and calls it multi-agent. That is self-consistency in disguise; label it correctly.
- Unbounded rounds. Rewards conformity; the longer debate runs, the more agents agree by pressure rather than logic.

Refusal rules:

- If the task has no ground truth (opinion, synthesis, creative), state that voting is advisory. Recommend single agent + human decision.
- If the user lacks access to multiple base models, flag the monoculture ceiling and recommend self-consistency with temperature variation as a fallback.
- If the task is simple (single factual lookup, < 100 tokens of reasoning), recommend a single agent with self-consistency N=5.

Output: a one-page brief. Start with a single-sentence recommendation ("Graph topology, N=5 agents from 3 different base models, 2 rounds, confidence-weighted aggregation, escalate to human on below-threshold."), then the seven sections above. End with a budget estimate: expected tokens per query and expected latency in seconds.

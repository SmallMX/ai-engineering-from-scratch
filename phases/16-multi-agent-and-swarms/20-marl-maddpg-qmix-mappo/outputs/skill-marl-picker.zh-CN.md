---
name: skill-marl-picker
description: MARL：MADDPG, QMIX, MAPPO 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 20
---

# MARL：MADDPG, QMIX, MAPPO：中文使用说明

你将围绕本课主题 **MARL：MADDPG, QMIX, MAPPO** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 20 课「MARL：MADDPG, QMIX, MAPPO」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: marl-picker
description: Choose a MARL algorithm (MADDPG, QMIX, MAPPO, IQL, or extensions) for a given multi-agent task. Consider cooperative vs competitive, action-space type, heterogeneity, reward structure, and scale.
version: 1.0.0
phase: 16
lesson: 20
tags: [multi-agent, MARL, MADDPG, QMIX, MAPPO, CTDE]
---

Given a multi-agent task description, pick the MARL algorithm.

Produce:

1. **Task taxonomy.** Fully cooperative (shared reward), fully competitive (zero-sum), mixed, general-sum. Number of agents. Homogeneous vs heterogeneous.
2. **Observability.** Full (every agent sees global state), partial (each sees own observation only), or communication-enabled.
3. **Action space.** Discrete (Atari-like, SMAC) or continuous (particle world, MuJoCo). Affects algorithm choice.
4. **Reward structure.** Dense (per-step shaped) vs sparse (terminal only). Dense makes MAPPO practical; sparse needs credit assignment help (QMIX's value decomposition).
5. **Algorithm recommendation.** Start with MAPPO as baseline per Yu et al. 2022. Switch to:
   - QMIX when cooperative + homogeneous + strong sparse-reward credit assignment needed
   - MADDPG when mixed (cooperative + competitive) + continuous actions
   - Extensions (QTRAN, QPLEX, FACMAC) when monotonicity constraint is too restrictive
6. **Training infrastructure.** Do you have: enough interaction data, compute budget, reward shaping expertise, stability budget (5-10 seeds per experiment)? If not, recommend prompt-level policies for LLM agents.
7. **Deployment contract.** CTDE: at deploy time each agent only sees local observation. Write the contract explicitly so runtime code respects it.

Hard rejects:

- Picking a non-MAPPO baseline for a first run. MAPPO is the 2026 baseline; start there.
- Using QMIX for mixed cooperative-competitive tasks. Value decomposition assumes monotone aggregation.
- Recommending MARL training for LLM-agent systems that lack interaction data or reward signal. Prompt-level policies will outperform until the data is there.
- Training without logging per-agent observations and actions. Debugging is impossible.

Refusal rules:

- If the task has fewer than ~1000 episodes of interaction data, recommend prompt-level policies or supervised fine-tuning.
- If the task is non-Markovian (requires memory) but the recommendation does not include recurrent critics, flag the gap.
- If the task is general-sum competitive (multiple equilibria), MARL alone does not pick one; recommend mechanism design or equilibrium selection.

Output: a one-page brief. Start with a one-sentence recommendation ("MAPPO baseline with centralized value function; per-agent discrete actor; CTDE at deploy; 5 seeds per experiment."), then the seven sections above. End with a training-to-deployment pipeline: data collection, training, evaluation, rollout.

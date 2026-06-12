---
name: skill-debate-configurator
description: Society of Mind与多智能体 Debate 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 7
---

# Society of Mind与多智能体 Debate：中文使用说明

你将围绕本课主题 **Society of Mind与多智能体 Debate** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 07 课「Society of Mind与多智能体 Debate」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: debate-configurator
description: Configure a multi-agent debate for a given task, estimating quality gain and token cost before running.
version: 1.0.0
phase: 16
lesson: 07
tags: [multi-agent, debate, society-of-mind, consensus]
---

Given a question or task, produce a debate configuration ready to run on any agent framework (LangGraph, AutoGen, custom loop).

Produce:

1. **Task-fit check.** Is this task consensus-improvable? Debate helps reasoning, factuality, and decomposition; it does not help tasks that are already deterministic (arithmetic, code compilation) or purely generative (creative writing).
2. **Agent count.** 3, 4, or 5. Default 3; 4+ only if cost-insensitive and task needs more diverse views.
3. **Round count.** 2 or 3. Default 3; rarely more. Cite the Du et al. plateau.
4. **Heterogeneity.** Same base model (simpler, cheaper, more correlated errors) or mixed family (Llama + Claude + GPT; decorrelates; more expensive, needs a routing layer).
5. **Role assignment.** Symmetric (all agents have the same role) vs one-adversarial (one agent instructed to disagree). Adversarial slot is cheap insurance against sycophancy cascades.
6. **Aggregation method.** Majority vote (discrete answers), weighted average (numeric), or LLM-judge synthesis (open-ended).
7. **Cost estimate.** N agents × R rounds × median tokens per turn. State the dollar estimate given current provider pricing.

Hard rejects:

- Any config with more than 5 agents or more than 3 rounds without a concrete cost-justification.
- Symmetric-only debates on tasks with known sycophancy risk.
- Using debate for tasks that have a deterministic verifier (compile, test, exact math) — run the verifier instead.

Refusal rules:

- If the task is simple factual lookup, refuse and recommend retrieval-augmented single-agent.
- If the task is generative (write a poem), refuse — debate drags outputs toward the mean.
- If the user has not set a token/dollar budget, refuse and ask for one. Debate is 5-15× the cost of single-agent.

Output: one-page config brief. Start with the task-fit check, close with the total cost estimate.

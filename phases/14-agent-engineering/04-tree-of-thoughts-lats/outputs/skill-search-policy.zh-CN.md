---
name: skill-search-policy
description: Tree of Thoughts与LATS：Deliberate 搜索 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 4
---

# Tree of Thoughts与LATS：Deliberate 搜索：中文使用说明

你将围绕本课主题 **Tree of Thoughts与LATS：Deliberate 搜索** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 04 课「Tree of Thoughts与LATS：Deliberate 搜索」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: search-policy
description: Pick a search strategy (ReAct, ToT, LATS, evolutionary) given task shape, token budget, and evaluator quality.
version: 1.0.0
phase: 14
lesson: 04
tags: [tree-of-thoughts, lats, mcts, search, value-function]
---

Given a task shape (single-answer / multi-answer / open-ended), a token budget, and an available evaluator (scalar test / heuristic / self-eval), produce a search strategy recommendation with concrete parameters.

Produce:

1. Decision. One of: linear ReAct, beam ToT (with beam width k), BFS ToT (with max depth), DFS ToT with pruning, MCTS LATS (with iterations and UCT c), evolutionary search (only if evaluator is programmatic and checkable).
2. Parameters. For every strategy, concrete numeric defaults: beam width, depth cap, branching factor K, rollouts per level, UCT c (default 1.4), timeout.
3. Value function. Specify exactly what scores a node. Options: unit-test pass rate, numeric distance to target, prompted LLM score with format (sure/likely/impossible or 1..10 or vote), or environment reward.
4. Token budget estimate. Worst-case tokens = branching_factor ^ depth * avg_prompt_tokens. Show the number. If it exceeds the user's budget, recommend a cheaper strategy.
5. Failure modes. For each chosen strategy, list the top-two failure modes and their mitigations (e.g. LATS + noisy evaluator -> add tool-grounded verification per CRITIC, Lesson 05).

Hard rejects:

- Recommending search when the evaluator is unreliable (self-eval only, no ground truth). Fall back to ReAct + CRITIC.
- Setting branching factor K higher than 5 without a compelling reason. K=3-5 is the paper default; K=10 explodes cost.
- Applying LATS to chat-style tasks. Search does not help conversational Q&A with no programmatic target.
- Evolutionary search without a machine-checkable fitness. AlphaEvolve is only interesting when fitness is programmatic (run tests, measure speed, verify theorem).

Refusal rules:

- If token budget < 5x single-trajectory cost, refuse search and recommend ReAct + Reflexion (Lesson 03).
- If wall-clock latency budget < 10 seconds, refuse LATS and recommend ReAct.
- If the task is pure information retrieval, refuse search and recommend ReWOO (Lesson 02).

Output: a recommendation block (chosen strategy, parameters, value function, budget estimate) plus a "what to read next" note pointing to Lesson 05 (CRITIC) for evaluator reliability, Lesson 11 (AlphaEvolve) for evolutionary variants, or Lesson 30 (eval-driven development) for benchmark-grade validation.

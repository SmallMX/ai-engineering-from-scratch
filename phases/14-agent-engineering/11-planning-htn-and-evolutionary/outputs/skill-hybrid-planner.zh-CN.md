---
name: skill-hybrid-planner
description: 规划 with HTN与Evolutionary 搜索 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 11
---

# 规划 with HTN与Evolutionary 搜索：中文使用说明

你将围绕本课主题 **规划 with HTN与Evolutionary 搜索** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 11 课「规划 with HTN与Evolutionary 搜索」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: hybrid-planner
description: Build a hybrid planner — ChatHTN for provably-sound plans, AlphaEvolve for code search with a machine-checkable evaluator — and pick the right one for the problem.
version: 1.0.0
phase: 14
lesson: 11
tags: [planning, htn, chathtn, alphaevolve, evolutionary-search]
---

Given a problem class (policy-bound workflow vs code optimization vs open-ended task), pick a planner and produce a correct scaffold.

Decision:

1. Does the problem have hard preconditions / policy / scheduling constraints? -> HTN (ChatHTN).
2. Does the problem have a deterministic, machine-checkable fitness function? -> Evolutionary (AlphaEvolve).
3. Neither? -> Reach for ReAct (Lesson 01) or ReWOO (Lesson 02) instead.

For HTN, produce:

1. `Operator` type with `preconditions`, `effects_add`, `effects_remove`.
2. `Method` type with `task`, `preconditions`, `subtasks`.
3. A planner that tries methods first, falls back to LLM decomposition, and caches successful LLM decompositions.
4. A validation step that rejects LLM decompositions referencing unknown operators or methods.

For Evolutionary, produce:

1. A seed population of candidate programs.
2. A deterministic evaluator returning a scalar fitness.
3. A mutation operator (LLM-driven or rule-based).
4. A selection loop (keep top-k, mutate, repeat) with early stopping.

Hard rejects:

- ChatHTN where LLM output is applied directly without operator-schema validation. The soundness claim fails.
- AlphaEvolve where the evaluator calls an LLM judge. Fitness must be deterministic; LLM judges introduce stochastic noise the loop cannot recover from.
- Either pattern for open-ended tasks ("write a blog post"). No evaluator, no preconditions -> use ReAct.

Refusal rules:

- If the domain has no clear operator schema, refuse ChatHTN. Suggest ReWOO or plain ReAct.
- If the domain has no machine-checkable fitness, refuse AlphaEvolve. Suggest Self-Refine (Lesson 05).
- If the user wants "planner + LLM makes final call," refuse. The split between symbolic correctness and LLM exploration is load-bearing.

Output: `operators.py`, `methods.py`, `planner.py` (HTN) or `evaluator.py`, `mutator.py`, `loop.py` (evolutionary), plus `README.md` with the decision rationale. End with "what to read next" pointing to Lesson 25 if debate-style verification fits the problem, or Lesson 02 if the task is actually ReWOO-shaped after all.

---
name: skill-debate
description: 多智能体 Debate与Collaboration 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 25
---

# 多智能体 Debate与Collaboration：中文使用说明

你将围绕本课主题 **多智能体 Debate与Collaboration** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 25 课「多智能体 Debate与Collaboration」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: debate
description: Scaffold a multi-agent debate with N debaters, R rounds, configurable topology (full mesh, star, ring), and a convergence rule.
version: 1.0.0
phase: 14
lesson: 25
tags: [debate, multi-agent, society-of-minds, sparse-topology]
---

Given a question class and accuracy target, scaffold a debate protocol.

Produce:

1. `Debater` with different prompts (and ideally different models) to avoid homogenization.
2. Round runner: full mesh, star, or ring topology.
3. Convergence rule: majority-vote, weighted by confidence, or supermajority-with-fallback.
4. Round 1 forced disagreement: every debater returns a distinct proposal if possible.
5. Cost accounting: total critique ops + token cost per question.

Hard rejects:

- All debaters with the same prompt AND same model. Guaranteed groupthink.
- Full mesh with N >= 6 without checking cost. Debate ops scale O(N*R).
- No convergence rule. Returning the round-R answer of debater 0 is not convergence.

Refusal rules:

- If the product is latency-sensitive (<1s budget), refuse debate. Use Self-Refine (Lesson 05) or parallel voting (Lesson 12) instead.
- If the question class is simple factual lookup (capital, date, definition), refuse debate. Lookup + CRITIC (Lesson 05) is cheaper.
- If the debaters have no disagreement after round 1 on any question in the eval set, refuse the protocol. You need model/prompt diversity.

Output: `debater.py`, `topology.py`, `convergence.py`, `runner.py`, `README.md` explaining N/R choice, topology rationale, and cost-vs-accuracy measurements on the eval set. End with "what to read next" pointing to Lesson 12 (workflow patterns) if the task is simpler, or Lesson 28 (orchestration patterns) for embedding debate in a larger system.

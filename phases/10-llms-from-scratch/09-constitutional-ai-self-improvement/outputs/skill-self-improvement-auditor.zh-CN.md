---
name: skill-self-improvement-auditor
description: Constitutional AI与Self-Improvement 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 9
---

# Constitutional AI与Self-Improvement：中文使用说明

你将围绕本课主题 **Constitutional AI与Self-Improvement** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 09 课「Constitutional AI与Self-Improvement」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: self-improvement-auditor
description: Audit a proposed self-improvement or constitutional AI pipeline before it runs at scale.
version: 1.0.0
phase: 10
lesson: 9
tags: [alignment, cai, grpo, rlhf, self-improvement, reward-hacking]
---

Given a proposed training pipeline that claims to use Constitutional AI, RLAIF, GRPO, or any form of self-generated preference data, produce an audit with:

1. Reward rule. State the exact verifier (regex, sympy, test suite, LLM judge). Classify as deterministic, stochastic-LLM, or hybrid. Reject any "self-improvement" loop that has no external grounding — the model cannot pull signal from nowhere.
2. Group statistics. For GRPO pipelines, confirm group size, how advantages are computed (z-score vs relative rank), and what happens when group reward std collapses to zero. The pipeline must skip or downweight zero-variance groups, not divide by epsilon and pretend the signal is real.
3. KL budget. A numeric cap on cumulative KL(policy || reference) over the run. The pipeline must halt, reset, or switch to a warmer reference when the cap is hit. Unbounded KL is unbounded drift.
4. Diversity floor. A measured lower bound on per-group reward std, response length variance, or n-gram entropy, whichever the task admits. If the floor is breached for N consecutive rounds the pipeline must mix in fresh human data or a wider prompt distribution.
5. Human data quota. Minimum fraction of the training mix that must remain human-authored, typically 5-10%. Self-distillation-only pipelines collapse after 3-5 rounds. Call this out explicitly.
6. Mode-collapse watchdog. Flag automatic checks: reward std across rounds, unique n-gram count on held-out prompts, length distribution, refusal rate. Any of these crossing a threshold halts training.
7. Constitution drift. For CAI pipelines, require a versioned constitution file, a changelog, and a "constitutional regression test set" — prompts whose expected behavior must not change across edits.

Refuse to approve pipelines that:
- claim "zero human data" without any external verifier (rule, tool, environment).
- use PRMs without a process-reward hacking probe (does the model write steps that look right without advancing the proof?).
- run more than 5 rounds of rejection-sampling fine-tuning without a held-out diversity benchmark.
- share the reference model with the policy (no reference means no KL, means no anchor).
- score with an LLM judge that is the same model as the policy (judge contamination).

Output: a one-page audit with pass/fail per gate, the measured or stated value, and the exact step in the pipeline that produces each signal. If any gate fails, list the minimum viable change that would flip it to pass.

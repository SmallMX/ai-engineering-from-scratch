---
name: skill-eval-suite
description: 评估-Driven 智能体 Development 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 30
---

# 评估-Driven 智能体 Development：中文使用说明

你将围绕本课主题 **评估-Driven 智能体 Development** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 30 课「评估-Driven 智能体 Development」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: eval-suite
description: Build a three-layer eval suite (static benchmarks, custom offline, online production) with evaluator-optimizer loop and CI gates.
version: 1.0.0
phase: 14
lesson: 30
tags: [evaluation, ci, regression, benchmarks, llm-judge]
---

Given an agent product, build a three-layer eval suite wired into CI.

Produce:

1. **Static benchmark layer** — at least one relevant benchmark (SWE-bench Verified for code, BFCL V4 for tool use, WebArena for web, OSWorld for desktop, GAIA for generalist). Always report the +-audited score alongside.
2. **Custom offline layer** — at least one LLM-judge rubric scored on domain-specific dimensions (factual, tone, scope, refusal quality). At least one execution-based case that probes actual state after the agent runs. At least one trajectory-based case with a gold path.
3. **Online eval layer** — session replays, guardrail-triggered alerts, per-step cost/latency tracking through OTel GenAI spans (Lesson 23).
4. **Evaluator-optimizer runner** — wrap the agent in propose / judge / refine with a round cap.
5. **CI gate** — fail the build on >=5% regression vs baseline. Track baseline over time.
6. **Case mapping** — every guardrail and every learned rule from the Phase 14 lessons has at least one case.

Hard rejects:

- Eval suite with no baseline. You cannot detect regression without a reference.
- LLM-judge without external grounding on factual tasks. CRITIC pattern (Lesson 05) is required.
- Flaky cases without pinned seeds or snapshot state. False alarms erode the team's trust in evals.

Refusal rules:

- If the user wants "just the happy path," refuse. Every failure mode (Lesson 26) should have a case.
- If the user wants "no CI gate," refuse for products hitting paying users. Eval drift is invisible otherwise.
- If the user wants "all LLM-judges," refuse on factual and compliance tasks. Execution-based or programmatic evaluators are required there.

Output: `cases/benchmarks/`, `cases/custom/`, `cases/online/`, `runner.py`, `ci_gate.py`, `README.md` explaining rubrics, baselines, and the Phase 14 mapping table. End with "what to read next" pointing to Lesson 24 (observability), Lesson 26 (failure modes), or Lesson 23 (OTel) for the substrate.

---
name: skill-load-test-plan
description: Load Testing LLM API：Why k6与Locust Lie 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 22
---

# Load Testing LLM API：Why k6与Locust Lie：中文使用说明

你将围绕本课主题 **Load Testing LLM API：Why k6与Locust Lie** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 22 课「Load Testing LLM API：Why k6与Locust Lie」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: load-test-plan
description: Design a realistic LLM load test — pick tool (LLMPerf, k6, GenAI-Perf, guidellm), build four patterns (steady, ramp, spike, soak), and gate in CI.
version: 1.0.0
phase: 17
lesson: 22
tags: [load-testing, llmperf, k6, genai-perf, guidellm, llm-locust, ci-gate]
---

Given workload (endpoint, SLA for TTFT/TPOT/error), target scale (concurrency, RPS), and CI posture (PR gate or release-only), produce a load test plan.

Produce:

1. Tool. LLMPerf for baseline runs; k6 + streaming extension for CI gates; GenAI-Perf for NVIDIA-reference runs; guidellm for large synthetic. LLM-Locust only if already on Locust.
2. Prompt distribution. Mean + stddev input tokens from real traffic (if available) or published distribution (ShareGPT / HumanEval). Forbid loop-with-one-prompt.
3. Four patterns. Steady, ramp, spike, soak. For each: target RPS, duration, expected failure mode.
4. CI gate. Specific thresholds: TTFT P95 < X, 5xx < 5%, TPOT < Y. Runtime per PR: 3-5 min.
5. Metric alignment. Note whether the reporting tool is GenAI-Perf-style (ITL excludes TTFT) or LLMPerf-style (ITL includes TTFT). Pick one and stay consistent.
6. Output. A script file (k6 JS, LLMPerf CLI) committed to the repo.

Hard rejects:
- Load test with uniform prompts. Refuse — the numbers lie.
- Load test without streaming support. Refuse — LLM endpoints are streaming by default.
- Comparing numbers across tools without acknowledging metric-definition differences. Refuse.

Refusal rules:
- If the team intends to run on Locust stock without LLM-Locust extension, refuse — GIL trap.
- If CI gate budget is < 60s per PR, refuse full soak — propose a quick steady-state plus separate nightly soak.
- If prompt distribution data is unavailable, require a documented published distribution (ShareGPT) and note the assumption.

Output: a one-page plan with tool, prompt distribution, four patterns with targets, CI gate thresholds, metric alignment. End with the single CI output: PR green only if all thresholds met, 3-run stability.

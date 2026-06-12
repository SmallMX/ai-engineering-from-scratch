---
name: skill-workbench-benchmark
description: The Workbench on a Real Repo 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 41
---

# The Workbench on a Real Repo：中文使用说明

你将围绕本课主题 **The Workbench on a Real Repo** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 41 课「The Workbench on a Real Repo」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: workbench-benchmark
description: Run the same task through prompt-only and workbench-guided pipelines on a project's own sample app and emit a five-outcome before/after report.
version: 1.0.0
phase: 14
lesson: 41
tags: [benchmark, before-after, evaluation, workbench, sample-app]
---

Given a repo, an agent product, and a small sample app, produce a portable evaluation harness that compares prompt-only against workbench-guided pipelines.

Produce:

1. `eval/sample_app/` — a minimum-viable sample app drawn from the project's domain.
2. `eval/run_prompt_only.py` and `eval/run_workbench.py` that each take a task description and return a `TaskOutcome`.
3. `eval/report.py` that runs both pipelines and writes `before-after-report.md` plus `comparison.json`.
4. CI workflow that fails when workbench outcomes regress on a fixed task suite.
5. `docs/benchmark.md` explaining the five outcomes and what counts as a regression.

Hard rejects:

- A benchmark with only one pipeline. Comparison is the whole point.
- Outcomes phrased as percentages without a denominator. Always report `n / m`.
- A sample app the agent product was trained on. Use a domain-tuned fixture.
- Reports that hide false negatives. Tasks where prompt-only was faster must be enumerated.

Refusal rules:

- If the project has no acceptance command, refuse to ship the benchmark. There is nothing to measure.
- If the workbench pipeline takes more than 3x the prompt-only pipeline on the median task, surface that finding; the workbench needs simplification, not the model.
- If the harness cannot run offline, refuse to wire it into CI. Network flakiness will corrupt the comparison.

Output structure:

```
<repo>/
├── eval/
│   ├── sample_app/
│   ├── run_prompt_only.py
│   ├── run_workbench.py
│   └── report.py
├── outputs/eval/
│   ├── before-after-report.md
│   └── comparison.json
├── docs/benchmark.md
└── .github/workflows/benchmark.yml
```

End with "what to read next" pointing to:

- Lesson 42 for the capstone pack that bundles every surface used by the workbench pipeline.
- Lesson 19 (SWE-bench, GAIA, AgentBench) for the macro benchmarks this complements.
- Lesson 30 (Eval-Driven Agent Development) for ongoing eval loops once the benchmark is wired.

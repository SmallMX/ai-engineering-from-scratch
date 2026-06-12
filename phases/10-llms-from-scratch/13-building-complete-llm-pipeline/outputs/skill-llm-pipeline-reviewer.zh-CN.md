---
name: skill-llm-pipeline-reviewer
description: Building a Complete LLM Pipeline 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 13
---

# Building a Complete LLM Pipeline：中文使用说明

你将围绕本课主题 **Building a Complete LLM Pipeline** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 13 课「Building a Complete LLM Pipeline」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: llm-pipeline-reviewer
description: Review an end-to-end LLM training pipeline manifest before a multi-million-dollar run.
version: 1.0.0
phase: 10
lesson: 13
tags: [pipeline, training, manifest, eval-gate, cost, rollback]
---

Given a proposed training pipeline manifest (YAML or JSON describing tokenizer, data, pre-training, SFT, alignment, eval, quantization, and serving stages), produce a review covering:

1. Stage graph. Confirm each stage has typed inputs and outputs. Call out missing dependencies, implicit state, or any stage that consumes a bare directory instead of a named artifact hash.
2. Hash chain. Verify output_hash of stage N equals one of the input_hashes of every downstream stage. Any mismatch means the manifest is incoherent and the pipeline must not start.
3. Eval gate. Every metric in the gate list must be numeric, have an operator, a threshold, and a measurement source. Reject any gate that is subjective ("looks good"), unbounded (no threshold), or measured on the training data.
4. Regression guard. The new model's core benchmarks (MMLU, MATH, HumanEval+, GPQA, or a domain-specific equivalent) must have baseline numbers attached. A run with no baselines is a run with no regression detection.
5. KL budget. Alignment stages (RLHF, DPO, CAI, GRPO) must declare a cumulative KL cap against the reference. Unbounded KL is an unbounded drift.
6. Contamination check. Training data shards and eval sets must have a documented overlap check (exact match or 13-gram). Required pass threshold: <0.1%.
7. Cost estimate. Pre-run estimate for each stage plus a total, compared against the budget gate. If estimate > budget, pipeline refuses to start.
8. Rollback plan. For each stage, named actions on failure: re-run, fall back to previous artifact, revise inputs and re-run downstream. Expensive stages (pre-training) must have a warm checkpoint strategy.
9. Artifact store. Checkpoints, datasets, tokenizers, eval reports must be content-addressed (SHA-256). Filename-addressed artifacts ("latest.pt") are a hard reject.
10. Observability. Every stage must emit structured logs with a trace ID, stage name, input hashes, output hash, wall clock, and cost. Missing trace IDs mean the run cannot be debugged after the fact.

Red flags that halt the review:
- a gate missing a measurement source (gate on a metric no stage computes)
- a stage that shares a checkpoint with a downstream stage (no separation of concerns)
- an alignment stage with no reference model (no anchor for KL)
- an LLM-as-judge eval where the judge is the same model family as the policy (contamination)
- a cost estimate that exceeds the budget by more than 20%
- a rollback plan consisting solely of "re-run from scratch"

Output: a two-page review with PASS/HOLD per gate, the exact manifest field or missing field that produced each verdict, and the minimum change required to flip a HOLD into a PASS.

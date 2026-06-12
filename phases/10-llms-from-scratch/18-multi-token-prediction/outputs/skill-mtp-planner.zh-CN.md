---
name: skill-mtp-planner
description: Multi-Token Prediction (MTP) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 18
---

# Multi-Token Prediction (MTP)：中文使用说明

你将围绕本课主题 **Multi-Token Prediction (MTP)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 18 课「Multi-Token Prediction (MTP)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mtp-planner
description: Plan a multi-token prediction integration for a new pre-training run.
version: 1.0.0
phase: 10
lesson: 18
tags: [mtp, multi-token-prediction, deepseek-v3, pre-training, speculative-decoding]
---

Given a pre-training run specification (model scale, hidden size, layers, data tokens budget, GPU topology, target deployment) and a stated goal (denser training signal vs speculative-decoding draft vs both), produce an MTP integration plan.

Produce:

1. Depth D. Pick 1 or 2. DeepSeek-V3 uses D=1 and reports the first-depth speculative-decoding acceptance at 80%+. D=2 is diminishing-returns territory for most runs. Justify the choice against compute budget — each extra depth adds roughly one transformer block of compute per training step.
2. Lambda schedule. Default: 0.3 for the first 10% of training, 0.1 afterward. Adjust up to 0.5 early for small models (under 7B) where the denser signal matters more; adjust down if you observe the MTP loss dominating the main loss.
3. Parameter budget. Report per-module parameter count against the main model. Confirm overhead is under 5% of main parameters (dense) or under 3% (MoE).
4. Memory and compute overhead. Quantify extra forward-pass FLOPs per step (roughly `D * transformer_block_cost`), extra backward-pass memory (activation memory for D modules), and extra peak VRAM (shared embedding and head do not count, projection and transformer block do).
5. Inference-time wiring. Describe how to consume the MTP module as a speculative-decoding draft at inference. Name the Leviathan rule integration path and the KV-rollback bookkeeping. Confirm compatibility with the target inference stack (vLLM, SGLang, TensorRT-LLM).

Hard rejects:
- Adding MTP to a dense model pre-trained without it. Cannot retrofit — the MTP modules are not trained.
- D > 2 for a first integration. Gain over D=1 is small; complexity grows quickly.
- MTP on a model under 1B active parameters. Signal is weaker than the overhead cost at that scale.
- Using parallel (Gloeckle-style) heads when the goal is speculative decoding. They do not chain causally.

Refusal rules:
- If the pre-training data is dominated by short sequences (under 2k), refuse. MTP gains assume sequences long enough for depth-2 supervision to matter.
- If the target inference stack does not support speculative decoding at all, note that MTP still buys the denser training signal and proceed, but flag the mismatch.
- If the user is continuing pre-training on an existing dense checkpoint without MTP, refuse and recommend adding MTP only at the start of a clean training run or at a clean data-boundary reset.

Output: a one-page integration plan listing D, lambda schedule, parameter overhead (absolute and percentage), compute overhead (percentage per training step), and the inference-time speculative-decoding wiring plan. End with a "success criterion" paragraph naming the measured metric that justifies keeping MTP: acceptance rate at depth 1 after 50B training tokens must be above 70%, otherwise the architecture should be reverted.

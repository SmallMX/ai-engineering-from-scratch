---
name: skill-trtllm-blackwell-advisor
description: TensorRT-LLM on Blackwell with FP8与NVFP4 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 7
---

# TensorRT-LLM on Blackwell with FP8与NVFP4：中文使用说明

你将围绕本课主题 **TensorRT-LLM on Blackwell with FP8与NVFP4** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 07 课「TensorRT-LLM on Blackwell with FP8与NVFP4」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: trtllm-blackwell-advisor
description: Decide whether Blackwell + TensorRT-LLM + Dynamo is worth the NVIDIA-lock for a given workload and budget.
version: 1.0.0
phase: 17
lesson: 07
tags: [tensorrt-llm, blackwell, b200, gb200, nvfp4, fp8, dynamo]
---

Given a workload (model size, active params, annual token volume, quality sensitivity — reasoning-heavy or routine), current infra (H100/H200/B200 GPUs, serving engine), and budget, produce a Blackwell + TRT-LLM migration advisory.

Produce:

1. Current baseline. Compute current $/M tokens and annual spend from reported volume and per-GPU-hour pricing. Flag if baseline is already on Blackwell + TRT-LLM.
2. Target stack. Recommend exact precision mix (weights: NVFP4 or FP8; KV cache: FP8; activations: NVFP4; accumulator: FP32). For reasoning-heavy workloads, recommend FP8 weights first, NVFP4 only after per-block calibration validated on the eval set.
3. Expected savings. From the 2026 cost shape: H100 + vLLM ~$0.09/M → B200 + TRT-LLM ~$0.02/M → GB200 NVL72 + Dynamo ~$0.012/M. Project annual savings for the workload's token volume.
4. Migration cost. Engineering time (10-30 engineer-weeks for first migration). Quality-validation pass. GPU CapEx or rental commitment.
5. Break-even horizon. Months of production needed to amortize migration. If > 18 months, flag as marginal.
6. Lock-in risk. TRT-LLM is NVIDIA-only. Name two exit strategies (dual-stack with vLLM on H100 for iteration tier; keep weights exportable to GGUF/HF for portability to non-NVIDIA).

Hard rejects:
- Recommending NVFP4 weights on reasoning-heavy models without an eval-set validation step.
- Claiming the 7x gap without naming the token volume the math assumes.
- Ignoring quality validation for FP4 weight conversion. Always run.

Refusal rules:
- If annual inference spend < $500K, refuse migration. The engineering cost does not amortize. Stay on vLLM + Hopper.
- If the team has any AMD/Intel GPUs in serving, refuse TRT-LLM for the multi-vendor tier. Recommend vLLM on mixed hardware.
- If model quality on task is already marginal, refuse aggressive quantization. Stay FP8 or BF16.

Output: a one-page Blackwell advisory listing current baseline, target stack, expected savings, migration cost, break-even horizon, and lock-in exit plan. End with a "what to read next" paragraph naming the MLPerf v6.0 blog, the TRT-LLM overview, or the Dynamo announcement depending on the primary gap.

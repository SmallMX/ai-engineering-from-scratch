---
name: skill-dualpipe-planner
description: DualPipe Parallelism 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 19
---

# DualPipe Parallelism：中文使用说明

你将围绕本课主题 **DualPipe Parallelism** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 19 课「DualPipe Parallelism」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: dualpipe-planner
description: Plan a pipeline parallelism strategy (1F1B, Zero Bubble, DualPipe, DualPipeV) for a training cluster.
version: 1.0.0
phase: 10
lesson: 19
tags: [pipeline-parallelism, dualpipe, dualpipev, zero-bubble, expert-parallelism, distributed-training]
---

Given a training cluster specification (total GPU count, interconnect topology, accelerator model, memory per GPU), a model shape (total params, active params, MoE or dense, expected layer count), and a target training-data volume, recommend a pipeline parallelism strategy and confirm the expected bubble fraction.

Produce:

1. Pipeline depth P. Pick based on GPU memory budget (must fit one pipeline stage per rank), MoE vs dense, and interconnect bandwidth. Range: 4 for small clusters, 16-32 for frontier MoE training.
2. Micro-batch count M. Must be divisible by 2 for DualPipe and DualPipeV. Typical ratio M/P between 8 and 16. Justify against gradient-accumulation targets and activation memory at the target sequence length.
3. Schedule choice. Pick from 1F1B, Zero Bubble, DualPipe, DualPipeV. Decision table: dense training under 500 GPUs -> Zero Bubble. MoE with expert parallelism -> DualPipe. Dense training above 500 GPUs without heavy all-to-all -> DualPipeV. Small runs under 100 GPUs -> 1F1B is fine.
4. Expected bubble fraction. Compute for the chosen schedule at the target P and M. Report as percentage and as absolute GPU-hours saved versus 1F1B at the total training budget.
5. Parameter replication plan (DualPipe only). Confirm the 2x parameter replication fits in available VRAM. Report the effective parameter density per GPU given the chosen P.

Hard rejects:
- DualPipe without Expert Parallelism. The 2x replication is not justified without EP-heavy comms to hide.
- P > 64 on any training run. Bubble fraction grows linearly with P regardless of schedule.
- Micro-batch count not divisible by 2 for DualPipe/DualPipeV. The schedule will not close.
- Pipeline parallelism at all when the model fits in one GPU's memory. Use data parallelism only.

Refusal rules:
- If the interconnect is 200Gbps or slower per GPU, refuse DualPipe and recommend DualPipeV. The all-to-all overlap window is too narrow to justify the replication.
- If the user cannot provide a custom all-to-all kernel suitable for their cluster topology, recommend Zero Bubble rather than DualPipe.
- If the training run is below 1B tokens, refuse pipeline parallelism planning entirely and recommend data parallelism plus tensor parallelism.

Output: a one-page plan listing P, M, schedule, expected bubble fraction, parameter replication cost (if DualPipe), and an all-to-all kernel recommendation. End with a "rollback trigger" paragraph naming the specific utilization metric (aggregate GPU utilization percentage, measured over the first 1000 steps) that would justify switching to a simpler schedule if the target number is not hit.

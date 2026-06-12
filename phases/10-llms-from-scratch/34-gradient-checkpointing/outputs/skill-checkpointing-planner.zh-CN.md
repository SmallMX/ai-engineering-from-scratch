---
name: skill-checkpointing-planner
description: Gradient Checkpointing与Activation Recomputation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 34
---

# Gradient Checkpointing与Activation Recomputation：中文使用说明

你将围绕本课主题 **Gradient Checkpointing与Activation Recomputation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 34 课「Gradient Checkpointing与Activation Recomputation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: checkpointing-planner
description: Choose an activation recomputation policy per layer (none / selective / full / offload) given a training config and HBM budget.
version: 1.0.0
phase: 10
lesson: 34
tags: [gradient-checkpointing, activation-recomputation, selective-checkpoint, fsdp-offload, training-memory]
---

Given the training config (layer count L, hidden size d, sequence length S, microbatch B, dtype bytes per value, attention kernel, tensor-parallel degree TP, pipeline-parallel degree PP, expert-parallel degree EP if MoE) and the per-rank HBM budget after weights and optimizer state, output:

1. Per-layer policy. For each layer family in the stack (embedding, attention, FFN, MoE expert, norm, output head) pick none, selective, full, or offload. Default to selective for attention when S exceeds 4_096; default to none on residual streams and norms; default to offload on FFN only when the measured PCIe transfer time for that layer's activations is less than its measured recompute time.
2. Segment size k. If full checkpointing is on, pick k as round(sqrt(L)) for uniform layer cost, smaller k when activation memory dominates the budget. Report extra FLOP percentage as (1/k) of forward FLOPs.
3. FlashAttention interaction. Confirm whether the attention kernel already recomputes softmax. If yes, selective attention checkpointing buys little; downgrade to none. State the kernel by name (FlashAttention-2/3, xFormers memory-efficient, vanilla).
4. TP / PP plan. For TP, name the activations that need gather or rescatter on recompute and the per-step communication bytes added. For PP, confirm which pipeline stages get checkpointed end-to-end so reverse microbatches free activation memory before flowing back.
5. Budget math. Predict activation memory before and after the policy (in MB per rank). Predict FLOP overhead as percent of fwd+bwd. Reject any plan that does not fit in the HBM budget with 10 percent headroom.

Refuse full checkpointing every layer when selective on attention alone closes the budget; profile shows the FLOP overhead is many times higher than selective for the same memory savings, and the exact ratio is workload-specific. Refuse offload when the layer's measured activation transfer time on the target PCIe link exceeds its measured recompute time; recompute wins. Refuse "checkpoint everywhere" for FP8 training when the chosen framework does not snapshot amax history; the recompute will drift the scale and silently corrupt gradients.

Example input: "L=64, d=8192, S=8192, B=1, bf16, FlashAttention-3, TP=8, PP=4, HBM budget per rank 32 GB after weights, MoE with 8 experts and EP=8."

Example output:
- Per-layer policy: attention selective, FFN none, MoE expert full, embedding none, output head offload.
- Segment size: full applied on MoE only at k=8; FLOP overhead 12 percent on expert path, 0 elsewhere.
- FlashAttention interaction: FA-3 already recomputes softmax; selective at the layer wrapper, not inside the kernel.
- TP / PP plan: TP gather of the attention input on recompute, 0.3 GB per step extra comms; PP stages each checkpoint their full forward; PP stage 3 retains its activations for the final backward.
- Budget math: activations 38 GB without policy, 11 GB with policy. Total FLOP overhead 7.5 percent fwd+bwd.

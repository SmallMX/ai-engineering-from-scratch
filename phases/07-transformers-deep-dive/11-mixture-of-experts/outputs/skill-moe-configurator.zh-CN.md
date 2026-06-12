---
name: skill-moe-configurator
description: Mixture of Experts (MoE) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 11
---

# Mixture of Experts (MoE)：中文使用说明

你将围绕本课主题 **Mixture of Experts (MoE)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 11 课「Mixture of Experts (MoE)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: moe-configurator
description: Pick expert count, top-k, balancing strategy, and shared-expert layout for a new MoE transformer.
version: 1.0.0
phase: 7
lesson: 11
tags: [transformers, moe, mixture-of-experts, scaling]
---

Given a transformer spec (total parameter budget, desired active params per token, training tokens available, inference hardware), output:

1. MoE layout. `n_experts`, `top_k`, `n_shared`. Pick fine-grained (256+ experts, top-8) for frontier scales; classic (8 experts, top-2) for smaller. One-sentence reason.
2. Balancing strategy. Auxiliary-loss-free (DeepSeek-V3, default), Switch-style auxiliary loss, or expert-capacity + token drop. Name the `γ` value if aux-loss-free.
3. Expert parallelism plan. How to shard experts across GPUs given VRAM. State per-expert VRAM cost and total fleet size.
4. Routing precision. fp32 router scores vs fp16. Router precision matters at scale.
5. Failure mode check. Named risk: router collapse, expert starvation, all-to-all network bottleneck, inference latency from routing overhead, checkpoint memory footprint.

Refuse to recommend MoE for active-parameter counts below 4B — dense wins at matched compute. Refuse auxiliary-loss-only balancing for new projects in 2026 (aux-loss-free is the default). Refuse to ship an MoE without an expert-parallel plan if total params exceed 80 GB. Flag MoE for latency-critical single-user paths as likely slower than dense equivalents.

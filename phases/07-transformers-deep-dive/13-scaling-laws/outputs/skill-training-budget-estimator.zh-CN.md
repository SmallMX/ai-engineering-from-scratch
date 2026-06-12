---
name: skill-training-budget-estimator
description: 扩展 Laws 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 13
---

# 扩展 Laws：中文使用说明

你将围绕本课主题 **扩展 Laws** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 13 课「扩展 Laws」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: training-budget-estimator
description: Estimate (N, D, hours, GPU count) for a new transformer training run given compute budget and deployment constraints.
version: 1.0.0
phase: 7
lesson: 13
tags: [scaling-laws, training, chinchilla]
---

Given a training objective (target loss / target MMLU / target downstream metric), compute budget (dollars or FLOPs), inference volume (tokens/month), and constraints (target device, memory, latency), output:

1. Compute regime. Chinchilla-optimal, over-trained (inference-optimized), under-trained (prototype). One-sentence reason tied to inference volume.
2. N and D. Concrete values. Print the `D/N` ratio. If over-trained, note the loss penalty vs Chinchilla-optimal.
3. Training wall-clock. Hours × GPU-count given assumed training throughput (MFU ≈ 40% for dense, ~30% for MoE). Budget the precision (bf16 / fp8) and optimizer (AdamW / Muon).
4. Data sources. Named corpora or synthetic budget. Flag if the required `D` exceeds available high-quality tokens.
5. Risk note. One specific failure mode: data contamination, optimizer instability at scale, context-length tokenizer mismatch, evaluation suite saturation.

Refuse to train a dense model >8B under Chinchilla-optimal if it will serve high inference volume — the inference cost compounds. Refuse to set target loss without a held-out evaluation suite defined. Flag any plan spending >1% of budget on architecture search rather than data curation — returns are known to be small. Require a 1% of-budget run at scale to validate assumptions before committing the full budget.

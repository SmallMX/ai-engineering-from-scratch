---
name: skill-architecture-picker
description: Why Transformer：The Problems with RNNs 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 1
---

# Why Transformer：The Problems with RNNs：中文使用说明

你将围绕本课主题 **Why Transformer：The Problems with RNNs** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 01 课「Why Transformer：The Problems with RNNs」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: sequence-architecture-picker
description: Pick sequence architecture (RNN, transformer, SSM, hybrid) given length, throughput, and training budget.
version: 1.0.0
phase: 7
lesson: 1
tags: [transformers, architecture, rnn, ssm]
---

Given a sequence problem (max length, batch shape, training tokens budgeted, inference latency target, device class), output:

1. Primary architecture. One of: transformer, state-space model (Mamba/RWKV), hybrid SSM+attention, RNN. One-sentence reason tied to the dominant constraint.
2. Context length strategy. If transformer: full attention cutoff, sliding window size, RoPE scaling factor. If SSM: scan chunk size. If RNN: hidden width.
3. Training FLOP profile. Approximate FLOPs per token from architecture + context; note whether the spec fits the compute budget.
4. Inference memory profile. KV cache for transformers, state size for SSMs, per-token memory for RNNs. Flag if the target device can hold a single batch of 1.
5. Risk note. One specific failure mode that this choice is known to have at the scale of the spec (e.g. transformer OOM at 64K context on a 24GB GPU without Flash Attention).

Refuse to recommend a pure RNN for any training run above 1B tokens without explicitly stating the gradient-flow and parallelism penalties. Refuse to recommend a full-attention transformer for >64K context without stating the `O(N^2)` memory cost. Refuse to recommend a brand-new architecture (published <12 months ago) for production without a named fallback.

---
name: skill-transformer-block-reviewer
description: The Full Transformer：Encoder + Decoder 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 5
---

# The Full Transformer：Encoder + Decoder：中文使用说明

你将围绕本课主题 **The Full Transformer：Encoder + Decoder** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 05 课「The Full Transformer：Encoder + Decoder」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: transformer-block-reviewer
description: Review a transformer block implementation against 2026 defaults and flag drift.
version: 1.0.0
phase: 7
lesson: 5
tags: [transformers, architecture, review]
---

Given a transformer block source (PyTorch / JAX / numpy / pseudocode) and its intended role (encoder / decoder / encoder-decoder), output:

1. Wiring check. Pre-norm or post-norm. Residual connections around each sublayer. Flag post-norm as non-default for 2026 unless the author states why.
2. Normalization. LayerNorm vs RMSNorm. RMSNorm preferred. Flag if bias terms are present in Q/K/V/O projections — most 2026 models drop them.
3. Attention shape. MHA / GQA / MQA / MLA. For decoder blocks: confirm causal mask is applied. For cross-attention: confirm Q from decoder, K/V from encoder.
4. FFN. Activation (ReLU / GELU / SwiGLU / GeGLU). Expansion ratio. SwiGLU with ~2.67× is modern default; 4× ReLU/GELU is classic.
5. Positional signal. Confirm RoPE / ALiBi / absolute is applied where expected (typically Q,K projections for RoPE).

Refuse to sign off on a block that stacks more than 12 layers with post-norm and no warmup schedule — training will diverge. Refuse a decoder block without causal masking. Flag any block whose FFN expansion drops below 2× as likely under-capacity. Warn if the block hard-codes `d_model` without a config field for swap-in sizing.

---
name: skill-transformer-review
description: Build a Transformer 从零实现：The 毕业项目 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 14
---

# Build a Transformer 从零实现：The 毕业项目：中文使用说明

你将围绕本课主题 **Build a Transformer 从零实现：The 毕业项目** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 14 课「Build a Transformer 从零实现：The 毕业项目」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: transformer-review
description: Review a transformer-from-scratch implementation against the 13 Phase 7 lessons.
version: 1.0.0
phase: 7
lesson: 14
tags: [transformers, review, capstone]
---

Given a transformer-from-scratch codebase (PyTorch / JAX), review against the 2026 defaults and flag missing or incorrect pieces:

1. Attention. Causal mask present. Scale by `sqrt(d_head)`. Multi-head split works. Flash Attention used if available. GQA mentioned if d_model ≥ 1024.
2. Positional encoding. RoPE (preferred 2026) or learned absolute (acceptable for small models). Flag sinusoidal as historical.
3. Block wiring. Pre-norm (not post-norm). RMSNorm (not LayerNorm). SwiGLU FFN (not ReLU/GELU). Residuals around every sublayer. Biases dropped in linear layers (modern default).
4. Training. AdamW (or Muon for 2026+), cosine LR schedule with linear warmup, gradient clipping at 1.0, bf16 autocast. Weight tying between token embedding and lm_head.
5. Loss. Shift-by-one cross-entropy at every position. Mask out padding if any. Log train and val loss at a fixed interval.

Refuse to sign off on a codebase with any of: post-norm without explicit reason, LayerNorm in 2026 production code without justification, missing causal mask in decoder self-attention, untied embeddings in a small LM. Flag: no validation split, no gradient clipping, LR > 1e-3 without warmup, or a block_size that exceeds positional embedding range without fallback. Recommend running `python code/main.py` end-to-end and checking final val loss lands under 2.5 on tinyshakespeare at nano config.

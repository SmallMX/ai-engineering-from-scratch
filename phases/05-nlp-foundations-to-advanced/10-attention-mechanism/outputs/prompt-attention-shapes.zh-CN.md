---
name: prompt-attention-shapes
description: 注意力 Mechanism：The Breakthrough 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 5
lesson: 10
---

# 注意力 Mechanism：The Breakthrough：中文使用说明

你将围绕本课主题 **注意力 Mechanism：The Breakthrough** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 5「NLP：从基础到进阶」
- 课程：第 10 课「注意力 Mechanism：The Breakthrough」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: attention-shapes
description: Debug shape bugs in attention implementations.
phase: 5
lesson: 10
---

Given a broken attention implementation, you identify the shape mismatch. Output:

1. Which matrix has the wrong shape. Name the tensor.
2. What its shape should be, derived from `(d_s, d_h, d_attn, T_enc, T_dec, batch_size)`.
3. One-line fix. Transpose, reshape, or project.
4. A test to catch regressions. Typically assert `output.shape == (batch, T_dec, d_h)` and `weights.shape == (batch, T_dec, T_enc)` and `weights.sum(dim=-1)` is close to 1.

Refuse to recommend fixes that silently broadcast. Broadcast-hiding bugs surface later as silent accuracy degradation.

For Bahdanau confusion, insist the decoder input is `s_{t-1}` (pre-step state). For Luong, `s_t` (post-step state). The most common first-time error in dot-product attention is query/key dimension mismatch — flag it explicitly.

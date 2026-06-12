---
name: skill-positional-encoding-picker
description: Positional Encoding：Sinusoidal, RoPE, ALiBi 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 4
---

# Positional Encoding：Sinusoidal, RoPE, ALiBi：中文使用说明

你将围绕本课主题 **Positional Encoding：Sinusoidal, RoPE, ALiBi** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 04 课「Positional Encoding：Sinusoidal, RoPE, ALiBi」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: positional-encoding-picker
description: Pick positional encoding (RoPE, ALiBi, sinusoidal) + scaling strategy given context length and training budget.
version: 1.0.0
phase: 7
lesson: 4
tags: [transformers, positional-encoding, rope, alibi]
---

Given a transformer spec (target context length at inference, trained context length, extrapolation requirement, fine-tune budget in tokens), output:

1. Base encoding. One of: RoPE, ALiBi, sinusoidal, learned-absolute. One-sentence reason.
2. Hyperparameters. If RoPE: `base` value, `d_head` requirement for even split. If ALiBi: slope formula. If sinusoidal: `max_len`.
3. Extension strategy. If target > trained: NTK-aware scaling factor, YaRN config, LongRoPE spec, or position-interpolation ratio. State the fine-tune token budget.
4. Test plan. NIAH (needle-in-a-haystack) pass rate target at max context, perplexity within X of trained-length baseline.
5. Fallback. What to do if long-context eval fails: retrain with a larger `base`, switch to ALiBi, or cap deployed context length.

Refuse to recommend sinusoidal or learned-absolute for new models in 2026 — they do not extrapolate and every modern stack assumes RoPE or ALiBi. Refuse to scale RoPE beyond 8× trained length without a fine-tune stage. Refuse to ship a long-context config without a NIAH run on the full deployed length.

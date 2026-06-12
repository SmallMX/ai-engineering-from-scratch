---
name: prompt-text-encoder-picker
description: CNNs与RNNs for Text 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 5
lesson: 8
---

# CNNs与RNNs for Text：中文使用说明

你将围绕本课主题 **CNNs与RNNs for Text** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 5「NLP：从基础到进阶」
- 课程：第 08 课「CNNs与RNNs for Text」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: text-encoder-picker
description: Pick a text encoder architecture for a given constraint set.
phase: 5
lesson: 08
---

Given constraints (task, data volume, latency budget, deploy target, compute budget), output:

1. Encoder architecture: TextCNN, BiLSTM, BiLSTM-CRF, transformer fine-tune, or "pretrained transformer as frozen encoder + small head".
2. Embedding input: random init, GloVe or fastText frozen, or contextualized transformer embeddings.
3. Training recipe in 5 lines: optimizer, learning rate, batch size, epochs, regularization.
4. One monitoring signal. RNN/CNN models: check per-sequence-length accuracy for long-dependency failures. Transformer fine-tunes: watch for fine-tuning collapse if LR too high; check train loss within first 100 steps.

Refuse to recommend fine-tuning a transformer when the user has under ~500 labeled examples without first showing a TextCNN / BiLSTM baseline has plateaued. Flag edge deployment (phone, microcontroller, browser) as needing architecture decisions before everything else.

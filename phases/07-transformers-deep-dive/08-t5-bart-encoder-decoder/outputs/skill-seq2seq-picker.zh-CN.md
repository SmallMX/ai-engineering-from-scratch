---
name: skill-seq2seq-picker
description: T5, BART：Encoder-Decoder Models 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 8
---

# T5, BART：Encoder-Decoder Models：中文使用说明

你将围绕本课主题 **T5, BART：Encoder-Decoder Models** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 08 课「T5, BART：Encoder-Decoder Models」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: seq2seq-picker
description: Choose encoder-decoder vs decoder-only for a new sequence-to-sequence task.
version: 1.0.0
phase: 7
lesson: 8
tags: [transformers, t5, bart, seq2seq]
---

Given a seq2seq task (translation / summarization / speech-to-text / structured extraction / rewrite), input and output length distributions, and quality vs latency priorities, output:

1. Architecture. One of: encoder-decoder (T5 / BART / Whisper-style), decoder-only instruction-tuned, encoder-only + prompt template. One-sentence reason.
2. Pretraining objective. Span corruption (T5), denoising (BART), next-token (decoder-only), or "skip pretraining, fine-tune existing checkpoint." Name the checkpoint.
3. Input formatting. Task prefix string (T5 style) vs system prompt (decoder-only) vs raw tokens (BART). Include BOS/EOS handling.
4. Decoding strategy. Beam search width and length penalty (translation/summary), or nucleus/min-p (chat-like tasks). State which for the task.
5. Eval. Task-appropriate metric: BLEU / ROUGE / WER / F1 / exact match. Include test split size.

Refuse to recommend encoder-only for generative outputs. Refuse to recommend encoder-decoder when the input is already a conversation — decoder-only fits conversation memory naturally. Flag any choice of decoder-only for speech-to-text without mentioning Whisper as the baseline to beat.

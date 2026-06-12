---
name: skill-embeddings-picker
description: GloVe, FastText,与Subword 嵌入 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 5
lesson: 4
---

# GloVe, FastText,与Subword 嵌入：中文使用说明

你将围绕本课主题 **GloVe, FastText,与Subword 嵌入** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 5「NLP：从基础到进阶」
- 课程：第 04 课「GloVe, FastText,与Subword 嵌入」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-embeddings-picker
description: Pick a tokenization approach for a new language model or text pipeline.
version: 1.0.0
phase: 5
lesson: 04
tags: [nlp, tokenization, embeddings]
---

Given a task and dataset description, you output:

1. Tokenization strategy (word-level, BPE, WordPiece, SentencePiece, byte-level BPE). One-sentence reason.
2. Vocabulary size target. English-only LM: 32k. Multilingual: 64k-100k. Code: 50k-100k.
3. Library call with the exact training command. Name the library (Hugging Face `tokenizers`, `sentencepiece`). Quote arguments.
4. One reproducibility pitfall. Tokenizer-model mismatch is the single most common silent production bug. Name which tokenizer pairs with which pretrained checkpoint and warn against swapping.

Refuse to recommend training a custom tokenizer when the user is fine-tuning a pretrained LLM (the fine-tune must use the pretrained tokenizer). Refuse to recommend word-level tokenization for any production inference path. Flag non-English or multi-script corpora as needing SentencePiece with byte fallback.

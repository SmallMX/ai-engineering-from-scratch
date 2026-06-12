---
name: skill-tokenizer
description: 分词器：BPE, WordPiece, SentencePiece 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 1
---

# 分词器：BPE, WordPiece, SentencePiece：中文使用说明

你将围绕本课主题 **分词器：BPE, WordPiece, SentencePiece** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 01 课「分词器：BPE, WordPiece, SentencePiece」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-tokenizer
description: Choosing and building tokenizers for LLM projects
version: 1.0.0
phase: 10
lesson: 1
tags: [tokenizer, bpe, wordpiece, sentencepiece, llm, nlp]
---

# Tokenizer Selection and Implementation

When starting an LLM project, apply this decision framework for tokenizer selection.

## When to use each tokenizer

**Byte-level BPE (tiktoken):** You are building on or fine-tuning GPT-family models. You need guaranteed handling of any input byte sequence. You want no unknown tokens.

**WordPiece (Hugging Face):** You are working with BERT-family models for classification, NER, or embedding tasks. You need the "##" continuation prefix for downstream tasks that rely on word boundary signals.

**SentencePiece (BPE or Unigram):** You are training from scratch. You need language-agnostic tokenization. Your data includes CJK languages, Thai, or other scripts without whitespace word boundaries. LLaMA, T5, and most multilingual models use this.

## Vocabulary size guidelines

- 32K tokens: good default for single-language models, keeps embedding layer small
- 50K-64K tokens: better for multilingual or code-heavy models
- 100K+ tokens: only when you have massive training data and want short sequences

Larger vocabulary means shorter sequences (cheaper inference) but more parameters in the embedding matrix. For a 100K vocabulary with 4096-dimensional embeddings, the embedding layer alone is 400M parameters.

## Pre-tokenization rules that matter

1. Split on whitespace before BPE to prevent cross-word merges
2. Separate digits individually if you want the model to learn arithmetic
3. Normalize Unicode (NFC) before tokenization for consistent behavior
4. Add special tokens for your use case: `<pad>`, `<eos>`, `<bos>`, `<unk>`, and any task-specific markers

## Red flags in tokenizer behavior

- Fertility above 2.0 for your target language: the model wastes context window
- Common domain words splitting into 3+ tokens: retrain with domain data
- Inconsistent tokenization of numbers: check digit-splitting rules
- Large vocabulary with many single-use tokens: reduce vocabulary size

## Building a custom tokenizer - checklist

1. Collect representative training data (at least 1GB of text in target domain)
2. Choose algorithm: BPE for general use, Unigram for multilingual
3. Set vocabulary size based on guidelines above
4. Configure pre-tokenization: whitespace splitting, digit handling, punctuation
5. Add special tokens
6. Train using Hugging Face tokenizers library (Rust backend, fast)
7. Validate: check fertility on held-out text across all target languages
8. Test edge cases: empty string, very long input, binary data, emoji, RTL text
9. Save and version the tokenizer alongside model checkpoints

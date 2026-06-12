---
name: skill-grammar-pipeline
description: POS Tagging与Syntactic Parsing 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 5
lesson: 7
---

# POS Tagging与Syntactic Parsing：中文使用说明

你将围绕本课主题 **POS Tagging与Syntactic Parsing** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 5「NLP：从基础到进阶」
- 课程：第 07 课「POS Tagging与Syntactic Parsing」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: grammar-pipeline
description: Design a classical POS + dependency pipeline for a downstream NLP task.
version: 1.0.0
phase: 5
lesson: 07
tags: [nlp, pos, parsing]
---

Given a downstream task (information extraction, rewrite validation, query decomposition, lemmatization), you output:

1. Tagset. Penn Treebank for English-only legacy pipelines, Universal Dependencies for multilingual or cross-lingual.
2. Library. spaCy for most production (`en_core_web_sm` / `_lg` / `_trf`), stanza for academic-grade multilingual, trankit for highest UD accuracy.
3. Integration snippet. The 3-5 lines that call the library and consume `.pos_`, `.dep_`, `.head`.
4. Failure mode to test. Noun-verb ambiguity (`saw`, `book`, `can`) and PP-attachment ambiguity are classical traps. Sample 20 outputs and eyeball.

Refuse to recommend rolling your own parser. Building parsers from scratch is a research project, not an application task. Flag any pipeline that consumes POS tags without handling lowercase / uppercase variants as fragile.

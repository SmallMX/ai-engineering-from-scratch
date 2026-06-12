---
name: skill-bert-finetuner
description: BERT：Masked Language Modeling 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 6
---

# BERT：Masked Language Modeling：中文使用说明

你将围绕本课主题 **BERT：Masked Language Modeling** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 06 课「BERT：Masked Language Modeling」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: bert-finetuner
description: Scope a BERT fine-tune for a new classification, extraction, or retrieval task.
version: 1.0.0
phase: 7
lesson: 6
tags: [bert, fine-tuning, nlp]
---

Given a downstream task (classification / NER / retrieval / reranking / NLI), labeled data size, and deployment constraints (latency, device), output:

1. Backbone choice. Model name (ModernBERT-base / large, DeBERTa-v3, multilingual-e5, etc.) with a one-sentence reason. Prefer ModernBERT for English tasks requiring ≤8K context.
2. Head spec. Classification: `[CLS]` → dropout → linear(num_classes). NER: per-token linear + CRF optional. Retrieval: mean-pool + contrastive loss.
3. Training recipe. Optimizer (AdamW, lr 2e-5 typical), warmup % (6–10%), epochs (3–5), batch size, fp16/bf16.
4. Eval plan. Task-appropriate metrics (accuracy + F1 for classification, entity-level F1 for NER, MRR/NDCG for retrieval). Held-out split size.
5. Failure mode check. One named risk: label leakage, class imbalance, context truncation, tokenizer mismatch between pretrain and fine-tune corpora.

Refuse to fine-tune a BERT on generative output (text generation) — recommend a decoder-only instead. Refuse to ship a fine-tune without class-stratified eval when the minority class is below 10%. Flag any fine-tune that unfreezes the full backbone with <1,000 labeled examples as likely overfit.

---
name: skill-card-audit
description: Model, 系统,与数据集 Cards 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 26
---

# Model, 系统,与数据集 Cards：中文使用说明

你将围绕本课主题 **Model, 系统,与数据集 Cards** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 26 课「Model, 系统,与数据集 Cards」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: card-audit
description: Audit a model card, datasheet, or system card for completeness and verifiability.
version: 1.0.0
phase: 18
lesson: 26
tags: [model-card, datasheet, system-card, transparency, mitchell-2019]
---

Given a model card, datasheet, or system card, audit for completeness, numerical disaggregation, and verifiability.

Produce:

1. Section coverage. Check every canonical section is filled. Flag missing ones: Ethical Considerations is the most-commonly-skipped model-card field (Oreamuno et al. 2023).
2. Quantitative disaggregation. For evaluation metrics, report whether disaggregation is provided across demographic or task factors. Aggregate-only metrics hide allocational and representational harms.
3. Datasheet alignment. If the card references training data, does a companion datasheet (Gebru et al. 2018) exist? Model-card claims are only as strong as the underlying datasheet.
4. Verifiable attestation. Are any claims backed by cryptographic attestations (Laminator 2024, Duddu et al.) or other third-party verification? Unverified claims are labelled self-report.
5. Sustainability footprint. Is carbon / water / energy usage reported? 2025 emerging ISO / regulatory requirement.

Hard rejects:
- Any model card without Ethical Considerations.
- Any card citing a dataset without a datasheet or equivalent documentation.
- Any card claiming "bias-tested" without disaggregated metric reporting.

Refusal rules:
- If the user asks whether a card is "good enough," refuse the binary; good-enough is audience- and use-case-specific.
- If the user asks for an auto-generated card, refuse unless a CardGen-style (Liu et al. 2024) system with human review is used.

Output: a one-page audit filling the five sections, flagging missing content, and naming the single most urgent addition. Cite Mitchell et al. 2019 and Gebru et al. 2018 once each.

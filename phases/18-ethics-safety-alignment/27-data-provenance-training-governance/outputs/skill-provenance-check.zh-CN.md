---
name: skill-provenance-check
description: 数据 Provenance与训练-数据 治理 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 27
---

# 数据 Provenance与训练-数据 治理：中文使用说明

你将围绕本课主题 **数据 Provenance与训练-数据 治理** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 27 课「数据 Provenance与训练-数据 治理」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: provenance-check
description: Check a training dataset against California AB 2013 and EU TDM opt-out obligations.
version: 1.0.0
phase: 18
lesson: 27
tags: [data-provenance, ab-2013, tdm-opt-out, legitimate-interest, dpa]
---

Given a training dataset used by a deployment, check compliance against California AB 2013 and EU TDM opt-out.

Produce:

1. AB 2013 coverage. Fill the 12 fields. Flag any missing or placeholder-only fields. Note that the summary becomes binding once published.
2. Opt-out compliance. Does the dataset respect machine-readable opt-out signals (robots.txt, C2PA "No AI Training", TDM.Reservation)? Pre-collection filter must be in place.
3. DPA jurisdiction mapping. For each jurisdiction the data subjects belong to, identify the applicable DPA and the 2025 legitimate-interest position (Irish DPC, Cologne Higher Regional Court, Hamburg DPA, UK ICO, Brazilian ANPD).
4. Irreversibility audit. If the dataset contains PII, what unlearning or remediation procedure is in place? Acknowledge that no procedure fully remediates training data.
5. Provenance-chain completeness. Is there a signed chain from the data source to the training pipeline? If the dataset is derived (crawled + filtered), document the derivation.

Hard rejects:
- Any deployment that cites AB 2013 without per-dataset 12-field summaries.
- Any deployment that does not respect robots.txt or equivalent opt-out signals.
- Any remediation claim that assumes surgical removal of data from trained weights.

Refusal rules:
- If the user asks whether a specific dataset is "safe to train on," refuse without jurisdiction-by-jurisdiction analysis.
- If the user asks for a universal compliance strategy, refuse — jurisdictions differ materially.

Output: a one-page check filling the five sections, identifying the highest-risk compliance gap, and naming the single most urgent remediation. Cite California AB 2013 and EU Copyright Directive TDM exception once each.

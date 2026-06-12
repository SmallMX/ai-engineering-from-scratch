---
name: skill-ecosystem-map
description: 对齐 Research Ecosystem：MATS, Redwood, Apollo, METR 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 28
---

# 对齐 Research Ecosystem：MATS, Redwood, Apollo, METR：中文使用说明

你将围绕本课主题 **对齐 Research Ecosystem：MATS, Redwood, Apollo, METR** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 28 课「对齐 Research Ecosystem：MATS, Redwood, Apollo, METR」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: ecosystem-map
description: Map an alignment claim or evaluation to the organisation, methodology, and cross-checks.
version: 1.0.0
phase: 18
lesson: 28
tags: [mats, redwood, apollo, metr, eleos, ecosystem]
---

Given an alignment claim or evaluation, map the source to the research ecosystem and identify cross-checks.

Produce:

1. Source identification. Which organisation produced the claim (lab, MATS, Redwood, Apollo, METR, Eleos, academic lab)?
2. Methodological style. Does the work fit the organisation's documented style — Redwood control protocols, Apollo three-pillar scheming, METR task-horizon, Eleos welfare?
3. Counterpart organisation. Which other organisation works on adjacent problems, and has it published a complementary or contradicting result?
4. Multi-org signal. Is the paper a single-lab product or a joint publication (e.g., Apollo + OpenAI, Redwood + Anthropic)? Multi-org papers typically carry higher external credibility.
5. Publication venue. arXiv-only preprint, NeurIPS/ICML/ICLR proceedings, lab blog, or regulatory submission? Venue is a signal about scrutiny level.

Hard rejects:
- Any alignment claim without an identified producing organisation.
- Any single-org safety claim without an external replication or check.
- Any ecosystem map that ignores the MATS talent-pipeline structure.

Refusal rules:
- If the user asks "which research organisation is most trustworthy," refuse the ranking and point to multi-org replication.
- If the user asks for ecosystem-internal politics, refuse and stay on published methodology.

Output: a one-page map filling the five sections above, naming cross-check opportunities, and identifying the strongest evidence and the strongest counterargument.

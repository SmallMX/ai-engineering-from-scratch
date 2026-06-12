---
name: skill-framework-diff
description: Frontier 安全 框架：RSP, PF, FSF 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 18
---

# Frontier 安全 框架：RSP, PF, FSF：中文使用说明

你将围绕本课主题 **Frontier 安全 框架：RSP, PF, FSF** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 18 课「Frontier 安全 框架：RSP, PF, FSF」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: framework-diff
description: Compare a new safety framework or release note against RSP v3.0, PF v2, FSF v3.0.
version: 1.0.0
phase: 18
lesson: 18
tags: [rsp, pf, fsf, frontier-safety, safety-case]
---

Given a new safety framework, policy, or release note, compare it against Anthropic RSP v3.0, OpenAI PF v2, DeepMind FSF v3.0 along the five structural axes.

Produce:

1. Tier structure. Does the framework define discrete capability thresholds? Are they per-domain (FSF-style) or global (RSP-style)?
2. CBRN threshold. What CBRN evaluation is required? Does it reference WMDP (Lesson 17) or an equivalent? Does it include an elicitation study?
3. AI R&D threshold. Is there a model-autonomous-research threshold? Is the bar "entry-level researcher" (Anthropic AI R&D-2) or "substantially accelerate scaling" (Anthropic AI R&D-4)?
4. Competitor-adjustment. Does the framework allow reduction of requirements if competitors ship without comparable safeguards? Frame as race-dynamic or as incentive-compatibility, as appropriate.
5. Safety-case structure. Is a written safety case required? Does it target monitoring, illegibility, or incapability? What is the evidence bar?

Hard rejects:
- Any safety framework without per-tier capability thresholds.
- Any framework that omits an external governance cross-reference (UK AISI, US CAISI, EU AI Office).
- Any framework that claims "we align with all published frameworks" without specific threshold numbers.

Refusal rules:
- If the user asks which framework is "best," refuse the ranking and point to structural alignment.
- If the user asks for a numeric threshold recommendation, refuse — thresholds are lab-specific and depend on their measurement infrastructure.

Output: a one-page side-by-side comparison against the three frameworks, flagged gaps, and one specific threshold recommendation to add. Cite RSP v3.0, PF v2, FSF v3.0 once each.

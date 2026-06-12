---
name: skill-cross-policy-diff
description: OpenAI Preparedness 框架与DeepMind Frontier 安全 框架 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 20
---

# OpenAI Preparedness 框架与DeepMind Frontier 安全 框架：中文使用说明

你将围绕本课主题 **OpenAI Preparedness 框架与DeepMind Frontier 安全 框架** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 20 课「OpenAI Preparedness 框架与DeepMind Frontier 安全 框架」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: cross-policy-diff
description: Produce a cross-policy comparison for a specific capability using the OpenAI Preparedness Framework v2, Anthropic RSP v3.0, and DeepMind FSF v3 as reference.
version: 1.0.0
phase: 15
lesson: 20
tags: [preparedness-framework, fsf, rsp, cross-policy, scaling-policy]
---

Given a specific frontier capability (e.g., "long-range autonomy," "autonomous replication and adaptation," "R&D automation"), produce a cross-policy diff showing how each of the three frameworks classifies the capability and what mitigations trigger.

Produce:

1. **OpenAI PF v2 classification.** Tracked or Research. If Tracked, name the Capabilities + Safeguards Report triggers. If Research, note the policy language is "potential" mitigations.
2. **Anthropic RSP v3.0 classification.** Which threshold (ASL-3, AI R&D-4, hardcoded prohibition)? Which mitigation (affirmative case, security + deployment)? Confirm whether the commitment lives in the Anthropic-unilateral tier or the industry-recommendation tier.
3. **DeepMind FSF v3 classification.** Which domain (Cyber, Bio, ML R&D, CBRN)? Which CCL or Tracked Capability Level? Is deceptive alignment monitoring invoked?
4. **Convergence summary.** Do the three policies agree on the capability's severity, or is there meaningful disagreement? Which classification is most rigorous, which least?
5. **Measurement dependency.** Every classification depends on capability measurement. Name how the capability is measured and which eval provider (METR, Apollo, internal, third-party) owns that measurement.

Hard rejects:
- Claims of cross-policy alignment based on announcement-language similarity without document-level evidence.
- Any classification that cannot point to a specific clause in the source document.
- Treating "Research Category" (OpenAI) as equivalent to "Tracked Category" — they have different operational consequences.

Refusal rules:
- If the user cannot produce the source document passages for each classification, refuse and require citations first.
- If the user treats policy-existence as evidence of mitigation-in-practice, refuse and require evidence of the specific mitigations firing.
- If the capability is claimed to be "covered" by a framework but the word does not appear in the document, refuse and require a concrete clause reference.

Output format:

Return a diff document with:
- **Capability definition** (one sentence)
- **OpenAI PF v2 row** (classification, trigger, source clause)
- **Anthropic RSP v3.0 row** (classification, trigger, unilateral-vs-recommendation)
- **DeepMind FSF v3 row** (domain, CCL / TCL, deceptive-alignment involvement)
- **Convergence summary** (agreement + meaningful disagreement)
- **Measurement ownership** (eval provider, eval cadence)
- **Reader recommendation** (most rigorous, least rigorous, justified)

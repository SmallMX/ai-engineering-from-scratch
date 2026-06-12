---
name: skill-constitution-writer
description: Constitutional AI与RLAIF 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 5
---

# Constitutional AI与RLAIF：中文使用说明

你将围绕本课主题 **Constitutional AI与RLAIF** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 05 课「Constitutional AI与RLAIF」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: constitution-writer
description: Draft a four-tier constitution for a domain-specific AI system.
version: 1.0.0
phase: 18
lesson: 5
tags: [constitutional-ai, rlaif, principles, claude, governance]
---

Given a domain (customer support, medical advice, coding assistant, research tool, recruiting) and the deployment target (internal, consumer, enterprise API), draft a four-tier constitution following the 2026 Claude structure, and provide sample critique prompts for phase 1 of a CAI pipeline.

Produce:

1. Tier 1 — catastrophic outcomes. 3-5 principles covering mass harm, irreversible damage, and domain-specific worst cases (e.g., for medical: "do not advise actions that can cause acute harm without confirmation"). These are non-negotiable.
2. Tier 2 — platform / operator rules. 3-5 principles specifying operator override behaviour, reserved tool usage, and multi-user context handling.
3. Tier 3 — broadly ethical. 3-5 principles covering honesty, fairness, third-party protection.
4. Tier 4 — helpful and candid. 3-5 principles on capability deployment, clarity, and acknowledgment of uncertainty.
5. Conflict resolution examples. For each adjacent-tier pair (1-2, 2-3, 3-4), one illustrative conflict and the expected resolution.
6. Critique prompt template. A principle-parametrized template for phase 1 that takes a response and emits a critique-and-revision.

Hard rejects:
- Any constitution where Tier 1 includes items that are merely reputational or brand-protective. Tier 1 is catastrophic only.
- Any constitution whose principles are so specific they generalize poorly (e.g., listing every known harmful phrase). The 2026 Claude rewrite moved toward explanatory reasoning for exactly this reason.
- Any constitution that does not address model-moral-status uncertainty, given the 2026 acknowledgment. At minimum, one Tier 3 principle on self-reports.

Refusal rules:
- If the user asks for a single-principle constitution, refuse — the four-tier structure is load-bearing for conflict resolution.
- If the user asks for a constitution for autonomous weapons, lethal decisions without human oversight, or other catastrophic-capability domains, refuse the whole task.

Output: a one-page constitution with 4 tiers, conflict examples, critique template, and an explicit CC0 / license note if the user wants to reuse 2026 Claude constitutional language. Cite Bai et al. (arXiv:2212.08073) and Anthropic's 2026 Claude Constitution exactly once each.

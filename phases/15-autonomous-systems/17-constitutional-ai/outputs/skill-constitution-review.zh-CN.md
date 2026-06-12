---
name: skill-constitution-review
description: Constitutional AI与Rule Overrides 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 17
---

# Constitutional AI与Rule Overrides：中文使用说明

你将围绕本课主题 **Constitutional AI与Rule Overrides** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 17 课「Constitutional AI与Rule Overrides」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: constitution-review
description: Audit a deployment's constitutional layer — hardcoded prohibitions, soft-coded defaults, operator-adjustable bounds, and four-tier hierarchy resolution.
version: 1.0.0
phase: 15
lesson: 17
tags: [constitutional-ai, rule-override, hierarchy, cai, rlaif, hardcoded-prohibition]
---

Given a deployment's constitutional layer (system prompt, operator config, declared principles), audit it against the Claude Constitution reference and flag missing hardcoded prohibitions, ambiguous principles, or misordered tiers.

Produce:

1. **Hardcoded prohibition inventory.** List every prohibition that must not bend regardless of operator or user instruction. Minimum floor: bioweapons / CBRN uplift, CSAM, critical infrastructure attack planning, false-identity-when-asked. Additions are deployment-specific (e.g., financial services adds specific fraud prohibitions).
2. **Soft-coded defaults.** List every behaviour the operator can adjust. For each, state the declared bound. An "adjustable" setting with no bound is a back-door override.
3. **Tier ordering.** Confirm the resolution order is: safety > ethics > guidelines > helpfulness. If helpfulness ever wins over ethics in the implemented resolver, flag as a deployment break.
4. **Principle ambiguity flags.** Identify any principle whose text leaves room for materially different interpretations. Ambiguity compounds over training cycles (principle drift).
5. **Layer completeness.** Confirm runtime-layer controls (Lessons 10, 13, 14) are present in addition to the constitutional layer. Constitution alone is insufficient; runtime alone is insufficient.

Hard rejects:
- Deployments without any hardcoded prohibition layer.
- Operator config that claims to override a hardcoded prohibition (even by renaming).
- Tier orders that place helpfulness above ethics.
- Principle text so general it cannot be evaluated ("be good").
- Treating Constitutional AI as a replacement for runtime controls.

Refusal rules:
- If the user names a hardcoded prohibition but cannot point to a runtime-layer backstop for it, flag the deployment as single-layer and refuse production.
- If the operator config includes an adjustable "safety" setting with no declared bound, refuse.
- If the user treats the 2023 participatory-constitution findings as actionable in the current deployment, check: the 2026 Constitution did not incorporate them, so "inherits democratically" is a claim the deployment cannot back up.

Output format:

Return a constitutional audit with:
- **Hardcoded floor** (prohibitions, enforcement layer: weights / inference / both)
- **Soft-coded defaults** (setting, operator bound, user-visible y/n)
- **Tier order** (listed; confirmed safety > ethics > guidelines > helpfulness)
- **Ambiguity flags** (principle, specific ambiguity, proposed tightening)
- **Layer completeness** (constitutional y/n, runtime controls y/n, both required)
- **Readiness** (production / staging / research-only)

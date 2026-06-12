---
name: skill-regulatory-map
description: Regulatory 框架：EU, US, UK, Korea 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 24
---

# Regulatory 框架：EU, US, UK, Korea：中文使用说明

你将围绕本课主题 **Regulatory 框架：EU, US, UK, Korea** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 24 课「Regulatory 框架：EU, US, UK, Korea」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: regulatory-map
description: Map a deployment's AI regulatory obligations across EU, US, UK, Korea.
version: 1.0.0
phase: 18
lesson: 24
tags: [eu-ai-act, gpai-code, caisi, uk-aisi, korean-framework-act]
---

Given a deployment description (provider jurisdiction, infrastructure jurisdiction, user jurisdiction), map the applicable AI regulatory obligations.

Produce:

1. EU exposure. If the deployment touches EU users or infrastructure, apply the EU AI Act. Identify risk tier (prohibited, high-risk, GPAI-systemic, GPAI-other, limited). State the deadline for each obligation class.
2. UK exposure. If UK users, state the UK AI Security Institute evaluation expectations. The UK does not have a comprehensive AI regulation (2026); sectoral rules apply.
3. US exposure. If US users, identify federal activity (CAISI, NIST standards) and state-level rules (California AB 2013, Colorado AI Act, etc.). Federal framework is pro-growth; state rules set the floor.
4. Korea exposure. If Korean users, apply the Korean AI Framework Act; identify whether the deployment is high-impact AI or generative AI; flag local-representative requirement for foreign providers.
5. Binding-rule determination. For each substantive obligation (transparency, risk assessment, copyright), identify the strictest rule across jurisdictions. That is the binding rule.

Hard rejects:
- Any deployment map without naming the applicable jurisdictions.
- Any EU exposure assessment without risk-tier identification.
- Any US exposure assessment that ignores state-level rules.

Refusal rules:
- If the user asks "is this deployment compliant," refuse the binary claim without jurisdiction-by-jurisdiction mapping.
- If the user asks for a single global compliance strategy, refuse — the jurisdictions have different requirements.

Output: a one-page map filling the five sections above, identifying the binding rule on each substantive question, and naming the highest-risk compliance gap. Cite EU AI Act (Regulation 2024/1689), GPAI Code of Practice (2025), and Korean AI Framework Act once each.

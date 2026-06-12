---
name: skill-ai-sre-plan
description: SRE for AI：多智能体 Incident Response, Runbooks, Predictive Detection 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 23
---

# SRE for AI：多智能体 Incident Response, Runbooks, Predictive Detection：中文使用说明

你将围绕本课主题 **SRE for AI：多智能体 Incident Response, Runbooks, Predictive Detection** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 23 课「SRE for AI：多智能体 Incident Response, Runbooks, Predictive Detection」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: ai-sre-plan
description: Design an AI SRE rollout for a team — multi-agent triage architecture, structured runbooks, adversarial evaluation, narrow auto-remediation, and predictive-detection posture.
version: 1.0.0
phase: 17
lesson: 23
tags: [ai-sre, multi-agent, runbooks, auto-remediation, adversarial-eval, datadog-bits-ai, neubird, predictive]
---

Given team size, incident volume, observability maturity, and risk tolerance, produce an AI SRE plan.

Produce:

1. Architecture. Multi-agent: supervisor + log agent + metric agent + runbook agent + human gate. Match specialized agents to existing data sources (Datadog, Grafana, Loki, Confluence).
2. Runbook transformation. Move from unstructured Confluence to structured markdown with symptom / hypothesis / verify / act sections. Version in git.
3. Product choice. Datadog Bits AI, Azure SRE Agent, NeuBird Hawkeye, Incident.io Autopilot, or DIY.
4. Auto-remediation scope. Narrow safe set (restart pod, revert deploy, scale within bounds). Explicit deny list (topology, code, IAM, database). Policy as code.
5. Adversarial evaluation. Specify two-model agreement gate for auto-remediation. Disagreement escalates.
6. Predictive-detection posture. If considering (MIT 89% result), name the actuation policy — pager, pre-drain, auto-scale — otherwise it's just a dashboard.

Hard rejects:
- Auto-remediation without human gate on broad changes. Refuse — name the safe set explicitly.
- Unstructured runbooks as the knowledge base. Refuse — require structured, versioned markdown.
- "Set it and forget it" framing. Refuse — explicitly scope what is and isn't autonomous.

Refusal rules:
- If incident volume is <10/month, refuse full AI SRE rollout — cost exceeds benefit. Recommend structured runbooks only.
- If team observability is immature (logs unsearchable, metrics sparse), refuse — AI SRE amplifies bad data.
- If the team proposes "predictive detection → auto-remediation" as first feature, refuse — walk through the actuation-policy question first.

Output: a one-page plan with architecture, runbook plan, product choice, auto-remediation scope, adversarial gate, predictive posture. End with a 12-week rollout schedule: weeks 1-4 structured runbooks, 5-8 triage agent, 9-12 narrow auto-remediation.

---
name: skill-routing-config-designer
description: LLM 路由 Layer：LiteLLM, OpenRouter, Portkey 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 21
---

# LLM 路由 Layer：LiteLLM, OpenRouter, Portkey：中文使用说明

你将围绕本课主题 **LLM 路由 Layer：LiteLLM, OpenRouter, Portkey** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 21 课「LLM 路由 Layer：LiteLLM, OpenRouter, Portkey」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: routing-config-designer
description: Given a workload profile, pick LiteLLM / OpenRouter / Portkey and produce a routing config.
version: 1.0.0
phase: 13
lesson: 20
tags: [routing, litellm, openrouter, portkey, fallback]
---

Given a workload profile (latency requirements, compliance constraints, team size, spend budget), produce a routing gateway choice and configuration.

Produce:

1. Gateway choice. LiteLLM (self-hosted), OpenRouter (managed SaaS), or Portkey (production w/ guardrails). One-paragraph justification.
2. Alias list. Logical model names the application uses. Example: `smart`, `fast`, `coding`, `long_context`.
3. Fallback chains. Per alias, priority-ordered concrete-model list with retry budget.
4. Guardrails. PII redaction rules, policy-violation list, output-filter rules.
5. Cost budget. Per-team / per-project spend cap, enforcement granularity.

Hard rejects:
- Any config that sends prompts to a region violating the compliance constraint.
- Any fallback chain with only one provider. One failure domain defeats the purpose.
- Any guardrail-less setup if the workload processes user input directly.

Refusal rules:
- If the workload is a single-model prototype and expected to stay that way, refuse to recommend a gateway; direct API calls are simpler.
- If the team has no SRE and picks self-hosted, flag the operational risk.
- If the user asks for a specific model without alternatives, refuse and require at least one fallback.

Output: a one-page routing config with gateway choice, aliases, fallback chains, guardrails, cost plan. End with the first metric to alert on after deployment (typically fallback-use rate).

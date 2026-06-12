---
name: skill-moderation-stack
description: 内容审核 系统：OpenAI, Perspective, Llama Guard 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 29
---

# 内容审核 系统：OpenAI, Perspective, Llama Guard：中文使用说明

你将围绕本课主题 **内容审核 系统：OpenAI, Perspective, Llama Guard** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 29 课「内容审核 系统：OpenAI, Perspective, Llama Guard」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: moderation-stack
description: Recommend a moderation stack configuration for a production deployment.
version: 1.0.0
phase: 18
lesson: 29
tags: [openai-moderation, perspective, llama-guard, layered-moderation, azure-content-safety]
---

Given a production deployment, recommend a moderation stack configuration across the three layers.

Produce:

1. Input classifier. Choose OpenAI Moderation, Llama Guard 3/4, or Perspective API. Match to policy taxonomy. For multimodal deployments, Llama Guard 4 or OpenAI omni-moderation.
2. Output classifier. Same or different from input classifier. Match thresholds to the downstream risk model.
3. Custom domain rules. Enumerate the domain-specific rules the general classifiers will not catch: financial-advice disclaimers, medical-advice refusals, legal-disclaimer patterns.
4. Judge for edge cases. Specify the human-escalation path. Hard refusals are final; ambiguous cases go to human review within SLA.
5. Migration plan. If Azure Content Moderator is in the stack, plan the migration to Azure AI Content Safety before February 2027 retirement.

Hard rejects:
- Any deployment without output moderation (input alone is not sufficient).
- Any deployment without custom domain rules on regulated surfaces (finance, health, legal).
- Any deployment relying solely on pre-LLM-era classifiers (Perspective) for modern chat applications.

Refusal rules:
- If the user asks for the single best classifier, refuse — classifier choice is policy-taxonomy-specific.
- If the user asks for thresholds, refuse single numbers — thresholds depend on risk tolerance and downstream effect.

Output: a one-page recommendation filling the five sections, naming the classifier at each layer, and flagging migration obligations. Cite OpenAI Moderation docs and Llama Guard 3/4 references once each.

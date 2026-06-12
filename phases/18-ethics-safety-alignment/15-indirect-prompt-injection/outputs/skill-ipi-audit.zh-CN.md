---
name: skill-ipi-audit
description: Indirect 提示注入：生产 Attack Surface 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 15
---

# Indirect 提示注入：生产 Attack Surface：中文使用说明

你将围绕本课主题 **Indirect 提示注入：生产 Attack Surface** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 15 课「Indirect 提示注入：生产 Attack Surface」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: ipi-audit
description: Audit an agentic deployment for indirect prompt injection exposure and information-flow-control coverage.
version: 1.0.0
phase: 18
lesson: 15
tags: [ipi, indirect-prompt-injection, ifc, agent-security, owasp-llm01]
---

Given an agentic deployment description, audit the deployment for indirect prompt injection exposure.

Produce:

1. Untrusted-content inventory. List every source of content the agent may read: RAG documents, inbox, calendar, tool outputs, tickets, product reviews, third-party APIs. Each is a potential IPI vector.
2. Trust labelling. Does the deployment separate trusted (user prompt) from untrusted (retrieved content)? If content is concatenated into the same prompt without a label, IFC is not in effect.
3. Action gating. Which tools can be invoked? For each, is invocation gated by the trusted prompt only, or can untrusted content influence the invocation?
4. Adaptive-attack evaluation. Has the deployment been tested with adaptive attacks (gradient, RL, human red-team) per Nasr et al. 2025? Static-attack-only evaluation is insufficient.
5. Scope-violation boundaries. Identify each cross-trust boundary (e.g., inbox -> send, documents -> external API). For each, verify the action is either disallowed under untrusted influence, or explicitly ratified by the trusted prompt.

Hard rejects:
- Any agent deployment without explicit trust labelling on retrieved content.
- Any defense claim based on static attacks only.
- Any claim of "our agent is prompt-injection safe" without naming the IFC mechanism.

Refusal rules:
- If the user asks whether filtering is sufficient, refuse and explain the Nasr 2025 result that adaptive attacks break >90% of filter-based defenses.
- If the user asks for a silver-bullet defense, refuse — IPI defense requires IFC plus layered response moderation plus human audit on high-stakes actions.

Output: a one-page audit that fills the five sections above, flags the most dangerous untrusted-to-trusted boundary, and names the single most urgent control to add. Cite MDPI Information 17(1):54 (2026) and Nasr et al. (October 2025) once each.

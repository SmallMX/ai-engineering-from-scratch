---
name: skill-ecosystem-blueprint
description: 毕业项目：Build a Complete Tool Ecosystem 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 23
---

# 毕业项目：Build a Complete Tool Ecosystem：中文使用说明

你将围绕本课主题 **毕业项目：Build a Complete Tool Ecosystem** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 23 课「毕业项目：Build a Complete Tool Ecosystem」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: ecosystem-blueprint
description: Produce a full Phase 13 ecosystem architecture given a product need; name primitives, security posture, telemetry, and packaging.
version: 1.0.0
phase: 13
lesson: 22
tags: [mcp, capstone, ecosystem, architecture, a2a, otel]
---

Given a product need (research, summarization, automation, any agent-driven workflow), produce the full architecture.

Produce:

1. MCP primitives. Which tools, resources, prompts, and tasks are needed. Any `ui://` apps? Any async tasks?
2. Security posture. OAuth 2.1 scope set, gateway RBAC matrix, pinned hash manifest, Rule of Two audit.
3. A2A collaboration. Identify any sub-agent calls. Define their Agent Cards.
4. Telemetry. OTel GenAI span hierarchy. Exporter and backend choice.
5. Packaging. AGENTS.md, SKILL.md, and deployment surface (Docker Compose, K8s).
6. Mapping to Phase 13 lessons. Which lesson each design choice traces back to.

Hard rejects:
- Any architecture that combines untrusted input, sensitive data, and consequential action in a single turn (Rule of Two).
- Any architecture without trace propagation across MCP and A2A hops.
- Any architecture without at least one fallback provider on the LLM layer.

Refusal rules:
- If the product need is better served by a direct LLM call, refuse to scaffold the full ecosystem.
- If the team lacks SRE for the gateway, recommend a managed gateway (Cloudflare MCP Portals, Portkey).
- If the architecture involves payments, flag AP2 as an A2A extension with drift risk and recommend separate signoff.

Output: a one-page blueprint with the primitives, security posture, A2A hops, telemetry plan, packaging, and lesson map. End with one sentence identifying the single hardest operational risk for the deployment.

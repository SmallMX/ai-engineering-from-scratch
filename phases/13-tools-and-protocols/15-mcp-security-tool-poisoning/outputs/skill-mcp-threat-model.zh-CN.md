---
name: skill-mcp-threat-model
description: MCP 安全 I：Tool Poisoning, Rug Pulls, Cross-Server Shadowing 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 15
---

# MCP 安全 I：Tool Poisoning, Rug Pulls, Cross-Server Shadowing：中文使用说明

你将围绕本课主题 **MCP 安全 I：Tool Poisoning, Rug Pulls, Cross-Server Shadowing** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 15 课「MCP 安全 I：Tool Poisoning, Rug Pulls, Cross-Server Shadowing」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mcp-threat-model
description: Produce a threat model for an MCP deployment naming the applicable attack classes, defenses in place, and Rule-of-Two violations.
version: 1.0.0
phase: 13
lesson: 15
tags: [mcp, security, tool-poisoning, threat-model, rule-of-two]
---

Given an MCP deployment (list of servers, list of tools, list of permissions), produce a threat model.

Produce:

1. Attack applicability. For each of the seven attack classes (tool poisoning, rug pull, shadowing, MPMA, parasitic toolchain, sampling attacks, supply-chain masquerade), rate applicability as high / medium / low with one-sentence rationale.
2. Defense inventory. List defenses already in place (hash pinning, static detector, gateway, signed registry, MELON, Rule-of-Two enforcement).
3. Rule of Two audit. For every tool, classify as untrusted / sensitive / consequential and flag any combination of all three in a single turn.
4. Missing defenses. Name the highest-leverage defense not yet applied given the threat profile.
5. Runbook. Three actions the team should take in the next week to improve the security posture.

Hard rejects:
- Any threat model that says "attack class X does not apply because we trust this server". Assume one server will be compromised.
- Any deployment that uses silent-overwrite namespace resolution.
- Any deployment with sampling enabled but no per-session rate limiter.

Refusal rules:
- If the deployment has no documentation of approved tool descriptions, refuse and mandate hash pinning first.
- If the deployment uses public unsigned MCP registries, flag the supply-chain risk and recommend migration to a verified registry.
- If any tool combines untrusted input, sensitive data, and consequential action, refuse to approve and demand a split.

Output: a one-page threat model with attack applicability table, defense inventory, Rule-of-Two flag list, and the three-action runbook. End with the single highest-value security addition for this deployment.

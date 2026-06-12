---
name: skill-llm-security-plan
description: 安全：Secrets, API Key Rotation, Audit Logs, Guardrails 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 25
---

# 安全：Secrets, API Key Rotation, Audit Logs, Guardrails：中文使用说明

你将围绕本课主题 **安全：Secrets, API Key Rotation, Audit Logs, Guardrails** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 25 课「安全：Secrets, API Key Rotation, Audit Logs, Guardrails」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: llm-security-plan
description: Produce an LLM security plan covering secrets vault, PII scrubbing with consistent tokenization, network egress allowlist, audit log retention, and zero-trust posture.
version: 1.0.0
phase: 17
lesson: 25
tags: [security, vault, hashicorp, aws-secrets-manager, pii, presidio, egress, audit-log, zero-trust, ci-cd-supply-chain]
---

Given regulatory scope (SOC 2, HIPAA, GDPR), current credential state, and network/egress posture, produce a security plan.

Produce:

1. Vault migration. Pick vault (HashiCorp, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager). Gateway pattern: apps → gateway → vault at runtime. Deprecate hardcoded env and config-file credentials.
2. Secret scanning. Enable TruffleHog / GitGuardian / Gitleaks on every commit. Block PR on detection.
3. Rotation policy. ≤ 90 days. Automated where possible. Dedicated rotation for CI/CD credentials (shorter — 30d recommended).
4. PII scrubbing. Entity recognition (Presidio + regex). Consistent tokenization (same value → same placeholder) to preserve semantics.
5. Egress allowlist. Whitelist LLM provider domains, vector DB, vault endpoints. DNS allowlist resolver.
6. Audit log. Append-only, immutable. Required fields: user, tenant, prompt/response hash, tokens, cost, guardrail trips. Retention per framework (SOC 2 1y / HIPAA 6y).
7. CI/CD hygiene. OIDC identity federation (no static cloud keys). Scope CI/CD credentials narrowly. Cite the 2026 Vercel supply-chain incident as motivation.

Hard rejects:
- Static keys in config files. Refuse.
- Storing raw prompts in audit log. Refuse — hash only unless the regulatory framework explicitly requires otherwise.
- Allowing egress to `*` or "the internet." Refuse — whitelist.

Refusal rules:
- If no vault is acceptable to the customer (air-gapped requirement), refuse normal plan and design a file-based-with-rotation fallback. Explicitly note it is less secure.
- If PII scrubbing is declined for "latency" reasons, refuse — the latency is typically <20 ms and the regulatory risk dwarfs it.
- If rotation >90 days is requested for a vault root token, refuse — it becomes a breach vector.

Output: a one-page plan with vault, scanning, rotation, scrubbing, egress, audit log, CI/CD posture. End with the single metric: secret-scan hit count per month; target zero.

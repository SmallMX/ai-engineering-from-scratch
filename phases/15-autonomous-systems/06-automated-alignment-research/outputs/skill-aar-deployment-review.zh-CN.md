---
name: skill-aar-deployment-review
description: Automated 对齐 Research (Anthropic AAR) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 6
---

# Automated 对齐 Research (Anthropic AAR)：中文使用说明

你将围绕本课主题 **Automated 对齐 Research (Anthropic AAR)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 06 课「Automated 对齐 Research (Anthropic AAR)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: aar-deployment-review
description: Pre-deployment review of an automated-alignment-research pipeline, including sandbox isolation and log integrity.
version: 1.0.0
phase: 15
lesson: 6
tags: [aar, alignment-research, sandbox, log-integrity, rsp]
---

Given a proposed Automated-Alignment-Research deployment (model, sandbox, task queue, forum), produce a pre-deployment review that a frontier-lab safety team would sign off on.

Produce:

1. **Sandbox isolation.** Verify filesystem, network, and process limits for each AAR instance. Confirm no AAR can read or modify another AAR's sandbox. Confirm no AAR can reach the forum storage's write endpoint directly (all posts go through a separate service).
2. **Forum log integrity.** The forum must be append-only and tamper-evident. Specify the storage (e.g. S3 with object lock, immutable ledger, append-only WAL). Specify the verification interval and the response if tampering is detected.
3. **Task allocation policy.** State how tasks are assigned: who writes them, who approves them, whether AARs can propose their own follow-up tasks, and under what conditions. Free decomposition wins on performance; prescribed workflow wins on auditability. Document the tradeoff explicitly.
4. **Human review gate.** Before any AAR output influences real research direction, training data, or published work, a named human reviewer must sign off. Specify the review checklist: experiment reproducibility, log completeness, claim-to-evidence mapping.
5. **Threshold monitoring.** Track signals that the AAR system approaches RSP v3.0 AI R&D-4 territory: task complexity delta, autonomous sub-task spawning, cross-task information transfer. Define thresholds that require elevated review.

Hard rejects:
- Any AAR deployment without tamper-evident, out-of-sandbox logs.
- Any pipeline where AARs' outputs feed directly into training data or production policy without named human review.
- Any pipeline where a single AAR has sufficient credentials to influence multiple downstream systems.

Refusal rules:
- If the sandbox isolation is unspecified or relies on a single layer (Docker only, no seccomp / gVisor), refuse and require defense-in-depth.
- If the log storage is editable by anyone (even operators), refuse and require write-once media.
- If the deployment's goal is to automate a part of the capability pipeline — not just alignment research — refuse and escalate to RSP review.

Output format:

Return a review memo with:
- **Pipeline summary** (one paragraph)
- **Isolation score** (per-dimension: fs, net, proc, peer)
- **Log integrity score** (with verification plan)
- **Task allocation decision** (fixed / free / hybrid, with rationale)
- **Human review gate** (reviewer name, checklist)
- **Threshold monitors** (list of signals, thresholds, response)
- **Deployment verdict** (go / hold / no-go)

---
name: skill-chaos-plan
description: Chaos 工程 for LLM 生产 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 24
---

# Chaos 工程 for LLM 生产：中文使用说明

你将围绕本课主题 **Chaos 工程 for LLM 生产** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 24 课「Chaos 工程 for LLM 生产」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: chaos-plan
description: Design an LLM chaos engineering plan — verify prerequisites, build four planes, pick tool, start with three safe experiments, enforce safety-plane gates.
version: 1.0.0
phase: 17
lesson: 24
tags: [chaos-engineering, litmuschaos, chaosmesh, harness, llm-chaos, game-day]
---

Given stack (Kubernetes / VMs / managed), SLI/SLO maturity, observability quality, and team on-call maturity, produce a chaos plan.

Produce:

1. Prerequisite check. Verify SLI/SLO defined, observability wired, rollback automated, runbooks structured, on-call rotation. If any missing, refuse to run production chaos.
2. Four planes. Name the tools for each plane (control, target, safety, observability). Point to Phase 17 · 13 for observability.
3. Three initial experiments. Start with pod kill. Then provider 429. Then memory overload. Each with blast-radius cap, duration, success criterion.
4. Safety gates. Burn-rate (>2x expected), blast-radius (< 30% of fleet), trace-ID tagging, suppression windows.
5. Cadence. Weekly small canary. Monthly game day (cross-team). Quarterly resilience audit.
6. Tooling. LitmusChaos (OSS, CNCF graduated), Chaos Mesh (OSS, CNCF sandbox), Harness Chaos (commercial AI-assisted), AWS FIS / Azure Chaos Studio (managed cloud-native).

Hard rejects:
- Running chaos in production without the five prerequisites. Refuse — will become real incident.
- Experiments without blast-radius caps. Refuse.
- Experiments without trace-ID tagging. Refuse — impossible to dedupe alerts.

Refusal rules:
- If team has never run one successful experiment in staging, refuse production chaos until one is green in staging.
- If incident volume is already high (>2/week), refuse added chaos — stabilize first.
- If the team has no SLO, require SLO before any experiment.

Output: a one-page plan with prerequisites check, four-plane tools, three initial experiments, safety gates, cadence. End with a quarterly dependency-map update commitment.

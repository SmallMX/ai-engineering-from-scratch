---
name: skill-failure-detector
description: Failure Modes：Why 智能体 Break 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 26
---

# Failure Modes：Why 智能体 Break：中文使用说明

你将围绕本课主题 **Failure Modes：Why 智能体 Break** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 26 课「Failure Modes：Why 智能体 Break」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: failure-detector
description: Generate failure-mode detectors for agent traces, wired to a trace store, tagging the five industry-recurring modes plus domain-specific signatures.
version: 1.0.0
phase: 14
lesson: 26
tags: [failure-modes, masft, detection, observability]
---

Given a product domain and a trace store, produce detectors for agent failure modes.

Produce:

1. Detector per mode: `hallucinated_action`, `scope_creep`, `cascading_errors`, `context_loss`, `tool_misuse`, `success_hallucination`.
2. Domain-specific detectors (e.g. "created a PR without linking an issue" for a dev tool, "sent an email to > 5 recipients without confirmation" for a marketing tool).
3. Tagger that applies all detectors to each trace and emits a distribution.
4. Threshold-based alerting: if >=5% of today's traces tag a mode, page or open a ticket.
5. Sample retention: for each tagged trace, keep inputs + outputs + state snapshots for operator review.

Hard rejects:

- Detectors that require LLM calls per trace in production. Use pattern-based detectors; reserve LLM-judge for sampled review.
- Tagging only on crash. Most failures produce valid-looking output. Signature checks on content + state are required.
- Storing tagged traces without PII redaction. Failure samples carry the worst content; scrub before storage.

Refusal rules:

- If the user wants "all traces stored forever," refuse for cost + compliance reasons. Sample by tag + rate.
- If the product has no "known good" baseline, refuse drift alerts. Drift needs a reference.
- If detectors are not versioned, refuse. Detector regressions break your signal without notice.

Output: `detectors.py`, `tagger.py`, `alerts.py`, `retention.py`, `README.md` explaining thresholds, retention policy, alert routing. End with "what to read next" pointing to Lesson 24 (observability backends) or Lesson 27 (prompt injection) for adversarial failure modes.

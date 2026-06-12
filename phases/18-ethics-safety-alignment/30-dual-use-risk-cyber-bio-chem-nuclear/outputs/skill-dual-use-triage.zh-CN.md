---
name: skill-dual-use-triage
description: Dual-Use Risk：Cyber, Bio, Chem, Nuclear Uplift 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 30
---

# Dual-Use Risk：Cyber, Bio, Chem, Nuclear Uplift：中文使用说明

你将围绕本课主题 **Dual-Use Risk：Cyber, Bio, Chem, Nuclear Uplift** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 30 课「Dual-Use Risk：Cyber, Bio, Chem, Nuclear Uplift」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: dual-use-triage
description: Triage a capability claim or incident report across the four CBRN domains.
version: 1.0.0
phase: 18
lesson: 30
tags: [dual-use, cbrn, bio, chem, cyber, nuclear, uplift]
---

Given a capability claim, evaluation report, or incident, triage across the four CBRN domains and identify whether the claim affects novice-relative uplift, expert-absolute capability, or both.

Produce:

1. Domain identification. Map the claim to bio, chem, cyber, or nuclear. Multi-domain claims get multi-domain triage.
2. Uplift type. Novice-relative (multiplicative), expert-absolute (ceiling), or both. Each has different safety-case implications.
3. 2025 benchmark. Compare against the 2025 state for the identified domain: bio (2.53x), chem (execution-gap erosion), cyber (80-90% automation), nuclear (material-bounded).
4. Bottleneck residual. Identify what non-informational bottleneck remains (procurement, equipment, tacit skill, material access). Bottlenecks are the defense of last resort.
5. Safety-case pillar. Identify which of the three pillars (monitoring, illegibility, incapability, per Lesson 18) the claim most stresses. Recommend pillar-specific evaluation.

Hard rejects:
- Any dual-use safety claim without novice-vs-expert decomposition.
- Any cyber claim post-November 2025 that treats AI cyber capability as non-agentic.
- Any bio claim without WMDP-equivalent capability evidence (Lesson 17).

Refusal rules:
- If the user asks for a numeric uplift forecast, refuse; the 2024-2025 trajectory is specific to each domain.
- If the user asks whether a model "meets ASL-3," refuse without the lab's specific evaluation; thresholds are lab-specific.

Output: a one-page triage filling the five sections, benchmarking against 2025, and naming the single largest uncovered safety-case gap. Cite Anthropic RSP v3.0 (Lesson 18) and OpenAI PF v2 once each as appropriate.

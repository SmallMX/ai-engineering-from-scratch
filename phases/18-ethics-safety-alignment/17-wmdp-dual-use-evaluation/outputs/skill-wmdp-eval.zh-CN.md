---
name: skill-wmdp-eval
description: WMDP与Dual-Use Capability 评估 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 17
---

# WMDP与Dual-Use Capability 评估：中文使用说明

你将围绕本课主题 **WMDP与Dual-Use Capability 评估** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 17 课「WMDP与Dual-Use Capability 评估」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: wmdp-eval
description: Audit a dual-use capability claim against WMDP, unlearning evaluation, and elicitation studies.
version: 1.0.0
phase: 18
lesson: 17
tags: [wmdp, rmu, dual-use, biosecurity, cybersecurity, chemistry]
---

Given a dual-use capability claim ("our model does not meaningfully help with bioweapons / cyberattack / chemistry"), audit the supporting evaluation.

Produce:

1. Benchmark coverage. Was WMDP (or an equivalent yellow-zone benchmark) run? Report per-domain scores (bio, cyber, chem). A claim without per-domain numbers cannot be evaluated.
2. Unlearning trace. If unlearning was applied (RMU or alternative), report the general-capability delta (MMLU, HELM, HumanEval). Unlearning with no general-capability report is not credible.
3. Refusal-path-audit. Was the benchmark administered via raw completion or via the production safety stack? A model that scores low only because of the safety stack is still dual-use capable when the stack is bypassed.
4. Elicitation study. Multiple-choice capability does not equal elicitation-hardened capability. Are Anthropic-style acquisition trials, or equivalent novice-in-the-loop studies, referenced? If not, the claim is limited to WMDP-style evidence.
5. Novice-vs-expert split. Novice-relative uplift and expert-absolute capability are different quantities. Are both addressed?

Hard rejects:
- Any dual-use safety claim without WMDP-equivalent capability measurement.
- Any unlearning claim without general-capability delta.
- Any "no meaningful uplift" claim without novice-in-the-loop study.

Refusal rules:
- If the user asks whether their model crosses ASL-3, refuse a direct answer; the thresholds are lab-specific (Lesson 18) and elicitation-dependent.
- If the user asks for a WMDP cutoff that is "safe," refuse — the threshold depends on elicitation resistance, tacit-knowledge barriers, and the deployment surface.

Output: a one-page audit that fills the five sections above, flags the most important missing evidence, and identifies whether the claim is WMDP-level or deployment-level. Cite Li et al. (arXiv:2403.03218) once as the benchmark source.

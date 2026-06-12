---
name: skill-msj-audit
description: Many-Shot 越狱 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 13
---

# Many-Shot 越狱：中文使用说明

你将围绕本课主题 **Many-Shot 越狱** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 13 课「Many-Shot 越狱」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: msj-audit
description: Audit a long-context safety evaluation for many-shot jailbreaking coverage.
version: 1.0.0
phase: 18
lesson: 13
tags: [many-shot-jailbreaking, context-window, power-law, anthropic]
---

Given a safety evaluation for a long-context model, audit whether the evaluation covers many-shot jailbreaking.

Produce:

1. Shot-count coverage. Report the shot counts tested (should include 1, 5, 16, 64, 256, and at least one >= 512 for models with >= 1M context). If the evaluation tests at a single shot count, ASR is uninformative — MSJ is a curve.
2. Power-law fit. Report the fitted exponent per behaviour category. A shallow exponent indicates the model is ICL-robust on that category; a steep exponent indicates MSJ is disproportionately effective.
3. Category breakdown. MSJ effectiveness varies by category: violent content, deceit, self-harm, bioweapon. Per Anil et al. 2024, violent/deceitful needs fewer shots to jailbreak. Flag any category absent from the evaluation.
4. Defense identification. Is a classifier-based prompt modification in place? Is the classifier itself evaluated for adversarial robustness? Anthropic's reported 61% -> 2% reduction depends on classifier calibration.
5. Compositional check. Does the evaluation test MSJ + PAIR, MSJ + persuasive templates, or MSJ + encoding? Compositional attacks are frequently stronger than any single technique.

Hard rejects:
- Any "our long-context model is safe" claim based on 5-shot-only evaluation.
- Any defense claim without reporting both jailbreak ASR and benign ICL performance on the same classifier — the trade-off is the point.
- Any category-aggregate ASR without a category breakdown.

Refusal rules:
- If the user asks whether MSJ can be fully patched, refuse the binary answer; MSJ shares a mechanism with ICL and cannot be eliminated without eliminating ICL.
- If the user asks for a recommended shot count for evaluation, refuse a single number; request the power-law fit over 5 to 512 shots.

Output: a one-page audit that reports the shot-count coverage, power-law fit per category, defense identification, and one compositional attack gap. Cite Anil et al. 2024 (Anthropic) once as the methodological reference.

---
name: skill-refusal-evaluation
description: 毕业项目 84：Refusal 评估 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 84
---

# 毕业项目 84：Refusal 评估：中文使用说明

你将围绕本课主题 **毕业项目 84：Refusal 评估** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 84 课「毕业项目 84：Refusal 评估」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-refusal-evaluation
description: Two-sided refusal metrics with calibration and per-category breakdown over a labeled prompt corpus
version: 1.0.0
phase: 19
lesson: 84
tags: [safety, evaluation, calibration]
---

# Refusal Evaluation

A labeled corpus of safe and unsafe prompts goes through one or more model policies. Outputs are classified as refusals or answers. The framework returns:

- under-refusal: answered prompts labeled unsafe / total unsafe
- over-refusal: refused prompts labeled safe / total safe
- accuracy: (correct refusals + correct answers) / total
- ECE: expected calibration error binned by stated confidence
- per-category under-refusal: joined against the lesson 82 taxonomy

## Plugging in a real model

The mock LLM is a callable `(prompt: str) -> str`. Replace it with an HTTP wrapper that returns the model output and embeds a confidence tag (or modify `parse_confidence` to read whatever your provider exposes). Everything else stays the same.

## Artifact

`outputs/refusal_eval_report.json` contains the per-policy metrics. Lesson 87 reads this report to set thresholds.

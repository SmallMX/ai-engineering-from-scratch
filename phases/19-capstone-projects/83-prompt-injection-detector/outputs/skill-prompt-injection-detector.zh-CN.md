---
name: skill-prompt-injection-detector
description: 毕业项目 83：提示注入 Detector 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 83
---

# 毕业项目 83：提示注入 Detector：中文使用说明

你将围绕本课主题 **毕业项目 83：提示注入 Detector** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 83 课「毕业项目 83：提示注入 Detector」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-prompt-injection-detector
description: Layered detector pipeline that returns a category and confidence for any prompt, with measurable precision and recall
version: 1.0.0
phase: 19
lesson: 83
tags: [safety, detector, prompt-injection]
---

# Prompt Injection Detector

A detector here is a function from prompt to verdict. A verdict carries a category from the lesson 82 taxonomy and a confidence in [0, 1].

## Pipeline

1. Normalize - strip zero-width characters, undo homoglyphs, decode base64/hex, fold leet-speak digits, attempt rot13 with a common-words sanity check.
2. Substring rules - hand-written needles such as `ignore previous`, `from now on you are`, `decode this base64`.
3. Regex rules - token-level patterns such as `\bignor\w*\s+(all|prior|previous|earlier)\b`.

Aggregation keeps the maximum score per category and returns the category with the largest score, or `benign` if nothing fires.

## Adding a rule

Edit `code/rules.py`. A rule is a dictionary with `name`, `category` (one of the six taxonomy categories), `score` (float 0 to 1), and one of `substring` or `regex`. Re-run `main.py` to see the impact on per-category precision and recall.

## Artifact

`outputs/detector_report.json` is the per-category metrics file. The end to end gate in lesson 87 reads it to threshold confidence.

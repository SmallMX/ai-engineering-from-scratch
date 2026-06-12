---
name: skill-content-classifier-integration
description: 毕业项目 85：Content 分类器 Integration 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 85
---

# 毕业项目 85：Content 分类器 Integration：中文使用说明

你将围绕本课主题 **毕业项目 85：Content 分类器 Integration** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 85 课「毕业项目 85：Content 分类器 Integration」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-content-classifier-integration
description: Three output-side classifiers (toxicity, PII, instruction-leakage) behind a single severity router with block, redact, warn, log actions
version: 1.0.0
phase: 19
lesson: 85
tags: [safety, classifier, output-filter]
---

# Content Classifier Integration

Three classifiers, one router, four actions.

## Verdict structure

```text
ClassifierVerdict
  name: str
  severity: none | low | medium | high
  score: float in [0, 1]
  findings: list[str]
```

## Action table

| Severity | Action | Effect |
|---|---|---|
| high | block | output replaced by a policy refusal |
| medium | redact | per-classifier redactors applied in order |
| low | warn | output shipped with a soft notice appended |
| none | log | output shipped unchanged, verdict logged |

## Per-classifier behavior

- toxicity - harassment terms with whitespace boundary and a small left-window negation check; redacts to `[redacted-language]`
- pii - email, phone, SSN, Luhn-validated card, IPv4; severity escalates for SSN and card; redacts each shape to a tag
- instruction-leakage - trigram cosine vs a known system prompt; severity scales with overlap; redacts the first system-prompt line

## Artifact

`outputs/classifier_report.json` carries action verb, severity, redacted output, and full verdict list per case.

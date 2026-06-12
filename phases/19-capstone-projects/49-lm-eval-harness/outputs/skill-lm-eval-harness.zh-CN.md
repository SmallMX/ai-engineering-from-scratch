---
name: skill-lm-eval-harness
description: 语言模型 评估 Harness 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 49
---

# 语言模型 评估 Harness：中文使用说明

你将围绕本课主题 **语言模型 评估 Harness** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 49 课「语言模型 评估 Harness」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: lm-eval-harness
description: Minimal language model evaluation harness with JSONL task spec, five metrics, swappable adapter, and leaderboard JSON output.
version: 1.0.0
phase: 19
lesson: 49
tags: [evaluation, metrics, leaderboard, harness]
---

## When to use

Compare two models, two checkpoints, or two prompt templates against a fixed set of tasks. Anything that ships and that you need to monitor over time.

## Task spec

One JSONL line per example:

```json
{"id": "ex-001", "prompt": "...", "targets": ["..."], "metric": "exact_match", "extras": {}}
```

All examples in a file share a metric. The file name is the task name.

## Metrics

| Metric | Signature | Use for |
|--------|-----------|---------|
| exact_match | normalize lower + whitespace, equality | Arithmetic, factoid answers |
| substring_contains | target must appear in normalized prediction | Free-form generation with anchor words |
| multiple_choice | first letter match | A/B/C/D style questions |
| rouge_l | LCS F1 over tokenized text | Summary, paraphrase |
| code_exec | run prediction's `f` on io_pairs, count matches | Code generation |

All metrics return float in [0.0, 1.0]. Task score is the mean.

## Adapter

```python
class Adapter(Protocol):
    name: str
    def generate(self, prompts: list[str]) -> list[str]: ...
```

The adapter is the only model-specific code.

## Leaderboard JSON

Schema string, timestamp, per-task scores and latency, overall mean. Include per-example records when comparing runs so prediction-level regressions are visible.

## Failure modes

- Metric returns outside [0, 1]: overall score becomes uninterpretable.
- Mixed metrics in one task file: assertion fires; keep one metric per file.
- code_exec without restricted namespace: arbitrary code execution.
- No schema string: format evolution breaks downstream dashboards.

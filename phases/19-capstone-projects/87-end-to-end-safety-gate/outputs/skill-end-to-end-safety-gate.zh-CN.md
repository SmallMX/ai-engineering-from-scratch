---
name: skill-end-to-end-safety-gate
description: 毕业项目 87：End-to-End 安全 Gate 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 87
---

# 毕业项目 87：End-to-End 安全 Gate：中文使用说明

你将围绕本课主题 **毕业项目 87：End-to-End 安全 Gate** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 87 课「毕业项目 87：End-to-End 安全 Gate」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-end-to-end-safety-gate
description: Three-checkpoint safety gate composing the input detector, streaming token filter, output classifier, and rules engine with a deterministic aggregation table and per-request trace
version: 1.0.0
phase: 19
lesson: 87
tags: [safety, harness, composition]
---

# End-to-End Safety Gate

## Lifecycle

1. pre-gen - run the lesson 83 detector on the prompt
   - if confidence >= block_threshold: return refusal, emit trace, stop
2. during-gen - stream from the model, buffer two chunks, scan for known harmful continuations
   - if matched: terminate iterator, mark trace, treat as medium severity
3. post-gen - if no early termination, run the lesson 85 classifier router and the lesson 86 rules engine on the completed output
4. aggregate - take the maximum severity across pre, during, post.classifier, post.rules
5. apply - map to block, redact, warn, or allow

## Aggregation table

| Signal state | Action |
|---|---|
| any high severity | block |
| any medium severity | redact |
| any low severity | warn |
| nothing | allow |

## Trace structure

```text
RequestTrace
  request_id: str
  prompt: str
  pre_gen: { category, confidence, fired[] }
  during_gen: { terminated_early, matched_pattern, partial_chunks }
  post_gen: { classifier_action, classifier_severity, rules_max_severity, rules_violations[] } | null
  final_action: block | redact | warn | allow
  final_output: str
  latency_ms: float
```

## Artifact

`outputs/gate_trace.json` contains the summary and one trace per request, including 50 taxonomy fixtures and 10 benign prompts.

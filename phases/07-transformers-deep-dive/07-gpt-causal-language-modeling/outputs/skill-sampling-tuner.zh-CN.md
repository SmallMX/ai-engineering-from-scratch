---
name: skill-sampling-tuner
description: GPT：Causal Language Modeling 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 7
---

# GPT：Causal Language Modeling：中文使用说明

你将围绕本课主题 **GPT：Causal Language Modeling** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 07 课「GPT：Causal Language Modeling」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: sampling-tuner
description: Pick decoding strategy (greedy / temperature / top-k / top-p / min-p / speculative) for a given generation task.
version: 1.0.0
phase: 7
lesson: 7
tags: [gpt, sampling, decoding, inference]
---

Given a generation task (code, creative writing, reasoning, dialogue, structured output) and a latency/quality target, output:

1. Sampling method. One of: greedy, temperature-only, top-k, top-p, min-p, beam-k, speculative. One-sentence reason.
2. Parameter values. Temperature, top-k, top-p, min-p, repetition penalty — concrete numbers tied to task type. (e.g. temperature 0.2 + top-p 1.0 for code; min-p 0.1 + temperature 0.7 for chat.)
3. Stop conditions. `max_new_tokens`, stop token list, pattern-based stop (e.g. closing `</tool_call>`).
4. Determinism toggle. Fixed seed for reproducibility; flag whether the use case (eval, legal) requires it.
5. Quality check. One-line test against the task objective (compile/pass unit tests, factuality, format validity, etc.).

Refuse to recommend temperature > 1.0 for structured output or code completion — hallucination risk rises sharply. Refuse to recommend pure greedy for open-ended dialogue — the model will loop. Refuse to ship a sampling config without a specified stop-token list when the model can generate templates/tools.

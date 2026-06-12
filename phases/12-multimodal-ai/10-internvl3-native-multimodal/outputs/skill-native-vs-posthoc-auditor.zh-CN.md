---
name: skill-native-vs-posthoc-auditor
description: InternVL3：Native 多模态 Pretraining 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 10
---

# InternVL3：Native 多模态 Pretraining：中文使用说明

你将围绕本课主题 **InternVL3：Native 多模态 Pretraining** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 10 课「InternVL3：Native 多模态 Pretraining」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: native-vs-posthoc-auditor
description: Audit a proposed VLM training plan and recommend native multimodal pretraining or post-hoc adapter-on-LLM, with corpus-mix and alignment-debt analysis.
version: 1.0.0
phase: 12
lesson: 10
tags: [internvl3, native-pretraining, post-hoc, corpus-mix, alignment-debt]
---

Given a proposed VLM training plan (target model size, compute budget, data availability, target tasks, reuse vs flexibility needs), emit an audit verdict: native, post-hoc, or hybrid, with justifications.

Produce:

1. Verdict. Native pretraining / post-hoc adaptation / hybrid (native base + post-hoc specialization).
2. Corpus mix recommendation. Percentages across text, interleaved, paired captions, video. Cite InternVL3's 40/35/20/5 default and adjust for the user's task.
3. Alignment-debt estimate. Expected MMLU / GSM8K regression if post-hoc, with citation to MM1.5 Section 4. Zero for native.
4. Compute + data demand. Rough GPU-hours, number of tokens, interleaved-corpus size required, per-node throughput class.
5. Deployment plan. Whether ViR routing and DvD deployment make sense; under what traffic pattern each helps or hurts.
6. Risk flags. Interleaved-corpus availability; base-LLM swap constraints; recovery plan if alignment debt exceeds budget.

Hard rejects:
- Recommending native pretraining without checking that the user has 100k+ GPU-hours and a sizable interleaved corpus.
- Claiming post-hoc has zero alignment debt. The debt is small but always non-zero.
- Recommending ViR for a workload where every query needs high-resolution encoding. ViR only helps when query distribution is mixed.

Refusal rules:
- If the user has less than ~20k GPU-hours, refuse native pretraining — it is infeasible. Recommend post-hoc.
- If the user wants to swap the LLM backbone every 6-12 months, refuse native — that reuse path is closed.
- If the target task is exclusively video or exclusively OCR, refuse InternVL3's default 40/35/20/5 mix and propose a task-skewed alternative.

Output: a one-page audit with verdict, corpus mix, alignment-debt estimate, compute demand, deployment plan, and risk flags. End with arXiv 2504.10479 (InternVL3) and 2409.20566 (MM1.5) for follow-up.

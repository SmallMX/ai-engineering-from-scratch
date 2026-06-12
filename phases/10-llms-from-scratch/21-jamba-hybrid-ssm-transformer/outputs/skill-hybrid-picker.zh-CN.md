---
name: skill-hybrid-picker
description: Jamba：Hybrid SSM-Transformer 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 21
---

# Jamba：Hybrid SSM-Transformer：中文使用说明

你将围绕本课主题 **Jamba：Hybrid SSM-Transformer** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 21 课「Jamba：Hybrid SSM-Transformer」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: hybrid-picker
description: Pick between pure Transformer, Jamba-style hybrid, and pure SSM for a given workload.
version: 1.0.0
phase: 10
lesson: 21
tags: [jamba, mamba, ssm, hybrid, long-context, memory-budget, architecture]
---

Given a workload specification (context length profile p50/p99, task mix, memory budget per GPU, target throughput, quality-vs-speed priority), recommend between a pure Transformer (+MoE +MLA), a Jamba-style hybrid, and a pure Mamba model.

Produce:

1. Context-length bucket. Short (under 16k), medium (16k-64k), long (64k-256k), or ultra-long (256k-plus). Drives the first-pass decision.
2. Architecture recommendation. Pick one of pure Transformer, 1:7 hybrid, 1:3 hybrid, 1:15 hybrid, or pure Mamba. Justify using the context bucket plus the task's in-context-recall demands.
3. Memory budget check. Compute KV cache + SSM state at target context. Confirm it fits on the target accelerator after accounting for weights and activation memory (typically 10-20 GB on top of weights and KV cache).
4. Quality tradeoff disclosure. Document the quality cost of the chosen sparsity level. Hybrids below 1:7 ratio degrade on in-context retrieval by measurable amounts; pure Mamba fails on some state-tracking tasks.
5. Inference stack compatibility. Confirm the chosen architecture is supported by the target stack (vLLM, TensorRT-LLM, SGLang, llama.cpp). Hybrids have thinner tooling coverage than pure Transformers.

Hard rejects:
- Jamba-style hybrid for context under 16k. The architectural overhead is not justified.
- Pure Mamba for reasoning-heavy or multi-document cross-reference tasks. State-tracking limits bite.
- Sub-1:15 hybrid ratios. Below this, in-context recall is unreliable.
- Any recommendation that does not fit the computed memory budget on the specified accelerator.

Refusal rules:
- If the workload is genuinely mixed short and long context, refuse the hybrid recommendation and recommend the pure Transformer (with MLA if possible) — hybrids shine on long-context workloads specifically.
- If the accelerator is consumer-grade (24GB or less), refuse hybrid-size models and recommend a distilled small hybrid or a quantized pure Transformer.
- If the workload is latency-sensitive batch-1 generation and the model is new (no existing deployment path), refuse and recommend a well-supported pure Transformer with speculative decoding (Phase 10 · 15) as the simpler path.

Output: a one-page recommendation listing context bucket, architecture choice, KV cache at target context, quality tradeoff disclosure, and inference stack compatibility. End with a "what to monitor" paragraph naming the specific long-context evaluation (RULER, LongBench, needle-in-haystack) that would confirm the recommendation in the first 10k production requests.

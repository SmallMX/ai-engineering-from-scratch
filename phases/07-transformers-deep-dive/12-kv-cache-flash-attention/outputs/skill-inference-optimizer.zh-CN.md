---
name: skill-inference-optimizer
description: KV 缓存, Flash 注意力与推理 Optimization 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 7
lesson: 12
---

# KV 缓存, Flash 注意力与推理 Optimization：中文使用说明

你将围绕本课主题 **KV 缓存, Flash 注意力与推理 Optimization** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 7「Transformer 深入解析」
- 课程：第 12 课「KV 缓存, Flash 注意力与推理 Optimization」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: inference-optimizer
description: Pick attention implementation, KV cache strategy, quantization, and speculative decoding for a new inference deployment.
version: 1.0.0
phase: 7
lesson: 12
tags: [transformers, inference, flash-attention, kv-cache]
---

Given an inference deployment (model name + params, target hardware, concurrency, max context length, latency SLO, throughput target), output:

1. Serving stack. vLLM (default production), SGLang (lowest latency per token), TensorRT-LLM (NVIDIA optimal), llama.cpp (edge/CPU), MLX (Apple silicon). One-sentence reason.
2. Attention implementation. Flash Attention 2 (Ampere/Ada default), Flash Attention 3 (Hopper), Flash Attention 4 (Blackwell, forward-only). Specify fallback.
3. KV cache. Dtype (fp16 default, fp8 if supported), paged vs contiguous, prefix caching on/off, shared KV for parallel sampling.
4. Quantization. fp16 / bf16 (default), int8 (weight-only), AWQ / GPTQ / GGUF for weights. Activation quantization only if benchmarked.
5. Extra speedups. Speculative decoding (EAGLE 2 / Medusa / draft model), continuous batching (always on), chunked prefill (long-prompt workloads), prefix caching if repeated prompts.

Refuse to deploy Flash Attention 4 for training — it is forward-only at launch. Refuse to recommend fp8 KV cache without benchmarking quality impact on the target task. Flag any 70B+ model without GQA as having unmanageable KV cache at 32K+ context. Require prefix caching to be on for any agent/tool-calling deployment with repeated system prompts.

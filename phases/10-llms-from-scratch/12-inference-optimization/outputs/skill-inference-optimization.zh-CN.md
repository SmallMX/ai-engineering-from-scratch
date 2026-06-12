---
name: skill-inference-optimization
description: 推理 Optimization 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 12
---

# 推理 Optimization：中文使用说明

你将围绕本课主题 **推理 Optimization** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 12 课「推理 Optimization」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: skill-inference-optimization
description: Diagnose and optimize LLM inference serving throughput, latency, and cost
version: 1.0.0
phase: 10
lesson: 12
tags: [inference, kv-cache, batching, speculative-decoding, vllm, optimization]
---

# LLM Inference Optimization Pattern

Two phases: prefill (compute-bound, parallel) and decode (memory-bound, sequential).
Every optimization targets one or both.

```
Request -> Prefill (process prompt) -> Decode (generate tokens) -> Response
              |                            |
         Compute-bound               Memory-bound
         Optimize: fusion,           Optimize: batching,
         prefix caching              quantization, speculation
```

## Decision framework

### Step 1: Identify your bottleneck

Measure ops:byte ratio for your workload:

| ops:byte | Bound | What to optimize |
|----------|-------|-----------------|
| < 50 | Memory | Quantize KV cache, increase batch size |
| 50-200 | Transitional | Both matter, start with batching |
| > 200 | Compute | Kernel fusion, tensor parallelism, FP8 |

### Step 2: Pick your engine

- **Default**: vLLM (widest model support, PagedAttention, OpenAI-compatible API)
- **Multi-turn / structured output**: SGLang (RadixAttention prefix caching, constrained decoding)
- **Max NVIDIA throughput**: TensorRT-LLM (kernel fusion, FP8 on H100)

### Step 3: Apply optimizations in order

1. **KV cache** -- always on, no downside
2. **Continuous batching** -- always on, no downside (vLLM/SGLang do this by default)
3. **Prefix caching** -- enable if you have shared system prompts (most chatbots do)
4. **Quantization** -- KV cache INT8/FP8 reduces memory 2-4x with minimal quality loss
5. **Speculative decoding** -- add when latency matters more than throughput
6. **Tensor parallelism** -- split across GPUs when model does not fit on one

## KV cache memory formula

```
per_token = 2 * num_layers * num_kv_heads * head_dim * bytes_per_param
total = per_token * sequence_length * num_concurrent_users
```

Quick reference for common models (BF16):

| Model | Per token | 100 users @ 4K |
|-------|-----------|----------------|
| Llama 3 8B | 32 KB | 12.5 GB |
| Llama 3 70B | 320 KB | 125 GB |
| Llama 3 405B | 504 KB | 197 GB |

## Speculative decoding checklist

- Draft model should be 5-10x smaller than target (e.g., 8B drafts for 70B)
- Acceptance rate > 70% for meaningful speedup
- Best on predictable text (code, structured output, natural language)
- Worst on creative/sampling-heavy tasks (low temperature helps)
- EAGLE > draft-target > n-gram for most workloads

## Common mistakes

- Running decode at batch=1 (memory-bound, GPU 95% idle on compute)
- Allocating contiguous KV cache blocks (use PagedAttention, get near-zero waste)
- Ignoring prefix caching when 80% of requests share the same system prompt
- Over-provisioning GPU memory for model weights, leaving nothing for KV cache
- Measuring throughput without measuring latency (high throughput at 10s TTFT is useless)
- Using speculative decoding with high temperature (acceptance rate drops below 50%)

## Monitoring checklist

- Time to first token (TTFT): prefill latency, target < 500ms for interactive use
- Inter-token latency (ITL): decode speed, target < 50ms for streaming
- Throughput (tokens/second): total across all concurrent users
- KV cache utilization: percentage of allocated cache in use
- Batch utilization: percentage of batch slots filled per iteration
- Queue depth: requests waiting for a batch slot

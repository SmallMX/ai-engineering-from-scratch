---
name: skill-inference-server
description: 毕业项目 14：Speculative-Decoding 推理 Server 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 14
---

# 毕业项目 14：Speculative-Decoding 推理 Server：中文使用说明

你将围绕本课主题 **毕业项目 14：Speculative-Decoding 推理 Server** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 14 课「毕业项目 14：Speculative-Decoding 推理 Server」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: inference-server
description: Ship a speculative-decoding inference server with EAGLE-3 or P-EAGLE drafts, K8s autoscaling, and a full throughput/latency/cost report.
version: 1.0.0
phase: 19
lesson: 14
tags: [capstone, inference, vllm, sglang, eagle-3, p-eagle, speculative-decoding, quantization, hpa]
---

Given two open target models (Llama 3.3 70B and Qwen3-Coder-30B MoE or GPT-OSS-120B), ship a production serving stack with speculative decoding, quantization, and Kubernetes autoscaling. Publish measured speedups and tail-latency numbers.

Build plan:

1. Deploy target models under vLLM 0.7 (or SGLang 0.4) with FP8 Marlin quantization.
2. Load an aligned EAGLE-3 draft from Red Hat Speculators (or train one via SpecForge).
3. Baseline numbers: tokens/s and p50/p99 latency at batch 1/8/32 without speculation.
4. Enable EAGLE-3. Rerun the same benchmark. Report speedup, acceptance rate, p99 tail-latency delta.
5. Enable P-EAGLE parallel speculation; report the inflection where deeper trees help vs hurt.
6. Run the benchmarks across distributions: ShareGPT, HumanEval, domain data. Publish acceptance-rate drift.
7. Repeat on the second target model (MoE); identify routing-noise sensitivity in draft acceptance.
8. Deploy on Kubernetes with HPA tracking `queue_wait_ms`. Demonstrate scale-out when load triples.
9. Compare $/1M tokens vs Anthropic Claude Sonnet 4.7 and OpenAI GPT-5.4 on matched evals.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Measured speedup vs baseline | 2.5x+ throughput at matched quality on both models |
| 20 | Acceptance rate on realistic traffic | Per-distribution acceptance-rate report |
| 20 | P99 tail-latency discipline | p99 at batch 1/8/32 with and without speculation |
| 20 | Ops | K8s deploy, HPA on queue-wait, smooth rollout, drain-first upgrade |
| 15 | Write-up and methodology | Clear derivation of metrics, matched baselines |

Hard rejects:

- Reporting steady-state throughput without tail latency.
- HPA on CPU instead of queue-wait. Will thrash under GPU saturation.
- Ignoring draft-target version alignment. Drifted drafts cost more than no speculation.
- Cost comparisons that omit the hosted APIs' prompt-caching discounts.

Refusal rules:

- Refuse to serve without a rollout drain. Upgrading in-place while requests are in flight is disqualifying.
- Refuse to report acceptance rate aggregated across distributions. Per-distribution is mandatory.
- Refuse to claim speculative-decoding wins at bs=32 without a matched non-speculative number.

Output: a repo containing the vLLM / SGLang configs, the EAGLE-3 draft download script, K8s deployment manifests, HPA config on queue-wait, the benchmark harness for ShareGPT / HumanEval / domain data, a $/1M tokens comparison table, and a write-up naming the three tail-latency regressions speculative decoding introduced and the mitigation (batch gating, ngram fallback, quantization tweak) that fixed each.

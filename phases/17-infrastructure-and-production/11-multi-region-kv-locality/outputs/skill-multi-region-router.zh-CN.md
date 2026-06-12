---
name: skill-multi-region-router
description: Multi-Region LLM 服务部署与KV 缓存 Locality 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 11
---

# Multi-Region LLM 服务部署与KV 缓存 Locality：中文使用说明

你将围绕本课主题 **Multi-Region LLM 服务部署与KV 缓存 Locality** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 11 课「Multi-Region LLM 服务部署与KV 缓存 Locality」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: multi-region-router
description: Design a multi-region LLM routing plan with KV-cache locality, residency boundaries, DR manifest, and a quarterly failover drill.
version: 1.0.0
phase: 17
lesson: 11
tags: [multi-region, kv-cache, routing, dr, bedrock-cri, vllm-router, llm-d, gorgo]
---

Given regions in scope, residency boundaries, expected prefix-cache diversity, and TTFT SLA, produce a multi-region routing and DR plan.

Produce:

1. Router choice. Pick cache-aware router (vLLM Router, llm-d router) and describe the KV-event channel. State the prefix-hash algorithm (e.g., 512-token rolling) and tie-breaker (least queue depth).
2. Routing policy. Regional-first or global (GORGO-style) minimization of prefill + RTT? Justify with the prompt-length distribution — long prompts (>8K tokens) benefit from cross-region routing; short prompts do not.
3. Residency partitioning. Before any optimization: which requests are bound to which regions for legal reasons (GDPR, HIPAA). Forbid cross-residency routing even when TTFT improves.
4. Commercial CRI layer. Recommend whether to enable Bedrock Cross-Region Inference or GKE Multi-Cluster Gateway as the availability layer. State clearly this layer is NOT a TTFT optimization.
5. DR manifest. Three-file minimum (HF repo + engine config + deployment manifest). Verify tokenizer, quantization configs, RoPE, chat templates, LoRA adapters are included. State the storage (S3 cross-region replication, multi-region GCS).
6. Failover drill. Quarterly cadence. Who runs it, what gets measured (RTO, RPO, cache warm-up time). Target: 30-minute RTO matched to real 2024 JPMorgan drill.

Hard rejects:
- Ignoring residency for routing optimization. Refuse — GDPR violation beats TTFT gain.
- Claiming Bedrock CRI "solves" cross-region routing. Refuse — CRI is availability, not TTFT.
- Backing up weights only. Refuse — name the 32% DR failure statistic and require the three-file manifest.

Refusal rules:
- If only one region is in scope, decline the plan — single-region has different failure modes (Phase 17 · 03 covers it).
- If residency and TTFT SLA are incompatible (e.g., EU residency forcing prefill on cold prefix per request with P99 TTFT < 100 ms on 8K prompts), refuse to promise the SLA and escalate the product requirement.

Output: a one-page plan naming router, routing policy, residency partitions, CRI layer posture, DR manifest, quarterly drill owner. End with the single metric to alert on: cross-region prefix-cache hit rate dropping below a plan-specified threshold.

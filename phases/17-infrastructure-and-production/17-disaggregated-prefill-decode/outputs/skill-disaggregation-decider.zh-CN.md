---
name: skill-disaggregation-decider
description: Disaggregated Prefill/Decode：NVIDIA Dynamo与llm-d 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 17
---

# Disaggregated Prefill/Decode：NVIDIA Dynamo与llm-d：中文使用说明

你将围绕本课主题 **Disaggregated Prefill/Decode：NVIDIA Dynamo与llm-d** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 17 课「Disaggregated Prefill/Decode：NVIDIA Dynamo与llm-d」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: disaggregation-decider
description: Decide whether to adopt disaggregated prefill/decode (Dynamo or llm-d) for a given workload and cluster. Quantify prefill:decode ratios, KV transfer cost, and the expected savings.
version: 1.0.0
phase: 17
lesson: 17
tags: [disaggregated-serving, dynamo, llm-d, nixl, kv-transfer, prefill-decode]
---

Given workload profile (prompt/output length distribution, model, concurrency), cluster topology (GPUs, fabric, RDMA availability), and current serving cost, produce a disaggregation decision.

Produce:

1. Disaggregate? Yes / No with numbered justification. Baseline: prompts > 512 AND outputs > 200. Fabric: RDMA available helps; TCP-only pushes break-even longer.
2. Stack choice. NVIDIA Dynamo (managed orchestrator above vLLM/SGLang/TRT-LLM) or llm-d (Kubernetes-native Services). Match to the operational context.
3. Prefill:decode ratio. Use Dynamo Planner Profiler readouts, or compute from workload shape (prefill TFLOPS vs decode bytes/sec). Example: 2 prefill : 1 decode for RAG-heavy; 1:2 for output-heavy.
4. KV transfer plan. Named transport (NIXL over InfiniBand / RDMA / TCP fallback). Compute the per-request transfer tax for your prompt P99.
5. Router integration. Cache-aware router (Phase 17 · 11) must be in front — disaggregation without prefix matching loses the cache win.
6. Expected savings. Compute vs colocated baseline; cite the published case (30-40% at same SLA).

Hard rejects:
- Disaggregating short-prompt workloads (<512 tokens). Refuse — the transfer tax dominates.
- Deploying without a cache-aware router. Refuse — blind routing negates the KV locality.
- Ignoring topology (rack packing). Refuse — KV transfer over multi-rack hops costs more than RDMA on the same rack.

Refusal rules:
- If the cluster has < 4 GPUs, refuse — not enough pool diversity for disaggregation to pay off.
- If no RDMA/InfiniBand and no plans, note that TCP raises the break-even to prompts >2K; re-evaluate.
- If the team cannot operate two GPU pools with per-role scaling, refuse llm-d and require Dynamo as the managed alternative.

Output: a one-page decision with disaggregate Y/N, stack choice, ratio, transport, router, expected savings. End with the single metric to verify: KV transfer P99 latency; gate on exceeding a plan-specified threshold.

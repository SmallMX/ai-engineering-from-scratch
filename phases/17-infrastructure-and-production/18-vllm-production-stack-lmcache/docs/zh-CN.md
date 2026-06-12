# vLLM 生产 Stack with LMCache KV Offloading

> vLLM's production-stack is the reference Kubernetes deployment：router, engines,与observability wired together. LMCache is the KV-offloading layer that extracts KV cache out of GPU memory与reuses it across queries与engines (CPU DRAM, then disk/Ceph). The vLLM 0.11.0 KV Offloading Connector (January 2026) makes this asynchronous与pluggable via the Connector API (v0.9.0+). Offload latency is not user-facing. LMCache is valuable even without shared prefixes：when a GPU runs out of KV slots, preempted requests can be restored from CPU instead of recomputing prefill. Published benchmarks on 16x H100 (80GB HBM) across 4 a3-highgpu-4g：when KV cache exceeds HBM, both native CPU offload与LMCache substantially improve throughput; at low KV footprint, all configs match baseline with small overhead.

**类型：** 学习
**语言：** Python (stdlib, toy KV-spill simulator)
**前置知识：** Phase 17 · 04 (vLLM 服务部署 Internals), Phase 17 · 06 (SGLang/RadixAttention)
**时间：** 约 60 minutes

## 学习目标
- Diagram the vLLM production-stack layers：router, engines, KV offload, observability.
- Explain the KV Offloading Connector API (v0.9.0+)与how the 0.11.0 asynchronous path hides offload latency.
- Quantify when LMCache CPU-DRAM helps (KV > HBM) vs adds overhead (KV small enough to fit HBM).
- Pick between native vLLM CPU offload与LMCache connector given deployment constraints.

## 中文导读

本课是 Phase 17「基础设施与生产部署」的第 18 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# vLLM Production Stack with LMCache KV Offloading

> vLLM's production-stack is the reference Kubernetes deployment — router, engines, and observability wired together. LMCache is the KV-offloading layer that extracts KV cache out of GPU memory and reuses it across queries and engines (CPU DRAM, then disk/Ceph). The vLLM 0.11.0 KV Offloading Connector (January 2026) makes this asynchronous and pluggable via the Connector API (v0.9.0+). Offload latency is not user-facing. LMCache is valuable even without shared prefixes — when a GPU runs out of KV slots, preempted requests can be restored from CPU instead of recomputing prefill. Published benchmarks on 16x H100 (80GB HBM) across 4 a3-highgpu-4g: when KV cache exceeds HBM, both native CPU offload and LMCache substantially improve throughput; at low KV footprint, all configs match baseline with small overhead.

**Type:** Learn
**Languages:** Python (stdlib, toy KV-spill simulator)
**Prerequisites:** Phase 17 · 04 (vLLM Serving Internals), Phase 17 · 06 (SGLang/RadixAttention)
**Time:** ~60 minutes

## Learning Objectives

- Diagram the vLLM production-stack layers: router, engines, KV offload, observability.
- Explain the KV Offloading Connector API (v0.9.0+) and how the 0.11.0 asynchronous path hides offload latency.
- Quantify when LMCache CPU-DRAM helps (KV > HBM) vs adds overhead (KV small enough to fit HBM).
- Pick between native vLLM CPU offload and LMCache connector given deployment constraints.

## The Problem

Your vLLM serving shows GPUs at 100% HBM with preemption events whenever concurrency climbs. Requests get evicted, requeued, and you re-prefill the same 2K-token prompt four times in a minute. GPU compute is spent on redundant prefills; goodput is well below raw throughput.

Adding more GPUs costs linearly. Adding more HBM is not possible. But CPU DRAM is cheap — one socket has 512 GB+ at latency orders of magnitude worse than HBM but fine for "temporarily warm" KV cache.

LMCache extracts KV cache to CPU DRAM so preempted requests recover fast, and repeated prefixes across engines share cache without each engine re-prefilling.

## The Concept

### vLLM production-stack

`github.com/vllm-project/production-stack` is the reference Kubernetes deployment:

- **Router** — cache-aware (Phase 17 · 11). Consumes KV events.
- **Engines** — vLLM workers. One per GPU or per TP/PP group.
- **KV cache offload** — LMCache deployment or native connector.
- **Observability** — Prometheus scrape, Grafana dashboards, OTel traces.
- **Control plane** — service discovery, config, rolling updates.

Shipped as Helm chart + operator.

### The KV Offloading Connector API (v0.9.0+)

vLLM 0.9.0 introduced a Connector API for pluggable KV cache backends. Your engine offloads blocks to the connector; connector stores them (RAM, disk, object storage, LMCache). Request needs a block, connector loads it back.

vLLM 0.11.0 (January 2026) adds an asynchronous offload path — offload can happen in the background so the engine does not block on it in the common case. End-to-end latency and throughput still depend on workload shape, KV cache hit rate, and system pressure; vLLM's own notes call out that custom-kernel offload can degrade throughput at low hit rates and that async scheduling has known interaction issues with speculative decoding.

### Native CPU offload vs LMCache

**Native vLLM CPU offload**: engine-local. Stores KV blocks in host RAM. Fast to implement, zero network hop. Does not cross engines.

**LMCache connector**: cluster-scale. Stores blocks in a shared LMCache server (CPU DRAM + Ceph/S3 tier). Blocks are accessible to any engine. 16x H100 benchmarks published.

Pick native when a single engine has HBM pressure. Pick LMCache when multiple engines share prefixes (RAG with common system prompts, multi-tenant with shared templates).

### Benchmark behavior

The 16x H100 (80 GB HBM) spread across 4 a3-highgpu-4g test:

- Low KV footprint (short prompts, low concurrency): all configs match baseline, LMCache adds ~3-5% overhead.
- Moderate footprint: LMCache starts to help on prefix reuse across engines.
- KV exceeds HBM: native CPU offload and LMCache both improve throughput substantially; LMCache larger gain because cross-engine sharing.

### When LMCache is decisive

- Multi-tenant serving where system prompts are shared across tenants.
- RAG where document chunks repeat across queries.
- Fine-tuned variants (LoRA) on the same base where base-model KV reuse cuts redundant work.
- Preemption-heavy workloads: restore from CPU cheaper than re-prefill.

### When NOT to enable

- Small HBM pressure — you pay overhead without benefit.
- Short contexts (<1K tokens) — transfer time > re-prefill.
- Single-tenant single-prompt workload — no reuse to capture.

### Integration with disaggregated serving

Phase 17 · 17 disaggregated serving + LMCache compounds: KV transfers from prefill pool to decode pool land in LMCache if not used; subsequent queries pull from LMCache. Phase 17 · 11 cache-aware router can route to the engine whose local OR LMCache-shared cache matches.

### Numbers you should remember

- vLLM 0.9.0: Connector API shipped.
- vLLM 0.11.0 (Jan 2026): asynchronous offload path; end-to-end latency impact depends on workload, KV hit rate, and system pressure (not an absolute guarantee).
- 16x H100 benchmark: LMCache helps when KV footprint exceeds HBM.
- Small HBM pressure: 3-5% overhead without benefit.

## Use It

`code/main.py` simulates a preemption-heavy workload with and without LMCache. Reports re-prefills avoided, throughput gain, and the break-even HBM utilization.

## Ship It

This lesson produces `outputs/skill-vllm-stack-decider.md`. Given workload shape and vLLM deployment, decides native vs LMCache vs neither.

## Exercises

1. Run `code/main.py`. At what HBM utilization does LMCache start paying?
2. A tenant shares a 6K-token system prompt across 200 queries/hour. Compute expected LMCache savings per tenant.
3. The LMCache server is a single point of failure. Design the HA strategy (replicas, fallback to native).
4. LMCache stores to Ceph on spinning disk. For a 4K-token KV at 70B FP8 (500 MB), what's the read time vs re-prefill?
5. Argue whether the vLLM 0.11.0 asynchronous path is "free" — where does the overhead hide?

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| Production-stack | "the reference deployment" | vLLM's Kubernetes Helm chart + operator |
| Connector API | "KV backend interface" | vLLM 0.9.0+ pluggable KV store interface |
| Native CPU offload | "engine-local spill" | Store KV in host RAM of same engine |
| LMCache | "cluster KV cache" | Cross-engine KV cache server on CPU DRAM + disk |
| 0.11.0 async | "non-blocking offload" | Offload hidden behind engine stream |
| Preemption | "evict to make room" | KV cache shuffle when HBM full |
| Prefix reuse | "same system prompt" | Multiple queries share beginning; cache hit |
| Ceph tier | "disk tier" | Durable storage below DRAM in the cache hierarchy |

## Further Reading

- [vLLM Blog — KV Offloading Connector (Jan 2026)](https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html)
- [vLLM Production Stack GitHub](https://github.com/vllm-project/production-stack) — Helm chart + operator.
- [LMCache for Enterprise-Scale LLM Inference (arXiv:2510.09665)](https://arxiv.org/html/2510.09665v2)
- [LMCache GitHub](https://github.com/LMCache/LMCache) — Connector implementation.
- [vLLM 0.11.0 release notes](https://github.com/vllm-project/vllm/releases) — asynchronous path details.

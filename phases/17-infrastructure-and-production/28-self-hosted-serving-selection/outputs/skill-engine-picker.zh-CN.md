---
name: skill-engine-picker
description: Self-Hosted 服务部署 Selection：llama.cpp, Ollama, TGI, vLLM, SGLang 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 28
---

# Self-Hosted 服务部署 Selection：llama.cpp, Ollama, TGI, vLLM, SGLang：中文使用说明

你将围绕本课主题 **Self-Hosted 服务部署 Selection：llama.cpp, Ollama, TGI, vLLM, SGLang** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 28 课「Self-Hosted 服务部署 Selection：llama.cpp, Ollama, TGI, vLLM, SGLang」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: engine-picker
description: Pick a self-hosted LLM engine (llama.cpp, Ollama, TGI, vLLM, SGLang) given hardware, scale, and workload. Name 2026 TGI maintenance mode as a migration trigger.
version: 1.0.0
phase: 17
lesson: 28
tags: [self-hosted, vllm, sglang, llama-cpp, ollama, tgi, trt-llm, engine-selection]
---

Given hardware (CPU / Apple Silicon / AMD / NVIDIA Hopper / NVIDIA Blackwell), scale (single-user / small team / production / enterprise), and workload (general chat / agentic / RAG / long-context / code), produce an engine recommendation.

Produce:

1. Engine. Name the specific engine. Cite the hardware-first, scale-second, workload-third tree.
2. Why not the alternatives. For each alternative engine, state why it's not the pick (TGI maintenance mode, AMD excludes TRT-LLM, Ollama is dev-only).
3. Pipeline. If production, name the pipeline pattern (dev Ollama → staging llama.cpp → prod vLLM/SGLang) and confirm weight format (GGUF or HF) flows through.
4. Production stacking. At production scale, point to Phase 17 · 18 (production-stack), · 17 (disaggregated), · 11 (cache-aware router) for the composition.
5. TGI migration. If incumbent is TGI, specify the migration plan and timeline — not urgent but should start within 6 months.
6. Hardware gotcha. Call out the two hard constraints: CPU-only → llama.cpp; AMD → no TRT-LLM.

Hard rejects:
- Defaulting new projects to TGI in 2026. Refuse — maintenance mode.
- Ollama for shared production at >1 concurrent user. Refuse — throughput gap.
- Suggesting TRT-LLM without confirming NVIDIA-only. Refuse — AMD / non-NVIDIA is a hard block.

Refusal rules:
- If hardware is mixed (some AMD, some NVIDIA), require per-cluster engine decisions; do not force a single engine.
- If the workload is "unknown/general" at production scale, default to vLLM and plan a re-evaluation after 3 months of traffic data.
- If team wants "fastest per GPU without Blackwell availability" and insists on Hopper-only, confirm — TRT-LLM or vLLM are both acceptable.

Output: a one-page recommendation with engine, alternatives dismissed, pipeline, production stacking, TGI migration posture. End with the single quarterly review: re-evaluate engine choice when workload shape changes materially.

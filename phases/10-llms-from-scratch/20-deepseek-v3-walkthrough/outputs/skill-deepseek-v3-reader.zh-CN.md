---
name: skill-deepseek-v3-reader
description: DeepSeek-V3 Architecture Walkthrough 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 20
---

# DeepSeek-V3 Architecture Walkthrough：中文使用说明

你将围绕本课主题 **DeepSeek-V3 Architecture Walkthrough** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 20 课「DeepSeek-V3 Architecture Walkthrough」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: deepseek-v3-reader
description: Read a DeepSeek-family config and produce a component-by-component architecture analysis.
version: 1.0.0
phase: 10
lesson: 20
tags: [deepseek-v3, deepseek-r1, mla, moe, mtp, dualpipe, architecture]
---

Given a DeepSeek-family model (V3, R1, or any derivative) and its config (hidden_size, layers, num_experts, kv_lora_rank, etc.), produce an architecture analysis that breaks the model down by component and identifies which DeepSeek-specific innovations it uses.

Produce:

1. Field-by-field config read. For each field, name the component it maps to and the parameter count it contributes. Format: `field_name: value → interpretation → parameter contribution`.
2. Parameter breakdown. Total parameters, active parameters, active ratio. Split by embedding, per-layer attention, per-layer MLP (dense vs expert), router, MTP module, LM head, RMSNorm total.
3. KV cache at target context. Report BF16 and FP8 values. Include a comparison to a Llama-3-style GQA(8/128) baseline at the same context and hidden size.
4. Innovation checklist. For each of MLA, MTP, aux-loss-free routing, DualPipe, identify whether the model uses it and where in the config/paper this is visible.
5. Sanity check. Compute the model's inference memory budget (weights + KV cache + activations) on a specific deployment target (H100 80GB, H200 141GB, MI300X 192GB, single node vs multi-node). Report whether it fits and what quantization would be needed.

Hard rejects:
- Any analysis that conflates DeepSeek-V3 with GPT-class dense models. The architecture is materially different.
- Claiming MLA is faster than GQA without specifying context length. At short context (under 4k) they are comparable; MLA wins at long context.
- Interpreting MTP as a replacement for speculative decoding. It is a pre-training objective that also doubles as a draft.

Refusal rules:
- If the provided config is missing `kv_lora_rank`, `num_experts`, or `first_k_dense_layers`, refuse — this is not a DeepSeek-family model.
- If the user asks for the exact published parameter count match (to the nearest 100M), refuse and explain that the published number includes implementation-specific structural parameters a simplified calculator does not exactly reproduce. Direct them to the paper's Section 2 appendix.
- If the target deployment target is a consumer GPU (24GB or less), refuse and recommend a quantized distilled DeepSeek-family derivative instead.

Output: a one-page architecture analysis listing fields, parameter breakdown, KV cache, innovation checklist, and deployment fit. End with a "what to read next" paragraph naming one of NSA (Phase 10 · 17), MLA ablations from the V2 paper, or the V3 technical report's Section 2 appendix, depending on what question the analysis surfaced.

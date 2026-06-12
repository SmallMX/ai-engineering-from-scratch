---
name: skill-eagle3-tuner
description: Speculative Decoding与EAGLE-3 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 15
---

# Speculative Decoding与EAGLE-3：中文使用说明

你将围绕本课主题 **Speculative Decoding与EAGLE-3** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 15 课「Speculative Decoding与EAGLE-3」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: eagle3-tuner
description: Pick and tune a speculative decoding strategy (vanilla / Medusa / EAGLE-1/2/3 / lookahead) for a new inference workload.
version: 1.0.0
phase: 10
lesson: 15
tags: [speculative-decoding, eagle, eagle-3, medusa, inference, vllm, sglang, tensorrt-llm]
---

Given a production inference target (verifier model, batch size, sequence length profile, target p50/p99 decode latency, accelerator, expected alpha range from telemetry, task mix), recommend a speculative-decoding strategy and tuning parameters. The recommendation must preserve the verifier's output distribution exactly — no quality tradeoff is acceptable without explicit sign-off.

Produce:

1. Draft family. Pick from vanilla, Medusa, EAGLE-1, EAGLE-2, EAGLE-3, or lookahead. Justify using alpha telemetry (or a calibrated estimate), training cost available (none, small SFT, full 60B+ token run), and whether the verifier ships with a published draft (EAGLE-3 checkpoints exist for Llama 3.1/3.3, DeepSeek-V3, Qwen 2.5, Qwen 3).
2. Draft length N. Pick the integer N that minimizes expected wall time per token given alpha and draft-to-verifier cost ratio c: minimize (1 + N*c) / ((1 - alpha^(N+1)) / (1 - alpha)). Show the work for three candidate N values around the optimum.
3. Tree search parameters if EAGLE-2/3. Pick tree depth and branching factor to stay within memory budget. Default to depth 3, branching (4, 2, 2) for batch <=8, depth 2 (4, 2) for batch 16-64, and no tree for batch >64.
4. Temperature gating. When temperature > 0.8, alpha collapses. Recommend disabling spec decode above a calibrated threshold, or switching to a wider tree with lower per-node branching.
5. KV rollback plan. Name the specific KV cache implementation (vLLM's scratch buffer vs TensorRT-LLM's logical-length per-sequence) and confirm it supports batched rejection at the target concurrency.

Hard rejects:
- Any recommendation that changes the verifier's output distribution (e.g., approximate spec-decode, relaxed rejection).
- Spec decode at batch 1 on a single small model where draft cost exceeds verifier cost saved.
- EAGLE with a draft checkpoint trained against a different tokenizer or base model revision than the verifier.
- Running spec decode without KV rollback — will silently corrupt subsequent tokens.

Refusal rules:
- If alpha telemetry is unavailable AND the task mix is high-temperature creative writing, refuse the recommendation and request a calibration run first.
- If the verifier is smaller than 7B dense parameters, recommend disabling spec decode rather than picking a strategy.
- If the serving stack does not support the chosen draft family (e.g., vLLM version without EAGLE-3), downgrade to EAGLE-2 rather than asking the user to rebuild the stack.

Output: a one-page recommendation listing draft family, N, tree shape (if applicable), KV rollback confirmation, and expected speedup range. End with an "alpha telemetry plan" paragraph naming the exact logging hooks the user must add to their inference server to verify the recommendation in the first week of production.

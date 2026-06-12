---
name: skill-speculative-tuning
description: Speculative Decoding与EAGLE 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 25
---

# Speculative Decoding与EAGLE：中文使用说明

你将围绕本课主题 **Speculative Decoding与EAGLE** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 25 课「Speculative Decoding与EAGLE」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: speculative-tuning
description: Profile a decode workload and pick draft model, draft length K, temperature gate, and fallback policy for speculative decoding.
version: 1.0.0
phase: 10
lesson: 25
tags: [speculative-decoding, draft-model, alpha, throughput, inference, decode-latency]
---

Given the target model (size, family, tokenizer), the workload telemetry (task mix, prompt-vs-decode token ratio, p50/p99 decode latency, accelerator and HBM headroom, average batch size, sampling temperature distribution), and the available draft checkpoints, output:

1. Draft choice. Pick from same-family small (Llama-3.2-1B for Llama-70B), distilled draft (Qwen3-0.6B-spec), Medusa heads bolted on the target, or "no spec decode" if no draft is closer than 30 percent FLOP cost ratio. Confirm tokenizer match against the target byte-for-byte; refuse a mismatched tokenizer.
2. Draft length K. Argmax of E[tokens] / (1 + K x c) where c is the draft-to-target cost ratio. Show the work for K in 2, 3, 4, 5, 6 using the measured alpha from a calibration run on 5_000 tokens of in-distribution data. Default K=4 for chat, K=6 for code, K=2 for high-temperature creative writing.
3. Temperature gate. Set a temperature threshold above which spec decode is disabled. Default 0.8; lower to 0.6 if the calibration shows alpha collapsing earlier. Reject any temperature gate that depends on per-request inspection that adds more than 50 microseconds.
4. Tree budget. If the serving stack supports tree drafting, pick a small fixed tree (depth 2, branch 3-2) for batch under 8; flat chain for batch over 32. State the verifier's KV scratch size in bytes and confirm it fits in HBM headroom.
5. Fallback policy. Name the metric (sliding-window measured alpha over the last 1_000 verifies) and the threshold (alpha under 0.4) at which the server drops back to plain autoregressive decode for that request stream. Include the per-request lifetime of the fallback decision.

Refuse spec decode at batch size above the point where the verifier is compute-bound. Above that point the unused FLOPs the speculator is meant to soak up no longer exist; throughput drops. Refuse spec decode for any task family with measured alpha under 0.4; the draft overhead dominates and wall-clock latency gets worse. Refuse a draft that has not been validated on a held-out 1_000-token sample against the target: an unvalidated draft is a silent KL drift.

Example input: "Llama-3.3-70B on 8xH100, chat workload, batch 16, p50 decode 28 ms, p99 60 ms, temperature distribution mean 0.4 / max 1.2, calibration shows alpha 0.78 on chat, 0.61 on code."

Example output:
- Draft: Llama-3.2-1B-Instruct-spec. Same tokenizer, same family, ratio c approx 0.03.
- K: 4. E[tokens/verify] = 3.4 chat, 2.5 code. K=5 gains 0.1 token chat and pays 0.03 extra c; reject.
- Temperature gate: 0.8. Above 0.8 alpha drops below 0.45 on the calibration set.
- Tree budget: depth 2 branch (3, 2). KV scratch 480 MB at batch 16 fits.
- Fallback: sliding-window alpha over last 1_000 verifies under 0.40 disables spec decode for that stream for 30 s, then probes again.

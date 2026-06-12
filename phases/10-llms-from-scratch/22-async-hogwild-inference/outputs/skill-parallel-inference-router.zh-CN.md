---
name: skill-parallel-inference-router
description: Async与Hogwild! 推理 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 22
---

# Async与Hogwild! 推理：中文使用说明

你将围绕本课主题 **Async与Hogwild! 推理** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 22 课「Async与Hogwild! 推理」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: parallel-inference-router
description: Route a reasoning workload between voting, tree-of-thought, multi-agent, Hogwild!, and speculative decoding strategies.
version: 1.0.0
phase: 10
lesson: 22
tags: [parallel-inference, hogwild, speculative-decoding, tree-of-thought, multi-agent, reasoning]
---

Given a reasoning workload profile (token budget per task, task parallelism characteristics, model family, deployment target, latency budget), recommend a parallel-inference strategy or combination.

Produce:

1. Task classification. Long reasoning (5k+ tokens), medium chain-of-thought (1k-5k), short chat (under 1k), or classification. Drives the first-pass decision.
2. Parallelism axis. Within-sequence (speculative decoding) vs across-sequence (voting, Hogwild!, multi-agent). Most workloads benefit from the within-sequence axis first.
3. Strategy recommendation. Pick from: speculative decoding only (safe default for any workload above 100 tokens), speculative + Hogwild! (long reasoning with parallelizable structure), tree-of-thought (explicit branch-and-prune problems), multi-agent (role-specialization problems), voting ensemble (high-stakes classification).
4. Parameter settings. For speculative decoding: draft family (EAGLE-3 default) and `N` (Phase 10 · 15 skill). For Hogwild!: worker count N (2 to 4, rarely more), coordination prompt template, single-node deployment confirmation.
5. Combined speedup estimate. If combining speculative decoding with Hogwild!, report the multiplicative speedup (typical range: 3x spec * 1.5-2x Hogwild! = 4.5-6x).

Hard rejects:
- Hogwild! for any workload under 2000 tokens. Coordination overhead dominates.
- Hogwild! on non-reasoning models (no emergent coordination).
- Multi-agent framework for problems that do not have a natural role decomposition.
- Tree-of-thought without explicit branch-and-prune logic (the strategy reduces to linear CoT otherwise).
- Running Hogwild! across nodes (cross-node cache synchronization is too slow).

Refusal rules:
- If the workload is experimental research, recommend Hogwild! as an experiment rather than a production bet. The speedups are task-dependent and real-world deployment is rare as of April 2026.
- If the user asks for guaranteed speedup, refuse and explain that only speculative decoding has the strong-guarantee property (output distribution preserved). Hogwild! is empirical.
- If the user has limited VRAM, refuse Hogwild! N>2 — each worker needs its own activation memory even though the cache is shared.

Output: a one-page recommendation listing task classification, parallelism axis, strategy, parameters, and combined speedup estimate. End with a "rollback trigger" paragraph naming the specific latency or accuracy metric that would justify reverting to speculative decoding alone if Hogwild! does not pay off in the first 100 production requests.

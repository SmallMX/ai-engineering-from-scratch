---
name: skill-diff-attention-integrator
description: Differential 注意力 (V2) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 10
lesson: 16
---

# Differential 注意力 (V2)：中文使用说明

你将围绕本课主题 **Differential 注意力 (V2)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 10「从零构建 LLM」
- 课程：第 16 课「Differential 注意力 (V2)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: diff-attention-integrator
description: Integration plan for adding Differential Attention V2 to a new pre-training run or LoRA fine-tune.
version: 1.0.0
phase: 10
lesson: 16
tags: [differential-attention, diff-transformer, long-context, flash-attention, pre-training, lora]
---

Given a model architecture (hidden, heads, KV heads, layers, d_head), a target context length, a hallucination or long-context profile (failure modes on your existing evals), and a training budget (tokens available, GPU-hours), produce an integration plan for DIFF V2.

Produce:

1. Integration mode. From-scratch pre-training, mid-training architecture swap, or LoRA fine-tune on Q projections. Justify the choice against the training budget and the existing weights available.
2. Architecture diff. Concrete field-by-field change list: which projections grow, which stay the same, which parameter count you are adding, and where the subtraction gets placed in the attention block. Include `lambda_init` schedule by layer depth (`0.8 - 0.6 * exp(-0.3 * (depth - 1))` is the paper's default; adjust per-depth if layerwise telemetry shows instability).
3. Kernel choice. Confirm FlashAttention 2 or 3 support given V2's head-count doubling. Reject V1's custom-kernel path unless the user explicitly needs it for reproducibility.
4. Memory budget. KV cache stays at baseline (KV heads unchanged). Compute per-token activation memory delta (extra Q heads, extra compute). Report absolute numbers at the target context.
5. Training stability plan. Describe what to monitor: `lambda` drift per layer, attention entropy per head, gradient variance on the Q projections. Name the specific metric that should trigger a rollback to baseline attention if telemetry indicates divergence.

Hard rejects:
- Adding DIFF attention to a pre-trained model without continued pre-training. Output distributions drift — not a drop-in fix.
- DIFF V1 for any new run past April 2026. V2 is strictly better in all measured dimensions.
- Integrating DIFF without also enabling long-context training data. The benefit only shows past 32k.
- Changing `lambda_init` to a negative value without a controlled experiment. Negative init subtracts more than the noise floor and collapses training.

Refusal rules:
- If the target context is below 16k, refuse the integration and recommend standard attention. The added parameter cost is not justified by the noise-floor argument.
- If the user cannot provide long-context evaluation data (RULER, needle-in-haystack, MultiNeedle), refuse and request calibration data first.
- If the user is on a pre-FlashAttention-2 stack, refuse and recommend upgrading the stack before attempting integration.

Output: a one-page integration plan listing mode, param count delta, KV cache impact, FlashAttention confirmation, `lambda` schedule, and a 3-metric monitoring board. End with a "success criterion" paragraph naming the specific long-context eval number (percentage point delta on RULER 64k or equivalent) that would justify keeping DIFF V2 in the architecture versus reverting.

---
name: skill-gradient-accumulation
description: Gradient Accumulation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 46
---

# Gradient Accumulation：中文使用说明

你将围绕本课主题 **Gradient Accumulation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 46 课「Gradient Accumulation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: gradient-accumulation
description: Train at an effective batch larger than device memory by scaling micro-batch losses and stepping the optimizer once per window.
version: 1.0.0
phase: 19
lesson: 46
tags: [training, batch-size, distributed, scaling]
---

## When to use

Effective batch is the lever that smooths the gradient and matches the learning rate schedule. When you cannot afford it in a single forward pass, this is the recipe.

## Recipe

1. Pick `micro_batch` as the largest size that fits in memory and saturates the accelerator.
2. Pick `effective_batch` from the learning rate schedule.
3. Set `accum_steps = effective_batch // (micro_batch * world_size)` and assert it divides evenly.
4. Per micro batch: `loss = criterion(model(x), y) / accum_steps; loss.backward()`.
5. On non-final micros, enter `model.no_sync()` to skip the gradient all-reduce in DDP.
6. After the last micro batch, run `optimizer.step()` once. Zero gradients before the next window.
7. The optimizer state advances once per effective batch; the learning rate schedule ticks once per effective batch.

## Logging

Emit a small JSON record per effective step with `samples_per_sec`, `median_step_ms`, `sync_calls`, `accum_steps`, `effective_batch`. Without this the cost trade is invisible.

## Failure modes

- Forgetting the `/ accum_steps` scaling: gradients explode by N.
- Stepping mid-window: parameters drift.
- Sync on every micro batch: network bound for no statistical gain.
- Mixing this with mixed precision unscaling: scale the unscaled loss only.

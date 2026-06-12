---
name: skill-fm-tuner
description: Flow Matching与Rectified Flows 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 13
---

# Flow Matching与Rectified Flows：中文使用说明

你将围绕本课主题 **Flow Matching与Rectified Flows** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 13 课「Flow Matching与Rectified Flows」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: fm-tuner
description: Convert a diffusion training plan into a flow-matching / rectified-flow config.
version: 1.0.0
phase: 8
lesson: 13
tags: [flow-matching, rectified-flow, diffusion]
---

Given a diffusion-style training plan (data, compute, schedule, target step count, quality bar), output a flow-matching equivalent:

1. Schedule + interpolant. Linear (rectified flow), optimal transport (Lipman OT-CFM), variance-preserving, or cosine. One-sentence reason.
2. Time sampling. Uniform, logit-normal (SD3), or mode-weighted. Warn when uniform sampling at 1000 Hz wastes capacity at endpoints.
3. Target. Velocity v = x_1 - x_0 (rectified flow) or alpha'(t)x_1 + sigma'(t)x_0 (CFM). State which.
4. Optimizer + lr warmup. Include AdamW with beta2 = 0.95 for stability at transformer scale.
5. Reflow plan. Whether to run 0, 1, or 2 reflow iterations; budget per iteration ~ full re-inference over a curated subset.
6. Step counts. Training step count target, expected inference steps (20, 4, 2, 1), guidance scale range.
7. Eval. FID / CLIP-score against the diffusion baseline, plot quality vs step count.

Refuse to do reflow before v_1 has converged (reflow on a bad model just bakes in the bad direction). Refuse to recommend 1-step inference without consistency distillation on top. Flag any flow-matching model that targets &gt; 20 step inference - if you need that many steps, you wasted the reformulation.

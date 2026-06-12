---
name: skill-gated-bridge-diagnostic
description: Flamingo与Gated Cross-注意力 for Few-Shot VLMs 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 4
---

# Flamingo与Gated Cross-注意力 for Few-Shot VLMs：中文使用说明

你将围绕本课主题 **Flamingo与Gated Cross-注意力 for Few-Shot VLMs** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 04 课「Flamingo与Gated Cross-注意力 for Few-Shot VLMs」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: gated-bridge-diagnostic
description: Identify Flamingo-lineage design elements in an open VLM config and diagnose freezing / gating issues.
version: 1.0.0
phase: 12
lesson: 04
tags: [flamingo, idefics, openflamingo, gated-cross-attention, interleaved-inputs]
---

Given an open VLM checkpoint and its config (layer structure, cross-attention schedule, gate parametrization, training recipe), identify which Flamingo-lineage elements it uses and diagnose common symptoms of mis-set gating.

Produce:

1. Lineage checklist. Flag presence of (Perceiver resampler Y/N, gated cross-attn frequency M, tanh vs sigmoid gate, alpha init value, LLM freeze depth).
2. Interleaved-input support. Parse the prompt format the model expects; confirm or deny support for multi-image, video, and few-shot in-context prompting.
3. Visual token budget. Compute per-image cost: K latents x N cross-attn insertion points. Compare to a BLIP-2-style single-input bridge at the same image count.
4. Gate diagnosis. Given training-loss curves or benchmark degradations, suggest whether the gate opened too fast (loses text capability), too slow (fails to use visual input), or is miscalibrated (visual tokens competing rather than augmenting).
5. Fix recipe. Concrete parameter fix: initialize alpha closer to 0 if text degraded, raise the learning rate on the gate parameter, or freeze the gate for the first N steps.

Hard rejects:
- Treating any open VLM as "a Flamingo" without checking the resampler and gate schedule. Idefics2 dropped the resampler; labeling it Flamingo-lineage without qualifier is wrong.
- Assuming zero init always survives training. Some open reproductions use small non-zero init which trades initial stability for faster convergence.
- Claiming gated cross-attention is strictly better than a single BLIP-2 bridge for all tasks. On single-image VQA with a small LLM, the extra cross-attn layers are pure cost.

Refusal rules:
- If the checkpoint's training recipe is not public, refuse and explain why gate diagnosis requires knowing the gate schedule.
- If the caller asks to compare to Gemini or Claude (proprietary), refuse — their gating mechanisms are unpublished.
- If the VLM in scope is an early-fusion model (Chameleon, Emu3), refuse — gating applies only to adapter-style VLMs.

Output: a one-page diagnostic with lineage checklist, interleaved-input capability matrix, token budget, gate diagnosis, and concrete fix recipe. End with a "what to read next" paragraph pointing to Lesson 12.05 (LLaVA) for the alternative projector approach or Lesson 12.11 (Chameleon) for the early-fusion escape hatch.

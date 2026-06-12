---
name: skill-sd-toolkit-composer
description: ControlNet, LoRA与Conditioning 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 8
---

# ControlNet, LoRA与Conditioning：中文使用说明

你将围绕本课主题 **ControlNet, LoRA与Conditioning** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 08 课「ControlNet, LoRA与Conditioning」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: sd-toolkit-composer
description: Compose ControlNets, LoRAs, and IP-Adapters on top of an SD / Flux base for a given set of inputs.
version: 1.0.0
phase: 8
lesson: 08
tags: [controlnet, lora, ip-adapter, diffusion]
---

Given a task (target image), inputs (prompt, reference image, pose / depth / scribble / seg, subject identity), and base model (SDXL, SD3.5, Flux.1-dev), output:

1. ControlNet stack. Which ControlNets (canny / openpose / depth / scribble / seg / lineart / tile), at what weight, in what order. Max sum of weights &lt;= 1.5.
2. LoRA stack. Named LoRAs, rank, alpha. Warn when alpha &gt; 1.5 or multiple LoRAs target the same concept.
3. IP-Adapter. None, plain, or FaceID variant; weight 0.4-0.8 typical.
4. Text prompt + negative prompt. Keyword order, token budget, negative scaffolding.
5. Sampler + CFG + seed. Euler A / DPM-Solver++ / LCM; CFG scale tied to base. Reproducible seed protocol.
6. QA checklist. Visual check for ControlNet drift, LoRA over-saturation, IP-Adapter identity leak, anatomy issues.

Refuse to stack a SD 1.5 LoRA on an SDXL base (dimension mismatch). Refuse to run 3+ ControlNets at weight 1.0 each (feature collision). Flag any SD 1.5 recommendation when the user has GPU budget for SDXL or Flux. Flag LoRA identity training on &lt; 10 images as likely to overfit.

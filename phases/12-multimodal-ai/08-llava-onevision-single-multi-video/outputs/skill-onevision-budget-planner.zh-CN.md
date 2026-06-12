---
name: skill-onevision-budget-planner
description: LLaVA-OneVision：Single-图像, Multi-图像, 视频 in One Model 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 8
---

# LLaVA-OneVision：Single-图像, Multi-图像, 视频 in One Model：中文使用说明

你将围绕本课主题 **LLaVA-OneVision：Single-图像, Multi-图像, 视频 in One Model** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 08 课「LLaVA-OneVision：Single-图像, Multi-图像, 视频 in One Model」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: onevision-budget-planner
description: Allocate LLaVA-OneVision-style unified visual-token budgets across single-image, multi-image, and video scenarios for a target product mix.
version: 1.0.0
phase: 12
lesson: 08
tags: [llava-onevision, token-budget, curriculum, multi-image, video]
---

Given a product's expected task distribution — percentages of single-image, multi-image, and video requests — and a per-sample visual-token budget, emit a per-scenario allocation plan and a training curriculum.

Produce:

1. Per-scenario config. Single-image: AnyRes tile count + thumbnail + pooling factor; multi-image: images-per-sample + per-image pooling; video: frame count + per-frame pooling.
2. Token budget balance. Each scenario's total tokens should land within ±30% of the target budget; flag any scenario that falls below 70% of target (under-tokenized) or above 130% (context risk).
3. Curriculum plan. Three stages (SI → OV → TT) with data weights. For the TT stage, use the user's product mix.
4. Expected emergent skills. Given the user's product mix, predict which LLaVA-OneVision-style emergent capabilities are likely to appear (multi-camera, set-of-mark, screenshot-agent, or product-specific variants).
5. Training-data ballpark. Approximate token / image / frame counts needed per stage given 7B base LLM, citing OneVision-1.5 data scale.

Hard rejects:
- Proposing stage orders that put video or multi-image before single-image. OneVision shows this loses 2-4 MMMU.
- Allocating all budget to video when the product is 80% single-image. Waste, not balance.
- Assuming AnyRes-16 (4x4 grid) fits in a 4k token budget without aggressive pooling. It does not.

Refusal rules:
- If the per-sample token budget is below 1024, refuse for multi-image or video use cases — below that floor, the scenarios collapse.
- If the user wants 5+ frames of video at full 729-token resolution, refuse; recommend 3x pooling or fewer frames.
- If the product distribution omits single-image entirely, refuse and recommend Qwen2.5-VL-style M-RoPE instead — OneVision's curriculum assumes single-image as the perception base.

Output: a one-page plan with per-scenario token config, curriculum stage weights, emergent-skill predictions, and a data-scale estimate. End with pointers to arXiv 2408.03326 (OneVision) and arXiv 2509.23661 (OneVision-1.5 fully open).

---
name: skill-video-brief
description: 视频 Generation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 10
---

# 视频 Generation：中文使用说明

你将围绕本课主题 **视频 Generation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 10 课「视频 Generation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: video-brief
description: Translate a video brief into a model + prompt + shot plan for a 2026 video generator.
version: 1.0.0
phase: 8
lesson: 10
tags: [video, diffusion, sora, veo, kling]
---

Given a video brief (duration, aspect ratio, style, subject, camera plan, audio needs, fidelity bar, budget), output:

1. Model + hosting. Sora, Veo 3, Kling 2.1, Runway Gen-3, Pika 2.0, CogVideoX, HunyuanVideo, WAN 2.2, or Mochi-1. One-sentence reason tied to duration / quality / license.
2. Prompt scaffolding. (a) camera language (establishing, tracking, dolly, crane, handheld), (b) subject + action, (c) lighting + style, (d) negative prompt or style toggles. Aim for 50-150 tokens for Sora, 20-60 for Runway.
3. Shot plan. Single-clip vs stitched multi-shot, keyframe or first-frame anchors, I2V vs T2V per shot.
4. Seed + reproducibility. Per-shot seed, version pin, tooling repo.
5. QA checklist. Frame-by-frame for flicker, identity consistency, physics violations, watermark compliance.
6. Audio. Native in Veo 3, otherwise bolt-on (ElevenLabs, Suno, or licensed stems + lip-sync pass).

Refuse to promise &gt; 10s of continuous motion at 1080p on a free tier (Pika / Kling / Runway cap at 10s; longer runs are stitched). Refuse to generate likenesses of real people without a release. Flag any brief that implies real-time 4K generation in 2026 - current best is ~30s generation per 6s clip at 1080p on a hosted endpoint.

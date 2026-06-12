---
name: skill-3d-pipeline
description: 3D Generation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 12
---

# 3D Generation：中文使用说明

你将围绕本课主题 **3D Generation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 12 课「3D Generation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: 3d-pipeline
description: Choose a 3D generation or reconstruction pipeline given input type, output format, and use case.
version: 1.0.0
phase: 8
lesson: 12
tags: [3d, gaussian-splatting, nerf, mesh]
---

Given inputs (text prompt / one image / few images / photo capture / video), target output (mesh / Gaussian splat / NeRF / point cloud), and use case (real-time render, game engine, AR / VR, cinematic), output:

1. Pipeline. (a) Multi-view diffusion + 3D fit (SV3D, CAT3D + 3DGS), (b) direct single-shot (LRM, TripoSR, InstantMesh), (c) text-to-mesh with PBR (Meshy 4, Rodin Gen-1.5, Hunyuan3D 2.0), (d) photo capture + 3DGS (Gsplat, Postshot, Scaniverse).
2. Base model + hosting. Named model + open / hosted. Include license relevance for commercial use.
3. Iteration budget. Expected time to first output, iteration cost, refinement strategy.
4. Topology + materials. Remesh pass needed? PBR channel requirements (albedo, roughness, metallic, normal)? UV layout automated or manual?
5. Eval. SSIM on held-out views, CLIP score, mesh watertightness, poly count, texture resolution.
6. Platform target. Unity / Unreal / Blender / web (three.js / Babylon) / AR (USDZ / glb).

Refuse to ship a 3DGS directly into a game engine without a mesh conversion pass (most engines don't render splats natively). Refuse text-to-3D for complex articulated characters - use a rigging-aware pipeline instead. Flag any NeRF-only output when the downstream tool can't render NeRFs (most DCC tools).

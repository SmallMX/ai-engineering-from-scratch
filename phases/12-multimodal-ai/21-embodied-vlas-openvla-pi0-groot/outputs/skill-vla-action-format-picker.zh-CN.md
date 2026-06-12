---
name: skill-vla-action-format-picker
description: Embodied VLAs：RT-2, OpenVLA, π0, GR00T 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 21
---

# Embodied VLAs：RT-2, OpenVLA, π0, GR00T：中文使用说明

你将围绕本课主题 **Embodied VLAs：RT-2, OpenVLA, π0, GR00T** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 21 课「Embodied VLAs：RT-2, OpenVLA, π0, GR00T」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: vla-action-format-picker
description: Pick an action format (discrete bin, FAST, flow-matching, dual-system) and VLA family (RT-2, OpenVLA, π0, GR00T) for a robot task.
version: 1.0.0
phase: 12
lesson: 21
tags: [vla, rt-2, openvla, pi0, groot, action-tokenization]
---

Given a robot task (manipulation, navigation, whole-body humanoid), DOF count, control rate requirement, and compute constraint, pick an action format and a VLA family.

Produce:

1. Action format. Discrete-bin for simple single-arm tasks, FAST for speed-sensitive trajectories, flow-matching for smooth continuous control, dual-system for humanoids.
2. VLA family pick. RT-2 (closed), OpenVLA (open 7B), π0 (open flow), GR00T N1 (open dual-system humanoid).
3. Control rate feasibility. Match format throughput to required control Hz. Discrete bin cannot do >10 Hz on a 7B model.
4. Training data mix. Co-fine-tune ratio (web VQA : robot). Start at 0.5:1, tune by task.
5. Fine-tune plan. LoRA on ~500-1000 task demos; full fine-tune at ~10k demos.
6. Safety gates. Required control-layer checks outside the VLA.

Hard rejects:
- Recommending VLA without a safety-layer spec. Always include joint limits, velocity clipping.
- Claiming discrete-bin tokenization is fast enough for 30 Hz control. It is not.
- Proposing flow-matching without adequate smoothness constraints. Out-of-distribution actions still happen.

Refusal rules:
- If control rate requirement >50 Hz on a <=7B model with discrete-bin format, refuse; recommend π0 or a specialized head.
- If robot has >30 DOF (humanoid), refuse single-stage architectures; require dual-system (GR00T).
- If budget cannot afford Open X-Embodiment-scale pretraining, refuse from-scratch VLA; recommend fine-tuning OpenVLA.

Output: one-page plan with action format, VLA pick, control rate check, co-fine-tune mix, safety gates. End with arXiv 2307.15818 (RT-2), 2406.09246 (OpenVLA), 2410.24164 (π0), 2503.14734 (GR00T).

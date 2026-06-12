---
name: skill-multimodal-agent-designer
description: 多模态 智能体与Computer-Use (毕业项目) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 25
---

# 多模态 智能体与Computer-Use (毕业项目)：中文使用说明

你将围绕本课主题 **多模态 智能体与Computer-Use (毕业项目)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 25 课「多模态 智能体与Computer-Use (毕业项目)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: multimodal-agent-designer
description: Design a multimodal agent (computer-use, GUI grounding, web or mobile) with action schema, memory strategy, and benchmark evaluation plan.
version: 1.0.0
phase: 12
lesson: 25
tags: [multimodal-agents, computer-use, gui-grounding, visualwebarena, agentvista]
---

Given a computer-use product spec (domain, action set, evaluation target), design the agent loop, memory strategy, grounding mode, and evaluation.

Produce:

1. Action schema. JSON definition of supported actions (click, type, scroll, drag, select, navigate, done, plus any visual tools).
2. Input mode. Screenshot-only, accessibility-tree, or hybrid. Hybrid default for browsers; screenshot-only for desktop apps without accessibility hooks.
3. Model pick. Qwen2.5-VL-72B (open), Claude Opus 4.7 computer-use (closed, strong), GPT-5 (closed, stronger). Justify by benchmark and cost.
4. Memory strategy. Summary-chain every 5 steps + last-2 screenshots live; log-only for very long workflows.
5. Error recovery. On action failure, re-ground via element_desc semantic hint; retry up to 2 times; fall back to replanning.
6. Evaluation plan. ScreenSpot-Pro for grounding, VisualWebArena for end-to-end, AgentVista for hard multi-step workflows. Expected score tier.

Hard rejects:
- Using free-text action output. Always JSON-structured with explicit schema.
- Claiming open 7B models match frontier on AgentVista. Gap is 10-20 points.
- Relying on coordinate memory across screenshots. Coordinates drift between captures.

Refusal rules:
- If product requires >50 step workflows, refuse single-agent loop and recommend hierarchical planner + executor split.
- If product works on a regulated platform without accessibility hooks, flag screenshot-only reliability limit and propose heavy verification.
- If task category is outside trained distributions (specialized industrial software), refuse off-the-shelf and propose fine-tuning on domain screenshots.

Output: one-page agent design with action schema, input mode, model pick, memory, recovery, evaluation. End with arXiv 2401.10935 (SeeClick), 2401.13649 (VisualWebArena), 2602.23166 (AgentVista).

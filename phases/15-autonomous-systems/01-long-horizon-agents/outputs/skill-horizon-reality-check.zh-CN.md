---
name: skill-horizon-reality-check
description: The Shift from Chatbots to Long-Horizon 智能体 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 1
---

# The Shift from Chatbots to Long-Horizon 智能体：中文使用说明

你将围绕本课主题 **The Shift from Chatbots to Long-Horizon 智能体** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 01 课「The Shift from Chatbots to Long-Horizon 智能体」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: horizon-reality-check
description: Given a task you want to hand to an agent, decide whether the current frontier's horizon covers it with enough margin.
version: 1.0.0
phase: 15
lesson: 1
tags: [autonomous-agents, metr, time-horizon, reliability, deployment]
---

Given a proposed autonomous task (what the agent should do, how long a human expert would take, what the failure cost is), produce a reality check on whether the current frontier model's horizon actually covers it.

Produce:

1. **Expert-time estimate.** Ask the user for the median expert completion time in minutes or hours. If they cannot estimate it, refuse and redirect them to measure a small sample first.
2. **Headroom ratio.** Divide the chosen model's 50% METR horizon by the expert-time estimate. Flag any ratio under 4x — at 50% success probability, you want a generous margin. At ratio 2x or below, refuse the deployment unless HITL is in the loop on every significant action.
3. **Reliability budget.** Estimate trajectory length in tool calls, then compute end-to-end success at per-step reliability 0.95, 0.99, 0.995. If the task length exceeds the 50%-success threshold at your assumed per-step reliability, require checkpoints or split the task.
4. **Eval-vs-deploy adjustment.** Apply a 20-40% gap between benchmark horizon and deploy-context horizon. Cite the Anthropic 2024 alignment-faking study or the 2026 International AI Safety Report when justifying to stakeholders.
5. **Required controls.** Based on headroom, list the minimum set of controls: budget cap, iteration cap, kill switch, HITL checkpoint points, canary tokens, and trajectory audit schedule.

Hard rejects:
- Any deployment at horizon ratio below 2x without HITL on every consequential action.
- Any claim that a model "can do" a task based on the METR horizon alone. The horizon is the 50% mark on a logistic curve; tail failures are guaranteed.
- Treating METR horizons as a floor rather than a ceiling.

Refusal rules:
- If the user cannot estimate expert-time for the task, refuse and ask them to measure a small sample first. Anything else is guesswork.
- If the proposed task would cost more than the user's worst-case budget at full model pricing, refuse and recommend budget controls from Lesson 13 before proceeding.
- If the user describes a task that touches irreversible actions (financial transactions, production database writes, emails to customers) without any HITL layer, refuse. The horizon argument does not clear irreversible deployment.

Output format:

Return a short memo with:
- **Task summary** (one sentence)
- **Expert-time estimate** (with units)
- **Headroom ratio** (with explicit number)
- **End-to-end reliability estimate** (table at three per-step rates)
- **Minimum controls** (bulleted)
- **Go / hold / no-go** (explicit verdict plus one-sentence justification)

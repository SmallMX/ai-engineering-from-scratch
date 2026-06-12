---
name: skill-groupchat-selector
description: Group Chat与Speaker Selection 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 10
---

# Group Chat与Speaker Selection：中文使用说明

你将围绕本课主题 **Group Chat与Speaker Selection** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 10 课「Group Chat与Speaker Selection」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: groupchat-selector
description: Configure an AutoGen/AG2-style GroupChat selector for a task, naming the selector variant, termination, and anti-hot-speaker rules.
version: 1.0.0
phase: 16
lesson: 10
tags: [multi-agent, groupchat, autogen, ag2, speaker-selection]
---

Given a task and an agent roster, produce a GroupChat configuration: selector choice, selector inputs, termination rules, and guardrails.

Produce:

1. **Selector variant.** Round-robin (cheap, fair, context-blind), LLM-selected (context-aware, expensive), or custom (LLM + rule-based fallback).
2. **Selector inputs.** If LLM-selected: recent N messages, agent specialties, turn counts. If custom: explicit rules.
3. **Termination rules.** Max rounds, TERMINATE token, goal-reached verifier, or combination.
4. **Hot-speaker mitigation.** Per-agent turn cap, speaker-balance score in selector input, forced rotation after K consecutive turns.
5. **Context bloat mitigation.** Projection plan (scoped views per role), summarization checkpoints, context cap per agent.
6. **Observability.** Log selector's input, selector's choice, per-turn agent latency.

Hard rejects:

- Any LLM-selected config without logging of selector's input/output. Debugging becomes impossible.
- Configs without a max_rounds cap.
- Symmetric chats (no specialization) on reasoning tasks — use debate (Lesson 07) instead.

Refusal rules:

- If the task has a known DAG structure, refuse GroupChat and recommend LangGraph static graph for determinism.
- If the task requires strict audit trails, refuse GroupChat; recommend LangGraph with checkpointer.
- If the agents number more than 5-6, refuse flat GroupChat and recommend nested groups or hierarchical pattern.

Output: a one-page GroupChat config brief. Close with the cost estimate (LLM-selected incurs one selector call per turn).

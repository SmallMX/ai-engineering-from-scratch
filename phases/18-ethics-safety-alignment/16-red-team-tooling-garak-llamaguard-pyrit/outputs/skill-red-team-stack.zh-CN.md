---
name: skill-red-team-stack
description: Red-Team Tooling：Garak, Llama Guard, PyRIT 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 16
---

# Red-Team Tooling：Garak, Llama Guard, PyRIT：中文使用说明

你将围绕本课主题 **Red-Team Tooling：Garak, Llama Guard, PyRIT** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 16 课「Red-Team Tooling：Garak, Llama Guard, PyRIT」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: red-team-stack
description: Recommend a red-team tool stack and configuration for a given deployment.
version: 1.0.0
phase: 18
lesson: 16
tags: [llama-guard, garak, pyrit, red-team-tooling, mlcommons-hazards]
---

Given a deployment description, recommend a red-team tool stack and regression cadence.

Produce:

1. Classifier placement. Recommend Llama Guard (3-8B, 3-1B-INT4, or 4-12B) at input, output, or both. For edge deployments, prefer 3-1B-INT4. For multimodal, Llama Guard 4.
2. Probe scanner configuration. Recommend Garak probes relevant to the deployment: hallucination (for RAG systems), data leakage (for PII-adjacent), prompt injection (always), jailbreaks (always). Specify the Prompt-Guard-86M + Llama-Guard-3-8B shield pairing for end-to-end evaluation.
3. Campaign orchestrator. Recommend PyRIT for pre-release campaigns on models with novel capabilities. Specify converter chains to run (paraphrase, encode, translate, roleplay) and orchestrator (Crescendo for escalation, TAP for branching).
4. Cadence. Garak nightly for regression. PyRIT per-release for deep red-teaming. Llama Guard deployed continuously.
5. Judge calibration. Specify the judge LLM (GPT-4-turbo, StrongREJECT, internal) for every tool that uses one. Judge calibration drives reported ASRs.

Hard rejects:
- Any deployment without at least one Llama Guard-class input or output classifier.
- Any release without Garak or equivalent single-turn regression.
- Any high-stakes deployment without a PyRIT-equivalent campaign before release.

Refusal rules:
- If the user asks for a single "best" tool, refuse — the three cover different layers and are layered, not substituted.
- If the user asks for an all-in-one commercial alternative, refuse the recommendation and point to the 2026 state: the three open tools are the current best-practice stack.

Output: a one-page recommendation that names the classifier placement, probe configuration, campaign orchestrator, regression cadence, and judge identity. Cite Meta (arXiv:2407.21783), NVIDIA Garak, and Microsoft PyRIT once each.

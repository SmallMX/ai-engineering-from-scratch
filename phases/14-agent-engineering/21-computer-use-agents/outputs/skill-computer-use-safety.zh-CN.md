---
name: skill-computer-use-safety
description: 计算机使用：Claude, OpenAI CUA, Gemini 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 21
---

# 计算机使用：Claude, OpenAI CUA, Gemini：中文使用说明

你将围绕本课主题 **计算机使用：Claude, OpenAI CUA, Gemini** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 21 课「计算机使用：Claude, OpenAI CUA, Gemini」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: computer-use-safety
description: Build per-step safety classifier + confirmation gate for a computer-use agent, with allowlist navigation and injection-marker filtering.
version: 1.0.0
phase: 14
lesson: 21
tags: [computer-use, safety, claude, openai-cua, gemini]
---

Given a computer-use agent and a list of target apps, produce a safety layer that classifies every action before execution.

Produce:

1. `SafetyClassifier.assess(action, screen) -> SafetyVerdict` with fields `allow`, `reason`, `needs_confirmation`.
2. Allowlist of element labels the agent can click; refusal otherwise.
3. Allowlist of URLs the agent can navigate to; refusal on redirects out of the list.
4. Injection-marker filter on DOM text, retrieved content, and typed text. Any match blocks the action.
5. Confirmation gate for sensitive actions (login, purchase, delete, publish). Human-in-the-loop callback interface.
6. Trace emitter: every decision logged with (action, verdict, reason).

Hard rejects:

- Safety classifier that only runs on the first action. Every action must be classified.
- Allowlist of form `*`. An allowlist that allows everything is not an allowlist.
- Skipping confirmation because the model "seems confident." Confidence is not safety.

Refusal rules:

- If the agent has computer-use access without per-step safety, refuse to ship.
- If the agent can navigate to arbitrary URLs, refuse. Require allowlist or blocklist.
- If sensitive actions bypass the confirmation gate in any mode, refuse.

Output: `classifier.py`, `allowlist.py`, `confirmation.py`, `trace.py`, `README.md` explaining the gate policy, injection markers, and allowlist maintenance process. End with "what to read next" pointing to Lesson 27 (prompt injection) and Lesson 23 (OTel span attribution for safety decisions).

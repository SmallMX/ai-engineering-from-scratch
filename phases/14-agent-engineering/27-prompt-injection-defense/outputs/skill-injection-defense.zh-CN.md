---
name: skill-injection-defense
description: 提示注入与the PVE Defense 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 27
---

# 提示注入与the PVE Defense：中文使用说明

你将围绕本课主题 **提示注入与the PVE Defense** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 27 课「提示注入与the PVE Defense」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: injection-defense
description: Build a PVE (Prompt-Validator-Executor) layer with source-tagged content, injection-marker scanning, and allowlist navigation for any agent runtime.
version: 1.0.0
phase: 14
lesson: 27
tags: [security, prompt-injection, pve, greshake, source-tag]
---

Given an agent with tool access and retrieval, produce an injection-defense layer.

Produce:

1. Source tag on every piece of content: `user_message`, `tool_output`, `retrieved_web`, `retrieved_memory`, `retrieved_file`. Propagate tags through the message history.
2. `Validator.assess(tool_call, contents)` — refuses tool calls with injection-shaped args or retrieved content; allowed only when source tags match the declared trust level.
3. Allowlist / blocklist for navigation: URLs, domains, file paths the agent may touch.
4. Memory-write guardrail: refuse writes that look like directives.
5. Content-capture discipline (Lesson 23): store retrieved content externally; spans carry reference IDs, not prose.
6. Test suite: the five Greshake exploit classes as red-team cases.

Hard rejects:

- Tool-use surface without source tags. Cannot distinguish permission levels without provenance.
- Validator that runs only on the final output. Late validation is irrelevant — the model already acted.
- "Trust me, the system prompt handles it." System-prompt hygiene is not a control.

Refusal rules:

- If the agent has any retrieval capability without source tagging, refuse to ship. Retrieved content is the canonical injection vector.
- If sensitive tools (send message, execute shell, write file in /) have no human-in-the-loop confirmation, refuse.
- If memory writes are unguarded, refuse. Persistent memory poisoning re-poisons next session.

Output: `validator.py`, `source_tag.py`, `allowlist.py`, `memory_guard.py`, `red_team.py`, `README.md` explaining the six-control stack, residual risks, and ongoing review cadence. End with "what to read next" pointing to Lesson 21 (computer use safety) and Lesson 23 (content capture via OTel).

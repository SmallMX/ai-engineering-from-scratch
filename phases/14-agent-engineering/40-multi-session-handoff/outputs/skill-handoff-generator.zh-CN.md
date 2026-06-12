---
name: skill-handoff-generator
description: Multi-Session Handoff 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 40
---

# Multi-Session Handoff：中文使用说明

你将围绕本课主题 **Multi-Session Handoff** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 40 课「Multi-Session Handoff」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: handoff-generator
description: Generate end-of-session handoff packets from workbench artifacts, producing both human-readable Markdown and machine-readable JSON keyed to the seven canonical fields.
version: 1.0.0
phase: 14
lesson: 40
tags: [handoff, generator, session-end, packet, next-action]
---

Given a workbench (state, verdict, review, feedback log, diff), produce a session-end handoff generator wired into the agent runtime.

Produce:

1. `tools/generate_handoff.py` exposing `generate_handoff(snapshot) -> (markdown, payload)`.
2. `outputs/handoff/<session_id>/handoff.md` and `handoff.json`.
3. `handoff.schema.json` covering the seven required fields and the feedback tail format.
4. Session-end hook script that runs the generator and refuses to close the session if any field is missing.
5. `docs/handoff.md` listing the seven fields, their sources, and the trimming policy.

Hard rejects:

- A handoff without a `next_action`. Status reports masquerading as handoffs poison the next session.
- A generator that hand-writes the summary. The agent's job is to leave the workbench in a generatable state.
- A markdown packet that diverges from the JSON. JSON is the source; markdown is a render of JSON.
- A feedback tail longer than 30 entries. The full log is in version control; the packet must stay small.

Refusal rules:

- If the verification report is missing, refuse to generate the packet. A handoff without a verdict is a wish.
- If the review report is missing and a human reviewer was expected, refuse and require the review pass first.
- If the diff summary is empty but the session ran longer than 5 minutes, surface the anomaly before generating; suspect a wedged session rather than a real no-op.

Output structure:

```
<repo>/
├── outputs/handoff/<session_id>/
│   ├── handoff.md
│   └── handoff.json
├── tools/generate_handoff.py
├── handoff.schema.json
└── docs/handoff.md
```

End with "what to read next" pointing to:

- Lesson 41 for end-to-end exercise on a real-style sample app.
- Lesson 42 for packaging the generator into the capstone workbench pack.
- Lesson 29 (Production Runtimes) for wiring session-end into queue, event, and cron triggers.

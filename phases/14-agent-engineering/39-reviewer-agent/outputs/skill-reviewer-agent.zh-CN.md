---
name: skill-reviewer-agent
description: Reviewer 智能体：Separate Builder from Marker 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 39
---

# Reviewer 智能体：Separate Builder from Marker：中文使用说明

你将围绕本课主题 **Reviewer 智能体：Separate Builder from Marker** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 39 课「Reviewer 智能体：Separate Builder from Marker」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: reviewer-agent
description: Stand up a reviewer agent role with a five-dimension rubric that reads builder artifacts, produces a structured review report, and starts human review from a written page instead of a blank one.
version: 1.0.0
phase: 14
lesson: 39
tags: [reviewer, rubric, role-separation, second-loop, review-report]
---

Given a builder agent already producing workbench artifacts, stand up a reviewer that reads them and writes structured reports.

Produce:

1. `agents/reviewer.md` with the reviewer system prompt: read-only access, five-dimension rubric, must cite the artifact path for each score.
2. `tools/reviewer.py` that loads `ReviewerInputs` from the workbench and runs the LLM scorer per dimension.
3. `outputs/review/<task_id>.json` as the canonical review report path.
4. `docs/reviewer-rubric.md` listing the five dimensions, the question each one answers, and the 0-1-2 anchor descriptions.
5. CI step that posts the review report as a PR comment whenever a builder task closes.

Hard rejects:

- A reviewer with write access to the diff. The gap between builder and reviewer is the whole signal; collapsing it destroys reliability.
- A rubric without anchor descriptions per score. "Score from 0 to 2" without anchors collapses to vibes.
- Review reports that omit citations. Every score must point at a file or trace entry.
- Sharing the builder's system prompt. Same model is fine; same prompt is not.

Refusal rules:

- If the builder produces no verification report, refuse to run the reviewer. Acceptance must hold before judgment is worth asking for.
- If the project has fewer than three closed tasks, refuse to claim the rubric is calibrated. Save the first reports as the calibration set.
- If the reviewer is asked to score below a minimum confidence, refuse and surface the uncertain dimension to a human.

Output structure:

```
<repo>/
├── agents/reviewer.md
├── tools/reviewer.py
├── outputs/review/
│   └── <task_id>.json
├── docs/reviewer-rubric.md
└── .github/workflows/review.yml
```

End with "what to read next" pointing to:

- Lesson 40 for the handoff packet that combines verification + review.
- Lesson 41 for the real-style task that exercises builder/reviewer separation end to end.
- Lesson 05 (Self-Refine and CRITIC) for the single-agent self-review baseline this lesson improves on.

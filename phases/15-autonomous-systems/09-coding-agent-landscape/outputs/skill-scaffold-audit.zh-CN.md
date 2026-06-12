---
name: skill-scaffold-audit
description: The 自主 Coding 智能体 Landscape (2026) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 9
---

# The 自主 Coding 智能体 Landscape (2026)：中文使用说明

你将围绕本课主题 **The 自主 Coding 智能体 Landscape (2026)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 09 课「The 自主 Coding 智能体 Landscape (2026)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: coding-scaffold-audit
description: Audit a proposed coding-agent scaffold (retrieval, verifier loop, sandbox, benchmark fit) before adopting it for production code changes.
version: 1.0.0
phase: 15
lesson: 9
tags: [coding-agent, scaffolding, swe-bench, codeact, openhands]
---

Given a proposed coding-agent scaffold (SWE-agent, OpenHands, Aider, Cline, Devin, Claude Code, or an in-house build), score it across four axes and flag where benchmark numbers will overstate production quality.

Produce:

1. **Retrieval.** Describe how the scaffold selects which files the agent reads before acting. Repo map, embedding search, explicit file list, or agent-driven `grep` calls. Quality of retrieval is the silent dominant reliability factor.
2. **Verifier loop.** Does the scaffold run tests, read the stack trace, and feed failure back into the next turn? If no verifier loop, flag as missing — this is usually a 10+ point absolute delta on SWE-bench-like tasks.
3. **Sandbox and blast radius.** Where do actions execute? Local file system, ephemeral container, managed VM. For CodeAct-style scaffolds, confirm the sandbox is hardened (no egress, no host mounts, time limit). For JSON tool-call scaffolds, confirm the tool validators reject every unintended side effect.
4. **Benchmark fit.** What distribution does the reported number (e.g., "80.9% on SWE-bench Verified") actually cover? Count the fraction of the benchmark made up of 1–2 line tasks; compare the reported score to SWE-bench Pro (10+ line tasks) for the same model. A scaffold whose headline number is driven by the easy tail is not a production signal.

Hard rejects:
- Any scaffold without a verifier loop used for tasks above trivial complexity.
- CodeAct scaffolds without sandbox isolation (no Docker, no rootless container, no VM) pointing at real repositories.
- Benchmark claims that do not disclose the distribution (easy-tail fraction, Pro-equivalent score).
- Tool-call scaffolds where a single tool can touch arbitrary paths with no validator (e.g., a raw `shell_exec` tool exposed to the model).

Refusal rules:
- If the user cannot produce the scaffold's test-suite pass-rate on a representative internal distribution, refuse and require a small-sample measurement first. Public benchmarks predict rank-order, not absolute quality.
- If the proposed scaffold would run against a production repository without a staging dry-run, refuse and require staging first. Coding agents rewrite files; coding agents with bad retrieval rewrite the wrong files.
- If the user plans to use benchmark scores alone (without their own evals) to make a go/no-go decision, refuse and require internal eval data.

Output format:

Return a scored memo with:
- **Retrieval score** (0–5 with mechanism described)
- **Verifier loop score** (0–5 with feedback format)
- **Sandbox score** (0–5 with isolation mechanism)
- **Benchmark fit score** (0–5 with internal distribution delta)
- **Deployment recommendation** (production / staging / research only)
- **One-line risk summary** (the most likely first production failure)

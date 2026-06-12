---
name: skill-init-script
description: Initialization Scripts for 智能体 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 35
---

# Initialization Scripts for 智能体：中文使用说明

你将围绕本课主题 **Initialization Scripts for 智能体** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 35 课「Initialization Scripts for 智能体」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: init-script
description: Interview a project and emit a deterministic init_agent.py with five probes plus a CI workflow that refuses to launch the agent if any probe fails.
version: 1.0.0
phase: 14
lesson: 35
tags: [init, probes, ci, workbench, fail-loud]
---

Given a repo, the agent product, and its dependency surface, produce a project-specific init script and CI wiring.

Produce:

1. `tools/init_agent.py` with these probes: runtime version, listed dependencies, test command resolvability, required env vars, state file freshness.
2. `init_report.json` schema documented next to the script. Each probe returns `(name, status: pass|warn|fail, detail)`.
3. `.github/workflows/agent-init.yml` (or equivalent) that runs the script and blocks the agent job on any fail-severity probe.
4. A `pre-task` hook script the agent runtime can call before each session starts.
5. Documentation in `docs/init.md` listing every probe, its severity, and how to fix a failure.

Hard rejects:

- Probes that call out to the network without a timeout. Init must be fast and offline-safe.
- Probes that require LLM calls. Init is deterministic plumbing.
- A non-zero exit code that the wrapper swallows. Fail loud is the whole point.
- Probes that touch state without idempotency. Two runs in a row must produce identical reports modulo timestamp.

Refusal rules:

- If the project has no test command, refuse to ship the script. Add the gap to the workbench audit instead.
- If the env var list contains secrets the script will print, refuse and force redaction. Init reports should never carry secrets.
- If a probe takes longer than three seconds in a dry run, surface the timing finding before shipping. Long probes turn init into ceremony.

Output structure:

```
<repo>/
├── tools/
│   ├── init_agent.py
│   └── pre_task.sh
├── docs/
│   └── init.md
└── .github/
    └── workflows/
        └── agent-init.yml
```

End with "what to read next" pointing to:

- Lesson 36 for the per-task scope contract that uses the init report's `repo_paths`.
- Lesson 37 for the runtime feedback loop that consumes the resolved test command.
- Lesson 38 for the verification gate that depends on probes passing.

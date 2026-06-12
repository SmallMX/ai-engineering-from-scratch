---
name: skill-agent-bundle
description: Skills与智能体 SDKs：Anthropic Skills, AGENTS.md, OpenAI Apps SDK 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 22
---

# Skills与智能体 SDKs：Anthropic Skills, AGENTS.md, OpenAI Apps SDK：中文使用说明

你将围绕本课主题 **Skills与智能体 SDKs：Anthropic Skills, AGENTS.md, OpenAI Apps SDK** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 22 课「Skills与智能体 SDKs：Anthropic Skills, AGENTS.md, OpenAI Apps SDK」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: agent-bundle
description: Produce a portable SKILL.md + AGENTS.md + MCP-server blueprint for a workflow, loadable across Claude Code, Cursor, Codex, and compatible agents.
version: 1.0.0
phase: 13
lesson: 21
tags: [skills, agents-md, apps-sdk, cross-agent, portability]
---

Given a workflow description, produce an agent bundle.

Produce:

1. SKILL.md. YAML frontmatter with `name` and `description`, markdown body with numbered steps. Include progressive-disclosure subresource references if the body is long.
2. AGENTS.md entry. A few lines to add to the repo's AGENTS.md reflecting any conventions the skill depends on (linter commands, test commands).
3. MCP server blueprint. Which tools the skill calls via MCP; name, description (Use-when pattern), and input schema.
4. Cross-agent translations. SkillKit-style notes on how this SKILL.md maps to Cursor rules, Codex `.codex.md`, Windsurf rules.
5. Loading path. Where agents will discover this bundle: `~/.anthropic/skills/`, `./skills/`, `~/.claude/skills/`.

Hard rejects:
- Any SKILL.md whose `name` is not `kebab-case`. Breaks discovery.
- Any SKILL.md without `description` in frontmatter. Agent runtimes skip it.
- Any bundle whose MCP tools are not named per Phase 13 · 05 rules.

Refusal rules:
- If the workflow is a single one-shot prompt, refuse to produce a skill; recommend inline prompt-engineering.
- If the workflow requires OAuth (e.g. Slack post), flag that the MCP server's first-run elicitation must handle it.
- If the target agents do not support SKILL.md (some IDEs), recommend translation via SkillKit or similar.

Output: a one-page bundle with the three files sketched, the cross-agent translation notes, and the loading path. End with the single agent to test the bundle in first.

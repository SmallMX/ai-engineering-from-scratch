---
name: skill-mcp-apps-spec
description: MCP Apps：Interactive UI Resources via `ui://` 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 14
---

# MCP Apps：Interactive UI Resources via `ui://`：中文使用说明

你将围绕本课主题 **MCP Apps：Interactive UI Resources via `ui://`** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 14 课「MCP Apps：Interactive UI Resources via `ui://`」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mcp-apps-spec
description: Produce the full MCP Apps contract for a tool that needs an interactive UI resource.
version: 1.0.0
phase: 13
lesson: 14
tags: [mcp, apps, ui-resources, csp, iframe-sandbox]
---

Given a tool that would benefit from an interactive UI (timeline, form, dashboard, map, chart), produce the MCP Apps contract.

Produce:

1. `ui://` URI. One canonical name for the UI resource (e.g. `ui://notes/timeline`).
2. Tool result shape. `content[]` with `text` preamble and `ui_resource` block; `_meta.ui` populated.
3. CSP. Minimum allowlist for `default-src`, `script-src`, `connect-src`, `img-src`, `style-src`. Avoid `'unsafe-inline'` unless necessary.
4. Permissions list. Camera / mic / geolocation / network if needed; empty if not.
5. postMessage entry points. Which `host.*` calls the UI will make and what they return.
6. Security checklist. Distinguish-from-host, no clickjacking, strict connect-src, HTML sanitization if any user content is rendered.

Hard rejects:
- CSP with `default-src *`. Wide-open security risk.
- Any `permissions` request beyond what the UI actually uses. Minimum privilege.
- Any ui:// resource that loads external scripts. Bundle or refuse.
- Any UI that renders user-controlled HTML without sanitization. XSS vector.

Refusal rules:
- If the UI is just a static result, refuse to scaffold an App; return text content.
- If the tool would benefit from native host widgets (progress bars, confirmation dialogs), recommend those instead.
- If the host does not yet support MCP Apps (VS Code stable, Zed, Windsurf as of 2026-04), flag fallback-to-text path.

Output: a one-page contract with the `ui://` URI, tool result JSON, CSP, permissions, postMessage entry points, and a security checklist. End with one sentence on the minimum host that will render this UI.

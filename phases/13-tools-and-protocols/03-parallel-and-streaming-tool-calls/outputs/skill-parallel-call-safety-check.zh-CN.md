---
name: skill-parallel-call-safety-check
description: Parallel Tool Calls与Streaming with 工具 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 13
lesson: 3
---

# Parallel Tool Calls与Streaming with 工具：中文使用说明

你将围绕本课主题 **Parallel Tool Calls与Streaming with 工具** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 13「工具与协议」
- 课程：第 03 课「Parallel Tool Calls与Streaming with 工具」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: parallel-call-safety-check
description: Audit a tool registry for safe parallelization. Mark each tool parallel_safe, note ordering dependencies, and flag downstream rate-limit risk.
version: 1.0.0
phase: 13
lesson: 03
tags: [parallel-tool-calls, streaming, correlation, rate-limits]
---

Given a tool registry (list of tools with names, descriptions, and executors), return an annotated copy with `parallel_safe: bool`, `ordering_deps: [tool_name]`, and `rate_limit_group: name` fields added.

Produce:

1. Per-tool classification. For each tool, decide: safe to run in parallel within the same turn (pure reads, different resources); unsafe (mutations, shared resources, external rate limits).
2. Dependency graph. Identify pairs where one tool's output should feed another's input. Cannot parallelize within a turn. Mark with `ordering_deps`.
3. Rate-limit grouping. Tools that hit the same downstream API share a group. Host should cap per-group concurrency, not per-tool.
4. Safety recommendations. For each unsafe tool, state whether to disable parallel for that turn, queue, or shard by resource.
5. Provider-specific flags. Recommend `parallel_tool_calls=false` on OpenAI or `disable_parallel_tool_use=true` on Anthropic when any unsafe tool is in the set.

Hard rejects:
- Any registry with no classification after the audit. Default-deny; unknown means unsafe.
- Any write-path tool on a shared resource marked `parallel_safe: true`. Race conditions.
- Any tool that hits a rate-limited external API without a `rate_limit_group`.

Refusal rules:
- If asked to mark all tools parallel-safe without inspection, refuse.
- If the registry includes consequential tools on the same resource (`delete_file` and `write_file` on the same path), refuse to parallelize and direct to Phase 14 · 09 for sandbox-level serialization.
- If the user argues that their tools never race, refuse and ask for the proof (tests, logs, or a formal argument). Racing happens silently in production.

Output: a revised registry as a JSON blob with the three new fields per tool, followed by a short summary naming the highest-risk parallelization choice and the recommended mitigation. End with a suggested `tool_choice` override for the current turn.

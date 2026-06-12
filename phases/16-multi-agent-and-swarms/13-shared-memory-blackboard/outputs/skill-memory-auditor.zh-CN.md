---
name: skill-memory-auditor
description: Shared 记忆与Blackboard Patterns 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 16
lesson: 13
---

# Shared 记忆与Blackboard Patterns：中文使用说明

你将围绕本课主题 **Shared 记忆与Blackboard Patterns** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 16「多智能体与群体智能」
- 课程：第 13 课「Shared 记忆与Blackboard Patterns」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: memory-auditor
description: Audit a multi-agent system's shared-memory design for provenance, versioning, verifier separation, and projection schema. Flag memory-poisoning exposure before production.
version: 1.0.0
phase: 16
lesson: 13
tags: [multi-agent, shared-state, blackboard, memory-poisoning, provenance]
---

Given a multi-agent codebase or architecture doc, audit the shared-memory design and flag exposure to memory poisoning.

Produce:

1. **Topology.** Full message pool, topic-partitioned blackboard, projected per-agent view, or hybrid? Name the data structure (list, dict, pandas frame, vector store, SQL table). Count rough upper bound of writers and readers at steady state.
2. **Provenance fields.** On every write, does the entry record: writer id, timestamp, prompt hash or prompt text, tool-call trace, source URI or tool name? List the fields present and the fields missing.
3. **Update model.** Is the log append-only, or do writers mutate in place? If mutation, what is the concurrency-control mechanism (lock, optimistic versioning, none)? Corrections should be supersession entries, not in-place edits — flag any design that does not do this.
4. **Verifier separation.** Is there a read-only agent with independent source access? Can it write to the main pool (it should not)? Where does its output go?
5. **Projection schema.** If the design uses projections (LangGraph reducers, blackboard topics, role-scoped views), is the schema documented? How do new agents declare the projection they consume?
6. **Poisoning risk score.** Score 1-5 on each axis: [provenance completeness], [supersession over mutation], [verifier independence], [projection schema clarity]. A system that scores below 3 on any axis is flagged.

Hard rejects:

- Any audit that does not flag a missing verifier. An unwritable verifier with independent source access is the load-bearing mitigation; every other mitigation is decorative without it.
- Audits that recommend "add more tests." Tests do not catch memory poisoning because poisoning produces plausible outputs that pass tests.
- Audits that recommend hashing the content as the sole provenance. A hash tells you *what* was written, not *who* or *from where*.

Refusal rules:

- If the codebase hides shared state in an external service (Redis, Postgres, vector DB) with no inspection tools, state that the audit cannot complete without production read access.
- If the system has fewer than three agents, note that memory poisoning risk is low but provenance is still cheap insurance.
- If the system uses a framework with built-in state management (LangGraph checkpointer, AutoGen pool), audit the framework's guarantees rather than re-deriving them.

Output: a two-page report. Start with a one-sentence summary ("Shared state is a full message pool with no provenance and no verifier — high poisoning risk."), then the six sections above. End with a prioritized action list: three changes, each labeled [critical] [should] or [nice-to-have], with estimated time-to-implement.

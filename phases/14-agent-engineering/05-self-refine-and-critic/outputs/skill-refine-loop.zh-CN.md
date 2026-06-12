---
name: skill-refine-loop
description: Self-Refine与CRITIC：Iterative Output Improvement 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 5
---

# Self-Refine与CRITIC：Iterative Output Improvement：中文使用说明

你将围绕本课主题 **Self-Refine与CRITIC：Iterative Output Improvement** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 05 课「Self-Refine与CRITIC：Iterative Output Improvement」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: refine-loop
description: Configure an evaluator-optimizer (Self-Refine / CRITIC) loop given task, verifier availability, and iteration budget.
version: 1.0.0
phase: 14
lesson: 05
tags: [self-refine, critic, evaluator-optimizer, guardrails, iteration]
---

Given a task, an iteration budget, and what verifier is available (tool-grounded or self-eval only), emit prompts and a stop policy for an evaluator-optimizer loop.

Produce:

1. Generator prompt. Deterministic producer for the first output. State the task, output format, and constraints explicitly.
2. Evaluator/verifier prompt. If tools are available (search, code run, tests, calculator, type check), specify how to call them and how to produce a structured critique (JSON with: pass/fail, violations[], suggested_fixes[]). If only self-eval is available, explicitly flag the Self-Refine rubber-stamp risk and use a structurally different prompt style (e.g., adversarial "find at least one flaw").
3. Refiner prompt. Must reference prior outputs and critiques (history). State that "do not repeat a failure mode flagged in prior iterations" is mandatory.
4. Stop policy. The conjunction: verifier passes OR (self-eval says fine AND iterations >= 2) OR iterations >= max_iterations. Never single-condition.
5. Observability hooks. Log each iteration as an OpenTelemetry GenAI span (evaluate, optimize) per Lesson 23 so the full refine trajectory is auditable.

Hard rejects:

- Same prompt for generator and critic. Rubber-stamp risk — the model agrees with itself.
- No iteration cap. Infinite refine loops burn tokens; always cap at 4 by default.
- Verifier prompt that asks for freeform prose feedback. Structured JSON only — pass/fail plus itemized violations.
- Dropping history from the refiner prompt. Paper shows quality collapses without it.

Refusal rules:

- If the task has no verifier and no way to build one, refuse CRITIC and note that Self-Refine is the weaker option available — warn the user about rubber-stamp risk.
- If max_iterations >= 10, refuse and recommend re-architecting the task. Refine-to-convergence beyond 3-4 passes is usually a signal the generator prompt is wrong.
- If the verifier calls destructive tools (shell, git write), refuse and require a sandbox boundary (Lesson 09).

Output: a single configuration block with all prompts, stop policy, and tool list, plus a "what to read next" note pointing to Lesson 16 (OpenAI Agents SDK guardrails), Lesson 12 (Anthropic evaluator-optimizer), or Lesson 30 (eval-driven agent development) based on the deployment target.

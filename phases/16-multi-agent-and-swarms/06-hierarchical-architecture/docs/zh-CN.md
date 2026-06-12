# Hierarchical Architecture与Its Failure Mode

> Hierarchical is supervisor nested. Manager agents over sub-managers over workers. CrewAI `Process.hierarchical` is the textbook version：a `manager_llm` dynamically delegates tasks与validates outputs. The LangGraph equivalent is `create_supervisor(create_supervisor(...))`. It is the natural pattern when the task is a real org chart. It is also the pattern most likely to collapse into managerial looping：manager agents assign work poorly, misinterpret sub-outputs, or fail to reach consensus. Sequential often beats it.

**类型：** Learn + Build
**语言：** Python (stdlib)
**前置知识：** Phase 16 · 05 (Supervisor Pattern)
**时间：** 约 60 minutes

## 学习目标
- 理解 Hierarchical Architecture与Its Failure Mode 在本阶段课程中的作用。
- 把核心概念映射到可运行代码、测验和课程产物。
- 保留英文术语、命令、路径和 API 名称，方便和原文对照。

## 中文导读

本课是 Phase 16「多智能体与群体智能」的第 06 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Hierarchical Architecture and Its Failure Mode

> Hierarchical is supervisor nested. Manager agents over sub-managers over workers. CrewAI `Process.hierarchical` is the textbook version: a `manager_llm` dynamically delegates tasks and validates outputs. The LangGraph equivalent is `create_supervisor(create_supervisor(...))`. It is the natural pattern when the task is a real org chart. It is also the pattern most likely to collapse into managerial looping — manager agents assign work poorly, misinterpret sub-outputs, or fail to reach consensus. Sequential often beats it.

**Type:** Learn + Build
**Languages:** Python (stdlib)
**Prerequisites:** Phase 16 · 05 (Supervisor Pattern)
**Time:** ~60 minutes

## Problem

Once the supervisor pattern clicks, the natural next step is "what if the workers are themselves supervisors?" Teams have sub-teams; companies have departments of departments. Hierarchical architectures mirror that.

The issue: LLM managers are not the same as human managers. A human manager has stable priors about what their reports know. An LLM manager re-reasons the org every turn from whatever is in its context. Tiny drift in that context, and the whole tree misallocates work.

## Concept

### The shape

```
                 Manager
                 ┌─────┐
                 └──┬──┘
           ┌────────┴────────┐
           ▼                 ▼
       Sub-Mgr A         Sub-Mgr B
       ┌─────┐           ┌─────┐
       └──┬──┘           └──┬──┘
         ┌┴──┬──┐          ┌┴──┐
         ▼   ▼  ▼          ▼   ▼
       W1  W2  W3         W4  W5
```

Every internal node plans, delegates, and synthesizes. Only leaves do work.

### Where it shines

- **Clear org mapping.** If the real task is departmental ("legal review the doc, finance review the doc, engineering review the doc, then summarize for exec"), the hierarchy is explicit.
- **Local summarization.** Each sub-manager synthesizes its team's output before the top manager sees it. Top manager sees three sub-manager summaries, not fifteen worker outputs.

### Where it breaks

Three failure modes the 2026 post-mortems keep finding:

1. **Task assignment error.** The manager reads the goal, hallucinates a decomposition, and delegates to the wrong sub-manager. Because the sub-manager obediently works on what it was given, the error only surfaces at the top synthesis — one level removed from where a human could have caught it.
2. **Output misinterpretation.** Sub-manager returns "unable to verify claim X." Top manager summarizes as "claim X not confirmed." Meaning drifts at every level.
3. **Consensus loops.** Two sub-managers disagree; top manager asks them to reconcile; they re-delegate down; workers re-run; sub-managers return slightly different answers; loop. CrewAI's `Process.hierarchical` guards against this with step limits, but the limit itself is now a hyperparameter.

### The deciding question

Sequential (linear pipeline) vs hierarchical: does your task actually have independent sub-teams, or is it one linear flow pretending to be a tree? If the latter, use sequential. If the former, use hierarchical but budget explicit reconciliation rules.

### CrewAI's implementation

`Process.hierarchical` wires a manager LLM over specialist crews. The manager:

- receives the top-level task,
- assigns subtasks to crews,
- evaluates crew outputs,
- decides whether to accept, re-delegate, or iterate.

Documentation: https://docs.crewai.com/en/introduction (look for "Hierarchical Process" under Core Concepts).

### LangGraph's implementation

LangGraph uses nested `create_supervisor` calls. The inner supervisor has its own graph; the outer supervisor treats the inner graph as an opaque node. This is cleaner than CrewAI for debugging (you can step through each graph separately) but harder to express dynamic reshaping of the tree.

Reference: https://reference.langchain.com/python/langgraph-supervisor.

## Build It

`code/main.py` runs a 3-level hierarchy:

- top manager: splits a task into "engineering" and "legal" branches,
- engineering sub-manager: splits into "frontend" and "backend" workers,
- legal sub-manager: one worker.

Demo contrasts happy path (everyone agrees) against a **perturbed path** where the top manager's decomposition mislabels "legal" as "finance" and watches the error cascade — the sub-manager obediently does finance work, the top synthesizer reports finance findings, the original legal question goes unanswered.

Run:

```
python3 code/main.py
```

Output shows both paths with a clear side-by-side of "what was asked" vs "what was delivered."

## Use It

`outputs/skill-hierarchy-fitness.md` evaluates whether a given task should use hierarchical, sequential, or flat supervisor. Inputs: task description, org structure, reconciliation budget. Output: pattern recommendation with the specific failure modes to guard against.

## Ship It

If you ship hierarchical:

- **Cap tree depth at 2.** Three levels already hides most errors from observability.
- **Explicit reconciliation budget.** Set max rounds before the top manager must commit. Usually 2.
- **Provenance on every synthesis.** Each node's summary must cite which leaf outputs produced it.
- **Alert on decomposition drift.** Log the manager's decomposition per step; diff against the user query. If the decomposition no longer covers the query, fire an alert.

## Exercises

1. Run `code/main.py` and compare happy vs perturbed. How many levels of manager hand-off does it take before the top output fully diverges from the user's question?
2. Add a third level (top → sub → sub-sub → worker). Measure how often the perturbed path corrects itself vs fully diverges as depth grows.
3. Implement a "canary" worker at each sub-manager that is always asked the original user question unchanged. Use the canary answer to detect decomposition drift. How should the manager react when the canary disagrees with the synthesized answer?
4. Read CrewAI's `Process.hierarchical` docs. Identify one concrete guardrail CrewAI applies (step limit, manager_llm constraint) and describe what failure mode it targets.
5. Compare nested LangGraph supervisors to CrewAI hierarchical. Which makes reconciliation loops cheaper to detect?

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| Hierarchical | "Org chart pattern" | Supervisors over supervisors; only leaves do work. |
| Manager LLM | "The boss" | The LLM that decomposes, assigns, and validates at an internal node. |
| Decomposition drift | "The boss lost the plot" | Top manager's split no longer covers the original question. |
| Reconciliation loop | "Endless meetings" | Sub-managers disagree; top re-delegates; workers re-run; loop until budget exhausted. |
| Depth-2 ceiling | "Don't go deeper than 2 levels" | Empirical guardrail: 3+ levels collapses observability. |
| Canary question | "Ground truth at every level" | A worker that is always asked the original query unchanged, to detect drift. |
| Provenance chain | "Who said what" | Trace from each synthesis back to the leaf outputs that produced it. |

## Further Reading

- [CrewAI introduction — Process.hierarchical](https://docs.crewai.com/en/introduction) — textbook hierarchical with a manager LLM
- [LangGraph supervisor reference](https://reference.langchain.com/python/langgraph-supervisor) — nested supervisor via `create_supervisor`
- [Anthropic engineering — Research system](https://www.anthropic.com/engineering/multi-agent-research-system) — why Anthropic deliberately chose flat supervisor over hierarchical
- [Cemri et al. — Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — MAST taxonomy; section on coordination failures documents decomposition drift

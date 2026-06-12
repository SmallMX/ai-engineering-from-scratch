# Orchestration Patterns：Supervisor, Swarm, Hierarchical

> Four orchestration patterns recur across 2026 frameworks：supervisor-worker, swarm / peer-to-peer, hierarchical, debate. Anthropic's guidance："It's about building the right system for your needs." Start simple; add topology only when a single agent plus five workflow patterns is insufficient.

**类型：** Learn + Build
**语言：** Python (stdlib)
**前置知识：** Phase 14 · 12 (Workflow Patterns), Phase 14 · 25 (多智能体 Debate)
**时间：** 约 60 minutes

## 学习目标
- Name the four recurring orchestration patterns与when each fits.
- Describe the 2026 LangChain recommendation：tool-call-based supervision vs supervisor libraries.
- Explain Anthropic's "build the right system" rule与how it gates topology choice.
- Implement all four in stdlib against a common scripted LLM.

## 中文导读

本课是 Phase 14「智能体工程」的第 28 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Orchestration Patterns: Supervisor, Swarm, Hierarchical

> Four orchestration patterns recur across 2026 frameworks: supervisor-worker, swarm / peer-to-peer, hierarchical, debate. Anthropic's guidance: "It's about building the right system for your needs." Start simple; add topology only when a single agent plus five workflow patterns is insufficient.

**Type:** Learn + Build
**Languages:** Python (stdlib)
**Prerequisites:** Phase 14 · 12 (Workflow Patterns), Phase 14 · 25 (Multi-Agent Debate)
**Time:** ~60 minutes

## Learning Objectives

- Name the four recurring orchestration patterns and when each fits.
- Describe the 2026 LangChain recommendation: tool-call-based supervision vs supervisor libraries.
- Explain Anthropic's "build the right system" rule and how it gates topology choice.
- Implement all four in stdlib against a common scripted LLM.

## The Problem

Teams reach for "multi-agent" before they need it. Four patterns recur across frameworks; once you can name them, you can pick the right one — or skip topology entirely.

## The Concept

### Supervisor-worker

- A central routing LLM dispatches to specialist agents.
- Decides: loop back to self, hand off to specialist, terminate.
- Specialists do not talk to each other; all routing goes through the supervisor.

Frameworks: LangGraph `create_supervisor`, Anthropic orchestrator-workers, CrewAI Hierarchical Process.

**2026 LangChain recommendation:** do supervision through direct tool calls rather than `create_supervisor`. Gives finer context engineering control — you decide exactly what each specialist sees.

### Swarm / peer-to-peer

- Agents hand off directly via a shared tool surface.
- No central router.
- Lower latency than supervisor (fewer hops).
- Harder to reason about (no single point of control).

Frameworks: LangGraph swarm topology, OpenAI Agents SDK handoffs (when all agents can hand off to all others).

### Hierarchical

- Supervisors managing sub-supervisors managing workers.
- Implemented as nested subgraphs in LangGraph; nested crews in CrewAI.
- Scales to large agent populations at the cost of operational complexity.

When you need it: when a single supervisor's context budget cannot hold descriptions of all specialists.

### Debate

- Parallel proposers + iterative cross-critique (Lesson 25).
- Not really orchestration — more verification — but shows up as a topology choice in frameworks.

### CrewAI Crew vs Flow

CrewAI formalizes two deployment modes:

- **Flow** for deterministic event-driven automation (recommended starting point for production).
- **Crew** for autonomous role-based collaboration.

This is orthogonal to the four patterns above but maps to topology: Flow is typically supervisor or hierarchical; Crew is typically supervisor with an LLM router.

### Anthropic's guidance

"Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."

Decision order:

1. Single agent + workflow patterns (Lesson 12) — start here.
2. Supervisor-worker — when you have 2-4 specialists.
3. Swarm — when latency matters more than reasoning clarity.
4. Hierarchical — only when supervisor context budget fails.
5. Debate — when accuracy matters more than cost.

### Where this pattern goes wrong

- **Topology-first thinking.** "We need multi-agent" before identifying what problem multi-agent solves.
- **Bouncing handoffs in swarm.** A -> B -> A -> B. Use hop counters.
- **Fake hierarchy.** Three layers because "enterprise"; two actual teams. Collapse.

## Build It

`code/main.py` implements all four patterns in stdlib against a scripted LLM:

- `Supervisor` — central router.
- `Swarm` — peer-to-peer with direct handoffs.
- `Hierarchical` — supervisors of supervisors.
- `Debate` — parallel proposers + critique.

Each pattern handles the same three-intent task (refund / bug / sales). Trace shapes differ.

Run it:

```
python3 code/main.py
```

Output: per-pattern trace + op count. Supervisor is cleanest; swarm is shortest; hierarchical is deepest; debate is most expensive.

## Use It

- **LangGraph** for supervisor and hierarchical (nested subgraphs).
- **OpenAI Agents SDK** for handoffs-as-tools (supervisor-shaped).
- **CrewAI Flow** for production deterministic.
- **Custom** for debate or when you want exact control.

## Ship It

`outputs/skill-orchestration-picker.md` picks a topology and implements it.

## Exercises

1. Convert a supervisor-worker to a swarm by removing the router. What breaks? What improves?
2. Add a hop counter to the swarm: refuse after 3 handoffs. Does it catch A->B->A bouncing?
3. Build a two-level hierarchical system for a 12-specialist domain. Where does the context budget fail without nesting?
4. Profile the four patterns on a production-shaped workload. Which wins on which metric (latency, cost, accuracy, debuggability)?
5. Read Anthropic's "Building Effective Agents" post. Map each of your production flows to one of the four. Any that don't map cleanly?

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| Supervisor-worker | "Router + specialists" | Central LLM dispatches to specialists; they don't talk to each other |
| Swarm | "Peer-to-peer" | Direct handoffs via shared tools; no central router |
| Hierarchical | "Supervisors of supervisors" | Nested subgraphs for large populations |
| Debate | "Proposer + critique" | Parallel proposers, cross-critique (Lesson 25) |
| Tool-call-based supervision | "Supervisor without a library" | Implement supervisor as direct tool calls for context control |
| Crew | "Autonomous team" | CrewAI's role-based collaboration mode |
| Flow | "Deterministic workflow" | CrewAI's event-driven production mode |

## Further Reading

- [Anthropic, Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — five patterns + agent vs workflow
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) — supervisor, swarm, hierarchical
- [CrewAI docs](https://docs.crewai.com/en/introduction) — Crew vs Flow
- [Du et al., Society of Minds (arXiv:2305.14325)](https://arxiv.org/abs/2305.14325) — debate pattern

# 基准：WebArena与OSWorld

> WebArena tests web-agent capability across four self-hosted apps. OSWorld tests desktop-agent capability across Ubuntu, Windows, macOS. At release (2023–2024) both showed a big gap between best-in-class agents与humans. The gap is narrowing; the failure modes haven't changed.

**类型：** 学习
**语言：** Python (stdlib)
**前置知识：** Phase 14 · 19 (SWE-bench, GAIA)
**时间：** 约 60 minutes

## 学习目标
- Describe WebArena's four self-hosted apps与why execution-based evaluation matters.
- Explain why OSWorld uses real OS screenshots instead of accessibility API.
- Name the two primary OSWorld failure modes：GUI grounding与operational knowledge.
- Summarize what OSWorld-G与OSWorld-Human add on top of the base benchmark.

## 中文导读

本课是 Phase 14「智能体工程」的第 20 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Benchmarks: WebArena and OSWorld

> WebArena tests web-agent capability across four self-hosted apps. OSWorld tests desktop-agent capability across Ubuntu, Windows, macOS. At release (2023–2024) both showed a big gap between best-in-class agents and humans. The gap is narrowing; the failure modes haven't changed.

**Type:** Learn
**Languages:** Python (stdlib)
**Prerequisites:** Phase 14 · 19 (SWE-bench, GAIA)
**Time:** ~60 minutes

## Learning Objectives

- Describe WebArena's four self-hosted apps and why execution-based evaluation matters.
- Explain why OSWorld uses real OS screenshots instead of accessibility APIs.
- Name the two primary OSWorld failure modes: GUI grounding and operational knowledge.
- Summarize what OSWorld-G and OSWorld-Human add on top of the base benchmark.

## The Problem

Generalist agents can call tools. Can they drive a browser across 20 clicks to complete a shopping checkout? Can they configure a Linux box using only keyboard and mouse? These are the questions WebArena and OSWorld answer.

## The Concept

### WebArena (Zhou et al., ICLR 2024)

- 812 long-horizon tasks across four self-hosted web apps: a shopping site, a forum, a GitLab-like dev tool, a business CMS.
- Plus utilities: map, calculator, scratchpad.
- Evaluation is execution-based via gym APIs — was the order placed, was the issue closed, was the CMS page updated?
- At release: best GPT-4 agent hit 14.41% success vs human 78.24%.

The self-hosted framing matters — the benchmark is not flaky because the target apps are pinned and reproducible.

### Extensions

- **VisualWebArena** — visually grounded tasks where success depends on interpreting images (screenshots as first-class observations).
- **TheAgentCompany** (Dec 2024) — adds terminal + coding; more like a real remote-work environment.

### OSWorld (Xie et al., NeurIPS 2024)

- 369 real computer tasks across Ubuntu, Windows, macOS.
- Free-form keyboard and mouse control of real applications.
- 1920×1080 screenshots as the observation.
- At release: best model 12.24% vs human 72.36%.

### Primary failure modes

1. **GUI grounding.** Pixel → element mapping. Models struggle to localize UI elements reliably in 1920×1080.
2. **Operational knowledge.** Which menu has the setting, which keyboard shortcut, which preference pane. Knowledge tail that humans build over years.

### Follow-ups

- **OSWorld-G** — 564-sample grounding suite + Jedi training set. Decomposes grounding from planning so you can measure them separately.
- **OSWorld-Human** — manually curated gold action trajectories. Shows top agents use 1.4-2.7x more steps than necessary (the trajectory-efficiency gap).

### Why this matters

Claude computer use, OpenAI CUA, Gemini 2.5 Computer Use (Lesson 21) all train on workloads shaped by WebArena and OSWorld. The benchmarks are the target; the production models are the shipped answer.

### Where benchmarking goes wrong

- **Screenshot-only evals.** OSWorld is screenshot-driven; evaluating an agent that uses DOM or accessibility APIs on OSWorld misses the grounding challenge.
- **Ignoring trajectory length.** Scoring only success-rate misses the 1.4-2.7x step inefficiency OSWorld-Human surfaces.
- **Stale self-hosted apps.** WebArena's apps pin specific versions; update without re-curation breaks comparability.

## Build It

`code/main.py` implements a toy web-agent harness:

- A minimal "shopping app" state machine: list_items, add_to_cart, checkout.
- Gold trajectories for 3 tasks.
- A scripted agent that attempts each task.
- Execution-based evaluator (state check) and trajectory-efficiency metric (steps vs gold).

Run it:

```
python3 code/main.py
```

Output: per-task success rate and trajectory efficiency, mirroring OSWorld-Human's methodology.

## Use It

- **WebArena Verified** self-hosted on an internal cluster for continuous evaluation.
- **OSWorld** in a VM fleet for desktop agents.
- **Computer-use agents** (Lesson 21) — Claude, OpenAI CUA, Gemini — all trained on workloads like these.
- **Your own product flows** — capture gold trajectories for your top 20 tasks; run agents against them weekly.

## Ship It

`outputs/skill-web-desktop-harness.md` builds a web/desktop agent harness with execution-based eval and trajectory efficiency metric.

## Exercises

1. Extend the toy harness with a second app (a forum). Write 3 tasks plus gold trajectories.
2. Add trajectory-efficiency reporting per task. On your toy, is the agent 1x, 2x, or 3x over gold?
3. Implement a "distractor" tool — one the gold trajectory never uses. Does the scripted agent get tempted?
4. Read OSWorld-G. How would you separate grounding failures from planning failures in your own evals?
5. Read WebArena's apps README. What breaks when you upgrade one of the pinned app versions?

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| WebArena | "Web agent benchmark" | 812 tasks across 4 self-hosted apps; gym-style evaluation |
| VisualWebArena | "Visual WebArena" | Visually grounded WebArena; screenshots are observations |
| OSWorld | "Desktop agent benchmark" | 369 tasks on real Ubuntu/Windows/macOS |
| GUI grounding | "Pixel-to-element mapping" | Model localizing UI elements in 1920x1080 |
| Operational knowledge | "OS know-how" | Which menu, which shortcut, which preference pane |
| OSWorld-G | "Grounding suite" | 564 grounding-only samples + training set |
| OSWorld-Human | "Gold trajectories" | Manual expert action sequences to measure efficiency |
| Trajectory efficiency | "Steps over gold" | Agent step count divided by human minimum |

## Further Reading

- [Zhou et al., WebArena (arXiv:2307.13854)](https://arxiv.org/abs/2307.13854) — four-app web benchmark
- [Xie et al., OSWorld (arXiv:2404.07972)](https://arxiv.org/abs/2404.07972) — cross-OS desktop benchmark
- [Anthropic, Introducing computer use](https://www.anthropic.com/news/3-5-models-and-computer-use) — Claude's benchmark-shaped capability
- [OpenAI, Computer-Using Agent](https://openai.com/index/computer-using-agent/) — OSWorld and WebArena numbers

# AlphaEvolve：Evolutionary Coding 智能体

> Pair a frontier coding model with an evolutionary loop与a machine-checkable evaluator. Let the loop run long enough. It discovers a 4x4 complex-matrix multiplication procedure that uses 48 scalar multiplications：the first improvement over Strassen in 56 years. It also finds a Google-wide Borg scheduling heuristic that recovers ~0.7% of cluster compute in production. The architecture is boring on purpose. The wins come from the evaluator's rigor.

**类型：** 学习
**语言：** Python (stdlib, evolutionary-loop toy)
**前置知识：** Phase 15 · 01 (long-horizon framing), Phase 15 · 02 (self-taught reasoning)
**时间：** 约 60 minutes

## 学习目标
- 理解 AlphaEvolve：Evolutionary Coding 智能体 在本阶段课程中的作用。
- 把核心概念映射到可运行代码、测验和课程产物。
- 保留英文术语、命令、路径和 API 名称，方便和原文对照。

## 中文导读

本课是 Phase 15「自主系统」的第 03 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# AlphaEvolve — Evolutionary Coding Agents

> Pair a frontier coding model with an evolutionary loop and a machine-checkable evaluator. Let the loop run long enough. It discovers a 4x4 complex-matrix multiplication procedure that uses 48 scalar multiplications — the first improvement over Strassen in 56 years. It also finds a Google-wide Borg scheduling heuristic that recovers ~0.7% of cluster compute in production. The architecture is boring on purpose. The wins come from the evaluator's rigor.

**Type:** Learn
**Languages:** Python (stdlib, evolutionary-loop toy)
**Prerequisites:** Phase 15 · 01 (long-horizon framing), Phase 15 · 02 (self-taught reasoning)
**Time:** ~60 minutes

## The Problem

Large language models can write code. Evolutionary algorithms can search over code. Both have been tried separately for decades; both hit ceilings. The LLM ceiling is confabulation: the model writes plausible code that does not do what it claims. The evolutionary ceiling is search cost: random mutations over syntax rarely produce compilable programs, let alone better ones.

AlphaEvolve (Novikov et al., DeepMind, arXiv:2506.13131, June 2025) combines them. The LLM proposes targeted edits to a program database; an automatic evaluator scores each variant; high-scoring variants become parents for future generations. The LLM handles the expensive step of writing plausible code; the evaluator catches the confabulations. The loop runs for hours to weeks.

Results reported: 48-scalar-multiplication 4x4 complex matrix multiplication (Strassen's 1969 bound was 49), a Borg scheduling heuristic in Google production, a 32.5% FlashAttention kernel speedup, Gemini training throughput improvements.

The architecture works because the evaluator is machine-checkable. It does not work where the evaluator isn't. That asymmetry is the lesson.

## The Concept

### The loop

1. Start from a seed program `P_0` that is correct but suboptimal.
2. Maintain a database of variant programs, each scored by the evaluator.
3. Sample one or more parents from the database (MAP-elites-style or island-based).
4. Prompt the LLM (Gemini Flash for many candidates, Gemini Pro for the hard ones) to produce a modified variant of the parent.
5. Compile, run, and evaluate the variant on the held-out evaluator.
6. Insert into the database keyed by its score and feature vector.
7. Repeat.

Two details matter. First, the LLM is prompted with more than the parent program — typically several top variants from the database, plus the evaluator signature, plus a short task description. The model's job is to propose a targeted change that might improve the score. Second, the database is structured (MAP-elites grid, island-based) so the loop explores diversity, not just the current leader.

### What makes the evaluator non-negotiable

AlphaEvolve's wins all come from domains where the evaluator is fast, deterministic, and hard to game:

- **Matrix multiplication algorithm**: a unit test that multiplies matrices and checks equality bit-identically.
- **Borg scheduling heuristic**: a production-grade simulator that replays historical cluster load and measures wasted compute.
- **FlashAttention kernel**: a correctness test plus a wall-clock benchmark on real hardware.
- **Gemini training throughput**: measured GPU-seconds per step.

In each case the evaluator catches the class of LLM errors that would otherwise dominate: confabulated correctness claims, performance claims that vanish on hardware, and edge-case failures. Remove the evaluator and the loop optimizes for pretty code.

### Reward hacking is the other face of that statement

Evolution optimizes for whatever the evaluator measures. If the evaluator is imperfect, the loop will find the imperfection. In an unverified domain the loop would optimize for the surface feature, not the intended behavior. DeepMind flags this explicitly in the paper: AlphaEvolve's successes transfer only to domains where evaluator rigor matches the ambition of the search.

Concrete 2025-2026 examples of reward hacking in code-search loops:

- Optimization targets that reward "time to complete" rewarded submitting empty solutions.
- Benchmark scores that reward correctness-under-test rewarded memorizing tests and overfitting.
- A "code quality" proxy rewarded removing comments and rewriting variable names, with no semantic change.

The fix in AlphaEvolve: ship a held-out evaluator the LLM has never seen, with inputs generated at evaluation time. Even then, DeepMind recommends strong review on any proposed deployment.

### Why LLM + search beats either alone

The LLM can produce compilable, semantically plausible modifications. A random-mutation GA on a 2000-line Python file almost always produces syntax errors. The LLM also concentrates search on plausible neighborhoods (change one function, not random bytes) which dramatically reduces wasted evaluator calls.

The evaluator, in turn, catches the LLM's confabulations. LLMs will confidently claim that a function "is O(n log n) in the limit" when it is actually O(n^2); a wall-clock benchmark makes the question settled.

### Where AlphaEvolve fits in the frontier stack

| System | Generator | Evaluator | Domain | Example win |
|---|---|---|---|---|
| AlphaEvolve | Gemini | correctness + benchmark | algorithms, kernels, schedulers | 48-mul 4x4 matmul |
| FunSearch (DeepMind, 2023) | PaLM / Codey | correctness | combinatorial math | cap-set lower bounds |
| AI Scientist v2 (Sakana, L5) | GPT/Claude | LLM critique + experiment | ML research | ICLR workshop paper |
| Darwin Godel Machine (L4) | agent scaffolding | SWE-bench / Polyglot | agent code | 20% → 50% SWE-bench |

All four are variations on the same recipe: generator plus evaluator, loop. The differences are what the evaluator grades and how rigorous it is.

## Use It

`code/main.py` implements a minimal AlphaEvolve-like loop over a toy symbolic-regression problem. The "LLM" is a stdlib proxy that proposes small syntactic mutations to a program that computes a target function. The "evaluator" measures mean squared error on held-out test points.

Watch:

- How the best score improves over generations.
- How a MAP-elites grid keeps diverse solutions alive so the loop doesn't converge on a local minimum.
- How removing the held-out test (training-only evaluator) lets the loop overfit spectacularly.

## Ship It

`outputs/skill-evaluator-rigor-audit.md` is the precondition for considering an AlphaEvolve-style loop in a new domain: does your evaluator actually catch the failures you care about?

## Exercises

1. Run `code/main.py`. Note the best score trajectory. Disable the held-out evaluator (flag `--no-holdout`) and re-run. Quantify the overfitting.

2. Read Section 3 of the AlphaEvolve paper on the MAP-elites grid. Design a feature-vector descriptor for a new problem (e.g. compiler optimization passes) that would keep the search diverse.

3. The 48-multiplication 4x4 result improved on Strassen's 49-mul bound after 56 years. Read Appendix F of the paper and explain in three sentences why the evaluator for this problem is particularly easy to get right, and why most domains are not like it.

4. Propose one domain where AlphaEvolve would fail. Identify exactly where the evaluator breaks and why.

5. For a domain you know, write the evaluator signature you would use. Include (a) correctness conditions, (b) performance metric, (c) held-out input generation rule, (d) at least one anti-reward-hacking check.

## Key Terms

| Term | What people say | What it actually means |
|---|---|---|
| AlphaEvolve | "DeepMind's evolutionary coding agent" | Gemini + program database + machine-checkable evaluator |
| MAP-elites | "Diversity-preserving archive" | Grid keyed by feature vectors; each cell holds the best variant with that descriptor |
| Island model | "Parallel evolution subpopulations" | Independent populations that migrate periodically; prevents premature convergence |
| Machine-checkable evaluator | "Deterministic oracle" | A unit test, simulator, or benchmark the LLM cannot fake — a prerequisite for this loop |
| Reward hacking | "Optimizing the measure, not the goal" | Loop finds a way to maximize score without doing the intended task |
| Seed program | "The starting point" | An initial correct-but-suboptimal program the loop evolves from |
| Held-out evaluator | "Evaluation data the LLM never saw" | Inputs generated at evaluation time to prevent memorization |

## Further Reading

- [Novikov et al. (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) — the full paper.
- [DeepMind blog on AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) — vendor writeup with results.
- [AlphaEvolve results repository](https://github.com/google-deepmind/alphaevolve_results) — discovered algorithms, including the 48-mul 4x4 matmul.
- [Romera-Paredes et al. (2023). Mathematical discoveries from program search with LLMs (FunSearch)](https://www.nature.com/articles/s41586-023-06924-6) — the predecessor system.
- [Anthropic — Responsible Scaling Policy v3.0 (Feb 2026)](https://anthropic.com/responsible-scaling-policy/rsp-v3-0) — frames evaluator-bound autonomy as a key research direction.

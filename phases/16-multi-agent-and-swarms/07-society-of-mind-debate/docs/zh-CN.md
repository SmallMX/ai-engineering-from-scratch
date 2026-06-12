# Society of Mind与多智能体 Debate

> Minsky's 1986 premise：intelligence is a society of specialists：gets rediscovered every decade. In 2023 Du et al. turned it into a concrete algorithm：multiple LLM instances propose answers, read each other's answers, critique,与update. Over N rounds they converge on a consensus that beats zero-shot CoT与reflection on six reasoning与factuality tasks. Two findings matter：both **multiple agents**与**multiple rounds** contribute independently. The society beats a single-agent monologue; the multi-round exchange beats one-shot voting.

**类型：** Learn + Build
**语言：** Python (stdlib)
**前置知识：** Phase 16 · 04 (Primitive Model)
**时间：** 约 60 minutes

## 学习目标
- 理解 Society of Mind与多智能体 Debate 在本阶段课程中的作用。
- 把核心概念映射到可运行代码、测验和课程产物。
- 保留英文术语、命令、路径和 API 名称，方便和原文对照。

## 中文导读

本课是 Phase 16「多智能体与群体智能」的第 07 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Society of Mind and Multi-Agent Debate

> Minsky's 1986 premise — intelligence is a society of specialists — gets rediscovered every decade. In 2023 Du et al. turned it into a concrete algorithm: multiple LLM instances propose answers, read each other's answers, critique, and update. Over N rounds they converge on a consensus that beats zero-shot CoT and reflection on six reasoning and factuality tasks. Two findings matter: both **multiple agents** and **multiple rounds** contribute independently. The society beats a single-agent monologue; the multi-round exchange beats one-shot voting.

**Type:** Learn + Build
**Languages:** Python (stdlib)
**Prerequisites:** Phase 16 · 04 (Primitive Model)
**Time:** ~60 minutes

## Problem

Self-consistency — sample one model many times and take the majority answer — is the cheapest reasoning improvement you can bolt on. It works, but it saturates fast. You can double your samples and not see another meaningful jump.

Debate breaks the saturation. Instead of N independent samples from one model, N agents read each other's reasoning and revise. The correlation between samples drops (they are no longer i.i.d.), and the convergence point is often correct where i.i.d. voting was confidently wrong.

## Concept

### The Du et al. 2023 algorithm

From arXiv:2305.14325 (ICML 2024):

1. Each of N agents produces an initial answer to the question.
2. For round r = 2..R: each agent is shown the other agents' round r-1 answers and asked "considering these, give your updated answer."
3. After R rounds, majority-vote the final answers.

The paper tests on MMLU, GSM8K, biographies, MATH, and factuality benchmarks. Debate consistently beats CoT and Self-Reflection.

### Two independent knobs

Ablations from the same paper:

- **Agent count alone** (1 round, majority vote of N) beats single-agent on most tasks, but plateaus.
- **Round count alone** (1 agent seeing its own prior reasoning) barely helps — reflection's known weakness.
- **Both together** produces the big jumps. The multi-round exchange between multiple agents drives the gain.

### Why it works

Two mechanisms:

1. **Exposure to disagreement.** When an agent sees another agent's reasoning chain with a different conclusion, it has to either justify or update. Either way, the context for round r+1 is richer than round r.
2. **Correlated error reduction.** In self-consistency, all samples come from the same model, so the errors correlate — you average into a confidently wrong answer. Different models or different seeds decorrelate. Different *debated views* decorrelate further.

### Heterogeneous debate

A-HMAD and related follow-ups use *different base models* for different agents. Llama + Claude + GPT debating reduces monoculture collapse (Lesson 26) because the correlated errors of one model family are not shared by the others.

Downside: a weak model participating in a debate can drag the consensus toward its wrong answer (see "Should we be going MAD?", arXiv:2311.17371).

### NLSOM — the 129-agent extension

Zhuge et al. ("Mindstorms in Natural Language-Based Societies of Mind," arXiv:2305.17066) scaled this idea to 129-member societies. The result: specialization and self-organization emerge with scale, and the system outperforms single-agent on tasks like visual question answering.

### Failure modes

- **Sycophancy cascade.** All agents defer to whichever agent sounds most confident. The debate collapses to the loudest voice. Prompting for adversarial roles ("one agent must argue the counter-position") helps.
- **Topic drift.** Debates over many rounds drift from the original question. Mitigation: re-inject the question every round.
- **Compute blowup.** N agents × R rounds = N·R LLM calls, each with a context that grows. A 5-agent, 5-round debate is 25 calls at growing context. Cost per question can exceed 10× a single CoT call.

## Build It

`code/main.py` runs a 3-agent × 3-round debate on a math question where each agent starts with a different (possibly wrong) answer. Agents are scripted — each "updates" by averaging the neighbors' answers weighted by a scripted confidence. Convergence is visible in the round-by-round log.

The demo shows two key effects:

- A single round of exchange moves agents closer to the correct answer.
- Extra rounds past round 2 show diminishing returns (matches Du et al.'s plateau).

Run:

```
python3 code/main.py
```

## Use It

`outputs/skill-debate-configurator.md` configures a debate for a new task: number of agents, number of rounds, heterogeneity (same model vs mixed), role assignment (symmetric vs one-adversarial). It also estimates the token cost before you run.

## Ship It

If you ship debate:

- **Cap rounds at 3.** Du et al. show 3 rounds capture most of the gain. More is cost, not quality.
- **Cap agents at 5.** Beyond 5, context bloat and cost dominate.
- **Heterogeneous by default.** At least two different base models in the pool.
- **Adversarial slot.** One agent prompted to disagree regardless. Breaks sycophancy.
- **Log every round.** Debate systems that hide intermediate rounds cannot be debugged or audited.

## Exercises

1. Run `code/main.py`, then set the round count to 5 and watch diminishing returns. At which round does additional convergence stop?
2. Add a fourth agent with an adversarial role: always disagree with the current majority. Does this break or improve convergence?
3. Plot (print) the agreement score per round (fraction of agents on the majority answer). When does it hit 1.0 and is that equivalent to "correct"?
4. Read Du et al. Section 4 ablations. Replicate the "agents-only" vs "rounds-only" vs "both" result using this code.
5. Read "Should we be going MAD?" (arXiv:2311.17371) and list two debate variants beyond round-robin — e.g., judge-led, chain-of-debate, adversarial.

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| Society of Mind | "Minsky's idea" | Intelligence as interacting specialists; 1986 framing now operationalized via LLM debate. |
| Multi-agent debate | "Agents argue" | N agents propose, critique each other, revise over R rounds, majority-vote. |
| Consensus | "They agree" | Not epistemic truth — just fraction-on-majority-answer. Can be confidently wrong. |
| Rounds | "Exchange steps" | One round = each agent reads the others and updates once. |
| Heterogeneous debate | "Mix model families" | Using different base models to decorrelate errors. |
| Sycophancy cascade | "Everyone agrees with the loud one" | Debate failure where agents defer to the most confident agent regardless of correctness. |
| NLSOM | "129-agent society" | Natural-language society of mind; Zhuge et al.'s scaled version. |
| Correlated error | "Same model, same bug" | Why self-consistency saturates; debate across different views decorrelates. |

## Further Reading

- [Du et al. — Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) — the reference paper, ICML 2024
- [Zhuge et al. — Mindstorms in Natural Language-Based Societies of Mind](https://arxiv.org/abs/2305.17066) — 129-agent NLSOM
- [Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs](https://arxiv.org/abs/2311.17371) — benchmarks debate variants
- [Debate project page](https://composable-models.github.io/llm_debate/) — Du et al.'s code, demos, and ablation details

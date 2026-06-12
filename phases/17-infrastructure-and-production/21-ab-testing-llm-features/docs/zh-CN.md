# A/B Testing LLM Features：GrowthBook, Statsig,与the Vibes Problem

> Traditional A/B testing was not built for non-deterministic LLM. The critical distinction：evals answer "can the model do the job?" A/B tests answer "do users care?" Both are required; shipping on vibe checks is over. What to test in 2026：prompt engineering (wording), model selection (GPT-4 vs GPT-3.5 vs OSS; accuracy vs cost vs latency), generation parameters (temperature, top-p). Real cases：a chatbot reward-model variant delivered +70% conversation length与+30% retention; Nextdoor AI subject-line experiments delivered +1% CTR after reward-function refinement; Khan Academy Khanmigo iterated on a latency-vs-math-accuracy axis. Platform split：**Statsig** (acquired by OpenAI for $1.1B in September 2025)：sequential testing, CUPED, all-in-one. **GrowthBook**：open-source, warehouse-native, Bayesian + Frequentist + Sequential engines, CUPED, SRM checks, Benjamini-Hochberg + Bonferroni corrections. You pick based on warehouse-SQL preference与whether "acquired by OpenAI" matters to your organization.

**类型：** 学习
**语言：** Python (stdlib, toy sequential test simulator)
**前置知识：** Phase 17 · 13 (可观测性), Phase 17 · 20 (Progressive Deployment)
**时间：** 约 60 minutes

## 学习目标
- Distinguish evals ("can the model do the job") from A/B tests ("do users care").
- Enumerate three testable axes (prompt, model, parameters)与pick the metric for each.
- Explain CUPED, sequential testing,与Benjamini-Hochberg multiple-comparison corrections.
- Pick Statsig or GrowthBook based on warehouse-SQL posture与corporate acquisition stance.

## 中文导读

本课是 Phase 17「基础设施与生产部署」的第 21 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem

> Traditional A/B testing was not built for non-deterministic LLMs. The critical distinction: evals answer "can the model do the job?" A/B tests answer "do users care?" Both are required; shipping on vibe checks is over. What to test in 2026: prompt engineering (wording), model selection (GPT-4 vs GPT-3.5 vs OSS; accuracy vs cost vs latency), generation parameters (temperature, top-p). Real cases: a chatbot reward-model variant delivered +70% conversation length and +30% retention; Nextdoor AI subject-line experiments delivered +1% CTR after reward-function refinement; Khan Academy Khanmigo iterated on a latency-vs-math-accuracy axis. Platform split: **Statsig** (acquired by OpenAI for $1.1B in September 2025) — sequential testing, CUPED, all-in-one. **GrowthBook** — open-source, warehouse-native, Bayesian + Frequentist + Sequential engines, CUPED, SRM checks, Benjamini-Hochberg + Bonferroni corrections. You pick based on warehouse-SQL preference and whether "acquired by OpenAI" matters to your organization.

**Type:** Learn
**Languages:** Python (stdlib, toy sequential test simulator)
**Prerequisites:** Phase 17 · 13 (Observability), Phase 17 · 20 (Progressive Deployment)
**Time:** ~60 minutes

## Learning Objectives

- Distinguish evals ("can the model do the job") from A/B tests ("do users care").
- Enumerate three testable axes (prompt, model, parameters) and pick the metric for each.
- Explain CUPED, sequential testing, and Benjamini-Hochberg multiple-comparison corrections.
- Pick Statsig or GrowthBook based on warehouse-SQL posture and corporate acquisition stance.

## The Problem

You hand-tuned a system prompt. It feels better. You ship it. Conversion changes by noise. You blame the metric. Or you shipped a new model and conversion didn't move — did the model degrade or was the change too small to detect? You don't know, because you shipped without an A/B.

Evals answer whether the model can do a task on a labeled set. They do not answer whether users prefer the output. Only a controlled online experiment answers that, and only if the experiment has enough power, controls for non-determinism, and corrects for multiple comparisons.

## The Concept

### Evals vs A/B tests

**Evals** — offline, labeled set, judge (rubric or LLM-as-judge or human). Answer: "Is the output correct / helpful / safe on this fixed distribution?"

**A/B test** — online, live users, randomized. Answer: "Does the new variant move the user-level metric that matters?"

Both required. Evals catch regressions before exposure; A/B confirms product impact after.

### What to test

1. **Prompt engineering** — wording, system-prompt structure, examples. Metric: task success, user retention, cost/request.
2. **Model selection** — GPT-4 vs GPT-3.5-Turbo vs Llama-OSS. Metric: accuracy (task) + cost/request + latency P99. Multi-objective.
3. **Generation parameters** — temperature, top-p, max_tokens. Metric: task-specific (output diversity vs determinism).

### CUPED — variance reduction

Controlled-experiments Using Pre-Experiment Data. Regress out pre-period variance before comparing post-period. Typical variance reduction: 30-70%. Effective sample size goes up for free.

Implementation: both Statsig and GrowthBook implement.

### Sequential testing

Classical A/B assumes fixed sample size. Sequential tests ("peek-and-decide") control false-positive rate under repeated looks. Always-valid sequential procedures (mSPRT, Howard's confidence sequences) let you stop early on clear winners.

### Multiple-comparison corrections

Running 20 A/B tests at 95% confidence produces one false positive by chance. Bonferroni correction tightens α per-test; Benjamini-Hochberg controls false-discovery rate. GrowthBook implements both.

### SRM — sample ratio mismatch

Assignment hash randomizes users to variants. If 50/50 split delivers 47/53, something is broken — SRM check flags it. Both platforms implement.

### Statsig vs GrowthBook

**Statsig**:
- Acquired by OpenAI for $1.1B (September 2025). Hosted, SaaS.
- Sequential testing, CUPED, held-out populations.
- All-in-one: feature flags + experimentation + observability.
- Best fit: team already wants a bundled product, doesn't care about OpenAI ownership.

**GrowthBook**:
- Open-source (MIT); warehouse-native (reads from Snowflake/BigQuery/Redshift directly).
- Multiple engines: Bayesian, Frequentist, Sequential.
- CUPED, SRM, Bonferroni, BH corrections.
- Self-host or managed cloud.
- Best fit: warehouse-SQL shop, data team controls the metric layer, wants OSS.

### Non-determinism complicates power

Same prompt produces varying outputs. Traditional power calculations assume IID observations. With LLM non-determinism, effective sample size is lower than nominal. Multiply required sample size by ~1.3-1.5x as a safety margin.

### Real case outcomes

- Chatbot reward model variant: +70% conversation length, +30% retention.
- Nextdoor subject lines: +1% CTR after reward-function refinement.
- Khan Academy Khanmigo: iterative latency-vs-math-accuracy trade.

### The anti-pattern: shipping on vibes

Every senior engineer can name a feature that was shipped because "it feels better" with no A/B. Most of them regressed product metrics the team didn't notice for months. A/B is the forcing function.

### Numbers you should remember

- Statsig acquired by OpenAI: $1.1B, September 2025.
- GrowthBook: open-source MIT; Bayesian + Frequentist + Sequential.
- CUPED variance reduction: 30-70%.
- LLM non-determinism → +30-50% sample-size buffer.

## Use It

`code/main.py` simulates a sequential A/B test with fixed and sequential boundaries. Shows how sequential lets you stop early.

## Ship It

This lesson produces `outputs/skill-ab-plan.md`. Given feature change, workload, baseline, picks platform, gates, sample size.

## Exercises

1. Run `code/main.py`. For an expected 5% lift with baseline 3% conversion, what sample size to 80% power?
2. Pick Statsig or GrowthBook for a healthcare-regulated on-prem customer.
3. Design an A/B that tests GPT-4 vs GPT-3.5 on cost-per-resolved-ticket. What's the primary metric, guardrail metric, secondary?
4. Your canary passes but A/B shows -1.2% conversion. Do you ship? Write the escalation criteria.
5. Apply CUPED to a pre-period with 60% of the variance of post. Compute the effective-sample-size boost.

## Key Terms

| Term | What people say | What it actually means |
|------|----------------|------------------------|
| Eval | "offline test" | Labeled-set evaluation of model capability |
| A/B test | "experiment" | Live randomized comparison on users |
| CUPED | "variance reduction" | Pre-period regression to reduce variance |
| Sequential test | "peek-ok test" | Always-valid procedure allowing early stop |
| Multiple comparison | "the family error" | Running many tests inflates false positives |
| Bonferroni | "tight correction" | Divide α by number of tests |
| Benjamini-Hochberg | "BH FDR" | False-discovery-rate control, less conservative |
| SRM | "bad split" | Sample ratio mismatch; assignment bug |
| Statsig | "OpenAI owned" | Commercial all-in-one, acquired 2025 |
| GrowthBook | "the OSS one" | MIT warehouse-native platform |
| mSPRT | "sequential probability ratio test" | Classical sequential procedure |

## Further Reading

- [GrowthBook — How to A/B Test AI](https://blog.growthbook.io/how-to-a-b-test-ai-a-practical-guide/)
- [Statsig — Beyond Prompts: Data-Driven LLM Optimization](https://www.statsig.com/blog/llm-optimization-online-experimentation)
- [Statsig vs GrowthBook comparison](https://www.statsig.com/perspectives/ab-testing-feature-flags-comparison-tools)
- [Deng et al. — CUPED](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf)
- [Howard — Confidence Sequences](https://arxiv.org/abs/1810.08240)

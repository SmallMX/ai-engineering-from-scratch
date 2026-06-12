# Anthropic Responsible 扩展 Policy v3.0

> RSP v3.0 went into effect February 24, 2026, replacing the 2023 policy. Two-tier mitigation：what Anthropic will do unilaterally vs what is framed as an industry-wide recommendation (including RAND SL-4 security standards). Adds Frontier 安全 Roadmaps与Risk Reports as standing documents rather than one-off deliverables. Drops the 2023 pause commitment. Introduces the AI R&D-4 threshold：once crossed, Anthropic must publish an affirmative case identifying misalignment risks与mitigations. Claude Opus 4.6 does not cross it. Anthropic states in the v3.0 announcement that "confidently ruling this out is becoming difficult." SaferAI rated the 2023 RSP at 2.2; they downgraded v3.0 to 1.9, putting Anthropic in the "weak" RSP category alongside OpenAI与DeepMind. Qualitative thresholds replaced the 2023 quantitative commitments; removing the pause clause is the sharpest regression.

**类型：** 学习
**语言：** Python (stdlib, RSP threshold decision engine)
**前置知识：** Phase 15 · 06 (AAR), Phase 15 · 07 (RSI)
**时间：** 约 45 minutes

## 学习目标
- 理解 Anthropic Responsible 扩展 Policy v3.0 在本阶段课程中的作用。
- 把核心概念映射到可运行代码、测验和课程产物。
- 保留英文术语、命令、路径和 API 名称，方便和原文对照。

## 中文导读

本课是 Phase 15「自主系统」的第 19 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Anthropic Responsible Scaling Policy v3.0

> RSP v3.0 went into effect February 24, 2026, replacing the 2023 policy. Two-tier mitigation: what Anthropic will do unilaterally vs what is framed as an industry-wide recommendation (including RAND SL-4 security standards). Adds Frontier Safety Roadmaps and Risk Reports as standing documents rather than one-off deliverables. Drops the 2023 pause commitment. Introduces the AI R&D-4 threshold: once crossed, Anthropic must publish an affirmative case identifying misalignment risks and mitigations. Claude Opus 4.6 does not cross it. Anthropic states in the v3.0 announcement that "confidently ruling this out is becoming difficult." SaferAI rated the 2023 RSP at 2.2; they downgraded v3.0 to 1.9, putting Anthropic in the "weak" RSP category alongside OpenAI and DeepMind. Qualitative thresholds replaced the 2023 quantitative commitments; removing the pause clause is the sharpest regression.

**Type:** Learn
**Languages:** Python (stdlib, RSP threshold decision engine)
**Prerequisites:** Phase 15 · 06 (AAR), Phase 15 · 07 (RSI)
**Time:** ~45 minutes

## The Problem

Frontier labs publish scaling policies that are partly technical documents, partly governance documents, and partly signals to regulators. RSP v3.0 is the current Anthropic document. Reading it closely matters not because compliance with it is binding (it is not), but because the framing shapes how a lab conceives of catastrophic risk and how they communicate trade-offs to the public.

The v3.0 vs v2.0 diff is the useful unit. What got added: Frontier Safety Roadmaps, Risk Reports, the AI R&D-4 threshold. What got removed: the 2023 pause commitment. What got reframed: a two-tier mitigation schedule split between Anthropic-unilateral and industry-recommendation. External review — SaferAI — downgraded the score from 2.2 (v2) to 1.9 (v3.0). This is how a scaling policy can get less rigorous while looking more polished.

## The Concept

### The two-tier mitigation schedule

- **Anthropic unilateral actions**: what Anthropic will do regardless of what other labs do. Training stops above a threshold, specific security measures, specific deployment gates.
- **Industry-wide recommendations**: what Anthropic thinks the industry should do collectively. Includes RAND SL-4 security standards. These are not commitments on Anthropic's side; they are policy advocacy.

The two-tier structure was not in v2. It means that a reader needs to look at which column each commitment lives in. A security measure in the "industry-wide recommendation" column is not Anthropic's promise; it is Anthropic's hope.

### The AI R&D-4 threshold

This is the capability level RSP v3.0 names as the important next threshold. Specifically: a model that could automate a substantial fraction of AI research at competitive cost. Once Anthropic believes a model crosses it, they must publish an affirmative case identifying misalignment risks and mitigations before continued scaling.

Claude Opus 4.6 does not cross it per the v3.0 announcement. The document adds: "confidently ruling this out is becoming difficult." That phrasing matters; it concedes that the threshold is close enough to be a live concern, not a speculative limit.

Lesson 6 (Automated Alignment Research) and Lesson 7 (Recursive Self-Improvement) feed directly into this threshold. Automated alignment researchers crossing research-quality bars is evidence that the AI R&D-4 threshold is approaching.

### Frontier Safety Roadmaps and Risk Reports

v3.0 elevates two artifact types to standing documents:

- **Frontier Safety Roadmap**: forward-looking document describing planned safety work, capability expectations, and mitigation research.
- **Risk Report**: retrospective document on specific models after release, describing observed capability and residual risk.

Both are public. Both are updated on a declared cadence. The utility is: reader can track how what Anthropic said they would do in a Roadmap compares to what they report in a Risk Report.

### Removing the pause clause

The 2023 RSP included an explicit pause commitment: if a model crossed specific capability thresholds, training would pause until mitigations were in place. v3.0 replaces the explicit pause with a softer formulation (publish an affirmative case, proceed if mitigations are adequate). SaferAI and other analysts called this out directly as the strongest regression in the new document.

The policy argument for the change: quantitative thresholds in 2023 turned out to be unreachable by 2026-era capability benchmarks because the benchmarks themselves were re-scaled. The counter-argument: a pause clause in a scaling policy is a commitment device; removing it removes the credibility of the policy.

### SaferAI's downgrade

SaferAI is an independent organization that rates RSP-style documents. Their public rating: 2023 Anthropic RSP scored 2.2 (out of a scale where 4.0 is the best current RSP and 1.0 is nominal). v3.0 scored 1.9. This moved Anthropic from "moderate" to "weak," joining OpenAI and DeepMind in the weak category.

The downgrade factors per SaferAI:
- Qualitative thresholds replaced quantitative ones.
- Pause commitment removed.
- AI R&D-4 threshold mitigations are described as "affirmative case" rather than specific measures.
- Review mechanisms depend on Anthropic's Safety Advisory Group, with limited independent oversight.

### What this lesson is not

This is not a lesson in compliance. RSP v3.0 is not a regulation; nothing forces Anthropic to follow it. The lesson is in reading the document with the specificity and skepticism it deserves. Scaling policies are the primary public signal frontier labs emit about catastrophic-risk posture. Reading them well is a practical skill for anyone whose work depends on frontier capabilities.

## Use It

`code/main.py` implements a small decision engine that mirrors the RSP threshold-evaluation shape: given a candidate model and a set of capability measurements, return whether the AI R&D-4 threshold is crossed, the required affirmative-case sections, and whether deployment can proceed. It's intentionally simple; the point is to make the document's logic explicit.

## Ship It

`outputs/skill-scaling-policy-review.md` reviews a scaling policy (Anthropic, OpenAI, DeepMind, or internal) against the v3.0 reference: two-tier structure, thresholds, pause commitments, independent review.

## Exercises

1. Run `code/main.py`. Feed in three synthetic models at different capability levels. Confirm the threshold evaluator behaves as expected and produces the right affirmative-case template.

2. Read RSP v3.0 in full (32 pages). Identify every commitment that lives in the "industry-wide recommendation" tier. Which of those commitments would have been "Anthropic unilateral" in v2?

3. Read SaferAI's RSP grading methodology. Reproduce their 1.9 score for v3.0 by applying their rubric to the document. Which rubric row drove the downgrade most?

4. The 2023 pause commitment was removed. Propose a replacement commitment that preserves the credibility of the policy while acknowledging the 2026 benchmark-rescaling problem.

5. Compare RSP v3.0 to OpenAI Preparedness Framework v2 (Lesson 20). Pick one area where v3.0 is stronger. Pick one area where the Preparedness Framework is stronger.

## Key Terms

| Term | What people say | What it actually means |
|---|---|---|
| RSP | "Anthropic's scaling policy" | Responsible Scaling Policy; v3.0 effective Feb 24, 2026 |
| AI R&D-4 | "Research-automation threshold" | Capability to automate substantial AI research at competitive cost |
| Affirmative case | "Safety justification" | Published argument that risks are identified and mitigations adequate |
| Frontier Safety Roadmap | "Forward plan" | Standing document on planned safety work and expected capabilities |
| Risk Report | "Retrospective on a model" | Standing document on observed capability and residual risk after release |
| Two-tier mitigation | "Unilateral vs industry" | Anthropic commitments vs industry recommendations, separated |
| Pause commitment | "2023 clause" | Explicit promise to pause training; removed in v3.0 |
| SaferAI rating | "Independent RSP grade" | Third-party rubric; v3.0 scored 1.9 (v2 was 2.2) |

## Further Reading

- [Anthropic — Responsible Scaling Policy v3.0](https://anthropic.com/responsible-scaling-policy/rsp-v3-0) — the full 32-page policy.
- [Anthropic — RSP v3.0 announcement](https://www.anthropic.com/news/responsible-scaling-policy-v3) — summary of changes from v2.
- [Anthropic — Frontier Safety Roadmap](https://www.anthropic.com/research/frontier-safety) — standing document linked from RSP v3.0.
- [Anthropic — Risk Report: Claude Opus 4.6](https://www.anthropic.com/research/risk-report-claude-opus-4-6) — retrospective on the current frontier model.
- [Anthropic — Measuring agent autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy) — connects AI R&D-4 to measured autonomy.

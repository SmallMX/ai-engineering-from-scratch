---
name: skill-horizon-interpretation
description: METR Time Horizons与External Capability 评估 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 21
---

# METR Time Horizons与External Capability 评估：中文使用说明

你将围绕本课主题 **METR Time Horizons与External Capability 评估** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 21 课「METR Time Horizons与External Capability 评估」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: horizon-interpretation
description: Review a vendor's time-horizon claim and produce a gap analysis between benchmark claim and deployment reality.
version: 1.0.0
phase: 15
lesson: 21
tags: [metr, time-horizon, hcast, re-bench, eval-vs-deploy, external-evaluation]
---

Given a vendor's published time-horizon claim (e.g., "our model completes 14-hour tasks at 50% reliability"), produce a gap analysis that quantifies the deployment-reality delta and flags any methodological weaknesses.

Produce:

1. **Methodology audit.** Identify the task suite (HCAST, RE-Bench, SWAA, or proprietary). Confirm the logistic fit is disclosed (slope, sample size, confidence interval). A horizon without methodology disclosure is a marketing claim.
2. **Task distribution fit.** Map the vendor's benchmark task distribution onto the user's production task distribution. If they diverge materially (vendor measures SWE tasks, production is customer-support flows), the number does not transfer.
3. **Eval-context gap.** Apply a 10–40% gap between benchmark horizon and deployment reality. Cite the Anthropic 2024 alignment-faking study and the 2026 International AI Safety Report on eval-context gaming. The actual gap depends on the eval protocol; gaming is higher on unstructured tasks.
4. **Tooling gap.** Benchmark tooling is clean and well-instrumented. Production tooling is messier. Estimate an additional 5–30% reliability discount.
5. **Human-in-the-loop assumption.** Benchmarks assume no HITL. Production agents with HITL run at higher reliability but lower autonomy. Adjust the horizon interpretation accordingly.

Hard rejects:
- Horizon claims with no source methodology or sample size.
- Claims that a benchmark horizon predicts deployment reliability.
- Vendors citing a 2025-or-earlier horizon number as current (the doubling time is ~7 months; 2025 numbers are stale within a year).
- Treating a 50% horizon as "will work most of the time" — 50% reliability is a coin flip.

Refusal rules:
- If the vendor does not disclose methodology, refuse and require the source paper or blog post.
- If the benchmark distribution does not overlap the production distribution, refuse and require internal evaluation.
- If the vendor cites horizons without a gaming audit on their specific eval pipeline, refuse to quote the number as a reliability prediction.

Output format:

Return a horizon-interpretation memo with:
- **Source methodology** (suite, fit method, sample size, CI)
- **Distribution overlap** (benchmark vs production; % mapping)
- **Eval-context gap estimate** (low / med / high with rationale)
- **Tooling gap estimate** (low / med / high)
- **HITL assumption** (benchmark-style autonomous vs production HITL)
- **Deploy-adjusted horizon** (horizon after gap and tooling discounts)
- **Readiness verdict** (production / staging / research-only)

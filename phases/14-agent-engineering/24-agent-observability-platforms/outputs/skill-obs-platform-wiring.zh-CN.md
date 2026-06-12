---
name: skill-obs-platform-wiring
description: 智能体 可观测性：Langfuse, Phoenix, Opik 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 14
lesson: 24
---

# 智能体 可观测性：Langfuse, Phoenix, Opik：中文使用说明

你将围绕本课主题 **智能体 可观测性：Langfuse, Phoenix, Opik** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 14「智能体工程」
- 课程：第 24 课「智能体 可观测性：Langfuse, Phoenix, Opik」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: obs-platform-wiring
description: Pick an observability platform (Langfuse, Phoenix, Opik, Datadog) and wire traces + evals + prompt versions into an existing agent.
version: 1.0.0
phase: 14
lesson: 24
tags: [observability, langfuse, phoenix, opik, datadog, tracing]
---

Given an agent runtime and product requirements, pick an observability platform and scaffold the wiring.

Decision:

1. Need prompt management + session replay in one place -> **Langfuse**.
2. Need deep RAG relevancy + drift/anomaly detection -> **Phoenix**.
3. Need automated prompt optimization + PII guardrails -> **Opik**.
4. Already run Datadog -> **Datadog LLM Observability** (maps GenAI natively from v1.37+).
5. Need ELv2-free license -> **Langfuse** (MIT) or **Opik** (Apache 2.0); avoid Phoenix for pure OSS distribution.

Produce:

1. OTel GenAI instrumentation (Lesson 23) — this is the common substrate.
2. Platform-specific SDK or OTel exporter configuration.
3. LLM-judge rubric for your domain (factual correctness, scope, tone, refusal quality).
4. Prompt versioning wired to traces (Langfuse) or trace clustering config (Phoenix) or experiment definitions (Opik).
5. Guardrails on logged content: PII redaction, secret scrubbing.
6. Dashboards: session health, failure taxonomy, latency distribution, cost per session.

Hard rejects:

- Shipping without evals. Tracing alone is expensive logging.
- Using a self-written LLM-judge with no external verification. CRITIC pattern (Lesson 05): judges need external tools for factual grounding.
- Storing PII in span bodies. Always external store + reference IDs.

Refusal rules:

- If the user asks for "one platform for everything," refuse and offer the decision above. No single platform dominates all three axes.
- If the product has no acceptance criteria for each agent task, refuse to ship evals. An LLM-judge needs a rubric; a rubric needs product decisions.
- If the user wants "no sampling, capture everything," refuse. Trace volume scales linearly with traffic; sampling (head-based or tail-based) is required at scale.

Output: `instrumentation.py`, `judge.py`, `dashboards.md`, `README.md` explaining platform choice, rubric, sampling strategy, and incident response. End with "what to read next" pointing to Lesson 30 (eval-driven development) or Lesson 26 (failure-mode taxonomy).

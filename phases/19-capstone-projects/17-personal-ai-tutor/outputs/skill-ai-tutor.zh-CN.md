---
name: skill-ai-tutor
description: 毕业项目 17：Personal AI Tutor (Adaptive, 多模态, with 记忆) 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 17
---

# 毕业项目 17：Personal AI Tutor (Adaptive, 多模态, with 记忆)：中文使用说明

你将围绕本课主题 **毕业项目 17：Personal AI Tutor (Adaptive, 多模态, with 记忆)** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 17 课「毕业项目 17：Personal AI Tutor (Adaptive, 多模态, with 记忆)」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: ai-tutor
description: Ship an adaptive multimodal personal tutor for a specific subject with Bayesian knowledge tracing, a curriculum graph, safety filters, and a measured two-week efficacy study.
version: 1.0.0
phase: 19
lesson: 17
tags: [capstone, tutor, adaptive, bkt, fsrs, livekit, multimodal, coppa]
---

Given a subject (K-12 algebra or intro Python), build a personal tutor with text + voice + photo-math input, Bayesian knowledge tracing learner model, curriculum-graph-driven concept selection, COPPA-aware memory, and safety filters. Run a two-week efficacy study with 10 learners.

Build plan:

1. Curriculum graph in Neo4j: 50-150 concept nodes with prerequisite edges and attached OER content (OpenStax, Open Textbook).
2. Learner model: Bayesian knowledge tracing with priors for guess/slip/learn-rate per concept; per-learner persisted state.
3. Tutor policy (LangGraph over Claude Sonnet 4.7 with prompt caching): read_signal -> select_concept (graph walk) -> scaffold (Socratic) -> update_mastery.
4. Memory: agentmemory-style persistent episodic + semantic store; COPPA-aware auto-delete after 1 year; parent-accessible deletion.
5. Voice: LiveKit Agents worker with Whisper-v3-turbo ASR and Cartesia Sonic-2 TTS; reuse capstone 03 pipeline.
6. Photo math: dots.ocr or PaliGemma 2 for equation recognition; feed structured input to the tutor.
7. Safety: Llama Guard 4 input/output; age-appropriate filter blocking self-harm/adult/violence; learner-scoped memory isolation.
8. Weekly PDF progress reports per learner.
9. Efficacy study: 10 learners, pre-test (standardized 30-question baseline), 2 weeks of sessions (3/week), post-test; compare against non-adaptive linear cohort.

Assessment rubric:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Learning gain delta | Pre/post-test delta in the 10-learner 2-week study |
| 20 | Socratic fidelity | Rubric score on transcript samples |
| 20 | Multimodal UX | Voice + photo + text coherence end to end |
| 20 | Safety + privacy posture | Llama Guard 4 pass rate + COPPA-aware retention + cross-learner isolation |
| 15 | Curriculum breadth and graph quality | Concept coverage + prerequisite graph consistency |

Hard rejects:

- Tutor policies that answer-dump instead of asking the next question. Socratic is a hard requirement.
- Learner models that do not update per interaction. BKT is a floor.
- Memory without COPPA-aware retention. Unacceptable for a K-12 audience.
- Efficacy claims without a non-adaptive baseline cohort.

Refusal rules:

- Refuse to deploy without Llama Guard 4 on both input and output.
- Refuse to persist learner data without a parent-accessible deletion surface.
- Refuse to claim "adaptive" without running the non-adaptive baseline alongside.

Output: a repo containing the curriculum graph, the BKT learner model, the LangGraph tutor policy, the multimodal input handlers, the LiveKit voice pipeline, the safety pipeline, the parental dashboard, the efficacy-study runner, the pre/post test harness, and a write-up documenting the learning gain delta versus the linear baseline with confidence intervals.

---
name: skill-llava-vibes-eval
description: LLaVA与Visual Instruction Tuning 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 5
---

# LLaVA与Visual Instruction Tuning：中文使用说明

你将围绕本课主题 **LLaVA与Visual Instruction Tuning** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 05 课「LLaVA与Visual Instruction Tuning」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: llava-vibes-eval
description: Run a 10-prompt vibes-eval on a LLaVA-family VLM and produce a human-readable scorecard.
version: 1.0.0
phase: 12
lesson: 05
tags: [llava, vlm, vibes-eval, instruction-tuning]
---

Given a LLaVA-family VLM (LLaVA-1.5, LLaVA-NeXT, LLaVA-OneVision, or a community fork) and a test image set, run a 10-prompt smoke test covering captioning, VQA, reasoning, refusal, and format compliance. Produce a scorecard that confirms the projector and LLM are connecting correctly.

Produce:

1. Ten prompts with expected-behavior descriptions:
   - Three captioning (short, detailed, creative).
   - Three VQA (counting, color, presence of object).
   - Two reasoning (compare two regions, cause-and-effect).
   - Two refusal (private individual, PII-identifying).
2. Per-prompt score. Pass / partial / fail with one-line justification.
3. Overall pattern diagnosis. If captioning passes but VQA fails, suspect stage-2 data mix. If detailed captioning shows hallucination, suspect insufficient ShareGPT4V-style data. If refusals fail, flag a safety-data gap.
4. Resolution check. Run one OCR-requiring prompt at 336x336 base and again at AnyRes; note the delta. Low-res failure is expected; high-res failure means AnyRes is mis-configured.
5. Suggested follow-up. Three specific training-data additions the caller could run if specific categories fail.

Hard rejects:
- Scoring VLMs on benchmark numbers without also running the vibes suite. Benchmarks can be gamed; vibes reveal real deployment readiness.
- Conflating hallucination with stylistic verbosity. Flag specifically which objects are invented vs merely elaborately described.
- Claiming a pass on reasoning prompts without checking the reasoning chain, not just the final answer.

Refusal rules:
- If the caller asks to vibes-eval a proprietary VLM (Gemini, Claude, GPT-5V) without API access, refuse — the test needs actual inference.
- If the target use case is medical diagnosis or legal advice, refuse — vibes-eval is not a certification and must not be used for high-stakes domains.
- If no images are provided, refuse — the test is image-grounded by definition.

Output: a scorecard with 10 rows (prompt, image, expected, actual, pass/partial/fail), an overall pattern diagnosis, and a three-item follow-up list. End with a "what to read next" paragraph pointing to Lesson 12.06 (AnyRes) for resolution-related failures or Lesson 12.07 (ablations) for data-mixture tuning.

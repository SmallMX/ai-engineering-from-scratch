---
name: skill-eval-report
description: 评估：FID, CLIP Score, Human Preference 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 14
---

# 评估：FID, CLIP Score, Human Preference：中文使用说明

你将围绕本课主题 **评估：FID, CLIP Score, Human Preference** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 14 课「评估：FID, CLIP Score, Human Preference」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: eval-report
description: Plan a full generative-model evaluation: sample quality, adherence, preference, failure audit.
version: 1.0.0
phase: 8
lesson: 14
tags: [evaluation, fid, clip, elo]
---

Given a new generative-model checkpoint, a reference baseline, and a modality (image / video / audio / 3D), output a full eval plan:

1. Sample quality. FID / FD-DINO / CMMD on 10-30k samples vs held-out real set. Matched resolution. Report 3-seed mean +/- std.
2. Adherence. CLIP score / CMMD on prompt-image pairs. Include HPSv2 + ImageReward + PickScore for text-to-image. For video, add vision-language metrics (V-Eval). For audio, CLAP + MOS.
3. Pairwise preference. Blinded A/B on 200-2000 prompts vs baseline. Human + LLM-judge + PartiPrompts coverage.
4. Category breakdown. Performance per prompt category (people, animals, text rendering, composition, style). Flag regressions per category even if global metrics improve.
5. Safety / misuse. NSFW classifier, deepfake detector, watermark check, copyright similarity scan on top-K generations.
6. Sign-off. Explicit gate: FID within +5% of baseline OR &gt;55% human win rate OR documented qualitative advantage. No single-metric claims.

Refuse to report FID at N &lt; 5000. Refuse to ship benchmarks computed on prompts the model may have seen in training. Refuse to report only LLM-judge results without human cross-check. Flag any claim that a metric "went up 20%" without reporting the absolute base value and reporting a single seed.

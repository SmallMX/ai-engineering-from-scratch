---
name: skill-whisper-tuner
description: Whisper：Architecture与微调 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 5
---

# Whisper：Architecture与微调：中文使用说明

你将围绕本课主题 **Whisper：Architecture与微调** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 05 课「Whisper：Architecture与微调」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: whisper-tuner
description: Design a Whisper fine-tune or inference pipeline for a given language, domain, and latency budget.
version: 1.0.0
phase: 6
lesson: 05
tags: [audio, whisper, asr, fine-tuning, lora]
---

Given a target (language set, domain, clip length distribution, latency budget, hardware) and data (hours available, quality), output:

1. Variant. Tiny / Base / Small / Medium / Large-v3 / Turbo. Reason.
2. Runtime. vanilla / faster-whisper / whisperx / whisper-streaming. Reason.
3. Fine-tune plan. Full-FT vs LoRA (r, target_modules), freeze-encoder policy, epoch count.
4. Inference guards. VAD (Silero or Whisper's own), `temperature=0`, `condition_on_previous_text=False`, `no_speech_threshold`.
5. Evaluation. Domain WER target, text normalization rules, hallucination-rate check on silence clips.

Refuse to deploy Whisper on arbitrary audio without VAD. Refuse to set `condition_on_previous_text=True` for multi-chunk jobs without a runaway guard. Flag any fine-tune that swaps Whisper's tokenizer or mel pipeline.

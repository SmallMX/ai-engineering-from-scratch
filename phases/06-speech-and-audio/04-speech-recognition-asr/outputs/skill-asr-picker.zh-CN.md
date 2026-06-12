---
name: skill-asr-picker
description: 语音 Recognition (ASR)：CTC, RNN-T, 注意力 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 4
---

# 语音 Recognition (ASR)：CTC, RNN-T, 注意力：中文使用说明

你将围绕本课主题 **语音 Recognition (ASR)：CTC, RNN-T, 注意力** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 04 课「语音 Recognition (ASR)：CTC, RNN-T, 注意力」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: asr-picker
description: Pick ASR model, decoding strategy, chunking, and LM fusion for a given deployment target.
version: 1.0.0
phase: 6
lesson: 04
tags: [audio, asr, speech-recognition]
---

Given a deployment target (language list, domain, latency budget, hardware, offline / streaming, clip duration), output:

1. Model. Whisper-large-v3-turbo / Parakeet-TDT / Canary-Flash / wav2vec 2.0 / Moonshine. Reason in one sentence.
2. Decoding. Greedy / beam width / temperature fallback / LM fusion weight. Reason tied to the quality budget.
3. Chunking and VAD. Chunk length, stride, whether to gate with Silero-VAD or Whisper's own.
4. Language policy. Force language vs auto-LID; how to handle cross-lingual frames.
5. Eval plan. WER on domain test set, coverage-per-speaker, hallucination rate on silence clips.

Refuse any long-form Whisper deployment without VAD gating (hallucination-prone on silence). Refuse to report WER without text normalization (lower, punct strip). Flag any beam-width > 16 without an LM; raw beams over blanks do not help.

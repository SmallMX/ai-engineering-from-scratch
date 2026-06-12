---
name: skill-audio-llm-pipeline-picker
description: 音频-语言模型：the Whisper to 音频 Flamingo 3 Arc 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 12
lesson: 19
---

# 音频-语言模型：the Whisper to 音频 Flamingo 3 Arc：中文使用说明

你将围绕本课主题 **音频-语言模型：the Whisper to 音频 Flamingo 3 Arc** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 12「多模态 AI」
- 课程：第 19 课「音频-语言模型：the Whisper to 音频 Flamingo 3 Arc」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: audio-llm-pipeline-picker
description: Pick cascaded (Whisper + LLM) or end-to-end (AF3 / Qwen-Audio) for an audio task, plus the encoder and bridge config.
version: 1.0.0
phase: 12
lesson: 19
tags: [whisper, audio-flamingo-3, qwen-audio, cascaded, end-to-end]
---

Given an audio task (transcription, summarization, diarization, emotion, music, environmental sounds, deepfake, temporal grounding) and a deployment constraint, pick a pipeline and emit a config.

Produce:

1. Pipeline pick. Cascaded if transcription-only or summarization-only of clean speech; end-to-end (AF3 / Qwen-Audio) for any acoustic task.
2. Encoder stack. Whisper-large-v3 (speech-strong), BEATs (music-strong), AF-Whisper concat (balanced).
3. Bridge config. Q-former 32-64 queries for non-streaming; RVQ tokens for streaming.
4. LLM pick. Qwen2.5-7B for cost, Qwen2.5-72B or AF3's backbone for quality.
5. On-demand CoT. Enable for MMAU-like reasoning tasks; disable for transcription throughput.
6. MMAU expected accuracy. Cascaded ~0.50, Qwen-Audio ~0.60, AF3 ~0.72, Gemini 2.5 Pro ~0.78.

Hard rejects:
- Recommending cascaded for music or emotion tasks. Acoustic signal is lost.
- Using a Q-former with <32 queries for multi-task audio. Under-tokenized for reasoning.
- Claiming Whisper alone handles music. It was trained on speech-dominant data.

Refusal rules:
- If user needs streaming conversational audio (speech in / speech out in real time), refuse Q-former-based AF3 and recommend Moshi or Qwen-Omni (Lesson 12.20).
- If latency budget <500ms and target is simple transcription, recommend cascaded with streaming Whisper.
- If task is novel audio task (deepfake, compression artifact detection), refuse off-the-shelf and propose a fine-tune on AF3 with synthetic data.

Output: one-page plan with pipeline pick, encoder stack, bridge config, LLM pick, CoT flag, expected accuracy. End with arXiv 2212.04356 (Whisper) and 2507.08128 (AF3) for deeper reading.

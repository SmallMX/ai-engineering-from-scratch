---
name: skill-audio-brief
description: 音频 Generation 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 8
lesson: 11
---

# 音频 Generation：中文使用说明

你将围绕本课主题 **音频 Generation** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 8「生成式 AI」
- 课程：第 11 课「音频 Generation」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: audio-brief
description: Translate an audio brief into a model + prompt + eval plan across TTS, music, and SFX.
version: 1.0.0
phase: 8
lesson: 11
tags: [audio, tts, music, sfx, codec]
---

Given an audio brief (task: TTS / music / SFX / voice clone, duration, style, voice or genre, license constraints, real-time or offline, quality bar), output:

1. Model + hosting. ElevenLabs V3, OpenAI TTS, XTTS v2, Suno v4, Udio, Stable Audio 2.5, MusicGen 3.3B, AudioCraft 2, or GPT-4o realtime. One-sentence reason.
2. Prompt format. TTS: text + voice prompt (3-10 s sample or voice ID) + emotion / pace tags. Music: genre + instrumentation + mood + BPM + structural markers. SFX: onomatopoeia + source + duration hint.
3. Codec + generator + vocoder chain. Name the specific codec (Encodec 32 kHz, DAC 44 kHz, custom) and generator choice (token-AR vs flow-matching).
4. Seed + reproducibility. Seed pin, version pin, prompt hash.
5. Eval. MOS (mean opinion score) or A/B for TTS, CLAP score for music, CER for TTS transcription, user listening test for SFX.
6. Guardrails. Voice-clone consent + watermark (PerTh / SynthID-audio), copyright scan on music output, training-data policy check.

Refuse to clone any voice without verified consent from the owner (Cassette-era "3-second prompt" is not consent). Refuse to ship music with unlicensed reference material. Flag any real-time target &lt; 200 ms that does not use a streaming token-AR model - diffusion-based audio cannot meet sub-300 ms TTFB in 2026.

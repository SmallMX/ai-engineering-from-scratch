---
name: skill-music-designer
description: 音乐 Generation：MusicGen, Stable 音频, Suno,与the Licensing Earthquake 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 9
---

# 音乐 Generation：MusicGen, Stable 音频, Suno,与the Licensing Earthquake：中文使用说明

你将围绕本课主题 **音乐 Generation：MusicGen, Stable 音频, Suno,与the Licensing Earthquake** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 09 课「音乐 Generation：MusicGen, Stable 音频, Suno,与the Licensing Earthquake」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: music-designer
description: Pick a music-generation model, license strategy, length plan, and disclosure metadata for a deployment.
version: 1.0.0
phase: 6
lesson: 09
tags: [music-generation, musicgen, stable-audio, suno, licensing]
---

Given the brief (instrumental vs song, length, commercial vs research, genre, budget), output:

1. Model. MusicGen (size) · Stable Audio Open · ACE-Step XL · YuE · Suno (v5) · Udio (v4) · ElevenLabs Music · Google Lyria 3 / RealTime · MiniMax Music 2.5. One-sentence reason.
2. License and rights. Commercial license for the generated clip · Attribution (CC) · Non-commercial limited · Owned catalog fine-tune. Document rightsholder and chain.
3. Length + structure. Single generation · chunked + crossfade · inpainting for bridge · stem separation if tracks need editing. Handle the 30-second drift wall explicitly.
4. Prompt schema. Key / BPM / genre / instrumentation + (for vocal models) lyrics + mood tags. Restrict celebrity names and trademarked style tags.
5. Disclosure + metadata. Watermark (AudioSeal where applicable), `isAIGenerated` metadata tag, AI-disclosure overlay for EU AI Act / CA SB 942 compliance.

Refuse celebrity-style prompts on open models (commercial APIs filter; self-host does not). Refuse non-commercial-licensed generations (Stable Audio Open) for paid products. Refuse deploying vocal-music without disclosure tagging. Flag stem-editing pipelines that depend on Udio stems — those come with commercial terms, not free use.

Example input: "Background music for a meditation app. Instrumental. Full commercial rights required. Up to 5 min per track."

Example output:
- Model: MusicGen-large (MIT) for instrumental with full commercial rights. No Stable Audio (non-commercial).
- License: MIT — commercial rights retained by deployer. Track rightsholder: app company.
- Length: chunk into 30s segments with 3s crossfade; 10 generations concatenated → 5 min. Add a subtle ambient fade-in/out envelope to hide drift.
- Prompt: `"slow ambient meditation, 60 BPM, soft strings and low pad, in D minor, no drums"` — pin BPM, pin key, pin instrumentation, explicitly exclude percussive elements.
- Disclosure: `"AI-generated music"` tag in app credits; metadata `creator=AI-Gen:MusicGen-large, date=<iso>`. AudioSeal optional (instrumental has lower forgery risk, but defense-in-depth).

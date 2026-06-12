---
name: skill-codec-picker
description: Neural 音频 Codecs：EnCodec, SNAC, Mimi, DAC与the Semantic-Acoustic Split 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 13
---

# Neural 音频 Codecs：EnCodec, SNAC, Mimi, DAC与the Semantic-Acoustic Split：中文使用说明

你将围绕本课主题 **Neural 音频 Codecs：EnCodec, SNAC, Mimi, DAC与the Semantic-Acoustic Split** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 13 课「Neural 音频 Codecs：EnCodec, SNAC, Mimi, DAC与the Semantic-Acoustic Split」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: codec-picker
description: Pick a neural audio codec (EnCodec / DAC / SNAC / Mimi) for a given generative or compression task.
version: 1.0.0
phase: 6
lesson: 13
tags: [codec, encodec, dac, snac, mimi, rvq, semantic-tokens]
---

Given the task (generative LM, compression, full-duplex dialogue, music editing, fidelity target), output:

1. Codec. EnCodec-24k · EnCodec-48k · DAC-44.1k · SNAC-24k · Mimi · (fallback: Opus for non-neural compression). One-sentence reason.
2. Frame rate + codebooks. Bitrate budget, codebook count (usually 4-12), sequence length for target clip duration.
3. Tokenization scheme. Flat vs hierarchical (SNAC) vs semantic+acoustic (Mimi). How the LM consumes tokens.
4. Decoder. In-codec decoder · external vocoder (HiFi-GAN) · LM-only (no vocoder, predict codec tokens directly). Explain why.
5. Training implications. Need to train encoder/decoder? Fine-tune on domain audio (speech-only → domain-specific music)? Frozen off-the-shelf?

Refuse DAC for AR-LM workloads on tight latency budgets — 86 Hz frame rate × 8 codebooks = 5,504 tokens per 10 s, too long for fast generation. Refuse Mimi for music — it's speech-tuned. Refuse EnCodec for semantic-conditional generation — no semantic codebook, blurry speech from text.

Example input: "Build an AR LM for text-to-speech TTS. Target TTFA 200 ms. English only."

Example output:
- Codec: Mimi. Semantic+acoustic split enables text → codebook 0 → codebooks 1-7 factorization, which is both fast and supports voice cloning.
- Frame rate + codebooks: 12.5 Hz · 8 codebooks · 4.4 kbps. 10 s = 1,000 tokens.
- Tokenization: predict codebook 0 first from text + speaker reference; then predict codebooks 1-7 given codebook 0 + speaker reference (depth-transformer pattern).
- Decoder: Mimi's built-in decoder, no external vocoder needed.
- Training: train the text-to-codec LM; freeze Mimi.

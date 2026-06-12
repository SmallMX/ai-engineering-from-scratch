---
name: skill-audio-loader
description: 音频 基础：Waveforms, Sampling, Fourier Transform 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 1
---

# 音频 基础：Waveforms, Sampling, Fourier Transform：中文使用说明

你将围绕本课主题 **音频 基础：Waveforms, Sampling, Fourier Transform** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 01 课「音频 基础：Waveforms, Sampling, Fourier Transform」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: audio-loader
description: Validate a raw audio file against a target model's expectations and resample it safely.
version: 1.0.0
phase: 6
lesson: 01
tags: [audio, speech, preprocessing]
---

Given an audio file (path, channels, sample rate, bit depth, codec) and a target model (ASR / TTS / classifier with a required sample rate and channel count), output:

1. Mismatches. List every dimension where the file does not match the target (sr, channels, duration floor, clipping check).
2. Resample plan. Source sr, target sr, resampling library (`torchaudio.transforms.Resample` or `librosa.resample`), anti-aliasing filter type.
3. Channel plan. Mono fold strategy (mean vs left-only), or multichannel pass-through when the model supports it.
4. Normalization. Peak vs RMS normalization, dBFS target, clipping guard.
5. Validation snippet. Python that loads the file, runs the transforms, and asserts the final array matches `(target_sr, dtype, channel_count, range)`.

Refuse to downsample without an anti-aliasing filter. Refuse to upsample beyond 2x without a reconstruction filter. Flag any input file with clipping peaks over ±0.999 or a DC offset above ±0.01.

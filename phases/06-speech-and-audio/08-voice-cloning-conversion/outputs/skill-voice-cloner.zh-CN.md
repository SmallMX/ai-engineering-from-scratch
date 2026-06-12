---
name: skill-voice-cloner
description: 语音 Cloning与语音 Conversion 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 8
---

# 语音 Cloning与语音 Conversion：中文使用说明

你将围绕本课主题 **语音 Cloning与语音 Conversion** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 08 课「语音 Cloning与语音 Conversion」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: voice-cloner
description: Pick cloning approach (zero-shot / conversion / adaptation), consent artifact, watermark, and safety filters for a voice-cloning deployment.
version: 1.0.0
phase: 6
lesson: 08
tags: [voice-cloning, voice-conversion, watermark, consent, safety]
---

Given the task (language, reference length available, adaptation budget, license constraints, consent status, deployment scale), output:

1. Approach. Zero-shot clone (F5-TTS / VibeVoice / Orpheus / OpenVoice V2) · voice conversion (kNN-VC / OpenVoice V2 tone-color) · speaker adaptation (XTTS v2 + LoRA / VITS full fine-tune).
2. Reference prep. Required length, SNR (≥ 20 dB), mono 16 kHz+, silence trim, `ref_text` (must match exactly for F5-TTS). Reject music-bed references.
3. Consent artifact. Explicit recorded consent from voice owner. Template: name + date + purpose + scope + revocation procedure. Store 7+ years.
4. Watermark. AudioSeal-embedded 16-bit payload on every output. Configure detector in CI to verify presence before publishing audio.
5. Safety filters. Named-entity (celebrity / politician / minor) prompt-rejection; rate-limit per-user per-hour; audit log of every clone generation; kill-switch.

Refuse to ship cloning without a watermarking strategy. Refuse to clone named celebrities / politicians / minors regardless of consent claims. Refuse references under 3 s or SNR &lt; 20 dB. Refuse F5-TTS for commercial deployments (CC-BY-NC). Refuse cross-lingual clone without explicitly flagging the accent-transfer gap.

Example input: "Accessibility app: let ALS patient bank their voice while still speaking, then speak through TTS after voice loss. English, US."

Example output:
- Approach: OpenVoice V2 (MIT, zero-shot, 6 s reference). Accessibility use case with inherent consent; patient is voice owner.
- Reference prep: record 5 × 6 s clips in studio-quality conditions (quiet room, USB mic, 24 kHz). Store raw + transcripts. Build centroid reference for stability.
- Consent: digital signature + video affirmation attesting to the purpose ("post-diagnosis voice reuse"), stored on encrypted volume with 10-year retention. Revocation hotline.
- Watermark: AudioSeal 16-bit payload encoding `patient_id` + `clip_id`; detector runs on every generation in CI.
- Safety: hard-filter named-entity prompts; log every generation; ROI-limited to patient's logged-in app instance. No API exposure.

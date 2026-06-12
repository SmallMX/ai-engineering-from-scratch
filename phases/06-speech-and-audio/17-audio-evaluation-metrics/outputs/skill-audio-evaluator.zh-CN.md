---
name: skill-audio-evaluator
description: 音频 评估：WER, MOS, UTMOS, MMAU, FAD,与the Open Leaderboards 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 17
---

# 音频 评估：WER, MOS, UTMOS, MMAU, FAD,与the Open Leaderboards：中文使用说明

你将围绕本课主题 **音频 评估：WER, MOS, UTMOS, MMAU, FAD,与the Open Leaderboards** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 17 课「音频 评估：WER, MOS, UTMOS, MMAU, FAD,与the Open Leaderboards」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: audio-evaluator
description: Pick metrics, benchmarks, normalization rules, and reporting format for any audio model release.
version: 1.0.0
phase: 6
lesson: 17
tags: [evaluation, wer, mos, utmos, eer, der, fad, mmau, leaderboard]
---

Given the task (ASR / TTS / cloning / speaker-verif / diarization / classification / music / LALM / streaming S2S), output:

1. Primary metric. WER · MOS · UTMOS · SECS · EER · DER · mAP · FAD · MMAU-Pro accuracy · latency P95. One choice.
2. Secondary metrics. 1-3 additional axes (speed, diversity, robustness) and reason.
3. Normalization rule. Lowercase, punctuation-strip, number expansion, whitespace collapse. Use Whisper-normalizer or custom, document it.
4. Public benchmark. The canonical leaderboard to report against (Open ASR, TTS Arena, MMAU-Pro, VoxCeleb1-O, AudioSet, LongAudioBench, etc.).
5. In-house set. Held-out domain data with N samples; demographic / acoustic slice breakdown.
6. Reporting format. Distribution (P50/P95/P99 for latency; per-class recall for classification; per-category for MMAU). Release notes template.

Refuse single-number evaluation for latency (report percentiles). Refuse aggregate-only for classification (report per-class). Refuse TTS releases without both MOS/UTMOS and SECS (when cloning). Refuse ASR releases without a WER normalization spec. Refuse music releases with only FAD — always pair with human MOS panel.

Example input: "Release of a new English-Spanish conversational TTS. Need to convince the team it's better than the existing Cartesia-Sonic baseline."

Example output:
- Primary: UTMOS (paired audio samples on 50 prompts per language) + human-panel MOS (20 listeners per language, blind A/B vs baseline).
- Secondary: TTFA median & P95 (must match baseline); SECS &gt; 0.80 vs a fixed voice reference (no speaker regression); CER on round-trip ASR (Whisper-large-v3-turbo) &lt; 2%.
- Normalization: Whisper-normalizer English + Hugging Face multilingual-normalizer Spanish for round-trip WER.
- Public benchmark: TTS Arena (English) and Artificial Analysis Speech for relative ELO positioning. Target: within 50 ELO of the closest competitor.
- In-house: 200 held-out prompts (100 per lang) covering money, dates, product names, 2-sentence narration, emotional read, code-switched. 10 demographic voices.
- Reporting: release note with headline (UTMOS + MOS), P50/P95 TTFA histogram, SECS CDF, CER per-category breakdown, failure-mode callouts (code-switched prompts failed at X%).

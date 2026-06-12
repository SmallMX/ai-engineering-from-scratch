---
name: skill-speaker-verifier
description: Speaker Recognition与Verification 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 6
---

# Speaker Recognition与Verification：中文使用说明

你将围绕本课主题 **Speaker Recognition与Verification** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 06 课「Speaker Recognition与Verification」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: speaker-verifier
description: Design a speaker verification or diarization pipeline with model choice, enrollment protocol, and threshold tuning.
version: 1.0.0
phase: 6
lesson: 06
tags: [audio, speaker, verification, diarization]
---

Given a target (verification vs identification vs diarization, domain, channel, threat model) and data (hours for threshold tuning, number of speakers, enrollment clip budget), output:

1. Embedder. ECAPA-TDNN / WavLM-SV / ReDimNet / x-vector. Reason.
2. Enrollment protocol. Number of clips, min duration, noise gate, channel match.
3. Scoring. Cosine / PLDA; with or without AS-norm; cohort size.
4. Threshold. Target FAR (fraud risk) or EER; tuning set size.
5. Spoof defense. Anti-spoof model (AASIST, RawNet2), liveness challenge, or replay detection.

Refuse any fraud-grade deployment without an anti-spoof front-end. Refuse to publish EER without reporting the evaluation set, its channel, and clip length distribution. Flag cosine thresholds fixed across domains without re-tuning.

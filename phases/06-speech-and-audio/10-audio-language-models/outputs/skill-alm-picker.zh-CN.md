---
name: skill-alm-picker
description: 音频-语言模型：Qwen2.5-Omni, 音频 Flamingo, GPT-4o 音频 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 10
---

# 音频-语言模型：Qwen2.5-Omni, 音频 Flamingo, GPT-4o 音频：中文使用说明

你将围绕本课主题 **音频-语言模型：Qwen2.5-Omni, 音频 Flamingo, GPT-4o 音频** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 10 课「音频-语言模型：Qwen2.5-Omni, 音频 Flamingo, GPT-4o 音频」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: alm-picker
description: Pick an audio-language model, benchmark subset, output modality (text vs speech), and guardrails for an audio-understanding task.
version: 1.0.0
phase: 6
lesson: 10
tags: [alm, lalm, qwen-omni, audio-flamingo, gemini-audio, mmau]
---

Given the task (speech / sound / music / multi-audio / long-audio, output modality, latency, license), output:

1. Model. Qwen2.5-Omni-7B · Qwen3-Omni · SALMONN · Audio Flamingo 3 · AF-Next · LTU · GAMA · Gemini 2.5 Pro (API) · GPT-4o Audio (API). One-sentence reason.
2. Benchmark subset to validate. MMAU-Pro speech / sound / music / multi-audio · LongAudioBench · AudioCaps · ClothoAQA. Pick the axis that matches the user task.
3. Output modality. Text-only · text + speech (Qwen-Omni, GPT-4o Audio). Budget for an additional speech decoder if needed.
4. Guardrails. Reject prompts that require multi-audio comparison when your model's multi-audio score is &lt; 30% (near-random). Diarize before LALM for &gt; 10-minute inputs.
5. Escalation. When should this task fall back to a specialized model — Whisper for transcription, BEATs for classification, pyannote for diarization. LALM is not the best of each.

Refuse to ship multi-audio comparison tasks without verifying your model scores &gt; 40% on the MMAU-Pro multi-audio subset. Refuse long-audio (&gt; 10 min) without upstream diarization. Flag any deploy that uses vendor-reported numbers without independent re-verification.

Example input: "Compliance audit: transcribe 10-minute bank-call recordings + detect if the agent read the mandatory disclosure."

Example output:
- Model: Whisper-large-v3-turbo for transcription + Gemini 2.5 Pro (via API) for disclosure-check QA over the transcript. LALM direct on raw audio is tempting but long-audio LALM accuracy drops past 10 min.
- Benchmark subset: MMAU-Pro speech subset (Gemini 2.5 Pro = 73.4%) — covers the speech-reasoning axis. Also spot-check on your own 50-call gold set.
- Output modality: text-only. Speech output not needed for an audit report.
- Guardrails: diarize with pyannote 3.1 first; send per-speaker segments separately; log confidence score per call.
- Escalation: if a call fails the disclosure check, route to human reviewer instead of autonomous flag.

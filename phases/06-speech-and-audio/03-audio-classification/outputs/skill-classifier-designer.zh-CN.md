---
name: skill-classifier-designer
description: 音频 Classification：From k-NN on MFCCs to AST与BEATs 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 6
lesson: 3
---

# 音频 Classification：From k-NN on MFCCs to AST与BEATs：中文使用说明

你将围绕本课主题 **音频 Classification：From k-NN on MFCCs to AST与BEATs** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 6「语音与音频」
- 课程：第 03 课「音频 Classification：From k-NN on MFCCs to AST与BEATs」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: classifier-designer
description: Pick architecture, augmentation, class-balance strategy, and eval metric for an audio classification task.
version: 1.0.0
phase: 6
lesson: 03
tags: [audio, classification, beats, ast]
---

Given an audio classification task (domain, label count, label density per clip, data volume, deployment target), output:

1. Architecture. k-NN-MFCC / 2D CNN / AST / BEATs / Whisper-encoder. One-sentence reason.
2. Augmentations. SpecAugment params (time mask, freq mask counts), mixup α, background noise mix level.
3. Class balance. Balanced sampler vs focal loss vs class weights. Pin to the tail-to-head ratio.
4. Loss + metric. CE / BCE / focal; primary metric (top-1 / mAP / macro-F1) and secondary.
5. Split + eval plan. Stratified k-fold, speaker-disjoint if speech, temporal split if streaming data.

Refuse any multi-label task scored only with top-1 accuracy; require mAP. Refuse to evaluate a speaker-conditioned task without speaker-disjoint splits. Flag any architecture from scratch on <10k labeled clips — start with a SSL-pretrained backbone.

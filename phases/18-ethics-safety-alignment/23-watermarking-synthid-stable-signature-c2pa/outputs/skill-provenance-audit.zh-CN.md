---
name: skill-provenance-audit
description: 水印：SynthID, Stable Signature, C2PA 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 23
---

# 水印：SynthID, Stable Signature, C2PA：中文使用说明

你将围绕本课主题 **水印：SynthID, Stable Signature, C2PA** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 23 课「水印：SynthID, Stable Signature, C2PA」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: provenance-audit
description: Audit a content deployment's provenance chain across watermarking and C2PA metadata.
version: 1.0.0
phase: 18
lesson: 23
tags: [watermarking, synthid, stable-signature, c2pa, provenance]
---

Given a content deployment with a provenance claim, audit the provenance chain.

Produce:

1. Watermark inventory. List every modality (text, image, audio, video) and the watermark applied in each. No watermark = no detection path.
2. Watermark robustness. For each watermark, name the adversarial class it survives (compression, cropping, paraphrase, fine-tune). Flag limitations per Kirchenbauer 2023 Section 6 (paraphrase) and "Stable Signature is Unstable" 2024 (fine-tune).
3. C2PA coverage. Is C2PA metadata attached? Is the signing chain from a trusted identity? Metadata can be stripped; presence is not sufficient.
4. Cross-modal detector. Is there a unified detector across modalities (SynthID 2025) or modality-specific only?
5. Regulatory alignment. Does the deployment meet EU AI Act Article 50 transparency obligations (effective August 2026)? Does it comply with the Transparency Code (final version June 2026)?

Hard rejects:
- Any "watermark" claim without a named mechanism and detector.
- Any "authenticity" claim based only on absence of watermark (model-not-watermarked ≠ authentic).
- Any image provenance claim without an assessment of the Fernandez 2024 removal attack.

Refusal rules:
- If the user asks "will this detect all AI content," refuse the binary claim; watermarking is model-specific.
- If the user asks for a universal provenance solution, refuse and point to the watermark + C2PA layered approach.

Output: a one-page audit filling the five sections, flagging robustness gaps per modality, and naming the single highest-value additional control. Cite SynthID (Google DeepMind), Stable Signature (Fernandez et al. 2023), and C2PA once each.

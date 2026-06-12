---
name: skill-encoding-audit
description: ASCII Art与Visual Jailbreaks 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 14
---

# ASCII Art与Visual Jailbreaks：中文使用说明

你将围绕本课主题 **ASCII Art与Visual Jailbreaks** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 14 课「ASCII Art与Visual Jailbreaks」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: encoding-audit
description: Audit a jailbreak-defense report across encoding-family attacks.
version: 1.0.0
phase: 18
lesson: 14
tags: [artprompt, ascii-art, encoding-attack, utes, structural-sleight]
---

Given a jailbreak-defense report, enumerate the encoding-family attacks covered and the defense layer that catches each.

Produce:

1. Encoding coverage. List each attack family evaluated: ASCII art (ArtPrompt), base64, leet-speak, UTF-8 homoglyphs, nested JSON / YAML / CSV, tree/graph UTES, image-modality. Flag families missing.
2. Defense-layer mapping. For each family, identify which defense layer (keyword filter, perplexity filter, paraphrase, retokenization, output classifier, multimodal moderator) catches it and which does not.
3. Visual-recognition gap. Per Jiang et al. 2024, PPL and Retokenization fail against ArtPrompt because the recognition happens at the visual level. Does the report's defense include anything that operates at the visual/structural level?
4. Generalization test. UTES (StructuralSleight) generalizes to arbitrary rare structures. Does the report test structures not in its training defense set?
5. Capability-safety tradeoff. A model with stronger visual-text capability (high ViTC score) is more vulnerable to ArtPrompt. Note the model's ViTC score if reported; request it if not.

Hard rejects:
- Any defense claim based solely on substring/keyword filtering.
- Any defense claim that covers one encoding family and extrapolates to "encoding attacks."
- Any defense claim without a per-family attack-success rate.

Refusal rules:
- If the user asks whether ArtPrompt is "patched," refuse and explain the recognition-level vs text-level defense gap.
- If the user asks for a recommended all-encoding defense, refuse a single recommendation — defense must be layered across all families that the deployment might face.

Output: a one-page audit that fills the five sections above, flags the primary encoding gap, and names the single most urgent defense layer to add. Cite Jiang et al. (arXiv:2402.11753) and StructuralSleight once each.

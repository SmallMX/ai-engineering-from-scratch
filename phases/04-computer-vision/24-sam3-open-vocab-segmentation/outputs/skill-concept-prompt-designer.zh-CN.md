---
name: skill-concept-prompt-designer
description: SAM 3 与开放词表分割 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 24
tags: [sam3, open-vocab, prompt-engineering, segmentation]
---

# SAM 3 与开放词表分割：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**SAM 3 与开放词表分割**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 开放词表分割通过文本概念指定要分割的对象。
- SAM 系列模型把 prompt 和图像结合生成 masks。
- text prompt、box prompt 和 point prompt 适合不同交互方式。
- mask quality 要结合边界、覆盖和语义正确性评估。
- 开放词表系统需要处理同义词、歧义和细粒度类别。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-concept-prompt-designer
description: Turn user utterances into well-formed SAM 3 concept prompts with splitting, disambiguation, and fallbacks
version: 1.0.0
phase: 4
lesson: 24
tags: [sam3, open-vocab, prompt-engineering, segmentation]
---

# Concept Prompt Designer

SAM 3's accuracy depends heavily on how the concept prompt is phrased. This skill normalises free-form user utterances into prompts that SAM 3 handles well.

## When to use

- Building a UI that accepts natural-language object queries.
- Exposing SAM 3 through an API where upstream callers send sentences.
- Debugging poor SAM 3 matches — often the prompt is malformed, not the model.

## Inputs

- `utterance`: raw user string.
- `context`: optional domain hint (e.g. "surveillance", "medical", "retail").
- `max_concepts`: maximum concepts to extract per utterance; default 5.

## Rules SAM 3 prefers

- **Short noun phrases, not sentences.** `"cat"` wins over `"there is a cat"`.
- **Concrete nouns.** `"skateboard"` wins over `"thing to ride on"`.
- **Modifiers immediately before the noun.** `"red car"` wins over `"car that is red"`.
- **Lowercase.** SAM 3 is robust but empirically slightly better on lowercase inputs.
- **Singular or plural.** Both work; plural helps when multiple instances are expected.

## Steps

1. **Tokenise by common separators** — comma, semicolon, "and", "or", "&".
2. **Drop filler prefixes** — "find", "show me", "segment", "detect", "locate", "a", "an", "the".
3. **Keep prepositional modifiers** only if they are visual — `"striped red umbrella"` yes, `"umbrella from yesterday"` no (the `"from yesterday"` is not in-image).
4. **Disambiguate collisions** using the optional `context`:
   - `"window"` in surveillance context -> `"building window"`.
   - `"window"` in medical context -> often error; suggest user clarify.
5. **Fallback** to the exact string if splitting yields zero concepts *and* the utterance contains at least one concrete noun. If no concrete noun can be extracted, do not emit a concept — return only warnings and ask the user to clarify (see Rules).
6. **Cap at `max_concepts`.** If more concepts were extracted than the caller asked for, keep the first `max_concepts` in utterance order and emit the rest under `dropped` with reason `"exceeded max_concepts"`. This keeps latency bounded when a user pastes a long enumeration.

## Output format

``\`
[designed prompts]
  utterance:    <original>
  concepts:     ["concept_1", "concept_2", ...]
  dropped:      ["filler_1", ...]
  warnings:     ["concept too abstract", "may match many classes", ...]

[sam3 calls]
  For each concept run: sam3.detect(image, concept)
  Merge outputs with distinct concept tags per detection.
``\`

## Examples

``\`
in:  "can you find me a cat or two dogs?"
out: ["cat", "dogs"]
dropped: ["can you find me", "a", "or two", "?"]
note: "dogs" kept plural because the utterance says "two dogs" — plural hint preserved.

in:  "segment the big red truck and the blue sedan"
out: ["big red truck", "blue sedan"]
dropped: ["segment", "the", "and"]

in:  "thing near the door"
out: ["door"]
warnings: ["'thing' is too abstract for SAM 3; fell back to 'door'"]

in:  "striped red umbrella, green hat, pink balloon"
out: ["striped red umbrella", "green hat", "pink balloon"]
``\`

## Rules

- Never pass sentences longer than 8 words to SAM 3 — accuracy drops above that.
- When an utterance contains no extractable concrete nouns, do not run SAM 3; return the warnings and ask for clarification.
- Do not split on punctuation inside quoted strings; preserve `"black and white cat"` as one concept if it is quoted.
- Always log the original utterance and the derived concepts for production debugging.

```

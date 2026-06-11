---
name: skill-ctc-decoder
description: OCR 与文档理解 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 19
tags: [ocr, ctc, decoding, sequence-models]
---

# OCR 与文档理解：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**OCR 与文档理解**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- OCR 包括文本检测、识别和版面理解。
- CTC 常用于不需要字符级对齐的序列识别。
- 文档理解还需要 reading order、table structure 和 key-value extraction。
- 扫描质量、旋转、字体和语言会影响 OCR。
- 端到端系统要区分识别错误和布局错误。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-ctc-decoder
description: Write greedy and beam-search CTC decoders from scratch, including length normalisation
version: 1.0.0
phase: 4
lesson: 19
tags: [ocr, ctc, decoding, sequence-models]
---

# CTC Decoder

Produce two decoding routines for CTC outputs: greedy (fast) and beam (better on noisy inputs).

## When to use

- Running OCR inference on custom CRNN outputs.
- Benchmarking a pretrained OCR model against different decoders.
- Implementing a simple beam search without pulling in ctcdecode.

## Inputs

- `log_probs`: (T, N, C) log-softmax over vocab (index 0 = blank by convention).
- `vocab`: list of C characters.
- `beam_width` (beam only): typically 5-10.

## Greedy decoder

``\`python
def greedy_ctc_decode(log_probs, vocab, blank=0):
    preds = log_probs.argmax(dim=-1).transpose(0, 1).cpu().tolist()
    out = []
    for seq in preds:
        decoded = []
        prev = None
        for idx in seq:
            if idx != prev and idx != blank:
                decoded.append(vocab[idx])
            prev = idx
        out.append("".join(decoded))
    return out
``\`

## Beam search decoder

``\`python
import heapq
import math

def beam_ctc_decode(log_probs, vocab, beam_width=5, blank=0):
    T, N, C = log_probs.shape
    lp = log_probs.cpu()
    results = []
    for n in range(N):
        beams = {("",): (0.0, -math.inf)}  # (prefix_tuple) -> (p_blank, p_nonblank)
        for t in range(T):
            logits_t = lp[t, n]
            new_beams = {}
            for prefix, (p_b, p_nb) in beams.items():
                for c in range(C):
                    p = logits_t[c].item()
                    if c == blank:
                        nb = p_b + p
                        nnb = p_nb + p
                        upd = new_beams.get(prefix, (-math.inf, -math.inf))
                        new_beams[prefix] = (
                            _logsumexp(upd[0], _logsumexp(nb, nnb)),
                            upd[1],
                        )
                    else:
                        last = prefix[-1] if prefix else ""
                        char = vocab[c]
                        if char == last:
                            # Case 1: stay on same prefix (collapse from p_nb)
                            upd = new_beams.get(prefix, (-math.inf, -math.inf))
                            new_beams[prefix] = (upd[0], _logsumexp(upd[1], p_nb + p))
                            # Case 2: extend prefix via blank-separated repeat ("a_a" -> "aa")
                            new_prefix = prefix + (char,)
                            upd = new_beams.get(new_prefix, (-math.inf, -math.inf))
                            new_beams[new_prefix] = (upd[0], _logsumexp(upd[1], p_b + p))
                        else:
                            new_prefix = prefix + (char,)
                            upd = new_beams.get(new_prefix, (-math.inf, -math.inf))
                            nb = _logsumexp(p_b, p_nb) + p
                            new_beams[new_prefix] = (upd[0], _logsumexp(upd[1], nb))
            beams = dict(heapq.nlargest(
                beam_width,
                new_beams.items(),
                key=lambda kv: _logsumexp(kv[1][0], kv[1][1]),
            ))
        best = max(beams.items(), key=lambda kv: _logsumexp(kv[1][0], kv[1][1]))[0]
        results.append("".join(best))
    return results


def _logsumexp(a, b):
    if a == -math.inf: return b
    if b == -math.inf: return a
    m = max(a, b)
    return m + math.log(math.exp(a - m) + math.exp(b - m))
``\`

## Rules

- The blank index in CTC is 0 by convention in PyTorch's `nn.CTCLoss`.
- Beam search improves accuracy on low-confidence inputs; on clean inputs the improvement is <1% CER.
- Never prune the beam below 5; the accuracy-latency trade flattens below that.
- When running beam search inside a tight latency budget, drop to greedy; the quality hit is small on most production OCR data.
- For large vocabularies (CJK with 3000+ characters), switch to `ctcdecode` (C++) instead of the pure Python version above; the Python beam quickly becomes the bottleneck.

```

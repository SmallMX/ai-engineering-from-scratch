---
name: skill-segmentation-mask-inspector
description: 语义分割：U-Net 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 7
tags: [computer-vision, segmentation, debugging, evaluation]
---

# 语义分割：U-Net：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**语义分割：U-Net**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 语义分割为每个像素预测类别。
- encoder 提取上下文，decoder 恢复空间分辨率。
- skip connections 把低层细节传回解码路径。
- Dice、IoU 和 pixel accuracy 是常见分割指标。
- mask 对齐和类别映射是分割任务常见错误来源。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-segmentation-mask-inspector
description: Report class distribution, predicted-mask statistics, and the classes most likely to be under-predicted or boundary-blurred
version: 1.0.0
phase: 4
lesson: 7
tags: [computer-vision, segmentation, debugging, evaluation]
---

# Segmentation Mask Inspector

A diagnostic for the gap between "the loss went down" and "the masks actually look right".

## When to use

- Right after a training run when mIoU looks fine but visual inspection says otherwise.
- Before deployment: checking the class balance of predictions against ground truth.
- When per-class IoU is high for large objects but low for small ones.
- Debugging boundary artefacts that do not show up in IoU because they are small in pixel count.

## Inputs

- `preds`: (N, H, W) tensor of predicted class IDs.
- `targets`: (N, H, W) tensor of ground-truth class IDs.
- `num_classes`: integer.
- Optional `class_names`: list of C strings.

## Steps

1. **Class pixel histograms.** Compute the percentage of pixels per class for `preds` and `targets`. Flag any class where `|pred% - gt%| / max(gt%, 1e-6) > 0.30` (relative deviation above 30%). For classes absent from ground truth (`gt% == 0`), flag any predicted share above `0.3` directly.

2. **IoU per class** and **boundary F1 per class**. Boundary F1 is computed by dilating each mask by 3 pixels, intersecting, and scoring. Classes with IoU > 0.7 but boundary F1 < 0.5 are blurring edges.

3. **Small-object recall.** Separate every ground-truth connected component into size buckets (tiny < 100 px, small < 1000 px, medium < 10000 px, large >= 10000 px). Report recall per bucket per class. Small-object recall below 0.3 while large-object recall is above 0.9 indicates a resolution / receptive-field problem.

4. **Confusion pairs.** For each class, find the class it most often confuses with (most common wrong predicted class within its ground-truth mask). Report the top 3 pairs.

5. **Saturation check (requires `probs` or `logits`, not just `preds`).** If the caller passes the raw per-pixel probability distribution `probs: (N, C, H, W)`, compute the fraction of pixels where `probs.max(dim=1) > 0.99` per class. High saturation (>0.9 of a class's pixels) suggests overconfidence — candidate for label smoothing or calibration. When only argmaxed `preds` are available, skip this step and note it in the report.

## Report format

``\`
[mask-inspector]
  classes: C

[class distribution]
  name       gt %    pred %   delta
  ...

[metrics]
  class       IoU     bF1    recall_tiny  recall_small  recall_medium  recall_large
  ...

[confusion pairs]
  class A confused with class B: <N> pixels (most common)
  class B confused with class A: <N> pixels
  ...

[verdict]
  most impactful issue: <one sentence>
``\`

## Rules

- Sort class rows by descending gt pixel share so the most frequent classes come first.
- Flag classes with IoU < 0.4 or boundary F1 < 0.3 as `critical`.
- When small-object recall is the dominant failure, recommend: higher-resolution training, smaller stride at the last encoder stage, or a feature-pyramid decoder.
- When boundary F1 is the dominant failure, recommend: boundary-aware loss (Lovasz or BoundaryLoss), TTA with horizontal flip, and stride-less decoder.
- Never output class indices as the only identifier; if `class_names` is provided, use it in every row.

```

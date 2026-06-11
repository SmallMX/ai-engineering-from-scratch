---
name: skill-anchor-designer
description: 目标检测：从零理解 YOLO 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 6
tags: [computer-vision, detection, anchors, kmeans]
---

# 目标检测：从零理解 YOLO：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**目标检测：从零理解 YOLO**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 目标检测同时预测类别和 bounding box。
- anchor、grid、objectness 和 box regression 是 YOLO 的核心组件。
- IoU 衡量预测框和真实框重叠程度。
- NMS 去掉重复框，保留高置信预测。
- mAP、precision、recall 和 IoU threshold 用于评估检测器。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-anchor-designer
description: Given a dataset of ground-truth boxes, run k-means on (w, h) and return anchor sets per FPN level plus coverage statistics
version: 1.0.0
phase: 4
lesson: 6
tags: [computer-vision, detection, anchors, kmeans]
---

# Anchor Designer

Anchors are the single most dataset-specific hyperparameter in an anchor-based detector. Default COCO anchors underperform on cell-culture images, satellite tiles, or small-object surveillance. This skill derives anchors that actually match the target data.

## When to use

- Before a first training run on a new dataset.
- When recall on very small or very large objects is weak on an otherwise healthy model.
- After a major dataset expansion where box size distribution may have shifted.

## Inputs

- `boxes`: numpy array of shape (N, 4) in either `(cx, cy, w, h)` or `(x1, y1, x2, y2)` format; at least 1000 positive boxes recommended.
- `num_anchors_per_level`: usually 3.
- `num_fpn_levels`: usually 3 (P3, P4, P5) or 4.
- `input_size`: training-resolution HxW.
- Optional `strides`: per-level strides; when omitted, take the first `num_fpn_levels` entries of `[8, 16, 32, 64]`. Pass a longer or shorter array explicitly if the detector's FPN has different strides.

## Steps

1. **Normalise boxes** to `(w, h)` pairs in pixel units at `input_size`. Drop any with w or h < 2 pixels.

2. **Run k-means** on `(w, h)` pairs, with `k = num_anchors_per_level * num_fpn_levels`. Use `1 - IoU(box, cluster)` as the distance function, not Euclidean distance — Euclidean on `(w, h)` collapses thin tall boxes and square boxes together. All boxes contribute equally (unweighted); if you have a class-imbalanced dataset and want larger-box recall, repeat rare-class boxes in the input array rather than passing a weight vector.

3. **Sort clusters by area** ascending. Split into `num_fpn_levels` groups of `num_anchors_per_level`. Smallest areas go to the highest-resolution level (smallest stride).

4. **Compute coverage statistics** per level:
   - `median IoU` of each ground-truth box to its best anchor at that level.
   - `recall@IoU=0.5` — percentage of boxes whose best anchor has IoU >= 0.5.
   - `area coverage` — fraction of boxes whose area falls within `[anchor_min_area / 4, anchor_max_area * 4]` of the level.

5. **Report per-level anchors** and flag levels where `recall@IoU=0.5 < 0.9`; that level's anchors do not match the data well and should be retuned or the number of anchors per level increased.

## Report format

``\`
[anchor-designer]
  total boxes:         <N>
  clusters:            <k>
  distance metric:     1 - IoU

[level P3  stride=8]
  anchors (w, h):      [(A, B), (C, D), (E, F)]
  median IoU:          <X>
  recall@IoU=0.5:      <X>
  coverage:            <X>
  flag:                ok | retune

[level P4  stride=16]
  ...

[summary]
  overall recall@IoU=0.5: <X>
  smallest anchor:        <w x h>
  largest anchor:         <w x h>
  recommendation:         <one sentence if any level flagged>
``\`

## Rules

- Always use IoU-based distance; Euclidean k-means produces visually reasonable but empirically worse anchors.
- Sort clusters by area, then assign to levels in ascending order.
- When `num_anchors_per_level = 1`, skip k-means entirely: split boxes into `num_fpn_levels` bins by area quantile (e.g. terciles for 3 levels), and set each level's anchor to the per-bin median (w, h). This is more robust than running k-means with `k = num_fpn_levels` on small datasets.
- Never output negative anchor dimensions; clamp at 1.
- If the dataset has < 200 boxes, warn the user that anchor search is unreliable and recommend using default COCO anchors plus more training data.

```

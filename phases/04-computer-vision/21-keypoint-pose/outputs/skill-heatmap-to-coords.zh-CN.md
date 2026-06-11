---
name: skill-heatmap-to-coords
description: 关键点检测与姿态估计 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 21
tags: [keypoint, pose, subpixel, inference]
---

# 关键点检测与姿态估计：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**关键点检测与姿态估计**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 关键点检测通常输出每个关键点的 heatmap。
- heatmap peak 转换为坐标需要考虑 stride 和 subpixel refinement。
- pose estimation 要处理遮挡、多人和关键点拓扑。
- OKS、PCK 等指标衡量关键点定位质量。
- 数据增强必须同步变换图像和 keypoints。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-heatmap-to-coords
description: Write the sub-pixel heatmap-to-coordinate routine used by every production pose model
version: 1.0.0
phase: 4
lesson: 21
tags: [keypoint, pose, subpixel, inference]
---

# Heatmap to Coords

Turn raw keypoint heatmaps into sub-pixel precise coordinates. The cheapest accuracy upgrade in every pose pipeline.

## When to use

- Deploying a heatmap-based keypoint model.
- Benchmarking pose metrics — OKS is extremely sensitive to sub-pixel accuracy.
- Porting pose code from one framework to another.

## Inputs

- `heatmaps`: `(N, K, H, W)` tensor, per-keypoint heatmaps from the model.
- `confidence_threshold`: discard keypoints whose peak is below this value.

## Steps

1. **Argmax** each heatmap to find the integer peak location.
2. **First-difference offset** — estimate sub-pixel offset from neighbouring pixels. The `0.25` coefficient is a heuristic calibrated for Gaussian heatmaps with `sigma >= 1`; for principled sub-pixel recovery, use a full quadratic fit (DARK) or a Gaussian fit.

``\`
dx = 0.25 * sign(heatmap[y, x+1] - heatmap[y, x-1])
dy = 0.25 * sign(heatmap[y+1, x] - heatmap[y-1, x])
``\`

For the DARK / quadratic variant, approximate using a local quadratic:

``\`
dx = -0.5 * (heatmap[y, x+1] - heatmap[y, x-1])
        / (heatmap[y, x+1] - 2 * heatmap[y, x] + heatmap[y, x-1] + eps)
``\`

The quadratic fit is more accurate on peaked heatmaps; the sign-based offset is the safer default when heatmaps are noisy.

3. **Add offset** to the integer peak.
4. **Confidence** — return the peak value per keypoint; clients use it to mask low-confidence predictions.
5. **Boundary case** — when the peak lands on the first or last pixel along an axis, one of the neighbours is clamped; the offset collapses to zero, which is the safest fallback.

## Output template

``\`python
import torch

def heatmap_to_coords_subpixel(heatmaps, threshold=0.2):
    N, K, H, W = heatmaps.shape
    flat = heatmaps.reshape(N, K, -1)
    conf, idx = flat.max(dim=-1)
    ys = (idx // W).float()
    xs = (idx % W).float()

    ys_int = ys.long()
    xs_int = xs.long()

    x_minus = (xs_int - 1).clamp(min=0)
    x_plus = (xs_int + 1).clamp(max=W - 1)
    y_minus = (ys_int - 1).clamp(min=0)
    y_plus = (ys_int + 1).clamp(max=H - 1)

    batch_idx = torch.arange(N).view(-1, 1).expand(-1, K)
    kp_idx = torch.arange(K).view(1, -1).expand(N, -1)

    dx_raw = (heatmaps[batch_idx, kp_idx, ys_int, x_plus]
              - heatmaps[batch_idx, kp_idx, ys_int, x_minus])
    dy_raw = (heatmaps[batch_idx, kp_idx, y_plus, xs_int]
              - heatmaps[batch_idx, kp_idx, y_minus, xs_int])
    dx = 0.25 * torch.sign(dx_raw)
    dy = 0.25 * torch.sign(dy_raw)

    at_left = xs_int == 0
    at_right = xs_int == (W - 1)
    at_top = ys_int == 0
    at_bottom = ys_int == (H - 1)
    dx = torch.where(at_left | at_right, torch.zeros_like(dx), dx)
    dy = torch.where(at_top | at_bottom, torch.zeros_like(dy), dy)

    refined_x = xs + dx
    refined_y = ys + dy
    coords = torch.stack([refined_x, refined_y], dim=-1)
    mask = conf >= threshold
    return coords, conf, mask
``\`

## Report

``\`
[subpixel decode]
  keypoints:   K
  threshold:   <float>
  valid_rate:  fraction of keypoints above threshold
``\`

## Rules

- Always clamp neighbour indices to valid range; off-edge keypoints have zero-difference offset but no crash.
- Return confidence alongside coordinates so clients can mask low-confidence points.
- Sub-pixel refinement only helps when the heatmap is smooth around the peak — check that training used a Gaussian target with sigma >= 1.
- For very small heatmap resolutions (< 48x48), consider upsampling the heatmap to full image size before extracting coordinates; the sub-pixel offset scales with the stride.

```

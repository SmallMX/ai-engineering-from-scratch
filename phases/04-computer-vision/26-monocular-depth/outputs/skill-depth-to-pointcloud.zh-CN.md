---
name: skill-depth-to-pointcloud
description: 单目深度与几何估计 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 26
tags: [depth, point-cloud, 3d, intrinsics]
---

# 单目深度与几何估计：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**单目深度与几何估计**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 单目深度从一张 RGB 图预测每个像素的距离。
- 深度估计依赖语义先验、几何线索和训练数据分布。
- relative depth 和 metric depth 是不同目标。
- 深度图可以转成 point cloud，但需要相机内参。
- 评估要关注 scale ambiguity、边界和远近场误差。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-depth-to-pointcloud
description: Build point clouds from depth maps with correct intrinsics handling and export to .ply
version: 1.0.0
phase: 4
lesson: 26
tags: [depth, point-cloud, 3d, intrinsics]
---

# Depth to Point Cloud

Turn a depth map plus a colour image into a textured point cloud, exportable for visualisation or further 3D work.

## When to use

- Visualising depth predictions as an actual 3D scene.
- Bootstrapping a sparse 3D reconstruction from a single image.
- Producing input for 3DGS training when SfM fails.
- Comparing predicted depth against LiDAR ground truth.

## Inputs

- `depth`: `(H, W)` numpy array of depths in the same units you want in the output (metres recommended).
- `rgb`: `(H, W, 3)` numpy array of colours (uint8 or float32 [0, 1]).
- `intrinsics`: `(fx, fy, cx, cy)` in pixel units.
- Optional `depth_scale`: multiplier to convert predicted depth units to metres.

## Pipeline

1. **Validate** — depth must be positive and finite everywhere you plan to include. Mask out invalid pixels.
2. **Lift** — `X = (u - cx) * d / fx`, `Y = (v - cy) * d / fy`, `Z = d` per pixel.
3. **Pair** with RGB — each 3D point gets an `(r, g, b)` triple from the matching pixel.
4. **Export** — PLY (portable), `.xyz` (lightweight), `.pcd` (Open3D-native), `.las`/`.laz` (geospatial).

## Implementation template

``\`python
import numpy as np

def depth_to_point_cloud(depth, intrinsics, depth_scale=1.0, min_depth=0.1, max_depth=100.0):
    H, W = depth.shape
    fx, fy, cx, cy = intrinsics
    v, u = np.meshgrid(np.arange(H), np.arange(W), indexing="ij")
    z = depth.astype(np.float32) * depth_scale
    valid = (z > min_depth) & (z < max_depth) & np.isfinite(z)
    x = (u - cx) * z / fx
    y = (v - cy) * z / fy
    points = np.stack([x, y, z], axis=-1)
    return points, valid


def write_ply(path, points, colors=None, valid_mask=None):
    p = points.reshape(-1, 3)
    if valid_mask is not None:
        p = p[valid_mask.flatten()]
    lines = [
        "ply",
        "format ascii 1.0",
        f"element vertex {p.shape[0]}",
        "property float x", "property float y", "property float z",
    ]
    if colors is not None:
        c = colors.reshape(-1, 3).astype(np.uint8)
        if valid_mask is not None:
            c = c[valid_mask.flatten()]
        lines += ["property uchar red", "property uchar green", "property uchar blue"]
    lines.append("end_header")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
        if colors is not None:
            for pt, col in zip(p, c):
                f.write(f"{pt[0]:.4f} {pt[1]:.4f} {pt[2]:.4f} {col[0]} {col[1]} {col[2]}\n")
        else:
            for pt in p:
                f.write(f"{pt[0]:.4f} {pt[1]:.4f} {pt[2]:.4f}\n")
``\`

## Report

``\`
[export]
  input depth shape:  (H, W)
  valid points:       <N> of <H*W>
  output format:      ply | xyz | pcd | las
  coordinate system:  camera (+X right, +Y down, +Z forward)
  scale:              metres | millimetres | normalised
``\`

## Rules

- Always mask invalid depth (zero, NaN, inf, saturated); including them produces a cloud of garbage points at the origin.
- For prediction from a relative-depth model, do NOT export as metric; prefix output filename with `relative_` to signal the convention.
- Keep the camera coordinate convention consistent (OpenCV: +X right, +Y down, +Z forward). Swap signs if the downstream tool expects OpenGL (+Y up).
- For dense scenes (> 1M points), offer a subsample parameter; PLY files > 500 MB are awkward to load everywhere.
- Never silently clip depth to produce "reasonable" output; clip explicitly with warned thresholds so users know what was discarded.

```

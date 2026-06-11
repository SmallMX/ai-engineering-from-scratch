---
name: skill-linear-probe-runner
description: 自监督视觉：SimCLR、DINO、MAE 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 17
tags: [self-supervised, evaluation, linear-probe, pytorch]
---

# 自监督视觉：SimCLR、DINO、MAE：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**自监督视觉：SimCLR、DINO、MAE**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 自监督视觉用无标签数据学习 representation。
- contrastive learning 拉近正样本，推远负样本。
- MAE 通过遮挡重建学习视觉结构。
- linear probe 用冻结特征检验 representation 质量。
- 预训练策略要匹配下游任务和数据规模。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-linear-probe-runner
description: Write the complete linear-probe evaluation for any frozen encoder and labelled dataset
version: 1.0.0
phase: 4
lesson: 17
tags: [self-supervised, evaluation, linear-probe, pytorch]
---

# Linear Probe Runner

Evaluate a frozen encoder's features by training a single linear classifier on top. The standard evaluation for every self-supervised paper.

## When to use

- Comparing self-supervised checkpoints.
- Tracking feature quality over pretraining epochs.
- Deciding whether a pretrained encoder is good enough for a downstream task without fine-tuning.

## Inputs

- `encoder`: frozen `nn.Module` returning a fixed-dim feature per image.
- `feature_dim`: dimensionality of the encoder output.
- `train_dataset`: labelled dataset (image, class_id).
- `val_dataset`: held-out set.
- `num_classes`: task classes.
- `epochs`: typically 100 for ImageNet-scale, 50 for smaller datasets.

## Steps

1. Set encoder to eval mode and `requires_grad=False` on every parameter.
2. Feature-extract both train and val sets once. Store as numpy arrays or a memory-mapped file.
3. Train a `nn.Linear(feature_dim, num_classes)` on the cached features with SGD + cosine schedule.
4. Standard hyperparameters: `lr=0.1`, `momentum=0.9`, `weight_decay=0`, `batch_size=1024`. Linear probe is surprisingly sensitive to `lr` — sweep if accuracy is poor.
5. Report top-1 accuracy on val at the end of training.

## Output template

``\`python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.optim import SGD
from torch.optim.lr_scheduler import CosineAnnealingLR

def extract(encoder, loader, device="cpu"):
    encoder.eval()
    feats, labels = [], []
    with torch.no_grad():
        for x, y in loader:
            f = encoder(x.to(device)).cpu()
            feats.append(f)
            labels.append(y)
    return torch.cat(feats), torch.cat(labels)


def linear_probe(encoder, feature_dim, train_loader, val_loader,
                 num_classes, epochs=50, lr=0.1, device="cpu"):
    for p in encoder.parameters():
        p.requires_grad = False

    f_train, y_train = extract(encoder, train_loader, device)
    f_val, y_val = extract(encoder, val_loader, device)

    head = nn.Linear(feature_dim, num_classes).to(device)
    opt = SGD(head.parameters(), lr=lr, momentum=0.9, weight_decay=0)
    sched = CosineAnnealingLR(opt, T_max=epochs)

    ds = torch.utils.data.TensorDataset(f_train, y_train)
    train_iter = DataLoader(ds, batch_size=1024, shuffle=True)

    best_val = 0.0
    for ep in range(epochs):
        head.train()
        for x, y in train_iter:
            x, y = x.to(device), y.to(device)
            loss = F.cross_entropy(head(x), y)
            opt.zero_grad(); loss.backward(); opt.step()
        sched.step()

        head.eval()
        with torch.no_grad():
            acc = (head(f_val.to(device)).argmax(-1).cpu() == y_val).float().mean().item()
        best_val = max(best_val, acc)
    return best_val
``\`

## Report

``\`
[linear probe]
  encoder:     <name + pretrain checkpoint>
  feature_dim: <int>
  epochs:      <int>
  best_val_top1: <float>
``\`

## Rules

- Never update encoder weights during linear probe; that would be a fine-tune, not a probe.
- Precompute features once; retraining the encoder on every epoch wastes 100x compute.
- Use SGD with cosine schedule and no weight decay; Adam sometimes underperforms here.
- Sweep learning rates at least once per encoder family; the optimum varies across SSL methods.

```

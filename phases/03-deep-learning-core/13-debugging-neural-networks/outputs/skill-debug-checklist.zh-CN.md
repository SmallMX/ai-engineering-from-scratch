---
name: skill-debug-checklist
description: 用于调试神经网络训练失败的决策树清单
version: 1.0.0
phase: 3
lesson: 13
tags: [debugging, neural-networks, training, diagnostics, deep-learning]
---

# 神经网络调试清单

训练出错时使用的系统化调试协议。按顺序执行；大多数 bug 会在前 3 步被抓住。

## 训练前（预防 bug）

1. 打印模型架构和参数量。这个规模对你的数据合理吗？
2. 用随机输入运行一次 forward pass。输出 shape 和目标 shape 匹配吗？
3. 检查 labels dtype 是否正确（CrossEntropyLoss 需要 Long，BCELoss 需要 Float）
4. 验证数据 normalization：输入 mean 应该接近 0，std 接近 1
5. 打印 5 对随机 (input, label)。标签符合预期吗？
6. 确认 train/test split 没有重复样本

## Overfit-one-batch 测试（60 秒，抓住 80% bug）

1. 从训练集中取 8-32 个样本
2. 用合理学习率训练 200 step
3. Loss 应接近 0。训练 accuracy 应达到 100%
4. 如果失败：bug 在模型、损失函数或训练循环里，不在数据或超参数里
5. 如果通过：继续完整训练

## Loss 不下降

1. 检查学习率。尝试 3 个值：current/10、current、current*10
2. 打印每层梯度范数。全为零意味着网络死亡或 graph 被 detach
3. 检查参数上 `requires_grad=True`。检查是否调用 `loss.backward()`
4. 检查是否在 `loss.backward()` 前调用 `optimizer.zero_grad()`
5. 检查是否在 `loss.backward()` 后调用 `optimizer.step()`
6. 验证模型参数被传给优化器：`optimizer = Adam(model.parameters())`

## Loss 是 NaN 或 Inf

1. 把学习率降低 10 倍
2. 给所有 log() 调用添加 epsilon：`torch.log(x + 1e-7)`
3. 给所有除法添加 epsilon：`x / (y + 1e-8)`
4. BCE loss 前 clamp 预测：`torch.clamp(pred, 1e-7, 1 - 1e-7)`
5. 使用 `torch.autograd.detect_anomaly()` 找到确切操作
6. 检查输入数据中的 NaN：`assert not torch.isnan(x).any()`

## Loss 振荡

1. 把学习率降低 3-10 倍
2. 增大 batch size（减少梯度噪声）
3. 添加 gradient clipping：`torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)`
4. 从 SGD 切换到 Adam（每参数自适应 LR）
5. 在训练前 5-10% 添加 learning rate warmup

## 过拟合（train acc 高，test acc 低）

1. 添加 dropout（从 p=0.1 开始，增加到 0.5）
2. 给 optimizer 添加 weight decay：`Adam(params, weight_decay=1e-4)`
3. 减小模型规模（更少层或更窄层）
4. 添加 data augmentation
5. 使用 early stopping：validation loss 连续 5+ epoch 上升时停止
6. 检查 train/test sets 之间的数据泄漏

## 欠拟合（train 和 test acc 都低）

1. 增加模型容量（更多层、更宽层）
2. 训练更多 epochs
3. 谨慎提高学习率
4. 暂时移除正则化，验证模型能否学习
5. 检查模型对任务是否有足够表达能力

## Dead ReLU 神经元

1. 检查每层零激活比例。>50% 是问题
2. 切换到 LeakyReLU(0.01) 或 GELU
3. 对权重使用 Kaiming initialization
4. 降低学习率（大更新会把神经元推入死亡区）
5. 在激活函数前添加 batch normalization

## 快速参考：学习率起点

| 优化器 | 任务 | 起始 LR |
|--------|------|---------|
| Adam | 从零训练 | 1e-3 |
| Adam | 微调预训练 | 1e-5 |
| SGD + momentum | 从零训练 | 1e-1 |
| SGD + momentum | 微调预训练 | 1e-3 |
| AdamW | Transformer 训练 | 3e-4 |

## 快速参考：batch size 影响

| Batch size | 梯度噪声 | 内存 | 泛化 |
|------------|----------|------|------|
| 8-16 | 高（noisy） | 低 | 通常更好 |
| 32-64 | 中等 | 中等 | 好的默认值 |
| 128-256 | 低（smooth） | 高 | 可能需要 warmup |
| 512+ | 很低 | 很高 | 需要 LR scaling |

## 什么都不行时

1. 把模型简化到 1 个隐藏层。它能学吗？
2. 把数据简化到 100 个样本。它能过拟合吗？
3. 把 loss 替换为 MSE。它能收敛吗？
4. 把 optimizer 替换为 SGD(lr=0.01)。它有进展吗？
5. 把数据替换为 synthetic data（例如 y = x[0] > 0）。它能学吗？
6. 如果这些都不行：bug 在你没看的代码里（data loading、preprocessing、tensor shapes）

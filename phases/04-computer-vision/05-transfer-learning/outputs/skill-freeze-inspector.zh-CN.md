---
name: skill-freeze-inspector
description: 迁移学习与微调 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 5
tags: [computer-vision, transfer-learning, debugging, pytorch]
---

# 迁移学习与微调：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**迁移学习与微调**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 迁移学习复用预训练模型已经学到的视觉特征。
- freeze backbone 可以减少训练成本和过拟合风险。
- fine-tuning 需要小学习率和谨慎的 layer 解冻策略。
- domain shift 决定是否需要更深层微调。
- LoRA、linear probe 和 full fine-tune 适合不同数据规模。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-freeze-inspector
description: Report which parameters are trainable, which BatchNorm layers are in eval mode, and whether the optimizer is actually consuming the trainable parameters
version: 1.0.0
phase: 4
lesson: 5
tags: [computer-vision, transfer-learning, debugging, pytorch]
---

# Freeze Inspector

Transfer-learning bugs hide in three places: parameters that should be frozen but are not, parameters that should be trainable but are not, and optimizers that were built before the freeze state changed. This skill surfaces all three in one pass.

## When to use

- Right after setting `requires_grad` on a subset of parameters.
- Before the first training step of a fine-tune run.
- After calling `freeze_bn_stats` or any helper that flips BN mode.
- When val accuracy is stuck at random and you suspect nothing is actually training.

## Inputs

- `model`: a PyTorch `nn.Module`.
- `optimizer`: the optimizer about to be used for training.
- Optional `expected_frozen_prefixes`: list of parameter-name prefixes that should be frozen (e.g. `["conv1", "bn1", "layer1"]`).

## Steps

1. **Walk parameters.** For each `(name, param)`:
   - record `requires_grad`
   - record `shape` and `numel`

2. **Walk modules.** For each module:
   - if it is BatchNorm, record whether it is in eval mode and whether its affine parameters are trainable.

3. **Inspect the optimizer.** For each parameter group:
   - flatten its `params` into a set of `id(p)`.
   - compare with the set of all `id(p)` for params where `requires_grad == True`.

4. **Detect the four failure modes:**
   - `leaked_train`: a param has `requires_grad=True` but does not appear in the optimizer (gradient is computed but never applied).
   - `ghost_train`: a param appears in the optimizer but has `requires_grad=False` (optimizer state is wasted; can also cause bugs if you later re-enable requires_grad).
   - `bn_mismatch`: either (a) a BN layer is in train mode (accumulates running stats) while its affine parameters (`weight`, `bias`) are frozen, or (b) a BN layer is in eval mode (frozen stats) while its affine parameters are trainable. Both states are inconsistent and almost always a bug.
   - `expected_vs_actual`: any prefix listed in `expected_frozen_prefixes` still has a trainable parameter.

## Report

``\`
[freeze-inspector]
  model trainable params: <N>
  model frozen params:    <N>
  batchnorm layers in eval mode: <count>
  batchnorm layers in train mode: <count>

[optimizer coverage]
  trainable params fed to optimizer: <M> of <N>
  leaked_train: <list of names> (trainable but not in optimizer)
  ghost_train:  <list of names> (in optimizer but frozen)

[bn audit]
  mismatched layers: <list of names>

[expectations]
  expected_frozen_prefixes: <...>
  violating params:         <list>

[verdict]
  ok | <one-line summary of the most severe issue>
``\`

## Rules

- Only report parameter names; never print the weights themselves.
- Sort every list alphabetically by parameter name.
- If optimizer coverage is 100% and there are no mismatches, return `ok` and stop.
- For `leaked_train`, always recommend rebuilding the optimizer after the freeze state changed.
- For `ghost_train`, recommend removing the parameter group or setting `requires_grad=True` if the intent was to train it.

```

---
name: skill-imbalanced-data
description: 处理不平衡数据 的中文辅助提示，用于连接经典 ML 算法、诊断和业务指标
version: 1.0.0
phase: 2
lesson: 17
tags: [imbalanced-data, smote, class-weights, threshold-tuning, evaluation]
---

# 处理不平衡数据：中文使用说明

你将作为机器学习学习助手，帮助用户理解并应用本课主题：**处理不平衡数据**。

回答时遵循这些原则：

1. 先判断任务类型和数据形态，再推荐模型或诊断方法。
2. 保留代码标识符、API 名称、指标名称和路径的英文原写法。
3. 每次建议都要说明适用前提、常见失败模式和验证方式。
4. 用小数据例子解释算法行为，避免只给抽象定义。
5. 最后给出一个用户可以运行的检查步骤。

## 本课关键点

- 类别不平衡会让 accuracy 失去意义。
- precision、recall、F1 和 PR-AUC 更适合稀有正类任务。
- 重采样包括 oversampling、undersampling 和 SMOTE。
- class weights 让模型更重视少数类错误。
- 阈值调节可以按业务成本改变召回和误报取舍。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-imbalanced-data
description: Decision checklist for handling imbalanced classification problems
version: 1.0.0
phase: 2
lesson: 17
tags: [imbalanced-data, smote, class-weights, threshold-tuning, evaluation]
---

# Imbalanced Data Strategy

A decision checklist for handling imbalanced classification. Follow this sequence to pick the right approach for your problem.

## Step 1: Measure the imbalance

- Count samples per class
- Compute the imbalance ratio (majority / minority)
- Mild: ratio < 3:1 (e.g., 70/30)
- Moderate: ratio 3:1 to 20:1 (e.g., 95/5)
- Severe: ratio > 20:1 (e.g., 99/1)

## Step 2: Pick the right metric

Prefer precision/recall/F1 over accuracy for imbalanced datasets. Choose based on your problem:

| Situation | Primary Metric | Secondary Metric |
|-----------|---------------|-----------------|
| Missing positives is very costly (fraud, disease) | Recall | F2 score |
| False alarms are costly (spam filter, recommendations) | Precision | F0.5 score |
| Both matter roughly equally | F1 score | MCC |
| Need a single ranking metric | AUPRC | AUC-ROC |
| Need to compare across datasets | MCC | AUPRC |

## Step 3: Choose a rebalancing strategy

### By imbalance severity

| Imbalance | First Try | Second Try | Avoid |
|-----------|-----------|------------|-------|
| Mild (< 3:1) | Class weights | Threshold tuning | Oversampling (unnecessary) |
| Moderate (3:1 to 20:1) | SMOTE + class weights | Threshold tuning on top | Undersampling (too much data loss) |
| Severe (> 20:1) | SMOTE + class weights + threshold | Ensemble with balanced bagging | Undersampling alone |

### By dataset size

| Dataset Size | Preferred Strategy | Reason |
|-------------|-------------------|--------|
| < 1,000 samples | Oversampling or SMOTE | Cannot afford to lose majority data |
| 1,000 - 10,000 | SMOTE + threshold tuning | Enough minority samples for k-NN |
| > 10,000 | Class weights or undersampling | Fast, sufficient minority data |

## Step 4: Apply the technique

### Class weights (always try first)
- In sklearn: `class_weight='balanced'`
- No data modification needed
- Works with any loss-based model
- Equivalent to oversampling in expectation

### SMOTE
- Apply only to training data (never test/validation)
- Use k=5 neighbors (default)
- Combine with class weights for best results
- Watch for noisy synthetic points near the boundary

### Threshold tuning
- Train model, get predicted probabilities on validation set
- Sweep thresholds from 0.05 to 0.95
- Pick threshold maximizing your chosen metric
- Always tune on validation data, never test data

## Step 5: Validate properly

- Use stratified cross-validation (preserves class ratios in each fold)
- Report metrics on the original (non-resampled) test set
- Never apply SMOTE before splitting -- only on training folds
- Compare against the "always predict majority" baseline

## Step 6: Common mistakes to avoid

- Applying SMOTE to the entire dataset before train/test split (data leakage)
- Using accuracy as the evaluation metric
- Not trying class weights first (simplest approach, often sufficient)
- Oversampling and then cross-validating (synthetic points leak across folds)
- Ignoring threshold tuning (free performance, no retraining needed)
- Using random undersampling on small datasets (throws away too much data)

## Quick Decision Tree

1. Is the imbalance ratio < 3:1? -> Try class weights only
2. Is the dataset > 10,000 samples? -> Class weights + threshold tuning
3. Is the dataset < 1,000 samples? -> SMOTE + class weights
4. Otherwise -> SMOTE + class weights + threshold tuning
5. Still not good enough? -> Balanced bagging ensemble

```

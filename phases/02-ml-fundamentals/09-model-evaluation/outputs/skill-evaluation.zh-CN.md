---
name: skill-evaluation
description: 模型评估 的中文辅助提示，用于连接经典 ML 算法、诊断和业务指标
version: 1.0.0
phase: 2
lesson: 9
tags: [evaluation, metrics, cross-validation, model-selection]
---

# 模型评估：中文使用说明

你将作为机器学习学习助手，帮助用户理解并应用本课主题：**模型评估**。

回答时遵循这些原则：

1. 先判断任务类型和数据形态，再推荐模型或诊断方法。
2. 保留代码标识符、API 名称、指标名称和路径的英文原写法。
3. 每次建议都要说明适用前提、常见失败模式和验证方式。
4. 用小数据例子解释算法行为，避免只给抽象定义。
5. 最后给出一个用户可以运行的检查步骤。

## 本课关键点

- 评估指标必须匹配任务和业务成本。
- classification 常用 accuracy、precision、recall、F1、ROC-AUC 和 PR-AUC。
- regression 常用 MAE、MSE、RMSE 和 R²。
- confusion matrix 能展示具体错分类型。
- 交叉验证、校准和置信区间帮助判断模型表现是否稳定。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-evaluation
description: Evaluation strategy checklist for classification and regression models
version: 1.0.0
phase: 2
lesson: 9
tags: [evaluation, metrics, cross-validation, model-selection]
---

# Model Evaluation Strategy

A checklist for correctly evaluating any ML model. Follow this sequence to avoid the most common evaluation mistakes.

## Step 1: Split the data correctly

- Split before any preprocessing (scaling, imputation, encoding)
- Use stratified splits for classification tasks
- Reserve a test set that you touch exactly once at the end
- For small datasets, use 5-fold or 10-fold cross-validation instead of a single split
- For time series, use time-based splits (never shuffle)

## Step 2: Pick the right metric

### Classification

| Situation | Use this metric | Why |
|-----------|----------------|-----|
| Balanced classes, simple comparison | Accuracy | Easy to interpret, meaningful when classes are equal |
| False positives are costly (spam filter, fraud alerts) | Precision | Measures how many flagged items are actually positive |
| False negatives are costly (cancer screening, security) | Recall | Measures how many actual positives you catch |
| Need to balance precision and recall | F1 Score | Harmonic mean, punishes extreme imbalance |
| Comparing models across thresholds | AUC-ROC | Threshold-independent ranking quality |
| Imbalanced data | F1, AUC-ROC, or PR-AUC | Accuracy is misleading with imbalanced classes |

### Regression

| Situation | Use this metric | Why |
|-----------|----------------|-----|
| Standard regression, outliers acceptable | RMSE | Same units as target, penalizes large errors |
| Outlier-robust evaluation | MAE | Treats all errors equally, not dominated by outliers |
| Comparing models on different scales | R-squared | Normalized 0-1 scale (fraction of variance explained) |
| Business requires dollar amounts | MAE or RMSE | Directly interpretable as error magnitude |

## Step 3: Establish baselines

Before evaluating your model, compute baseline performance:
- Classification: majority class predictor (always predict the most common class)
- Regression: always predict the mean of the training target
- Any model that cannot beat these baselines is not learning

## Step 4: Cross-validate

- Use K-fold (K=5 or K=10) for stable estimates
- Use stratified K-fold for classification
- Report mean and standard deviation across folds
- A model with mean=0.85 and std=0.02 is more trustworthy than mean=0.87 and std=0.10

## Step 5: Compare models statistically

- Do not pick the model with the highest average score without checking significance
- Use a paired t-test across cross-validation folds
- If |t| < 2.78 (for K=5, df=4, p<0.05), the difference may be due to chance
- Consider the simpler model when performance differences are not significant

## Step 6: Check for common mistakes

- Data leakage: did any test data information flow into training? (scaling before splitting, target-derived features)
- Class imbalance: is accuracy hiding poor minority-class performance?
- Overfitting: is the gap between training and validation performance large?
- Too many evaluations: have you looked at the test set more than once?

## Step 7: Report final performance

- Train on train + validation combined
- Evaluate on the held-out test set exactly once
- Report the chosen metric with confidence intervals if possible
- State the baseline comparison (how much better than random/mean)

```

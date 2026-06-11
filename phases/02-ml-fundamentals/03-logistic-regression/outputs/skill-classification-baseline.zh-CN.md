---
name: skill-classification-baseline
description: 逻辑回归 的中文辅助提示，用于连接经典 ML 算法、诊断和业务指标
version: 1.0.0
phase: 2
lesson: 3
tags: [classification, logistic-regression, baseline, preprocessing]
---

# 逻辑回归：中文使用说明

你将作为机器学习学习助手，帮助用户理解并应用本课主题：**逻辑回归**。

回答时遵循这些原则：

1. 先判断任务类型和数据形态，再推荐模型或诊断方法。
2. 保留代码标识符、API 名称、指标名称和路径的英文原写法。
3. 每次建议都要说明适用前提、常见失败模式和验证方式。
4. 用小数据例子解释算法行为，避免只给抽象定义。
5. 最后给出一个用户可以运行的检查步骤。

## 本课关键点

- 逻辑回归用于分类，而不是回归；它输出类别概率。
- sigmoid 把任意实数 logit 映射到 0 到 1 之间。
- binary cross-entropy 惩罚对正确类别的低置信度。
- decision boundary 由线性 logit 决定，概率由 sigmoid 给出。
- 阈值选择会改变 precision、recall 和业务取舍。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-classification-baseline
description: Establish a strong classification baseline before reaching for complex models
version: 1.0.0
phase: 2
lesson: 3
tags: [classification, logistic-regression, baseline, preprocessing]
---

# Classification Baseline Guide

Before trying complex models, establish a baseline with logistic regression. It trains in seconds, produces probabilities, and is fully interpretable. A surprising number of real-world problems never need anything fancier.

## Decision Checklist

1. Is the decision boundary likely linear?
   - Yes: logistic regression will probably be sufficient
   - No: you still want it as a baseline to measure improvement

2. How many features do you have?
   - Under 50: standard logistic regression works fine
   - 50 to 10,000: add L2 regularization (Ridge)
   - Over 10,000 (e.g., TF-IDF text features): use L1 regularization (Lasso) or LinearSVC

3. Is the dataset imbalanced?
   - Under 5:1 ratio: probably fine without adjustment
   - 5:1 to 50:1: use `class_weight="balanced"` in sklearn
   - Over 50:1: combine class weighting with appropriate metric (precision, recall, or F1)

4. Are features on different scales?
   - Always standardize before logistic regression. It uses gradient-based optimization, and unscaled features slow convergence or distort the decision boundary.

5. Are there missing values?
   - Impute before fitting. Logistic regression cannot handle NaNs.
   - Use median imputation for numeric columns, mode for categorical.

## When logistic regression is good enough

- Binary classification with mostly linear feature relationships
- You need probability outputs (not just class labels)
- Interpretability is required (coefficients indicate feature importance direction and relative magnitude after standardization)
- Training data is small (hundreds to low thousands of samples)
- You need a fast model for real-time serving (single dot product at inference)
- Regulatory or compliance requirements demand explainability

## When to upgrade

- Accuracy plateaus well below the target and you have tried feature engineering
- The relationship between features and target is clearly nonlinear (check residual plots)
- You have large tabular data (10k+ rows): try gradient boosting (XGBoost or LightGBM)
- Features have complex interactions that polynomial features cannot capture
- You have image, text, or sequential data: logistic regression on raw inputs will not work

## Preprocessing steps for a classification baseline

1. **Train/test split** first, before any preprocessing. This prevents data leakage.
2. **Handle missing values**: median impute numeric, mode impute categorical.
3. **Encode categoricals**: one-hot for low cardinality (under 10 values), target encoding for higher. Fit target encoding only on training folds (use out-of-fold encoding to prevent leakage).
4. **Scale numerics**: StandardScaler (zero mean, unit variance). Fit on train, transform both.
5. **Fit logistic regression** with `C=1.0` (default regularization).
6. **Evaluate**: confusion matrix, precision, recall, F1. Not just accuracy.
7. **Tune threshold**: default 0.5 is rarely optimal. Sweep 0.1 to 0.9 and pick the threshold that matches your precision/recall priority.

## Common mistakes

- Evaluating only accuracy on imbalanced data (a model predicting the majority class scores high but is useless)
- Forgetting to scale features (logistic regression with unscaled features trains slowly and converges to a worse solution)
- Using the test set to tune the decision threshold (use validation or cross-validation)
- Skipping the baseline and jumping straight to XGBoost (you lose interpretability and have no reference point)
- Not checking for multicollinearity (highly correlated features inflate coefficient variance)

## Quick reference

| Scenario | Model | Regularization | Key setting |
|----------|-------|---------------|-------------|
| Few features, interpretable | LogisticRegression | L2 (default) | C=1.0 |
| Many features, some irrelevant | LogisticRegression | L1 | penalty="l1", solver="saga" |
| High-dim sparse (text) | SGDClassifier | L1 or ElasticNet | loss="log_loss" |
| Imbalanced classes | LogisticRegression | L2 | class_weight="balanced" |
| Need probabilities | LogisticRegression | L2 | predict_proba() |
| Need class labels only | LinearSVC | L2 | Faster than LR for large data |

```

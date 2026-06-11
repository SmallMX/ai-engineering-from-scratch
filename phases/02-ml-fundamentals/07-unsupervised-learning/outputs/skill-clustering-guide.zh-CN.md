---
name: skill-clustering-guide
description: 无监督学习 的中文辅助提示，用于连接经典 ML 算法、诊断和业务指标
version: 1.0.0
phase: 2
lesson: 7
tags: [clustering, k-means, dbscan, hierarchical, gmm, unsupervised]
---

# 无监督学习：中文使用说明

你将作为机器学习学习助手，帮助用户理解并应用本课主题：**无监督学习**。

回答时遵循这些原则：

1. 先判断任务类型和数据形态，再推荐模型或诊断方法。
2. 保留代码标识符、API 名称、指标名称和路径的英文原写法。
3. 每次建议都要说明适用前提、常见失败模式和验证方式。
4. 用小数据例子解释算法行为，避免只给抽象定义。
5. 最后给出一个用户可以运行的检查步骤。

## 本课关键点

- 无监督学习用于发现数据中的隐藏结构。
- clustering 把相似样本分组，常见方法包括 k-means 和 DBSCAN。
- dimensionality reduction 把高维数据压缩到低维表示。
- 异常检测可以看作发现不符合主结构的样本。
- 评估无监督模型时要结合内部指标和业务解释。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-clustering-guide
description: Choose the right clustering algorithm based on data shape, noise, and constraints
version: 1.0.0
phase: 2
lesson: 7
tags: [clustering, k-means, dbscan, hierarchical, gmm, unsupervised]
---

# Clustering Algorithm Selection Guide

Clustering has no single best algorithm. The right choice depends on cluster shape, whether you know the number of clusters, how much noise is in the data, and how large the dataset is.

## Decision Checklist

1. Do you know the number of clusters?
   - Yes: K-Means or GMM
   - No: DBSCAN (finds clusters automatically), or hierarchical (cut the dendrogram at different levels)

2. What shape are the clusters?
   - Roughly spherical (blob-like): K-Means
   - Elliptical with different sizes: GMM
   - Arbitrary shapes (crescents, rings, chains): DBSCAN
   - Nested or hierarchical: hierarchical clustering

3. Does the data contain noise or outliers?
   - Yes: DBSCAN (labels noise points explicitly) or GMM (low-probability points are outliers)
   - No: K-Means is fine

4. Do you need soft assignments (probabilities)?
   - Yes: GMM gives P(cluster | data point) for each cluster
   - No: K-Means or DBSCAN give hard assignments

5. How large is the dataset?
   - Under 10,000: any algorithm works
   - 10,000 to 1,000,000: K-Means (fast), Mini-Batch K-Means (faster)
   - Over 1,000,000: Mini-Batch K-Means or BIRCH. Hierarchical is too slow.

## When to use each approach

**K-Means**: the default starting point. Fast (O(n * k * iterations)), simple, and good enough for many problems. Use the elbow method or silhouette score to pick K. Limitations: assumes spherical clusters, sensitive to initialization (use K-Means++ or run multiple times), cannot handle varying cluster sizes well.

**DBSCAN**: best for discovering clusters of arbitrary shape and automatically detecting outliers. Two parameters: eps (neighborhood radius) and min_samples (minimum density). Does not require specifying K. Limitations: struggles when clusters have very different densities, and tuning eps can be tricky. Use a k-distance plot to estimate eps: compute the distance to each point's k-th nearest neighbor, sort, and look for an elbow.

**Hierarchical (Agglomerative)**: builds a tree of merges. Useful when you want to explore cluster structure at multiple granularities (cut the dendrogram at different heights). Ward's linkage works best for compact clusters. Single linkage finds elongated clusters but is sensitive to noise. Limitations: O(n^2) memory and O(n^3) time, so impractical for large datasets.

**GMM (Gaussian Mixture Models)**: soft clustering with probabilistic assignments. Models each cluster as a Gaussian distribution with its own mean and covariance. Better than K-Means when clusters are elliptical or overlapping. Use BIC (Bayesian Information Criterion) to select the number of components. Limitations: assumes Gaussian distributions, can fail on non-convex shapes, sensitive to initialization.

## Evaluating cluster quality (no labels)

| Metric | What it measures | Range | Use when |
|--------|-----------------|-------|----------|
| Silhouette score | Cohesion vs separation | -1 to 1 (higher is better) | Comparing K values or algorithms |
| Inertia (within-cluster SS) | Tightness of clusters | 0 to inf (lower is better) | Elbow method for K-Means |
| BIC / AIC | Model fit with complexity penalty | Lower is better | Choosing number of GMM components |
| Calinski-Harabasz index | Ratio of between to within variance | Higher is better | Quick comparison |
| Davies-Bouldin index | Average similarity between clusters | Lower is better | Penalizes overlapping clusters |

## Common mistakes

- Running K-Means without scaling features (features on larger scales dominate the distance calculation)
- Picking K by eyeballing data in 2D when the actual data is high-dimensional (use silhouette scores)
- Using K-Means on non-spherical clusters (crescent or ring-shaped data needs DBSCAN)
- Setting DBSCAN eps too large (everything in one cluster) or too small (everything is noise)
- Treating cluster labels as ground truth (clustering is exploratory; validate with domain knowledge)
- Running hierarchical clustering on datasets with more than 20,000 points (memory and time explode)

## Quick reference

| Algorithm | Cluster shape | Finds K | Handles noise | Soft assignments | Scalability |
|-----------|--------------|---------|---------------|-----------------|-------------|
| K-Means | Spherical | No (you set K) | No | No | Millions |
| Mini-Batch K-Means | Spherical | No | No | No | Tens of millions |
| DBSCAN | Arbitrary | Yes | Yes | No | Hundreds of thousands |
| Hierarchical | Any (linkage-dependent) | Flexible (cut dendrogram) | Depends on linkage | No | Under 20k |
| GMM | Elliptical | No (you set K) | Partial (low probability) | Yes | Under 100k |
| HDBSCAN | Arbitrary | Yes | Yes | Partial | Hundreds of thousands |

```

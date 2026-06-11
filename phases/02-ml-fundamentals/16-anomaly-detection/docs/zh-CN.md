# 异常检测

> 正常很容易定义。异常就是那些不合群的东西。

**类型：** Build  
**语言：** Python  
**前置知识：** Phase 2, Lessons 01-15  
**时间：** 约 60 分钟

## 学习目标

- 异常检测寻找偏离正常模式的数据点。
- 统计方法使用 z-score、IQR 或分布假设。
- 距离和密度方法包括 kNN、LOF 和 DBSCAN。
- Isolation Forest 通过随机切分隔离异常点。
- 阈值选择要结合误报成本、漏报成本和业务反馈。

## 问题

本课是 Phase 2 机器学习基础的一部分。目标是把 Phase 1 的数学工具落到经典 ML 工作流里：如何定义问题，如何选择模型，如何训练、评估、诊断，并把实验变成可复现的 pipeline。

学习时不要只记算法名字。你要能回答：这个模型在假设什么？它优化什么目标？什么时候会失败？应该用什么指标判断它是否真的有效？

## 核心概念

1. 异常检测寻找偏离正常模式的数据点。
2. 统计方法使用 z-score、IQR 或分布假设。
3. 距离和密度方法包括 kNN、LOF 和 DBSCAN。
4. Isolation Forest 通过随机切分隔离异常点。
5. 阈值选择要结合误报成本、漏报成本和业务反馈。

## 动手构建

按照本课 `code/` 目录运行示例。先理解从零实现，再观察同一思想如何映射到常用 ML API。每次运行都记录输入特征、目标变量、训练配置、评估指标和错误样本。

建议流程：

1. 明确任务类型：classification、regression、clustering、ranking、forecasting 或 anomaly detection。
2. 明确 baseline：先用简单模型得到可解释的基准结果。
3. 查看数据划分方式，避免泄漏和错误评估。
4. 运行本课代码，并改动关键超参数观察指标变化。
5. 总结模型失败模式，以及下一步应该调数据、特征、模型还是指标。

## 关键公式与代码片段

以下片段保留自英文原文，便于直接复制运行或对照数学符号。

```mermaid
flowchart TD
    A[Anomaly Types] --> B[Point Anomaly]
    A --> C[Contextual Anomaly]
    A --> D[Collective Anomaly]

    B --> B1["Single unusual value<br/>Temperature: 500F"]
    C --> C1["Unusual in context<br/>90F in January"]
    D --> D1["Unusual sequence<br/>50 failed logins"]

    style B fill:#fdd,stroke:#333
    style C fill:#ffd,stroke:#333
    style D fill:#fdf,stroke:#333
```

```text
z_score = (x - mean) / std
anomaly if |z_score| > threshold
```

```text
Q1 = 25th percentile
Q3 = 75th percentile
IQR = Q3 - Q1
lower_bound = Q1 - factor * IQR
upper_bound = Q3 + factor * IQR
anomaly if x < lower_bound or x > upper_bound
```

```mermaid
flowchart TD
    A[All Data Points] --> B{Random Feature + Random Split}
    B --> C[Left Partition]
    B --> D[Right Partition]
    C --> E{Random Feature + Random Split}
    E --> F[Normal Point - deep in tree]
    E --> G[More splits needed...]
    D --> H["Anomaly - isolated quickly (short path)"]

    style H fill:#fdd,stroke:#333
    style F fill:#dfd,stroke:#333
```

```text
score(x) = 2^(-average_path_length(x) / c(n))
```

```mermaid
flowchart LR
    A[Raw Data] --> B[Train on Normal Data Only]
    B --> C[Score All Test Data]
    C --> D[Rank by Anomaly Score]
    D --> E[Evaluate Top-K Flagged Items]
    E --> F[Precision at K / AUPRC]

    style A fill:#f9f,stroke:#333
    style F fill:#9f9,stroke:#333
```

```python
def zscore_detect(X, threshold=3.0):
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std[std == 0] = 1.0
    z = np.abs((X - mean) / std)
    return z.max(axis=1) > threshold
```

```python
def iqr_detect(X, factor=1.5):
    q1 = np.percentile(X, 25, axis=0)
    q3 = np.percentile(X, 75, axis=0)
    iqr = q3 - q1
    iqr[iqr == 0] = 1.0
    lower = q1 - factor * iqr
    upper = q3 + factor * iqr
    outside = (X < lower) | (X > upper)
    return outside.any(axis=1)
```

```python
class IsolationTree:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def fit(self, X, depth=0):
        n, p = X.shape
        if depth >= self.max_depth or n <= 1:
            self.is_leaf = True
            self.size = n
            return self
        self.is_leaf = False
        self.feature = np.random.randint(p)
        x_min = X[:, self.feature].min()
        x_max = X[:, self.feature].max()
        if x_min == x_max:
            self.is_leaf = True
            self.size = n
            return self
        self.threshold = np.random.uniform(x_min, x_max)
        left_mask = X[:, self.feature] < self.threshold
        self.left = IsolationTree(self.max_depth).fit(X[left_mask], depth + 1)
        self.right = IsolationTree(self.max_depth).fit(X[~left_mask], depth + 1)
        return self
```

```python
class IsolationForest:
    def __init__(self, n_estimators=100, max_samples=256, seed=42):
        self.n_estimators = n_estimators
        self.max_samples = max_samples

    def fit(self, X):
        sample_size = min(self.max_samples, X.shape[0])
        max_depth = int(np.ceil(np.log2(sample_size)))
        for _ in range(self.n_estimators):
            idx = rng.choice(X.shape[0], size=sample_size, replace=False)
            tree = IsolationTree(max_depth=max_depth)
            tree.fit(X[idx])
            self.trees.append(tree)

    def anomaly_score(self, X):
        avg_path = average path length across all trees
        scores = 2.0 ** (-avg_path / c(max_samples))
        return scores
```

> 英文原文还包含 3 个代码/公式块；中文正文保留关键片段，完整实现见本课 `code/` 目录。


## 使用它

完成本课后，你应该能把这个算法放进真实 ML 流程：先建立 baseline，再用合适指标评估，最后根据 bias、variance、数据质量和业务成本决定下一步。

## 练习

1. 用本课算法构建一个最小 baseline。
2. 改变一个关键超参数，并解释指标变化。
3. 找出至少一个失败样本或错误分组，说明模型为什么错。
4. 完成 `quiz.zh-CN.json` 中的测验，并回到英文原文核对术语。

## 关键术语

| 术语 | 中文理解 | ML 中的作用 |
|------|----------|-------------|
| baseline | 基准模型 | 给复杂方法提供参照 |
| feature | 特征 | 模型实际看到的输入表示 |
| target | 目标 | 模型要预测或解释的变量 |
| metric | 指标 | 把模型表现转成可比较数字 |
| generalization | 泛化 | 模型在未见数据上的表现 |
| leakage | 泄漏 | 训练时意外使用了评估时不可用的信息 |

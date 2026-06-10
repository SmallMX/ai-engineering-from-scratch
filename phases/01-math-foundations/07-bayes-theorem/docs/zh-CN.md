# 贝叶斯定理

> 概率关心你预期什么；贝叶斯定理关心你学到了什么。

**类型：** Learn  
**语言：** Python  
**前置知识：** Phase 1，第 06 课  
**时间：** 约 60 分钟

## 学习目标

- Bayes theorem 用 evidence 更新 belief：posterior ∝ likelihood × prior。
- prior 是观察数据前的信念，likelihood 是数据在某假设下出现的概率，posterior 是更新后的信念。
- base rate 很重要，忽略它会导致医学检测、异常检测和分类任务中的误判。
- Naive Bayes 假设特征条件独立，用简单概率模型做文本分类。
- Bayesian thinking 在不确定性估计、A/B test、垃圾邮件过滤和诊断系统中非常实用。

## 问题

本课是 Phase 1 数学基础的一部分。目标不是把数学当成孤立公式来背，而是把它连接到 AI 系统中的具体动作：数据如何被表示，模型如何变换表示，loss 如何给出方向，以及训练为什么会稳定或失稳。

学习时请把每个概念都追问三件事：它在空间中做了什么？它在代码里对应哪个运算？它在神经网络、检索、生成模型或优化中解决什么问题？

## 核心概念

1. Bayes theorem 用 evidence 更新 belief：posterior ∝ likelihood × prior。
2. prior 是观察数据前的信念，likelihood 是数据在某假设下出现的概率，posterior 是更新后的信念。
3. base rate 很重要，忽略它会导致医学检测、异常检测和分类任务中的误判。
4. Naive Bayes 假设特征条件独立，用简单概率模型做文本分类。
5. Bayesian thinking 在不确定性估计、A/B test、垃圾邮件过滤和诊断系统中非常实用。

## 动手构建

按照本课 `code/` 目录运行示例实现。优先先读从零实现版本，再对照 NumPy、PyTorch 或 Julia 中的同类操作。你应该能解释每一行 shape 如何变化，而不是只得到一个数值结果。

建议流程：

1. 先手算一个 2D 或 2x2 的小例子。
2. 运行本课代码，确认输出和手算一致。
3. 改动输入 shape 或参数，观察结果如何变化。
4. 把同一概念连接回 AI 场景，例如 embeddings、attention、loss、optimization 或 sampling。

## 关键公式与代码片段

以下片段保留自英文原文，便于直接复制运行或对照数学符号。

```text
P(A|B) = P(A and B) / P(B)
```

```text
P(B|A) = P(A and B) / P(A)
```

```text
P(A and B) = P(A|B) * P(B) = P(B|A) * P(A)

Therefore:

P(A|B) = P(B|A) * P(A) / P(B)
```

```text
P(B) = P(B|A) * P(A) + P(B|not A) * P(not A)
```

```text
P(sick)          = 0.0001     (prior: disease is rare)
P(positive|sick) = 0.99       (likelihood: test catches it)
P(positive|healthy) = 0.01    (false positive rate)

P(positive) = P(positive|sick) * P(sick) + P(positive|healthy) * P(healthy)
            = 0.99 * 0.0001 + 0.01 * 0.9999
            = 0.000099 + 0.009999
            = 0.010098

P(sick|positive) = P(positive|sick) * P(sick) / P(positive)
                 = 0.99 * 0.0001 / 0.010098
                 = 0.0098
                 = 0.98%
```

```text
P(spam)                = 0.3      (30% of email is spam)
P("lottery"|spam)      = 0.05     (5% of spam emails contain "lottery")
P("lottery"|not spam)  = 0.001    (0.1% of legitimate emails contain "lottery")

P("lottery") = 0.05 * 0.3 + 0.001 * 0.7
             = 0.015 + 0.0007
             = 0.0157

P(spam|"lottery") = 0.05 * 0.3 / 0.0157
                  = 0.955
                  = 95.5%
```

```text
P(class | feature_1, feature_2, ..., feature_n)
  = P(class) * P(feature_1|class) * P(feature_2|class) * ... * P(feature_n|class)
    / P(feature_1, feature_2, ..., feature_n)
```

```text
score(class) = P(class) * product of P(feature_i | class)
```

```text
P("free"|spam) = (number of spam emails containing "free") / (total spam emails)
```

```text
P(word|class) = (count(word, class) + 1) / (total_words_in_class + vocabulary_size)
```

```text
P(parameters|data) proportional to P(data|parameters) * P(parameters)
```

```python
def bayes(prior, likelihood, false_positive_rate):
    evidence = likelihood * prior + false_positive_rate * (1 - prior)
    posterior = likelihood * prior / evidence
    return posterior

result = bayes(prior=0.0001, likelihood=0.99, false_positive_rate=0.01)
print(f"P(sick|positive) = {result:.4f}")
```

> 英文原文还包含 7 个代码/公式块；中文正文保留关键块，完整可运行代码见本课 `code/` 目录。


## 使用它

完成本课后，你应该能在真实 AI 代码中识别这个数学概念出现的位置，并用它调试问题：shape mismatch、相似度异常、loss 不下降、数值爆炸、采样过于随机或过于保守等。

## 练习

1. 用一个最小数字例子复现本课核心公式。
2. 运行本课 `code/` 中的 Python 或 Julia 文件，并记录每个中间变量的 shape。
3. 找一个 AI 应用场景，说明本课概念在其中的输入、输出和失败模式。
4. 完成 `quiz.zh-CN.json` 中的测验，并回到英文原文核对术语。

## 关键术语

| 术语 | 中文理解 | AI 中的作用 |
|------|----------|-------------|
| representation | 表示 | 把现实对象变成可计算向量或张量 |
| transformation | 变换 | 用矩阵、函数或运算改变表示 |
| gradient | 梯度 | 指示 loss 变化最快方向，用于学习 |
| stability | 稳定性 | 保证训练和数值计算不会爆炸或消失 |
| approximation | 近似 | 在可计算成本内保留最重要结构 |

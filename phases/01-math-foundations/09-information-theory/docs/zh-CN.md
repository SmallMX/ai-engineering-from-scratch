# 信息论

> 信息论衡量惊讶程度。Loss functions 正是建立在它之上。

**类型：** Learn  
**语言：** Python  
**前置知识：** Phase 1，第 06 课  
**时间：** 约 60 分钟

## 学习目标

- self-information 衡量某个事件带来的惊讶程度：越罕见，信息量越大。
- entropy 是分布的平均不确定性。
- cross-entropy 衡量用预测分布编码真实分布需要多少额外信息。
- KL divergence 衡量一个分布相对另一个分布的差异，是变分推断和 RL 中的核心量。
- language model 的 next-token loss 本质上就是 cross-entropy。

## 问题

本课是 Phase 1 数学基础的一部分。目标不是把数学当成孤立公式来背，而是把它连接到 AI 系统中的具体动作：数据如何被表示，模型如何变换表示，loss 如何给出方向，以及训练为什么会稳定或失稳。

学习时请把每个概念都追问三件事：它在空间中做了什么？它在代码里对应哪个运算？它在神经网络、检索、生成模型或优化中解决什么问题？

## 核心概念

1. self-information 衡量某个事件带来的惊讶程度：越罕见，信息量越大。
2. entropy 是分布的平均不确定性。
3. cross-entropy 衡量用预测分布编码真实分布需要多少额外信息。
4. KL divergence 衡量一个分布相对另一个分布的差异，是变分推断和 RL 中的核心量。
5. language model 的 next-token loss 本质上就是 cross-entropy。

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
I(x) = -log(p(x))
```

```text
Event              Probability    Surprise (bits)
Fair coin heads    0.5            1.0
Rolling a 6        0.167          2.58
1-in-1000 event    0.001          9.97
Certain event      1.0            0.0
```

```text
H(P) = -sum( p(x) * log(p(x)) )  for all x
```

```text
Fair coin:    H = -(0.5 * log2(0.5) + 0.5 * log2(0.5)) = 1.0 bit
Biased coin:  H = -(0.99 * log2(0.99) + 0.01 * log2(0.01)) = 0.08 bits
```

```text
H(P, Q) = -sum( p(x) * log(q(x)) )  for all x
```

```text
H(P, Q) = -log(q(true_class))
```

```text
D_KL(P || Q) = sum( p(x) * log(p(x) / q(x)) )  for all x
             = H(P, Q) - H(P)
```

```text
I(X; Y) = H(X) - H(X|Y)
        = H(X) + H(Y) - H(X, Y)
```

```text
H(Y|X) = H(X,Y) - H(X)
```

```text
0 <= H(Y|X) <= H(Y)
```

```text
H(X,Y) = -sum sum p(x,y) * log(p(x,y))   for all x, y
```

```text
H(X,Y) <= H(X) + H(Y)
```

> 英文原文还包含 13 个代码/公式块；中文正文保留关键块，完整可运行代码见本课 `code/` 目录。


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

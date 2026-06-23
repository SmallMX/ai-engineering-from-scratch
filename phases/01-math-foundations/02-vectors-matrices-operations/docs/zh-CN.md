# 向量、矩阵与运算

> 每个神经网络都只是加了一些步骤的矩阵乘法。

**类型：** Build  
**语言：** Python, Julia  
**前置知识：** Phase 1，第 01 课  
**时间：** 约 60 分钟

## 学习目标

- 向量是有顺序的数字列表，在 AI 中表示数据点、特征或参数。
- 矩阵是二维数字网格，神经网络的权重矩阵会把输入向量变成输出向量。
- 矩阵乘法的 shape 规则是 `(m x n) @ (n x p) = (m x p)`，内部维度必须匹配。
- element-wise multiplication 和 matrix multiplication 含义不同，是初学者最常见的 shape bug 来源。
- broadcasting 让 bias vector 可以自动扩展到 batch 维度。

## 问题

本课是 Phase 1 数学基础的一部分。目标不是把数学当成孤立公式来背，而是把它连接到 AI 系统中的具体动作：数据如何被表示，模型如何变换表示，loss 如何给出方向，以及训练为什么会稳定或失稳。

学习时请把每个概念都追问三件事：它在空间中做了什么？它在代码里对应哪个运算？它在神经网络、检索、生成模型或优化中解决什么问题？

## 核心概念

1. 向量是有顺序的数字列表，在 AI 中表示数据点、特征或参数。
2. 矩阵是二维数字网格，神经网络的权重矩阵会把输入向量变成输出向量。
3. 矩阵乘法的 shape 规则是 `(m x n) @ (n x p) = (m x p)`，内部维度必须匹配。
4. element-wise multiplication 和 matrix multiplication 含义不同，是初学者最常见的 shape bug 来源。
5. broadcasting 让 bias vector 可以自动扩展到 batch 维度。

## 动手构建

按照本课 `code/` 目录运行示例实现。优先先读从零实现版本，再对照 NumPy、PyTorch 或 Julia 中的同类操作。你应该能解释每一行 shape 如何变化，而不是只得到一个数值结果。

建议流程：

1. 先手算一个 2D 或 2x2 的小例子。
2. 运行本课代码，确认输出和手算一致。
3. 改动输入 shape 或参数，观察结果如何变化。
4. 把同一概念连接回 AI 场景，例如 embeddings、attention、loss、optimization 或 sampling。

## 关键公式与代码片段

以下片段为核心数学概念与代码实现，已添加详细的中文注释说明，便于直接阅读、复制运行或对照数学符号。

```text
-- 神经网络单层的前向传播公式：输出 = 激活函数(权重矩阵 @ 输入向量 + 偏置向量)
output = activation(weights @ input + bias)
```

```text
v = [3, 4]        -- 二维向量（2D vector）
w = [1, 0, -2]    -- 三维向量（3D vector）
```

```text
A = | 1  2  3 |     -- 2x3 矩阵（2 行 3 列）
    | 4  5  6 |
```

```text
(128 x 784) @ (784 x 1) = (128 x 1)
  weights       input       output    -- 对应：权重 @ 输入 = 输出

Inner dimensions: 784 = 784  -- 内维度匹配，矩阵乘法有效
```

```text
-- 逐元素相乘（Hadamard 积）：对应位置的元素直接相乘
| 1  2 |   | 5  6 |   | 5  12 |
| 3  4 | * | 7  8 | = | 21 32 |
```

```text
-- 矩阵乘法（点积/矩阵积）：左矩阵行向量乘以右矩阵列向量并求和
| 1  2 |   | 5  6 |   | 1*5+2*7  1*6+2*8 |   | 19  22 |
| 3  4 | @ | 7  8 | = | 3*5+4*7  3*6+4*8 | = | 43  50 |
```

```text
| 1  2  3 |   +   [10, 20, 30]
| 4  5  6 |

广播机制（Broadcasting）在行方向上复制拉伸向量，使其形状与矩阵一致：

| 1  2  3 |   | 10  20  30 |   | 11  22  33 |
| 4  5  6 | + | 10  20  30 | = | 14  25  36 |
```

```python
class Vector:
    """从零实现的向量类，包含基本的向量运算"""
    def __init__(self, data):
        # 将输入数据转换为列表存储
        self.data = list(data)
        # 向量的维度（长度）
        self.size = len(self.data)

    def __repr__(self):
        # 友好的打印输出格式
        return f"Vector({self.data})"

    def __add__(self, other):
        # 向量加法：对应元素相加
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        # 向量减法：对应元素相减
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        # 数量乘法（标量乘法）：标量乘以向量中的每个元素
        return Vector([x * scalar for x in self.data])

    def dot(self, other):
        # 向量点积（内积）：对应元素乘积之和
        return sum(a * b for a, b in zip(self.data, other.data))

    def magnitude(self):
        # 向量的模（L2 范数）：各元素平方和的平方根
        return sum(x ** 2 for x in self.data) ** 0.5
```

```python
class Matrix:
    """从零实现的矩阵类，包含基本的矩阵运算与线性代数操作"""
    def __init__(self, data):
        # 使用嵌套列表存储矩阵的行数据
        self.data = [list(row) for row in data]
        # 矩阵的行数
        self.rows = len(self.data)
        # 矩阵的列数
        self.cols = len(self.data[0])
        # 矩阵的形状 (行数, 列数)
        self.shape = (self.rows, self.cols)

    def __repr__(self):
        # 友好的打印输出格式，按行换行对齐
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix({self.shape}):\n  {rows_str}"

    def __add__(self, other):
        # 矩阵加法：对应元素相加（要求形状相同）
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __sub__(self, other):
        # 矩阵减法：对应元素相减（要求形状相同）
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def scalar_multiply(self, scalar):
        # 数量乘法（标量乘法）：标量乘以矩阵中的每个元素
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def element_wise_multiply(self, other):
        # 逐元素相乘（Hadamard 积）：对应位置元素相乘（要求形状相同）
        return Matrix([
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def matmul(self, other):
        # 矩阵乘法：结果矩阵的 i 行 j 列元素为左矩阵第 i 行与右矩阵第 j 列的点积
        # 要求：当前矩阵的列数 (self.cols) 必须等于右矩阵的行数 (other.rows)
        return Matrix([
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ])

    def transpose(self):
        # 矩阵转置：行与列互换 (A^T)_ij = A_ji
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

    def determinant(self):
        # 计算矩阵行列式（仅支持方阵，采用拉普拉斯展开递归计算）
        if self.shape == (1, 1):
            return self.data[0][0]
        if self.shape == (2, 2):
            # 2x2 矩阵行列式公式：ad - bc
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        # 沿第一行进行拉普拉斯展开
        for j in range(self.cols):
            # 构造余子式矩阵（划去第 0 行和第 j 列后的子矩阵）
            minor = Matrix([
                [self.data[i][k] for k in range(self.cols) if k != j]
                for i in range(1, self.rows)
            ])
            # 累加代数余子式
            det += ((-1) ** j) * self.data[0][j] * minor.determinant()
        return det

    def inverse_2x2(self):
        # 计算 2x2 矩阵的逆矩阵
        det = self.determinant()
        if det == 0:
            raise ValueError("矩阵是奇异的（行列式为 0），不存在逆矩阵")
        # 2x2 矩阵求逆公式：(1/det) * [[d, -b], [-c, a]]
        return Matrix([
            [self.data[1][1] / det, -self.data[0][1] / det],
            [-self.data[1][0] / det, self.data[0][0] / det]
        ])

    @staticmethod
    def identity(n):
        # 生成大小为 n x n 的单位矩阵（对角线为 1，其余为 0）
        return Matrix([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])
```

```python
# 初始化两个 2x2 矩阵
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

# 测试矩阵加法
print("A + B =", (A + B).data)
# 测试矩阵乘法
print("A @ B =", A.matmul(B).data)
# 测试矩阵转置
print("A^T =", A.transpose().data)
# 测试行列式计算
print("det(A) =", A.determinant())
# 测试 2x2 矩阵求逆
print("A^-1 =", A.inverse_2x2().data)

# 生成 2x2 单位矩阵
I = Matrix.identity(2)
# 验证性质：A @ A^-1 = I（因浮点数精度限制，可能存在微小的极小值偏差）
print("A @ A^-1 =", A.matmul(A.inverse_2x2()).data)
```

```python
import random

# 输入向量 (3 x 1 矩阵/列向量)
inputs = Matrix([[0.5], [0.8], [0.2]])
# 权重矩阵 (2 x 3 矩阵，值随机初始化在 [-1, 1] 之间)
weights = Matrix([
    [random.uniform(-1, 1) for _ in range(3)]
    for _ in range(2)
])
# 偏置向量 (2 x 1 矩阵/列向量，初始化为 0.1)
bias = Matrix([[0.1], [0.1]])

# 实现矩阵形式的 ReLU 激活函数：f(x) = max(0, x)
def relu_matrix(m):
    return Matrix([[max(0, val) for val in row] for row in m.data])

# 线性组合：Z = W @ X + b
pre_activation = weights.matmul(inputs) + bias
# 非线性激活：A = ReLU(Z)
output = relu_matrix(pre_activation)

# 输出相关形状与结果
print(f"Input shape: {inputs.shape}")
print(f"Weight shape: {weights.shape}")
print(f"Output shape: {output.shape}")
print(f"Output: {output.data}")
```

```python
import numpy as np

# 使用 NumPy 定义 2x2 矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# NumPy 常见运算测试
print("A + B =\n", A + B)                  # 矩阵相加
print("A * B (element-wise) =\n", A * B)    # 逐元素相乘（Hadamard 积）
print("A @ B (matrix multiply) =\n", A @ B) # 矩阵乘法
print("A^T =\n", A.T)                       # 矩阵转置
print("det(A) =", np.linalg.det(A))         # 计算行列式
print("A^-1 =\n", np.linalg.inv(A))         # 计算逆矩阵
print("I =\n", np.eye(2))                   # 生成 2x2 单位矩阵

# 使用 NumPy 构建神经网络层的前向传播
inputs = np.random.randn(3, 1)             # 随机输入向量 (3 x 1)
weights = np.random.randn(2, 3)            # 随机权重矩阵 (2 x 3)
bias = np.array([[0.1], [0.1]])            # 偏置向量 (2 x 1)
# 一行代码实现：ReLU(W @ X + b)，使用 np.maximum 实现逐元素取最大值
output = np.maximum(0, weights @ inputs + bias)

print(f"\nNeural network layer: {weights.shape} @ {inputs.shape} = {output.shape}")
print(f"Output:\n{output}")
```

> 英文原文还包含 1 个代码/公式块；中文正文保留关键块，完整可运行代码见本课 `code/` 目录。


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

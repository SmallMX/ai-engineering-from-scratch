# 线性代数直觉

> 每个 AI 模型，本质上都是披着华丽外衣的矩阵数学。

**类型：** Learn  
**语言：** Python, Julia  
**前置知识：** Phase 0  
**时间：** 约 60 分钟

## 学习目标

- 向量既是点，也是方向；坐标告诉你它在空间中的位置。
- 矩阵是空间变换：旋转、缩放、投影、拉伸都可以由矩阵表达。
- 点积衡量两个向量的对齐程度，是相似度搜索和 attention score 的基础。
- 线性无关、rank 和 basis 告诉你一组特征到底包含多少独立信息。
- LoRA 用低秩矩阵表示权重更新，把大模型微调压缩到很少的可训练参数。

## 问题

本课是 Phase 1 数学基础的一部分。目标不是把数学当成孤立公式来背，而是把它连接到 AI 系统中的具体动作：数据如何被表示，模型如何变换表示，loss 如何给出方向，以及训练为什么会稳定或失稳。

学习时请把每个概念都追问三件事：它在空间中做了什么？它在代码里对应哪个运算？它在神经网络、检索、生成模型或优化中解决什么问题？

## 核心概念

1. 向量既是点，也是方向；坐标告诉你它在空间中的位置。
2. 矩阵是空间变换：旋转、缩放、投影、拉伸都可以由矩阵表达。
3. 点积衡量两个向量的对齐程度，是相似度搜索和 attention score 的基础。
4. 线性无关、rank 和 basis 告诉你一组特征到底包含多少独立信息。
5. LoRA 用低秩矩阵表示权重更新，把大模型微调压缩到很少的可训练参数。

## 动手构建

按照本课 `code/` 目录运行示例实现。优先先读从零实现版本，再对照 NumPy、PyTorch 或 Julia 中的同类操作。你应该能解释每一行 shape 如何变化，而不是只得到一个数值结果。

建议流程：

1. 先手算一个 2D 或 2x2 的小例子。
2. 运行本课代码，确认输出和手算一致。
3. 改动输入 shape 或参数，观察结果如何变化。
4. 把同一概念连接回 AI 场景，例如 embeddings、attention、loss、optimization 或 sampling。

## 关键公式与代码片段

以下片段保留自英文原文，便于直接复制运行或对照数学符号。

### 1. 矩阵乘法作为空间变换 (Matrix Transformation)
在几何上，矩阵乘法代表着空间变换（如旋转、缩放、降维等），它将输入向量映射到新的坐标空间。这正是神经网络中**线性层 (Linear Layer / Dense Layer)** 的数学本质：通过权重矩阵的乘法将输入的特征向量变换到新的表示空间。

```mermaid
graph LR
    subgraph Before
        A["Point A"]
        B["Point B"]
    end
    subgraph Matrix["Matrix Multiplication"]
        M["M (transformation)"]
    end
    subgraph After
        A2["Point A'"]
        B2["Point B'"]
    end
    A --> M
    B --> M
    M --> A2
    M --> B2
```

### 2. 向量点积与方向相似度 (Dot Product & Similarity)
点积用于衡量两个向量在空间中的夹角方向关系。在 AI 中，它构成了**余弦相似度 (Cosine Similarity)** 以及 **Transformer 注意力机制 (Attention)** 的核心——Query 与 Key 向量的点积越大，说明特征相似度或关联度越高；点积为 0 则表示两特征正交无关。

```text
a · b = a₁×b₁ + a₂×b₂ + ... + aₙ×bₙ

Same direction:      a · b > 0  (similar)
Perpendicular:       a · b = 0  (unrelated)
Opposite direction:  a · b < 0  (dissimilar)
```

### 3. 线性相关性与信息冗余 (Linear Dependence)
若某个向量（如下面的 $v_3$）完全可以通过其他基底向量的线性组合来表示，则称它们线性相关。在机器学习的特征工程中，这代表**特征冗余**（没有带来新的独立维度信息），通常需要通过降维（如 PCA）来识别和消除。

```text
v1 = [1, 0, 0]
v2 = [0, 1, 0]
v3 = [2, 1, 0]   # v3 = 2*v1 + v2
```

### 4. 正交投影与残差提取 (Orthogonal Projection)
将向量 $a$ 正交投影到目标向量 $b$ 的方向上，能把 $a$ 拆解为“与 $b$ 同向的投影分量”和“与 $b$ 垂直的正交残差”。在 AI 中，这常用于**数据降维**或**向量消偏 (Debiasing)**（例如通过减去偏见方向上的投影来消除词向量中的性别歧视分量）。

```text
proj_b(a) = (a dot b / b dot b) * b
```

```mermaid
graph LR
    subgraph Projection["Projection of a onto b"]
        direction TB
        O["Origin"] --> |"b (direction)"| B["b"]
        O --> |"a (original)"| A["a"]
        O --> |"proj_b(a)"| P["projection"]
        A -.-> |"residual (perpendicular)"| P
    end
```

### 5. 施密特正交化算法 (Gram-Schmidt Orthonormalization)
此算法输入一组普通（线性无关）的向量，通过逐步剔除它们在已确定基底方向上的投影分量并对模长进行单位化，最终构造出一组两两垂直且长度为 1 的**标准正交基**。在 AI 中这有助于在隐空间中构建**解耦表征 (Disentangled Representation)**。

```text
Input:  v1, v2, v3, ... (linearly independent)

u1 = v1 / |v1|

w2 = v2 - (v2 dot u1) * u1
u2 = w2 / |w2|

w3 = v3 - (v3 dot u1) * u1 - (v3 dot u2) * u2
u3 = w3 / |w3|

Output: u1, u2, u3, ... (orthonormal basis)
```

```python
class Vector:
    def __init__(self, components):
        # 初始化向量，保存分量列表和维度大小
        self.components = list(components)
        self.dim = len(self.components)

    def __add__(self, other):
        # 运算符重载：向量加法 (对应元素相加)
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        # 运算符重载：向量减法 (对应元素相减)
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self, other):
        # 计算点积：对应元素相乘并求和
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        # 计算向量的 L2 范数 (模长/长度)
        return sum(x**2 for x in self.components) ** 0.5

    def normalize(self):
        # 向量归一化 (将模长缩放到 1，方向不变)
        mag = self.magnitude()
        return Vector([x / mag for x in self.components])

    def cosine_similarity(self, other):
        # 计算两个向量的余弦相似度 (点乘除以两模长之积)
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def __repr__(self):
        # 友好打印格式
        return f"Vector({self.components})"


# 定义两个测试向量
a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

print(f"a + b = {a + b}")
print(f"a · b = {a.dot(b)}")
print(f"|a| = {a.magnitude():.4f}")
print(f"cosine similarity = {a.cosine_similarity(b):.4f}")
```

```python
class Matrix:
    def __init__(self, rows):
        # 初始化矩阵，保存行数据和形状 (行数, 列数)
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))

    def __matmul__(self, other):
        # 运算符重载 `@` 用于矩阵乘法
        if isinstance(other, Vector):
            # 矩阵乘以向量 (结果为向量)
            return Vector([
                sum(self.rows[i][j] * other.components[j] for j in range(self.shape[1]))
                for i in range(self.shape[0])
            ])
        rows = []
        # 矩阵乘以矩阵 (结果为矩阵)
        for i in range(self.shape[0]):
            row = []
            for j in range(other.shape[1]):
                row.append(sum(
                    self.rows[i][k] * other.rows[k][j]
                    for k in range(self.shape[1])
                ))
            rows.append(row)
        return Matrix(rows)

    def transpose(self):
        # 矩阵转置 (行列互换)
        return Matrix([
            [self.rows[j][i] for j in range(self.shape[0])]
            for i in range(self.shape[1])
        ])

    def __repr__(self):
        # 友好打印格式
        return f"Matrix({self.rows})"


# 旋转变换测试：定义一个将二维向量逆时针旋转 90 度的变换矩阵
rotation_90 = Matrix([[0, -1], [1, 0]])
point = Vector([3, 1])

# 执行矩阵-向量乘法，进行空间变换
rotated = rotation_90 @ point
print(f"Original: {point}")
print(f"Rotated 90°: {rotated}")
```

```python
import random

# 设置随机种子以确保结果可复现
random.seed(42)
# 初始化 2x3 的权重矩阵，模拟 3 维特征输入向 2 维输出的特征映射
weights = Matrix([[random.gauss(0, 0.1) for _ in range(3)] for _ in range(2)])
# 输入的 3 维向量
input_vector = Vector([1.0, 0.5, -0.3])

# 矩阵相乘，执行前向传播计算
output = weights @ input_vector
print(f"Input (3D): {input_vector}")
print(f"Output (2D): {output}")
print("This is what a neural network layer does -- matrix multiplication.")
```

```julia
# Julia 语言实现，支持 Unicode 数学运算符
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

println("a + b = ", a + b)
println("a · b = ", a ⋅ b)       # Julia 原生支持数学符号点积 \cdot 并按 Tab 键输入
println("|a| = ", √(a ⋅ a))      # \sqrt 并按 Tab 键输入根号
println("cosine = ", (a ⋅ b) / (√(a ⋅ a) * √(b ⋅ b)))

# 矩阵-向量相乘 (模拟神经网络层)
# Julia 中矩阵定义格式：空格分隔列，分号分隔行
W = [0.1 -0.2 0.3; 0.4 0.5 -0.1]
x = [1.0, 0.5, -0.3]
println("Wx = ", W * x)
println("This is a neural network layer.")
```

```python
def is_linearly_independent(vectors):
    # 判断一组向量是否线性无关 (通过高斯消元求矩阵的秩)
    n = len(vectors)
    dim = len(vectors[0].components)
    mat = Matrix([v.components[:] for v in vectors])
    rows = [row[:] for row in mat.rows]
    rank = 0
    # 对矩阵进行简化行阶梯形变换 (RREF)
    for col in range(dim):
        pivot = None
        for row in range(rank, len(rows)):
            if abs(rows[row][col]) > 1e-10:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col]
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
        rank += 1
    # 秩若等于向量个数，则线性无关
    return rank == n


def project(a, b):
    # 计算向量 a 在 b 方向上的正交投影向量
    scalar = a.dot(b) / b.dot(b)
    return Vector([scalar * x for x in b.components])


def gram_schmidt(vectors):
    # 施密特正交化算法：将线性无关向量组转化为标准正交基
    orthonormal = []
    for v in vectors:
        w = v
        # 减去当前向量在已生成的所有正交基方向上的投影分量
        for u in orthonormal:
            proj = project(w, u)
            w = w - proj
        # 如果残差模长接近于零，说明该向量是线性相关的，予以跳过
        if w.magnitude() < 1e-10:
            continue
        # 归一化后加入基底列表
        orthonormal.append(w.normalize())
    return orthonormal


# 定义三个线性无关向量
v1 = Vector([1, 0, 0])
v2 = Vector([1, 1, 0])
v3 = Vector([1, 1, 1])

# 执行正交化转换
basis = gram_schmidt([v1, v2, v3])
for i, u in enumerate(basis):
    print(f"u{i+1} = {u}")
    print(f"  |u{i+1}| = {u.magnitude():.6f}") # 验证正交基模长是否为 1

# 验证正交基两两正交性 (点积应当为 0)
print(f"u1 · u2 = {basis[0].dot(basis[1]):.6f}")
print(f"u1 · u3 = {basis[0].dot(basis[2]):.6f}")
print(f"u2 · u3 = {basis[1].dot(basis[2]):.6f}")
```

```python
import numpy as np

# 使用 NumPy 构建向量
a = np.array([1, 2, 3], dtype=float)
b = np.array([4, 5, 6], dtype=float)

print(f"a + b = {a + b}")
print(f"a · b = {np.dot(a, b)}")                                        # 用 np.dot 计算点积
print(f"|a| = {np.linalg.norm(a):.4f}")                                 # 用 np.linalg.norm 计算向量模长
print(f"cosine = {np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)):.4f}") # 夹角余弦相似度

# 初始化随机权重矩阵并执行矩阵-向量乘法 (神经网络层前向传播模拟)
W = np.random.randn(2, 3) * 0.1
x = np.array([1.0, 0.5, -0.3])
print(f"Wx = {W @ x}")                                                  # 使用 @ 符号实现矩阵乘法
```

> 英文原文还包含 2 个代码/公式块；中文正文保留关键块，完整可运行代码见本课 `code/` 目录。


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

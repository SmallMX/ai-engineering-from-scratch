# Lesson: phases/01-math-foundations/01-linear-algebra-intuition/docs/en.md
#
# 本脚本手写实现了基础的向量 (Vector) 与矩阵 (Matrix) 运算。
# 主要涵盖向量加减、标量乘法、点积、模长、归一化、投影、夹角及施密特正交化算法，
# 同时也模拟了矩阵乘以向量（空间几何变换及神经网络线性映射）的计算过程。

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

    def __mul__(self, scalar):
        # 运算符重载：标量乘法 (每个分量乘以标量)
        return Vector([x * scalar for x in self.components])

    def dot(self, other):
        # 计算两个向量的点积
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        # 计算向量的模长 (L2 范数)
        return sum(x**2 for x in self.components) ** 0.5

    def normalize(self):
        # 向量归一化 (使其模长为 1，方向保持不变)
        mag = self.magnitude()
        return Vector([x / mag for x in self.components])

    def cosine_similarity(self, other):
        # 计算两个向量的余弦相似度
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def angle_between(self, other):
        # 计算两个向量之间的夹角 (以角度度为单位)
        import math
        cos_theta = self.cosine_similarity(other)
        # 裁剪值以防止因浮点数误差导致超出 [-1.0, 1.0] 的数学定义域
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return math.degrees(math.acos(cos_theta))

    def project_onto(self, other):
        # 计算当前向量在 target (other) 向量上的正交投影向量
        scalar = self.dot(other) / other.dot(other)
        return Vector([scalar * x for x in other.components])

    def __repr__(self):
        # 友好打印格式
        return f"Vector({self.components})"


def is_independent(vectors):
    # 判断一组向量是否线性无关 (通过高斯消元求行阶梯形矩阵的秩)
    n = len(vectors)
    if n == 0:
        return True
    dim = vectors[0].dim
    rows = [v.components[:] for v in vectors]
    rank = 0
    # 对矩阵按列遍历进行初等行变换
    for col in range(dim):
        pivot = None
        # 寻找当前列中的主元行
        for row in range(rank, len(rows)):
            if abs(rows[row][col]) > 1e-10:
                pivot = row
                break
        if pivot is None:
            continue
        # 交换行，将主元行换到当前最上方未化简的行
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        # 缩放主元行使主元系数为 1
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]
        # 消去其他行在当前列上的分量
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col]
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
        rank += 1
    # 秩若等于向量个数，说明各向量之间线性无关
    return rank == n


def gram_schmidt(vectors):
    # 施密特正交化算法：将输入的线性无关向量组转换为标准正交基
    orthonormal = []
    for v in vectors:
        w = v
        # 逐步减去在已生成的所有正交基底方向上的投影分量
        for u in orthonormal:
            proj = w.project_onto(u)
            w = w - proj
        # 若残差向量的模长近乎为零，说明当前向量与前面的基底线性相关，予以过滤
        if w.magnitude() < 1e-10:
            continue
        # 归一化并添加至正交基底列表
        orthonormal.append(w.normalize())
    return orthonormal


class Matrix:
    def __init__(self, rows):
        # 初始化矩阵，保存行数据和矩阵形状 (行数, 列数)
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))

    def __matmul__(self, other):
        # 运算符重载 `@` 用于矩阵相乘
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

    def rank(self):
        # 计算矩阵的秩 (通过高斯消元求化简行阶梯形矩阵的主元个数)
        rows = [row[:] for row in self.rows]
        m, n = self.shape
        r = 0
        for col in range(n):
            pivot = None
            for row in range(r, m):
                if abs(rows[row][col]) > 1e-10:
                    pivot = row
                    break
            if pivot is None:
                continue
            rows[r], rows[pivot] = rows[pivot], rows[r]
            scale = rows[r][col]
            rows[r] = [x / scale for x in rows[r]]
            for row in range(m):
                if row != r and abs(rows[row][col]) > 1e-10:
                    factor = rows[row][col]
                    rows[row] = [rows[row][j] - factor * rows[r][j] for j in range(n)]
            r += 1
        return r

    def __repr__(self):
        # 友好打印格式
        return f"Matrix({self.rows})"


if __name__ == "__main__":
    print("=== Vectors ===")
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * 3 = {a * 3}")
    print(f"a · b = {a.dot(b)}")
    print(f"|a| = {a.magnitude():.4f}")
    print(f"â (normalized) = {a.normalize()}")
    print(f"cosine_similarity(a, b) = {a.cosine_similarity(b):.4f}")

    print("\n=== Matrices ===")
    rotation_90 = Matrix([[0, -1], [1, 0]])
    point = Vector([3, 1])
    rotated = rotation_90 @ point
    print(f"Rotate {point} by 90° → {rotated}")

    print("\n=== Angle Between Vectors ===")
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    v3 = Vector([1, 1])
    print(f"Angle between {v1} and {v2}: {v1.angle_between(v2):.1f} degrees")
    print(f"Angle between {v1} and {v3}: {v1.angle_between(v3):.1f} degrees")
    print(f"Angle between {v1} and {v1}: {v1.angle_between(v1):.1f} degrees")

    print("\n=== Projection ===")
    a = Vector([3, 4])
    b = Vector([1, 0])
    proj = a.project_onto(b)
    residual = a - proj
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"proj_b(a) = {proj}")
    print(f"residual = {residual}")
    print(f"residual dot b = {residual.dot(b):.6f}")

    print("\n=== Linear Independence ===")
    e1 = Vector([1, 0, 0])
    e2 = Vector([0, 1, 0])
    e3 = Vector([0, 0, 1])
    dep = Vector([2, 1, 0])
    print(f"{{e1, e2, e3}} independent: {is_independent([e1, e2, e3])}")
    print(f"{{e1, e2, 2*e1+e2}} independent: {is_independent([e1, e2, dep])}")

    print("\n=== Gram-Schmidt Orthogonalization ===")
    u1 = Vector([1, 1, 0])
    u2 = Vector([1, 0, 1])
    u3 = Vector([0, 1, 1])
    basis = gram_schmidt([u1, u2, u3])
    for i, vec in enumerate(basis):
        print(f"u{i+1} = {vec}")
    print(f"u1 dot u2 = {basis[0].dot(basis[1]):.6f}")
    print(f"u1 dot u3 = {basis[0].dot(basis[2]):.6f}")
    print(f"u2 dot u3 = {basis[1].dot(basis[2]):.6f}")
    for i, vec in enumerate(basis):
        print(f"|u{i+1}| = {vec.magnitude():.6f}")

    print("\n=== Matrix Rank ===")
    full_rank = Matrix([[1, 0], [0, 1]])
    rank_deficient = Matrix([[1, 2], [2, 4]])
    rectangular = Matrix([[1, 0, 0], [0, 1, 0]])
    print(f"Identity 2x2 rank: {full_rank.rank()}")
    print(f"[[1,2],[2,4]] rank: {rank_deficient.rank()}")
    print(f"[[1,0,0],[0,1,0]] rank: {rectangular.rank()}")

    print("\n=== Neural Network Layer (Matrix x Vector) ===")
    import random
    random.seed(42)
    weights = Matrix([[random.gauss(0, 0.1) for _ in range(3)] for _ in range(2)])
    input_vec = Vector([1.0, 0.5, -0.3])
    output = weights @ input_vec
    print(f"Input (3D):  {input_vec}")
    print(f"Output (2D): {output}")
    print("^ This is literally what a neural network layer does.")

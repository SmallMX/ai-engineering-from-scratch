# Lesson: phases/01-math-foundations/03-matrix-transformations/docs/en.md
#
# 本脚本手写实现了基本的 2D/3D 矩阵变换（包括旋转、缩放、剪切和反射）。
# 包含了 2D 和 3D 矩阵行列式的求解、特征值与特征向量的从零计算、特征分解的重构，
# 以及与 NumPy 相关计算的对比演示。
# 所有实现均采用 Python 原生标准库，并在演示部分辅助以 NumPy 的校验。

import math


def rotation_2d(theta):
    """生成 2D 旋转矩阵，用于将向量逆时针旋转 theta 弧度"""
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s], [s, c]]


def rotation_3d_z(theta):
    """生成绕 z 轴旋转 theta 弧度的 3D 旋转矩阵（x-y 平面旋转，z 轴保持不变）"""
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def rotation_3d_x(theta):
    """生成绕 x 轴旋转 theta 弧度的 3D 旋转矩阵（y-z 平面旋转，x 轴保持不变）"""
    c, s = math.cos(theta), math.sin(theta)
    return [[1, 0, 0], [0, c, -s], [0, s, c]]


def rotation_3d_y(theta):
    """生成绕 y 轴旋转 theta 弧度的 3D 旋转矩阵（x-z 平面旋转，y 轴保持不变）"""
    c, s = math.cos(theta), math.sin(theta)
    return [[c, 0, s], [0, 1, 0], [-s, 0, c]]


def scaling_2d(sx, sy):
    """生成 2D 缩放矩阵，沿 x 轴缩放 sx 倍，沿 y 轴缩放 sy 倍"""
    return [[sx, 0], [0, sy]]


def shearing_2d(kx, ky):
    """生成 2D 剪切矩阵，kx 为水平剪切系数，ky 为垂直剪切系数"""
    return [[1, kx], [ky, 1]]


def reflection_x():
    """生成关于 x 轴镜像反射 of 2D 矩阵（翻转 y 分量）"""
    return [[1, 0], [0, -1]]


def reflection_y():
    """生成关于 y 轴镜像反射 of 2D 矩阵（翻转 x 分量）"""
    return [[-1, 0], [0, 1]]


def mat_vec_mul(matrix, vector):
    """计算矩阵与向量的相乘（对向量施加矩阵所代表的空间线性变换）"""
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]


def mat_mul(a, b):
    """计算两个矩阵的乘法（代表复合变换，即先进行右矩阵变换，再进行左矩阵变换）"""
    rows_a, cols_b = len(a), len(b[0])
    cols_a = len(a[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(rows_a)
    ]


def det_2x2(m):
    """计算 2x2 矩阵的行列式值：ad - bc"""
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det_3x3(m):
    """计算 3x3 矩阵的行列式值（采用一阶按行展开计算）"""
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def eigenvalues_2x2(matrix):
    """从零求解 2x2 矩阵的特征值。
    依据特征方程：lambda^2 - trace(A)*lambda + det(A) = 0
    """
    a, b = matrix[0]
    c, d = matrix[1]
    # 计算矩阵的迹 (trace) 和行列式 (det)
    trace = a + d
    det = a * d - b * c
    # 一元二次方程求根公式的判别式
    discriminant = trace ** 2 - 4 * det
    if discriminant < 0:
        # 复特征值（纯旋转变换时产生复根）
        real = trace / 2
        imag = (-discriminant) ** 0.5 / 2
        return (complex(real, imag), complex(real, -imag))
    # 实特征值
    sqrt_disc = discriminant ** 0.5
    return ((trace + sqrt_disc) / 2, (trace - sqrt_disc) / 2)


def eigenvector_2x2(matrix, eigenvalue):
    """从零求解 2x2 矩阵对应特定特征值的单位特征向量"""
    a, b = matrix[0]
    c, d = matrix[1]
    # 求解齐次线性方程组 (A - lambda*I)v = 0
    # 若 b 不为 0，可通过第一行求解
    if abs(b) > 1e-10:
        v = [b, eigenvalue - a]
    # 若 c 不为 0，可通过第二行求解
    elif abs(c) > 1e-10:
        v = [eigenvalue - d, c]
    # 若非对角线元素都为 0，则矩阵为对角矩阵，特征向量为标准单位向量
    else:
        if abs(a - eigenvalue) < 1e-10:
            v = [1, 0]
        else:
            v = [0, 1]
    # 归一化特征向量，使其模长为 1
    mag = (v[0] ** 2 + v[1] ** 2) ** 0.5
    return [v[0] / mag, v[1] / mag]


def fmt(v, decimals=4):
    """辅助格式化输出数值或向量列表的函数"""
    if isinstance(v, list):
        return [round(x, decimals) for x in v]
    return round(v, decimals)


def demo_basic_transformations():
    """演示 2D 基础线性变换（旋转、缩放、剪切、反射）对点的变换效果"""
    print("=" * 60)
    print("BASIC TRANSFORMATIONS")
    print("=" * 60)

    point = [1.0, 0.0]
    theta = math.pi / 4

    # 旋转 45 度
    rotated = mat_vec_mul(rotation_2d(theta), point)
    print(f"\nRotate (1,0) by 45 deg: {fmt(rotated)}")

    # 缩放
    scaled = mat_vec_mul(scaling_2d(2, 3), [1.0, 1.0])
    print(f"Scale (1,1) by (2,3): {fmt(scaled)}")

    # 剪切
    sheared = mat_vec_mul(shearing_2d(1, 0), [1.0, 1.0])
    print(f"Shear (1,1) kx=1: {fmt(sheared)}")

    # 反射
    reflected = mat_vec_mul(reflection_y(), [2.0, 1.0])
    print(f"Reflect (2,1) across y-axis: {fmt(reflected)}")

    reflected_x = mat_vec_mul(reflection_x(), [2.0, 1.0])
    print(f"Reflect (2,1) across x-axis: {fmt(reflected_x)}")


def demo_unit_square():
    """演示线性变换和行列式对单位正方形四个顶点的影响（面积变化率）"""
    print("\n" + "=" * 60)
    print("TRANSFORMATIONS ON A UNIT SQUARE")
    print("=" * 60)

    square = [[0, 0], [1, 0], [1, 1], [0, 1]]
    labels = ["origin", "right", "top-right", "top"]

    print("\nOriginal square:")
    for label, pt in zip(labels, square):
        print(f"  {label}: {pt}")

    transforms = [
        ("Rotate 45 deg", rotation_2d(math.pi / 4)),
        ("Scale (2, 0.5)", scaling_2d(2, 0.5)),
        ("Shear kx=0.5", shearing_2d(0.5, 0)),
        ("Reflect y-axis", reflection_y()),
    ]

    for name, matrix in transforms:
        print(f"\n{name}:")
        for label, pt in zip(labels, square):
            result = mat_vec_mul(matrix, pt)
            print(f"  {label}: {pt} -> {fmt(result)}")
        # 观察行列式，应与图形面积缩放比例绝对值相同
        print(f"  det = {fmt(det_2x2(matrix))}")


def demo_composition():
    """演示矩阵乘法的非交换性（变换顺序对结果的影响）与行列式乘积性质"""
    print("\n" + "=" * 60)
    print("COMPOSITION OF TRANSFORMATIONS")
    print("=" * 60)

    R = rotation_2d(math.pi / 2)
    S = scaling_2d(2, 0.5)

    # 两种不同的变换顺序
    rotate_then_scale = mat_mul(S, R)
    scale_then_rotate = mat_mul(R, S)

    point = [1.0, 0.0]

    result1 = mat_vec_mul(rotate_then_scale, point)
    result2 = mat_vec_mul(scale_then_rotate, point)

    print(f"\nPoint: {point}")
    print(f"Rotate 90 then scale (2, 0.5): {fmt(result1)}")
    print(f"Scale (2, 0.5) then rotate 90: {fmt(result2)}")
    print("Order matters.")  # 说明变换顺序极为重要，R @ S != S @ R

    # 验证 det(A @ B) = det(A) * det(B)
    print(f"\ndet(R) = {fmt(det_2x2(R))}")
    print(f"det(S) = {fmt(det_2x2(S))}")
    print(f"det(S @ R) = {fmt(det_2x2(rotate_then_scale))}")
    print(f"det(S) * det(R) = {fmt(det_2x2(S) * det_2x2(R))}")
    print("Determinant of composition = product of determinants.")


def demo_3d_rotations():
    """演示 3D 空间下绕三个坐标轴的旋转变换"""
    print("\n" + "=" * 60)
    print("3D ROTATIONS")
    print("=" * 60)

    point = [1.0, 0.0, 0.0]
    theta = math.pi / 2

    # 执行 3D 旋转
    rz = mat_vec_mul(rotation_3d_z(theta), point)
    rx = mat_vec_mul(rotation_3d_x(theta), point)
    ry = mat_vec_mul(rotation_3d_y(theta), point)

    print(f"\nPoint: {point}")
    print(f"Rotate 90 around z: {fmt(rz)}")
    print(f"Rotate 90 around x: {fmt(rx)}")
    print(f"Rotate 90 around y: {fmt(ry)}")

    # 验证旋转矩阵的行列式始终为 1
    print(f"\ndet(Rz) = {fmt(det_3x3(rotation_3d_z(theta)))}")
    print(f"det(Rx) = {fmt(det_3x3(rotation_3d_x(theta)))}")
    print(f"det(Ry) = {fmt(det_3x3(rotation_3d_y(theta)))}")
    print("All rotation determinants = 1 (volume preserved).")


def demo_eigenvalues_from_scratch():
    """演示从零求解 2x2 矩阵的特征值与特征向量并验证特征方程"""
    print("\n" + "=" * 60)
    print("EIGENVALUES AND EIGENVECTORS (FROM SCRATCH, 2x2)")
    print("=" * 60)

    matrices = [
        ("Symmetric", [[2, 1], [1, 2]]),
        ("Upper triangular", [[3, 1], [0, 2]]),
        ("Scaling", [[3, 0], [0, 5]]),
        ("Rotation 90", [[0, -1], [1, 0]]),
    ]

    for name, A in matrices:
        vals = eigenvalues_2x2(A)
        print(f"\n{name}: {A}")
        print(f"  Eigenvalues: {vals[0]}, {vals[1]}")

        # 如果特征值为实数，则计算并验证其对应的特征向量
        if all(isinstance(v, (int, float)) for v in vals):
            for val in vals:
                vec = eigenvector_2x2(A, val)
                result = mat_vec_mul(A, vec)
                scaled = [val * vec[0], val * vec[1]]
                print(f"  lambda={fmt(val)}, v={fmt(vec)}")
                print(f"    A @ v = {fmt(result)}")
                print(f"    l * v = {fmt(scaled)}")
        else:
            print("  Complex eigenvalues: pure rotation, no real eigenvectors.")


def demo_eigendecomposition():
    """演示实对称/上三角矩阵的特征分解 A = V @ D @ V^-1 并从分解重构原矩阵"""
    print("\n" + "=" * 60)
    print("EIGENDECOMPOSITION (2x2, FROM SCRATCH)")
    print("=" * 60)

    A = [[3, 1], [0, 2]]
    vals = eigenvalues_2x2(A)

    v0 = eigenvector_2x2(A, vals[0])
    v1 = eigenvector_2x2(A, vals[1])

    # 构造特征向量矩阵 V
    V = [[v0[0], v1[0]], [v0[1], v1[1]]]
    # 构造对角线为特征值的矩阵 D
    D = [[vals[0], 0], [0, vals[1]]]

    # 计算 V 的逆矩阵 V^-1
    det_v = det_2x2(V)
    V_inv = [
        [V[1][1] / det_v, -V[0][1] / det_v],
        [-V[1][0] / det_v, V[0][0] / det_v],
    ]

    # 根据公式 V @ D @ V^-1 重构 A
    reconstructed = mat_mul(mat_mul(V, D), V_inv)

    print(f"\nA = {A}")
    print(f"Eigenvalues: {fmt(vals[0])}, {fmt(vals[1])}")
    print(f"V (eigenvectors as columns):")
    for row in V:
        print(f"  {fmt(row)}")
    print(f"D (eigenvalues on diagonal):")
    for row in D:
        print(f"  {fmt(row)}")
    print(f"Reconstructed A = V @ D @ V^-1:")
    for row in reconstructed:
        print(f"  {fmt(row)}")


def demo_determinant_meaning():
    """演示行列式的几何含义（判断空间映射后的缩放比、方向翻转及奇异坍缩）"""
    print("\n" + "=" * 60)
    print("DETERMINANT AS VOLUME SCALING FACTOR")
    print("=" * 60)

    cases = [
        ("Rotation 45 deg", rotation_2d(math.pi / 4)),
        ("Scale (2, 3)", scaling_2d(2, 3)),
        ("Shear kx=1", shearing_2d(1, 0)),
        ("Reflect y-axis", reflection_y()),
        ("Singular [[1,2],[2,4]]", [[1, 2], [2, 4]]),
    ]

    print()
    for name, m in cases:
        d = det_2x2(m)
        if d == 0:
            meaning = "space collapses, irreversible"  # 空间降维坍缩，变换不可逆
        elif d < 0:
            meaning = "orientation flipped"  # 空间方向/手性发生翻转
        elif abs(d - 1.0) < 1e-10:
            meaning = "area preserved"  # 面积保持不变
        else:
            meaning = f"area scaled by {abs(d):.1f}x"  # 面积按比例缩放
        print(f"det({name}) = {fmt(d):>8}  ({meaning})")


def demo_numpy_comparison():
    """使用 NumPy 库对前述的手写计算进行科学计算库级别的对比校验"""
    print("\n" + "=" * 60)
    print("NUMPY COMPARISON")
    print("=" * 60)

    try:
        import numpy as np
    except ImportError:
        print("\nNumPy not installed. Skipping.")
        return

    theta = math.pi / 4
    # 定义 NumPy 旋转矩阵
    R = np.array([[math.cos(theta), -math.sin(theta)],
                  [math.sin(theta), math.cos(theta)]])

    point = np.array([1.0, 0.0])
    print(f"\nRotate (1,0) by 45 deg: {R @ point}")

    # 特征值与特征向量求解校验
    A = np.array([[2, 1], [1, 2]], dtype=float)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"\nA = {A.tolist()}")
    print(f"Eigenvalues (numpy): {eigenvalues}")
    print(f"Eigenvectors (numpy, columns):\n{eigenvectors}")

    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        lam = eigenvalues[i]
        print(f"  A @ v{i} = {A @ v}, lambda * v{i} = {lam * v}")

    # 特征分解与重构校验
    B = np.array([[3, 1], [0, 2]], dtype=float)
    vals, vecs = np.linalg.eig(B)
    D = np.diag(vals)
    V = vecs
    reconstructed = V @ D @ np.linalg.inv(V)
    print(f"\nEigendecomposition of {B.tolist()}:")
    print(f"  Reconstructed: {reconstructed.tolist()}")

    # 3D 旋转检验
    Rz = np.array(rotation_3d_z(math.pi / 2))
    point_3d = np.array([1.0, 0.0, 0.0])
    print(f"\n3D rotate (1,0,0) 90 deg around z: {np.round(Rz @ point_3d, 4)}")

    # 协方差矩阵特征值与主成分分析 (PCA) 的对应关系展示
    cov = np.array([[2.0, 1.0], [1.0, 3.0]])
    vals, vecs = np.linalg.eig(cov)
    print(f"\nCovariance matrix: {cov.tolist()}")
    print(f"Principal components (eigenvectors): columns of\n{vecs}")
    print(f"Variance along each (eigenvalues): {vals}")
    print("PCA picks the eigenvectors with the largest eigenvalues.")


if __name__ == "__main__":
    # 执行各项基础变换与线性代数几何意义的演示
    demo_basic_transformations()
    demo_unit_square()
    demo_composition()
    demo_3d_rotations()
    demo_eigenvalues_from_scratch()
    demo_eigendecomposition()
    demo_determinant_meaning()
    demo_numpy_comparison()


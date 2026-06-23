# Lesson: phases/01-math-foundations/01-linear-algebra-intuition/docs/en.md
#
# 本文件通过 Julia 演示向量与矩阵的基本运算。
# 包含向量加减、标量乘法、点积、模长、归一化、余弦相似度计算，
# 以及矩阵乘以向量的变换，并模拟神经网络中的线性映射过程。

# 引入 Julia 线性代数标准库
using LinearAlgebra

println("=== Vectors ===")
# 定义两个 3D 浮点数向量
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

println("a = ", a)
println("b = ", b)
# 向量基本运算：加法、减法、标量乘法
println("a + b = ", a + b)
println("a - b = ", a - b)
println("a * 3 = ", a * 3)

# 向量点积（Julia 原生支持数学符号 \cdot 作为点积运算符，也可以用 dot(a, b)）
println("a · b = ", a ⋅ b)
# 计算向量的欧几里得范数（模长）
println("|a| = ", norm(a))
# 向量归一化（模长缩放为 1，方向保持不变）
println("â = ", normalize(a))

# 计算向量 a 和 b 的余弦相似度
cosine = (a ⋅ b) / (norm(a) * norm(b))
println("cosine_similarity(a, b) = ", round(cosine, digits=4))

println("\n=== Matrices ===")
# 定义一个 90 度逆时针旋转矩阵
rotation_90 = [0 -1; 1 0]
# 二维位置向量
point = [3.0, 1.0]
# 矩阵乘以向量：在空间中将其旋转 90 度
rotated = rotation_90 * point
println("Rotate ", point, " by 90° → ", rotated)

println("\n=== Neural Network Layer ===")
# 随机初始化一个 2x3 的权重矩阵（模拟从 3D 到 2D 的特征变换）
W = randn(2, 3) * 0.1
# 3D 输入向量
x = [1.0, 0.5, -0.3]
# 矩阵与输入向量相乘得到 2D 输出
output = W * x
println("Input (3D):  ", x)
println("Output (2D): ", output)
println("^ This is literally what a neural network layer does.")

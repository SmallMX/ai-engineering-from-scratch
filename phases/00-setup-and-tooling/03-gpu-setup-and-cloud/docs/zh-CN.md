# GPU 设置与云端

> 用 CPU 训练适合学习。真正训练时，你需要 GPU。

**类型：** Build
**语言：** Python
**先修：** Phase 0, Lesson 01
**时间：** ~45 分钟

## 学习目标

- 使用 `nvidia-smi` 和 PyTorch 的 CUDA API 验证本地 GPU 可用性
- 配置带 T4 GPU 的 Google Colab，用于免费云端实验
- benchmark CPU vs GPU 的矩阵乘法，并测量加速比
- 使用 fp16 经验规则估算 VRAM 能容纳的最大模型

## 问题

Phases 1-3 的大多数 lesson 用 CPU 就能正常运行。但一旦开始训练 CNNs、transformers 或 LLMs（phases 4+），你就需要 GPU 加速。一次在 CPU 上需要 8 小时的训练，在 GPU 上可能只要 10 分钟。

你有三个选择：本地 GPU、云 GPU，或 Google Colab（免费）。

## 概念

```text
你的选择：

1. 本地 NVIDIA GPU
   成本：$0（你已经拥有）
   设置：安装 CUDA + cuDNN
   最适合：经常使用、大数据集

2. Google Colab（免费层）
   成本：$0
   设置：无
   最适合：快速实验、家里没有 GPU

3. 云 GPU（Lambda、RunPod、Vast.ai）
   成本：$0.20-2.00/hr
   设置：SSH + install
   最适合：严肃训练、大模型
```

## 构建它

### 选项 1：本地 NVIDIA GPU

检查你是否有 NVIDIA GPU：

```bash
nvidia-smi
```

安装带 CUDA 的 PyTorch：

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

### 选项 2：Google Colab

1. 打开 [colab.research.google.com](https://colab.research.google.com)
2. Runtime > Change runtime type > T4 GPU
3. 运行 `!nvidia-smi` 验证

可以把这门课程中的 notebooks 直接上传到 Colab。

### 选项 3：云 GPU

对于 Lambda Labs、RunPod 或 Vast.ai：

```bash
ssh user@your-gpu-instance

pip install torch torchvision torchaudio
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

### 没有 GPU？没问题。

大多数 lesson 都能在 CPU 上完成。需要 GPU 的 lesson 会明确说明，并提供 Colab links。

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")
```

## 构建它：GPU vs CPU benchmark

```python
import torch
import time

size = 5000

a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU: {gpu_time:.3f}s")
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")
```

## 练习

1. 运行上面的 benchmark，比较 CPU 和 GPU 时间
2. 如果你没有 GPU，在 Google Colab 上运行它并比较结果
3. 检查你有多少 GPU memory，并估算能放下的最大模型（经验规则：fp16 每个参数 2 bytes）

## 关键术语

| 术语 | 人们常说 | 实际含义 |
|------|----------|----------|
| CUDA | “GPU programming” | NVIDIA 的并行计算平台，让你可以在 GPU 上运行代码 |
| VRAM | “GPU memory” | GPU 上的 video RAM，和系统 RAM 分开。它限制模型大小。 |
| fp16 | “Half precision” | 16-bit 浮点数，内存占用是 fp32 的一半，同时精度损失很小 |
| Tensor Core | “Fast matrix hardware” | 专门用于矩阵乘法的 GPU cores，比普通 cores 快 4-8 倍 |

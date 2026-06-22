# -*- coding: utf-8 -*-
# 路径: phases/00-setup-and-tooling/12-debugging-and-profiling/code/debug_tools.py
# 描述: 包含用于 PyTorch/Python 模型训练调试与性能分析的工具函数与类
# 教学内容引用自 docs/en.md
# 包含张量打印、时间测量、内存分析、形状检查、NaN检测、设备检查、梯度健康度、GPU内存监控等工具

import sys
import time
import tracemalloc
import logging

# 配置基本的日志输出格式和日志级别
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# 检查是否安装了 PyTorch 库，以便在无 GPU/PyTorch 环境下优雅降级
try:
    import torch
    import torch.nn as nn
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False


def debug_print(name, tensor):
    """打印 PyTorch 张量的元数据和基本统计信息，便于快速定位形状不匹配或数值异常。

    参数:
        name (str): 张量的自定义标识名称。
        tensor (torch.Tensor): 待检测的 PyTorch 张量。
    """
    print(f"  {name}: shape={tensor.shape}, dtype={tensor.dtype}, "
          f"device={tensor.device}, "
          f"min={tensor.min().item():.4f}, max={tensor.max().item():.4f}, "
          f"mean={tensor.mean().item():.4f}, "
          f"has_nan={tensor.isnan().any().item()}")


class Timer:
    """用于测量代码块执行时间的上下文管理器。

    用法:
        with Timer("自定义操作名称"):
            # 需要测量的耗时计算
    """
    def __init__(self, name=""):
        self.name = name
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"  [{self.name}] {self.elapsed:.4f}s")


def check_shapes(model, sample_input):
    """在模型前向传播过程中，通过注册钩子（hooks）来检查并打印各个子层的输入和输出张量形状。

    参数:
        model (nn.Module): 需要追踪形状的 PyTorch 模型。
        sample_input (torch.Tensor): 模拟输入的数据张量。
    """
    print(f"  Input: {sample_input.shape}")
    hooks = []

    def make_hook(name):
        def hook(module, inp, out):
            in_shape = inp[0].shape if isinstance(inp, tuple) else inp.shape
            out_shape = out.shape if hasattr(out, "shape") else type(out).__name__
            print(f"    {name}: {in_shape} -> {out_shape}")
        return hook

    # 为所有子模块注册前向传播钩子
    for name, module in model.named_modules():
        if name:
            hooks.append(module.register_forward_hook(make_hook(name)))

    with torch.no_grad():
        model(sample_input)

    # 运行结束后移除钩子，防止对后续推理/训练过程产生副作用
    for h in hooks:
        h.remove()


def detect_nan(model, loss, step):
    """检测损失值（loss）是否为 NaN。如果是，则遍历模型参数并检查对应的梯度是否出现 NaN 或 Inf。

    参数:
        model (nn.Module): 正在训练的 PyTorch 模型。
        loss (torch.Tensor): 当前步骤的损失值张量。
        step (int): 当前训练步骤。

    返回:
        bool: 如果检测到 NaN 损失则返回 True，否则返回 False。
    """
    if torch.isnan(loss):
        print(f"  NaN loss detected at step {step}")
        for name, param in model.named_parameters():
            if param.grad is not None:
                if torch.isnan(param.grad).any():
                    print(f"    NaN gradient in {name}")
                if torch.isinf(param.grad).any():
                    print(f"    Inf gradient in {name}")
        return True
    return False


def check_devices(model, *tensors):
    """检查输入参数/张量的计算设备（CPU/CUDA等）是否与模型所在设备匹配。

    参数:
        model (nn.Module): PyTorch 模型。
        *tensors (torch.Tensor): 需要与模型设备进行匹配验证的张量列表。
    """
    model_device = next(model.parameters()).device
    print(f"  Model device: {model_device}")
    for i, t in enumerate(tensors):
        status = "OK" if t.device == model_device else "MISMATCH"
        print(f"    Tensor {i}: {t.device} [{status}]")


def check_gradient_health(model):
    """计算当前模型梯度的总 L2 范数，并自动对过大（可能爆炸）或为零（可能消失）的梯度发出警告。

    参数:
        model (nn.Module): 包含了最新梯度的模型。

    返回:
        float: 计算得到的梯度总范数值。
    """
    total_norm = 0.0
    for name, param in model.named_parameters():
        if param.grad is not None:
            grad_norm = param.grad.data.norm(2).item()
            total_norm += grad_norm ** 2
            if grad_norm > 100:
                print(f"    WARNING: large gradient in {name}: {grad_norm:.2f}")
            if grad_norm == 0:
                print(f"    WARNING: zero gradient in {name}")
    total_norm = total_norm ** 0.5
    print(f"  Total gradient norm: {total_norm:.4f}")
    return total_norm


def demo_print_debugging():
    """演示如何使用 debug_print 函数来监控张量的基本统计状态并捕获异常数值。"""
    print("\n--- 1. Print Debugging for Tensors ---")
    x = torch.randn(32, 784)
    debug_print("input batch", x)

    w = torch.randn(784, 128)
    out = x @ w
    debug_print("after matmul", out)

    # 模拟并打印包含异常 NaN 值的张量
    with_nan = out.clone()
    with_nan[0, 0] = float("nan")
    debug_print("with injected NaN", with_nan)


def demo_timing():
    """演示如何使用 Timer 上下文管理器来精确测算不同规模矩阵乘法的耗时。"""
    print("\n--- 2. Timing Code Sections ---")

    with Timer("matrix multiply 1000x1000"):
        a = torch.randn(1000, 1000)
        b = torch.randn(1000, 1000)
        _ = a @ b

    with Timer("matrix multiply 5000x5000"):
        a = torch.randn(5000, 5000)
        b = torch.randn(5000, 5000)
        _ = a @ b


def demo_memory_tracking():
    """演示如何使用 python 的 tracemalloc 模块追踪内存分配，以快速检测内存泄漏或高占用位置。"""
    print("\n--- 3. Memory Tracking (tracemalloc) ---")
    tracemalloc.start()

    # 模拟分配一些内存
    if HAS_TORCH:
        data = [torch.randn(100, 100) for _ in range(100)]
        more_data = torch.randn(1000, 1000)
    else:
        # 如果未安装 PyTorch，则使用标准的 Python 列表模拟内存分配
        data = [[float(i) for i in range(100)] for _ in range(10000)]
        more_data = [float(i) for i in range(1000000)]

    # 获取当前内存快照并分析
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")
    print("  Top 5 memory allocations:")
    for stat in top_stats[:5]:
        print(f"    {stat}")

    # 清理并停止追踪
    del data, more_data
    tracemalloc.stop()


def demo_shape_checking():
    """演示如何通过 check_shapes 来检查和输出前向传播中各个连续网络层的张量维度变化。"""
    print("\n--- 4. Shape Checking Through Model ---")

    model = nn.Sequential(
        nn.Linear(784, 256),
        nn.ReLU(),
        nn.Linear(256, 64),
        nn.ReLU(),
        nn.Linear(64, 10),
    )

    sample = torch.randn(4, 784)
    check_shapes(model, sample)


def demo_nan_detection():
    """演示如何检测训练中的 NaN 损失，并根据梯度进一步排查故障层。"""
    print("\n--- 5. NaN Detection ---")

    model = nn.Sequential(
        nn.Linear(784, 256),
        nn.ReLU(),
        nn.Linear(256, 10),
    )

    x = torch.randn(4, 784)
    target = torch.randint(0, 10, (4,))
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    # 正常的前向和反向传播步骤
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, target)
    loss.backward()
    print(f"  Normal loss: {loss.item():.4f}")
    nan_found = detect_nan(model, loss, step=0)
    print(f"  NaN detected: {nan_found}")

    # 模拟反向传播中遇到异常的 NaN 损失
    fake_nan_loss = torch.tensor(float("nan"))
    print(f"  Simulated NaN loss: {fake_nan_loss.item()}")
    nan_found = detect_nan(model, fake_nan_loss, step=99)
    print(f"  NaN detected: {nan_found}")


def demo_device_checking():
    """演示如何检测模型与张量是否位于同一设备，避免不同计算设备带来的运行时奔溃。"""
    print("\n--- 6. Device Checking ---")

    model = nn.Linear(10, 5)
    t1 = torch.randn(4, 10)
    t2 = torch.randn(4, 10)

    check_devices(model, t1, t2)

    # 若环境支持 CUDA，进一步测试设备混合（Mismatch）场景
    if torch.cuda.is_available():
        model_gpu = model.cuda()
        t_cpu = torch.randn(4, 10)
        t_gpu = torch.randn(4, 10).cuda()
        print("  With mixed devices:")
        check_devices(model_gpu, t_cpu, t_gpu)


def demo_gradient_health():
    """演示如何调用 check_gradient_health 计算反向传播梯度的总范数并进行异常诊断。"""
    print("\n--- 7. Gradient Health Check ---")

    model = nn.Sequential(
        nn.Linear(784, 256),
        nn.ReLU(),
        nn.Linear(256, 10),
    )

    x = torch.randn(4, 784)
    target = torch.randint(0, 10, (4,))
    criterion = nn.CrossEntropyLoss()

    output = model(x)
    loss = criterion(output, target)
    loss.backward()
    check_gradient_health(model)


def demo_gpu_memory():
    """演示如果 CUDA 可用时，如何监测和分析 GPU 内存的实时分配与保留占用情况。"""
    print("\n--- 8. GPU Memory Summary ---")

    if not torch.cuda.is_available():
        print("  No GPU available. Skipping GPU memory demo.")
        print("  On a GPU machine, torch.cuda.memory_summary() shows:")
        print("    - Allocated memory per block size")
        print("    - Cached (reserved) memory")
        print("    - Peak memory usage")
        return

    print(f"  GPU: {torch.cuda.get_device_name(0)}")
    print(f"  Allocated: {torch.cuda.memory_allocated() / 1e6:.1f} MB")
    print(f"  Cached: {torch.cuda.memory_reserved() / 1e6:.1f} MB")

    # 观察分配超大张量后的显存占用变化
    large_tensor = torch.randn(10000, 10000, device="cuda")
    print(f"  After 10k x 10k tensor:")
    print(f"    Allocated: {torch.cuda.memory_allocated() / 1e6:.1f} MB")

    # 清理并显式释放 CUDA 缓存
    del large_tensor
    torch.cuda.empty_cache()
    print(f"  After cleanup:")
    print(f"    Allocated: {torch.cuda.memory_allocated() / 1e6:.1f} MB")


def demo_logging():
    """演示如何使用 Python 标准 logging 模块以结构化和可配置日志级别记录训练事件。"""
    print("\n--- 9. Structured Logging ---")

    logger.info("Training started: lr=0.001, batch_size=32, epochs=10")
    logger.info("Step 100: loss=2.3026, accuracy=0.10")
    logger.warning("Loss spike detected: 15.7 at step 450")
    logger.info("Step 1000: loss=0.4512, accuracy=0.87")
    logger.info("Training complete: best_loss=0.3201")


def demo_conditional_breakpoint():
    """说明如何设置条件断点（Conditional Breakpoint），在特定异常（如损失极高或为 NaN）时自动暂停程序并切入 pdb 交互模式进行排查。"""
    print("\n--- 10. Conditional Breakpoint Pattern ---")
    print("  In real code, use this pattern:")
    print()
    print("    for step in range(num_steps):")
    print("        loss = train_step(model, batch)")
    print("        if loss.item() > 10 or torch.isnan(loss):")
    print("            breakpoint()  # drops into pdb")
    print()
    print("  Useful pdb commands once inside:")
    print("    p tensor.shape       # print shape")
    print("    p tensor.device      # check device")
    print("    p tensor.grad        # inspect gradients")
    print("    p tensor.isnan().sum()  # count NaNs")
    print("    c                    # continue execution")
    print("    q                    # quit debugger")


def main():
    """根据依赖库是否安装，有条件地执行各种 AI 调试和分析工具的演示示例。"""
    print("=" * 60)
    print("  AI Debugging and Profiling Toolkit")
    print("  Phase 0, Lesson 12")
    print("=" * 60)

    if not HAS_TORCH:
        print("\nPyTorch not installed. Install with:")
        print("  uv pip install torch")
        print("\nRunning non-PyTorch demos only...\n")
        demo_memory_tracking()
        demo_logging()
        return 1

    demo_print_debugging()
    demo_timing()
    demo_memory_tracking()
    demo_shape_checking()
    demo_nan_detection()
    demo_device_checking()
    demo_gradient_health()
    demo_gpu_memory()
    demo_logging()
    demo_conditional_breakpoint()

    print("\n" + "=" * 60)
    print("  All demos complete.")
    print("  Next: introduce bugs intentionally and practice catching them.")
    print("=" * 60 + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

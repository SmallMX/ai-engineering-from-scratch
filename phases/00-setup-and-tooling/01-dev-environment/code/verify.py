# Lesson: phases/00-setup-and-tooling/01-dev-environment/docs/en.md
#
# 本脚本用于验证“从零开发 AI”所需的本地开发环境是否配置正确。
# 包含 Python 版本、基本库（NumPy 等）、外部命令行工具（Git 等）的校验，
# 以及 GPU 和 PyTorch 的环境验证。

import sys
import shutil
import subprocess

# 定义核心环境检查项。每项是一个三元组: (检查名称, 检查函数, 详情显示(可选))
CHECKS = [
    ("Python 3.10+", lambda: sys.version_info >= (3, 10), f"Python {sys.version}"),
    ("NumPy", lambda: __import__("numpy"), None),
    ("Matplotlib", lambda: __import__("matplotlib"), None),
    ("Jupyter", lambda: __import__("jupyter"), None),
    ("Git", lambda: shutil.which("git") is not None, None),
    ("Node.js", lambda: shutil.which("node") is not None, None),
    ("Rust (cargo)", lambda: shutil.which("cargo") is not None, None),
]

# 定义可选的 GPU 环境检查项
GPU_CHECKS = [
    ("PyTorch", lambda: __import__("torch"), None),
    (
        "CUDA",
        lambda: __import__("torch").cuda.is_available(),
        lambda: __import__("torch").cuda.get_device_name(0) if __import__("torch").cuda.is_available() else "Not available",
    ),
]


def run_check(name, check_fn, detail_fn=None):
    """
    运行单个环境检查项。
    
    参数:
        name: 检查项名称
        check_fn: 返回布尔值或能成功导入的函数
        detail_fn: 返回详细信息的字符串或可调用对象
    返回:
        布尔值，代表检查是否通过
    """
    try:
        result = check_fn()
        if result is False:
            raise Exception("Check returned False")
        detail = ""
        if detail_fn:
            if callable(detail_fn):
                detail = f" ({detail_fn()})"
            else:
                detail = f" ({detail_fn})"
        print(f"  [PASS] {name}{detail}")
        return True
    except Exception:
        print(f"  [FAIL] {name}")
        return False


def main():
    print("\n=== AI Engineering from Scratch — Environment Check ===\n")

    print("Core:")
    # 统计核心检查通过项
    passed = sum(run_check(name, fn, detail) for name, fn, detail in CHECKS)
    total = len(CHECKS)

    print("\nGPU (optional):")
    # 统计 GPU 检查通过项
    gpu_passed = sum(run_check(name, fn, detail) for name, fn, detail in GPU_CHECKS)
    gpu_total = len(GPU_CHECKS)

    print(f"\nResult: {passed}/{total} core checks passed", end="")
    if gpu_passed > 0:
        print(f", {gpu_passed}/{gpu_total} GPU checks passed")
    else:
        print(" (no GPU — that's fine, most lessons work on CPU)")

    # 如果所有核心检查项全部通过，则开发环境准备完毕
    if passed == total:
        print("\nYou're ready. Start with Phase 1.\n")
    else:
        print("\nFix the failed checks above, then run this script again.\n")

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())

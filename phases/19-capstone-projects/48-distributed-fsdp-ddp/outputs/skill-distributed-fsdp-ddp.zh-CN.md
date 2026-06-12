---
name: skill-distributed-fsdp-ddp
description: Distributed 数据 Parallel与FSDP 从零实现 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 48
---

# Distributed 数据 Parallel与FSDP 从零实现：中文使用说明

你将围绕本课主题 **Distributed 数据 Parallel与FSDP 从零实现** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 48 课「Distributed 数据 Parallel与FSDP 从零实现」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: distributed-fsdp-ddp
description: Bring up multi-rank training with a from-scratch DDP wrapper and an FSDP parameter sharding sketch on the gloo or nccl backend.
version: 1.0.0
phase: 19
lesson: 48
tags: [distributed, ddp, fsdp, collectives]
---

## When to use

The model fits on one device but you need more throughput (DDP). The model does not fit on one device (FSDP). Either case: a multi-rank training setup with the same code path.

## Bring up the process group

```python
os.environ["MASTER_ADDR"] = "127.0.0.1"
os.environ["MASTER_PORT"] = str(port)
dist.init_process_group(backend="gloo", rank=rank, world_size=world_size)
```

`gloo` is the CPU backend; `nccl` is the GPU backend. Both implement the same collective surface.

## Wrap the model

1. On rank 0, build the model from your seed.
2. Wrap it with the DDP shell.
3. The shell's `__init__` calls `dist.broadcast(p.data, src=0)` for every parameter and buffer.
4. After every `loss.backward()`, the trainer calls `sync_grads()`.
5. `sync_grads()` calls `dist.all_reduce(p.grad, op=SUM)` and `p.grad.div_(world_size)`.
6. Optimizer step on every rank with the same averaged gradient.

## Shard parameters (FSDP sketch)

1. Flatten each parameter, pad to a multiple of `world_size`.
2. Keep your shard locally; release the rest.
3. Before forward, `dist.all_gather(...)` to rebuild the full tensor on every rank.
4. After forward, drop the full tensor.

## Failure modes

- Skipping the broadcast: ranks start from different inits, diverge silently.
- Forgetting to divide after sum: gradients scaled by world_size, optimizer steps too big.
- Using cross-device rename for checkpoints: not atomic; same lesson 47 trap.
- Mixing CPU and CUDA tensors on the same collective: backend mismatch, run hangs.

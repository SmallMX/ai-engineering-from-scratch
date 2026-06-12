---
name: skill-checkpoint-save-resume
description: Checkpoint Save与Resume 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 19
lesson: 47
---

# Checkpoint Save与Resume：中文使用说明

你将围绕本课主题 **Checkpoint Save与Resume** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 19「毕业项目」
- 课程：第 47 课「Checkpoint Save与Resume」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: checkpoint-save-resume
description: Atomic, sharded checkpoints with full RNG capture so a killed run resumes mid-epoch with the same loss trajectory.
version: 1.0.0
phase: 19
lesson: 47
tags: [training, durability, resume, sharded-state]
---

## When to use

Any training run longer than the wallclock cap of the cluster, any run that must survive a node reboot, any model too large for a single payload.

## Payload shape

```python
{
  "schema": "ckpt.v1",
  "model": model.state_dict(),
  "optimizer": opt.state_dict(),
  "scheduler": sched.state_dict(),
  "state": {"step": int, "epoch": int, "batch_in_epoch": int, "losses": [float, ...]},
  "rng": {"python": ..., "numpy": ..., "torch_cpu": ..., "torch_cuda": ...},
  "wall_saved_at": time.time(),
}
```

## Atomic save

1. Write the payload to a unique temp file in the same directory as the target.
2. `os.replace(tmp, target)` to swap atomically.
3. Never write directly to the target name.

## Sharded layout

- `model.shard-NNN.pt` per shard, round robin on keys or split by parameter group.
- `meta.pt` carries optimizer, scheduler, train state, RNG, and the shard manifest.
- `index.json` carries `sha256` for every shard and for `meta.pt`.
- Loader verifies every hash before merging.

## Mid-epoch resume

- Save `(epoch, batch_in_epoch)` next to `step`.
- Restore RNG state before the first batch of the resumed epoch.
- Fast-forward the generator past consumed batches.

## Failure modes

- Cross-device rename: not atomic, lose the previous file. Put temp in same directory.
- Forgetting RNG: resumed loss diverges from baseline. Run the demo's assertion.
- Forgetting optimizer state: next step lurches. Same diff blows up.
- Pruning the wrong checkpoint: keep last K plus best.

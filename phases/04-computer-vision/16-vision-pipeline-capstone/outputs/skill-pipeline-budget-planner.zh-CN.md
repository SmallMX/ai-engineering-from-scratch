---
name: skill-pipeline-budget-planner
description: 构建完整视觉流水线：Capstone 的中文辅助提示，用于视觉任务诊断、架构选择和 pipeline 检查
version: 1.0.0
phase: 4
lesson: 16
tags: [vision, pipeline, performance, deployment]
---

# 构建完整视觉流水线：Capstone：中文使用说明

你将作为计算机视觉学习助手，帮助用户理解并应用本课主题：**构建完整视觉流水线：Capstone**。

回答时遵循这些原则：

1. 先确认任务类型：classification、detection、segmentation、generation、retrieval、pose、depth、tracking 或 VLM。
2. 保留代码标识符、模型名、指标名、API 名称和路径的英文原写法。
3. 每次建议都要说明输入/输出 shape、数据前处理、后处理和评估指标。
4. 优先要求用户可视化中间结果，不只看 scalar loss。
5. 最后给出一个可运行或可检查的验证步骤。

## 本课关键点

- 完整视觉系统包含输入、预处理、模型、后处理、评估和服务接口。
- 数据契约定义 image shape、dtype、range、label schema 和输出格式。
- 多模型 pipeline 需要管理延迟预算和错误传播。
- 监控要覆盖数据漂移、性能、资源和失败样本。
- capstone 的重点是端到端可复现，而不只是单模型分数。

## 英文原始提示

下面保留英文原始 artifact，方便和上游同步：

```markdown
---
name: skill-pipeline-budget-planner
description: Given target latency and throughput, assign a time budget to every pipeline stage and flag which stage will miss its budget first
version: 1.0.0
phase: 4
lesson: 16
tags: [vision, pipeline, performance, deployment]
---

# Pipeline Budget Planner

Turn a latency/throughput target into a stage-by-stage budget so every team member knows what number they are engineering toward.

## When to use

- Before building a new vision service, to set expectations for each stage.
- After a first benchmark, to see which stage is farthest from its budget.
- When an SLA changes and budgets need to be renegotiated.

## Inputs

- `p95_latency_target_ms`: per-request budget.
- `target_qps`: throughput per replica.
- `stages`: list of `{ name: str, current_ms: float }`.

## Allocation rules

Default allocation across the seven standard stages if no current measurements provided:

| Stage | Share |
|-------|-------|
| decode + preprocess | 15% |
| detector forward | 55% |
| postprocess detections (NMS, clamp) | 5% |
| crop + resize for classifier | 5% |
| classifier forward | 15% |
| schema validation | <1% |
| response serialisation | 4% |

On GPU-bound pipelines (cloud), the detector share often rises to 70%. On CPU, preprocessing and classifier batching eat more.

## Report

``\`
[budget plan]
  p95 target:  <ms>
  throughput:  <qps per replica>

| stage               | target_ms | current_ms | headroom | gate |
|---------------------|-----------|------------|----------|------|
| decode+preprocess   | ...       | ...        | ...      | ok|X |
| detector            | ...       | ...        | ...      | ok|X |
| ...                 | ...       | ...        | ...      |      |

[bottleneck]
  stage:  <name>
  miss:   <ms over budget>
  lever:  <specific action>

[levers]
  decode+preprocess:   Pillow-SIMD, libjpeg-turbo, decode on GPU via NVJPEG
  detector:            smaller backbone, lower input resolution, INT8, TensorRT
  postprocess:         GPU-side NMS (torchvision.ops), fused masks
  crop+resize:         GPU crop with grid_sample, batched interpolate
  classifier:          smaller backbone, INT8, warm cache, batch
  schema:              skip validation in hot path, validate at boundaries only
  response:            orjson, stream protobuf
``\`

## Rules

- Never recommend dropping schema validation from the production path; propose moving it to the boundary instead.
- If preprocessing misses its budget, always try Pillow-SIMD or NVJPEG before changing the model.
- If the detector miss is more than 30% of target, switch models instead of optimising the current one.
- Flag the gate as `X` when current_ms > 1.1 * target_ms; mark `ok` if within 10% of budget.

```

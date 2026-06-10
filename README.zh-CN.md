# AI Engineering from Scratch 中文说明

> 这是一个从零构建 AI 工程能力的课程仓库：先手写数学、模型和智能体循环，再使用生产级框架理解同一件事。

这个 fork 正在逐步中文化。英文原文保留在原文件中，中文译文使用 `zh-CN` 旁路文件，方便以后继续同步上游。

## 快速找目录

如果你只是想找课表，直接看下面两处：

- **中文导航：** 本文件的 [课程目录](#课程目录)
- **完整英文课表：** [README.md#contents](README.md#contents)

每节课的目录结构固定：

```text
phases/<阶段>/<课程>/
├── docs/
│   ├── en.md       # 英文正文
│   └── zh-CN.md    # 中文正文，逐步补齐中
├── code/           # 可运行代码
├── quiz.json       # 英文测验
├── quiz.zh-CN.json # 中文测验，逐步补齐中
└── outputs/        # prompt / skill / agent / MCP 等课程产物
```

## 现在怎么读

推荐按照课程自然顺序从 Phase 0 开始看。Phase 0 的 12 节课已经补齐中文正文、中文测验和中文产物，可以直接按顺序学习。

### Phase 0：环境搭建与工具

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [开发环境](phases/00-setup-and-tooling/01-dev-environment/docs/zh-CN.md) | [Dev Environment](phases/00-setup-and-tooling/01-dev-environment/) | 已完成 |
| 02 | [Git 与协作](phases/00-setup-and-tooling/02-git-and-collaboration/docs/zh-CN.md) | [Git & Collaboration](phases/00-setup-and-tooling/02-git-and-collaboration/) | 已完成 |
| 03 | [GPU 设置与云端环境](phases/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/zh-CN.md) | [GPU Setup & Cloud](phases/00-setup-and-tooling/03-gpu-setup-and-cloud/) | 已完成 |
| 04 | [API 与密钥](phases/00-setup-and-tooling/04-apis-and-keys/docs/zh-CN.md) | [APIs & Keys](phases/00-setup-and-tooling/04-apis-and-keys/) | 已完成 |
| 05 | [Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks/docs/zh-CN.md) | [Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks/) | 已完成 |
| 06 | [Python 环境](phases/00-setup-and-tooling/06-python-environments/docs/zh-CN.md) | [Python Environments](phases/00-setup-and-tooling/06-python-environments/) | 已完成 |
| 07 | [面向 AI 的 Docker](phases/00-setup-and-tooling/07-docker-for-ai/docs/zh-CN.md) | [Docker for AI](phases/00-setup-and-tooling/07-docker-for-ai/) | 已完成 |
| 08 | [编辑器设置](phases/00-setup-and-tooling/08-editor-setup/docs/zh-CN.md) | [Editor Setup](phases/00-setup-and-tooling/08-editor-setup/) | 已完成 |
| 09 | [数据管理](phases/00-setup-and-tooling/09-data-management/docs/zh-CN.md) | [Data Management](phases/00-setup-and-tooling/09-data-management/) | 已完成 |
| 10 | [终端与 Shell](phases/00-setup-and-tooling/10-terminal-and-shell/docs/zh-CN.md) | [Terminal & Shell](phases/00-setup-and-tooling/10-terminal-and-shell/) | 已完成 |
| 11 | [面向 AI 的 Linux](phases/00-setup-and-tooling/11-linux-for-ai/docs/zh-CN.md) | [Linux for AI](phases/00-setup-and-tooling/11-linux-for-ai/) | 已完成 |
| 12 | [调试与 Profiling](phases/00-setup-and-tooling/12-debugging-and-profiling/docs/zh-CN.md) | [Debugging & Profiling](phases/00-setup-and-tooling/12-debugging-and-profiling/) | 已完成 |

Phase 3 也已经补齐中文正文、中文测验和中文产物，可以在完成前置基础后继续阅读。

### Phase 3：深度学习核心

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [感知机](phases/03-deep-learning-core/01-the-perceptron/docs/zh-CN.md) | [The Perceptron](phases/03-deep-learning-core/01-the-perceptron/) | 已完成 |
| 02 | [多层网络与前向传播](phases/03-deep-learning-core/02-multi-layer-networks/docs/zh-CN.md) | [Multi-Layer Networks](phases/03-deep-learning-core/02-multi-layer-networks/) | 已完成 |
| 03 | [从零实现反向传播](phases/03-deep-learning-core/03-backpropagation/docs/zh-CN.md) | [Backpropagation from Scratch](phases/03-deep-learning-core/03-backpropagation/) | 已完成 |
| 04 | [激活函数](phases/03-deep-learning-core/04-activation-functions/docs/zh-CN.md) | [Activation Functions](phases/03-deep-learning-core/04-activation-functions/) | 已完成 |
| 05 | [损失函数](phases/03-deep-learning-core/05-loss-functions/docs/zh-CN.md) | [Loss Functions](phases/03-deep-learning-core/05-loss-functions/) | 已完成 |
| 06 | [优化器](phases/03-deep-learning-core/06-optimizers/docs/zh-CN.md) | [Optimizers](phases/03-deep-learning-core/06-optimizers/) | 已完成 |
| 07 | [正则化](phases/03-deep-learning-core/07-regularization/docs/zh-CN.md) | [Regularization](phases/03-deep-learning-core/07-regularization/) | 已完成 |
| 08 | [权重初始化与训练稳定性](phases/03-deep-learning-core/08-weight-initialization/docs/zh-CN.md) | [Weight Initialization](phases/03-deep-learning-core/08-weight-initialization/) | 已完成 |
| 09 | [学习率调度与 Warmup](phases/03-deep-learning-core/09-learning-rate-schedules/docs/zh-CN.md) | [Learning Rate Schedules](phases/03-deep-learning-core/09-learning-rate-schedules/) | 已完成 |
| 10 | [构建你自己的迷你框架](phases/03-deep-learning-core/10-mini-framework/docs/zh-CN.md) | [Mini Framework](phases/03-deep-learning-core/10-mini-framework/) | 已完成 |
| 11 | [PyTorch 入门](phases/03-deep-learning-core/11-intro-to-pytorch/docs/zh-CN.md) | [Introduction to PyTorch](phases/03-deep-learning-core/11-intro-to-pytorch/) | 已完成 |
| 12 | [JAX 入门](phases/03-deep-learning-core/12-intro-to-jax/docs/zh-CN.md) | [Introduction to JAX](phases/03-deep-learning-core/12-intro-to-jax/) | 已完成 |
| 13 | [调试神经网络](phases/03-deep-learning-core/13-debugging-neural-networks/docs/zh-CN.md) | [Debugging Neural Networks](phases/03-deep-learning-core/13-debugging-neural-networks/) | 已完成 |

每课都包含：

- `docs/zh-CN.md`：中文正文
- `quiz.zh-CN.json`：中文测验
- `outputs/*.zh-CN.md`：中文 prompt / skill / artifact

查看中文化进度：

```bash
python3 scripts/audit_translations.py --phase 0
```

查看原仓库课程结构是否仍然有效：

```bash
python3 scripts/audit_lessons.py --phase 0
```

## 课程目录

全仓库共有 20 个 phase、503 节课。下面是中文导航表；点击 phase 目录可以进入对应阶段文件夹，点击“英文课表”可以跳到原 README 的详细 lesson 列表。

| Phase | 中文名称 | 课程数 | 目录 | 详细课表 |
|:---:|---|:---:|---|---|
| 0 | 环境搭建与工具 | 12 | [phases/00-setup-and-tooling](phases/00-setup-and-tooling/) | [英文课表](README.md#phase-0) |
| 1 | 数学基础 | 22 | [phases/01-math-foundations](phases/01-math-foundations/) | [英文课表](README.md#phase-1) |
| 2 | 机器学习基础 | 18 | [phases/02-ml-fundamentals](phases/02-ml-fundamentals/) | [英文课表](README.md#phase-2) |
| 3 | 深度学习核心 | 13 | [phases/03-deep-learning-core](phases/03-deep-learning-core/) | [英文课表](README.md#phase-3) |
| 4 | 计算机视觉 | 28 | [phases/04-computer-vision](phases/04-computer-vision/) | [英文课表](README.md#phase-4) |
| 5 | NLP：从基础到进阶 | 29 | [phases/05-nlp-foundations-to-advanced](phases/05-nlp-foundations-to-advanced/) | [英文课表](README.md#phase-5) |
| 6 | 语音与音频 | 17 | [phases/06-speech-and-audio](phases/06-speech-and-audio/) | [英文课表](README.md#phase-6) |
| 7 | Transformer 深入解析 | 14 | [phases/07-transformers-deep-dive](phases/07-transformers-deep-dive/) | [英文课表](README.md#phase-7) |
| 8 | 生成式 AI | 14 | [phases/08-generative-ai](phases/08-generative-ai/) | [英文课表](README.md#phase-8) |
| 9 | 强化学习 | 12 | [phases/09-reinforcement-learning](phases/09-reinforcement-learning/) | [英文课表](README.md#phase-9) |
| 10 | 从零构建 LLM | 22 | [phases/10-llms-from-scratch](phases/10-llms-from-scratch/) | [英文课表](README.md#phase-10) |
| 11 | LLM 工程 | 17 | [phases/11-llm-engineering](phases/11-llm-engineering/) | [英文课表](README.md#phase-11) |
| 12 | 多模态 AI | 25 | [phases/12-multimodal-ai](phases/12-multimodal-ai/) | [英文课表](README.md#phase-12) |
| 13 | 工具与协议 | 23 | [phases/13-tools-and-protocols](phases/13-tools-and-protocols/) | [英文课表](README.md#phase-13) |
| 14 | 智能体工程 | 42 | [phases/14-agent-engineering](phases/14-agent-engineering/) | [英文课表](README.md#phase-14) |
| 15 | 自主系统 | 22 | [phases/15-autonomous-systems](phases/15-autonomous-systems/) | [英文课表](README.md#phase-15) |
| 16 | 多智能体与群体智能 | 25 | [phases/16-multi-agent-and-swarms](phases/16-multi-agent-and-swarms/) | [英文课表](README.md#phase-16) |
| 17 | 基础设施与生产部署 | 28 | [phases/17-infrastructure-and-production](phases/17-infrastructure-and-production/) | [英文课表](README.md#phase-17) |
| 18 | 伦理、安全与对齐 | 30 | [phases/18-ethics-safety-alignment](phases/18-ethics-safety-alignment/) | [英文课表](README.md#phase-18) |
| 19 | 毕业项目 | 85 | [phases/19-capstone-projects](phases/19-capstone-projects/) | [英文课表](README.md#phase-19) |

## 学习路线

如果你还没有系统学过 AI，建议按顺序走：

```text
Phase 0 -> Phase 1 -> Phase 2 -> Phase 3 -> Phase 7 -> Phase 10 -> Phase 11 -> Phase 14
```

如果你已经会机器学习，但对深度学习不扎实，可以从 Phase 3 开始：

```text
phases/03-deep-learning-core/
```

如果你的目标是做 LLM 应用和智能体，可以优先看：

```text
phases/10-llms-from-scratch/
phases/11-llm-engineering/
phases/13-tools-and-protocols/
phases/14-agent-engineering/
```

## 翻译约定

翻译规范见 [TRANSLATION.zh-CN.md](TRANSLATION.zh-CN.md)。

中文术语表见 [glossary/terms.zh-CN.md](glossary/terms.zh-CN.md)。

当前策略：

- 不覆盖英文原文。
- 中文正文放在 `docs/zh-CN.md`。
- 中文测验放在 `quiz.zh-CN.json`。
- 中文 prompt / skill 放在 `outputs/*.zh-CN.md`。
- 代码、命令、路径、API 名称保持英文。

## 原 README 摘要

这套课程不是“调用 API 就完事”的教程。它要求你先从数学和代码层面构建核心机制：

- 手写向量、矩阵、梯度和反向传播
- 手写 tokenizer、attention、Transformer 和 LLM 训练流程
- 手写 RAG、工具调用、MCP、agent loop 和多智能体系统
- 再把同样的概念映射到 PyTorch、JAX、LLM 工程和生产系统

每节课都产出一个可复用 artifact：prompt、skill、agent、MCP server 或可运行代码。课程的核心节奏是：

```text
MOTTO -> PROBLEM -> CONCEPT -> BUILD IT -> USE IT -> SHIP IT
```

也就是先理解问题，再从零实现，然后使用生产级框架，最后留下一个能复用的工具。

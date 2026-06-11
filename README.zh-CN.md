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

推荐按照课程自然顺序从 Phase 0 开始看。Phase 0 到 Phase 4 已经补齐中文正文、中文测验和中文产物，可以直接按顺序学习。

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

### Phase 1：数学基础

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [线性代数直觉](phases/01-math-foundations/01-linear-algebra-intuition/docs/zh-CN.md) | [Linear Algebra Intuition](phases/01-math-foundations/01-linear-algebra-intuition/) | 已完成 |
| 02 | [向量、矩阵与运算](phases/01-math-foundations/02-vectors-matrices-operations/docs/zh-CN.md) | [Vectors, Matrices & Operations](phases/01-math-foundations/02-vectors-matrices-operations/) | 已完成 |
| 03 | [矩阵变换](phases/01-math-foundations/03-matrix-transformations/docs/zh-CN.md) | [Matrix Transformations](phases/01-math-foundations/03-matrix-transformations/) | 已完成 |
| 04 | [机器学习微积分](phases/01-math-foundations/04-calculus-for-ml/docs/zh-CN.md) | [Calculus for Machine Learning](phases/01-math-foundations/04-calculus-for-ml/) | 已完成 |
| 05 | [链式法则与自动微分](phases/01-math-foundations/05-chain-rule-and-autodiff/docs/zh-CN.md) | [Chain Rule & Automatic Differentiation](phases/01-math-foundations/05-chain-rule-and-autodiff/) | 已完成 |
| 06 | [概率与分布](phases/01-math-foundations/06-probability-and-distributions/docs/zh-CN.md) | [Probability and Distributions](phases/01-math-foundations/06-probability-and-distributions/) | 已完成 |
| 07 | [贝叶斯定理](phases/01-math-foundations/07-bayes-theorem/docs/zh-CN.md) | [Bayes' Theorem](phases/01-math-foundations/07-bayes-theorem/) | 已完成 |
| 08 | [优化](phases/01-math-foundations/08-optimization/docs/zh-CN.md) | [Optimization](phases/01-math-foundations/08-optimization/) | 已完成 |
| 09 | [信息论](phases/01-math-foundations/09-information-theory/docs/zh-CN.md) | [Information Theory](phases/01-math-foundations/09-information-theory/) | 已完成 |
| 10 | [降维](phases/01-math-foundations/10-dimensionality-reduction/docs/zh-CN.md) | [Dimensionality Reduction](phases/01-math-foundations/10-dimensionality-reduction/) | 已完成 |
| 11 | [奇异值分解](phases/01-math-foundations/11-singular-value-decomposition/docs/zh-CN.md) | [Singular Value Decomposition](phases/01-math-foundations/11-singular-value-decomposition/) | 已完成 |
| 12 | [张量运算](phases/01-math-foundations/12-tensor-operations/docs/zh-CN.md) | [Tensor Operations](phases/01-math-foundations/12-tensor-operations/) | 已完成 |
| 13 | [数值稳定性](phases/01-math-foundations/13-numerical-stability/docs/zh-CN.md) | [Numerical Stability](phases/01-math-foundations/13-numerical-stability/) | 已完成 |
| 14 | [范数与距离](phases/01-math-foundations/14-norms-and-distances/docs/zh-CN.md) | [Norms and Distances](phases/01-math-foundations/14-norms-and-distances/) | 已完成 |
| 15 | [机器学习统计学](phases/01-math-foundations/15-statistics-for-ml/docs/zh-CN.md) | [Statistics for Machine Learning](phases/01-math-foundations/15-statistics-for-ml/) | 已完成 |
| 16 | [采样方法](phases/01-math-foundations/16-sampling-methods/docs/zh-CN.md) | [Sampling Methods](phases/01-math-foundations/16-sampling-methods/) | 已完成 |
| 17 | [线性方程组](phases/01-math-foundations/17-linear-systems/docs/zh-CN.md) | [Linear Systems](phases/01-math-foundations/17-linear-systems/) | 已完成 |
| 18 | [凸优化](phases/01-math-foundations/18-convex-optimization/docs/zh-CN.md) | [Convex Optimization](phases/01-math-foundations/18-convex-optimization/) | 已完成 |
| 19 | [面向 AI 的复数](phases/01-math-foundations/19-complex-numbers/docs/zh-CN.md) | [Complex Numbers for AI](phases/01-math-foundations/19-complex-numbers/) | 已完成 |
| 20 | [傅里叶变换](phases/01-math-foundations/20-fourier-transform/docs/zh-CN.md) | [The Fourier Transform](phases/01-math-foundations/20-fourier-transform/) | 已完成 |
| 21 | [机器学习图论](phases/01-math-foundations/21-graph-theory/docs/zh-CN.md) | [Graph Theory for Machine Learning](phases/01-math-foundations/21-graph-theory/) | 已完成 |
| 22 | [随机过程](phases/01-math-foundations/22-stochastic-processes/docs/zh-CN.md) | [Stochastic Processes](phases/01-math-foundations/22-stochastic-processes/) | 已完成 |

### Phase 2：机器学习基础

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [什么是机器学习](phases/02-ml-fundamentals/01-what-is-machine-learning/docs/zh-CN.md) | [What Is Machine Learning](phases/02-ml-fundamentals/01-what-is-machine-learning/) | 已完成 |
| 02 | [线性回归](phases/02-ml-fundamentals/02-linear-regression/docs/zh-CN.md) | [Linear Regression from Scratch](phases/02-ml-fundamentals/02-linear-regression/) | 已完成 |
| 03 | [逻辑回归](phases/02-ml-fundamentals/03-logistic-regression/docs/zh-CN.md) | [Logistic Regression & Classification](phases/02-ml-fundamentals/03-logistic-regression/) | 已完成 |
| 04 | [决策树与随机森林](phases/02-ml-fundamentals/04-decision-trees/docs/zh-CN.md) | [Decision Trees & Random Forests](phases/02-ml-fundamentals/04-decision-trees/) | 已完成 |
| 05 | [支持向量机](phases/02-ml-fundamentals/05-support-vector-machines/docs/zh-CN.md) | [Support Vector Machines](phases/02-ml-fundamentals/05-support-vector-machines/) | 已完成 |
| 06 | [K 近邻与距离](phases/02-ml-fundamentals/06-knn-and-distances/docs/zh-CN.md) | [KNN & Distance Metrics](phases/02-ml-fundamentals/06-knn-and-distances/) | 已完成 |
| 07 | [无监督学习](phases/02-ml-fundamentals/07-unsupervised-learning/docs/zh-CN.md) | [Unsupervised Learning: K-Means, DBSCAN](phases/02-ml-fundamentals/07-unsupervised-learning/) | 已完成 |
| 08 | [特征工程与选择](phases/02-ml-fundamentals/08-feature-engineering/docs/zh-CN.md) | [Feature Engineering & Selection](phases/02-ml-fundamentals/08-feature-engineering/) | 已完成 |
| 09 | [模型评估](phases/02-ml-fundamentals/09-model-evaluation/docs/zh-CN.md) | [Model Evaluation: Metrics, Cross-Validation](phases/02-ml-fundamentals/09-model-evaluation/) | 已完成 |
| 10 | [偏差-方差权衡](phases/02-ml-fundamentals/10-bias-variance/docs/zh-CN.md) | [Bias, Variance & the Learning Curve](phases/02-ml-fundamentals/10-bias-variance/) | 已完成 |
| 11 | [集成方法](phases/02-ml-fundamentals/11-ensemble-methods/docs/zh-CN.md) | [Ensemble Methods: Boosting, Bagging, Stacking](phases/02-ml-fundamentals/11-ensemble-methods/) | 已完成 |
| 12 | [超参数调优](phases/02-ml-fundamentals/12-hyperparameter-tuning/docs/zh-CN.md) | [Hyperparameter Tuning](phases/02-ml-fundamentals/12-hyperparameter-tuning/) | 已完成 |
| 13 | [机器学习流水线](phases/02-ml-fundamentals/13-ml-pipelines/docs/zh-CN.md) | [ML Pipelines & Experiment Tracking](phases/02-ml-fundamentals/13-ml-pipelines/) | 已完成 |
| 14 | [朴素贝叶斯](phases/02-ml-fundamentals/14-naive-bayes/docs/zh-CN.md) | [Naive Bayes](phases/02-ml-fundamentals/14-naive-bayes/) | 已完成 |
| 15 | [时间序列基础](phases/02-ml-fundamentals/15-time-series/docs/zh-CN.md) | [Time Series Fundamentals](phases/02-ml-fundamentals/15-time-series/) | 已完成 |
| 16 | [异常检测](phases/02-ml-fundamentals/16-anomaly-detection/docs/zh-CN.md) | [Anomaly Detection](phases/02-ml-fundamentals/16-anomaly-detection/) | 已完成 |
| 17 | [处理不平衡数据](phases/02-ml-fundamentals/17-imbalanced-data/docs/zh-CN.md) | [Handling Imbalanced Data](phases/02-ml-fundamentals/17-imbalanced-data/) | 已完成 |
| 18 | [特征选择](phases/02-ml-fundamentals/18-feature-selection/docs/zh-CN.md) | [Feature Selection](phases/02-ml-fundamentals/18-feature-selection/) | 已完成 |

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

### Phase 4：计算机视觉

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [图像基础：像素、通道与色彩空间](phases/04-computer-vision/01-image-fundamentals/docs/zh-CN.md) | [Image Fundamentals: Pixels, Channels, Color Spaces](phases/04-computer-vision/01-image-fundamentals/) | 已完成 |
| 02 | [从零实现卷积](phases/04-computer-vision/02-convolutions-from-scratch/docs/zh-CN.md) | [Convolutions from Scratch](phases/04-computer-vision/02-convolutions-from-scratch/) | 已完成 |
| 03 | [CNN：从 LeNet 到 ResNet](phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/zh-CN.md) | [CNNs: LeNet to ResNet](phases/04-computer-vision/03-cnns-lenet-to-resnet/) | 已完成 |
| 04 | [图像分类](phases/04-computer-vision/04-image-classification/docs/zh-CN.md) | [Image Classification](phases/04-computer-vision/04-image-classification/) | 已完成 |
| 05 | [迁移学习与微调](phases/04-computer-vision/05-transfer-learning/docs/zh-CN.md) | [Transfer Learning & Fine-Tuning](phases/04-computer-vision/05-transfer-learning/) | 已完成 |
| 06 | [目标检测：从零理解 YOLO](phases/04-computer-vision/06-object-detection-yolo/docs/zh-CN.md) | [Object Detection — YOLO from Scratch](phases/04-computer-vision/06-object-detection-yolo/) | 已完成 |
| 07 | [语义分割：U-Net](phases/04-computer-vision/07-semantic-segmentation-unet/docs/zh-CN.md) | [Semantic Segmentation — U-Net](phases/04-computer-vision/07-semantic-segmentation-unet/) | 已完成 |
| 08 | [实例分割：Mask R-CNN](phases/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/zh-CN.md) | [Instance Segmentation — Mask R-CNN](phases/04-computer-vision/08-instance-segmentation-mask-rcnn/) | 已完成 |
| 09 | [图像生成：GANs](phases/04-computer-vision/09-image-generation-gans/docs/zh-CN.md) | [Image Generation — GANs](phases/04-computer-vision/09-image-generation-gans/) | 已完成 |
| 10 | [图像生成：扩散模型](phases/04-computer-vision/10-image-generation-diffusion/docs/zh-CN.md) | [Image Generation — Diffusion Models](phases/04-computer-vision/10-image-generation-diffusion/) | 已完成 |
| 11 | [Stable Diffusion：架构与微调](phases/04-computer-vision/11-stable-diffusion/docs/zh-CN.md) | [Stable Diffusion — Architecture & Fine-Tuning](phases/04-computer-vision/11-stable-diffusion/) | 已完成 |
| 12 | [视频理解：时间建模](phases/04-computer-vision/12-video-understanding/docs/zh-CN.md) | [Video Understanding — Temporal Modeling](phases/04-computer-vision/12-video-understanding/) | 已完成 |
| 13 | [3D 视觉：点云与 NeRF](phases/04-computer-vision/13-3d-vision-nerf/docs/zh-CN.md) | [3D Vision: Point Clouds, NeRFs](phases/04-computer-vision/13-3d-vision-nerf/) | 已完成 |
| 14 | [视觉 Transformer (ViT)](phases/04-computer-vision/14-vision-transformers/docs/zh-CN.md) | [Vision Transformers (ViT)](phases/04-computer-vision/14-vision-transformers/) | 已完成 |
| 15 | [实时视觉：边缘部署](phases/04-computer-vision/15-real-time-edge/docs/zh-CN.md) | [Real-Time Vision: Edge Deployment](phases/04-computer-vision/15-real-time-edge/) | 已完成 |
| 16 | [构建完整视觉流水线：Capstone](phases/04-computer-vision/16-vision-pipeline-capstone/docs/zh-CN.md) | [Build a Complete Vision Pipeline](phases/04-computer-vision/16-vision-pipeline-capstone/) | 已完成 |
| 17 | [自监督视觉：SimCLR、DINO、MAE](phases/04-computer-vision/17-self-supervised-vision/docs/zh-CN.md) | [Self-Supervised Vision — SimCLR, DINO, MAE](phases/04-computer-vision/17-self-supervised-vision/) | 已完成 |
| 18 | [开放词表视觉：CLIP](phases/04-computer-vision/18-open-vocab-clip/docs/zh-CN.md) | [Open-Vocabulary Vision — CLIP](phases/04-computer-vision/18-open-vocab-clip/) | 已完成 |
| 19 | [OCR 与文档理解](phases/04-computer-vision/19-ocr-document-understanding/docs/zh-CN.md) | [OCR & Document Understanding](phases/04-computer-vision/19-ocr-document-understanding/) | 已完成 |
| 20 | [图像检索与度量学习](phases/04-computer-vision/20-image-retrieval-metric/docs/zh-CN.md) | [Image Retrieval & Metric Learning](phases/04-computer-vision/20-image-retrieval-metric/) | 已完成 |
| 21 | [关键点检测与姿态估计](phases/04-computer-vision/21-keypoint-pose/docs/zh-CN.md) | [Keypoint Detection & Pose Estimation](phases/04-computer-vision/21-keypoint-pose/) | 已完成 |
| 22 | [从零理解 3D Gaussian Splatting](phases/04-computer-vision/22-3d-gaussian-splatting/docs/zh-CN.md) | [3D Gaussian Splatting from Scratch](phases/04-computer-vision/22-3d-gaussian-splatting/) | 已完成 |
| 23 | [Diffusion Transformers 与 Rectified Flow](phases/04-computer-vision/23-diffusion-transformers-rectified-flow/docs/zh-CN.md) | [Diffusion Transformers & Rectified Flow](phases/04-computer-vision/23-diffusion-transformers-rectified-flow/) | 已完成 |
| 24 | [SAM 3 与开放词表分割](phases/04-computer-vision/24-sam3-open-vocab-segmentation/docs/zh-CN.md) | [SAM 3 & Open-Vocabulary Segmentation](phases/04-computer-vision/24-sam3-open-vocab-segmentation/) | 已完成 |
| 25 | [视觉语言模型：ViT-MLP-LLM 模式](phases/04-computer-vision/25-vision-language-models/docs/zh-CN.md) | [Vision-Language Models (ViT-MLP-LLM)](phases/04-computer-vision/25-vision-language-models/) | 已完成 |
| 26 | [单目深度与几何估计](phases/04-computer-vision/26-monocular-depth/docs/zh-CN.md) | [Monocular Depth & Geometry Estimation](phases/04-computer-vision/26-monocular-depth/) | 已完成 |
| 27 | [多目标跟踪与视频记忆](phases/04-computer-vision/27-multi-object-tracking/docs/zh-CN.md) | [Multi-Object Tracking & Video Memory](phases/04-computer-vision/27-multi-object-tracking/) | 已完成 |
| 28 | [世界模型与视频扩散](phases/04-computer-vision/28-world-models-video-diffusion/docs/zh-CN.md) | [World Models & Video Diffusion](phases/04-computer-vision/28-world-models-video-diffusion/) | 已完成 |

每课都包含：

- `docs/zh-CN.md`：中文正文
- `quiz.zh-CN.json`：中文测验
- `outputs/*.zh-CN.md`：中文 prompt / skill / artifact

查看中文化进度：

```bash
python3 scripts/audit_translations.py --phase 4
```

查看原仓库课程结构是否仍然有效：

```bash
python3 scripts/audit_lessons.py --phase 4
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

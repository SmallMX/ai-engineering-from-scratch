# AI Engineering from Scratch 中文说明

> 这是一个从零构建 AI 工程能力的课程仓库：先手写数学、模型和智能体循环，再使用生产级框架理解同一件事。

这个 fork 已经补齐课程中文旁路译文。英文原文保留在原文件中，中文译文使用 `zh-CN` 旁路文件，方便以后继续同步上游。

## 快速找目录

如果你只是想找课表，直接看下面两处：

- **中文导航：** 本文件的 [课程目录](#课程目录)
- **完整英文课表：** [README.md#contents](README.md#contents)

每节课的目录结构固定：

```text
phases/<阶段>/<课程>/
├── docs/
│   ├── en.md       # 英文正文
│   └── zh-CN.md    # 中文正文
├── code/           # 可运行代码
├── quiz.json       # 英文测验
├── quiz.zh-CN.json # 中文测验
└── outputs/        # prompt / skill / agent / MCP 等课程产物
```

## 现在怎么读

推荐按照课程自然顺序从 Phase 0 开始看。Phase 0 到 Phase 19 已经补齐中文正文、中文测验和中文产物，可以直接按顺序学习。

### Phase 0：环境搭建与工具

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [开发环境](phases/00-setup-and-tooling/01-dev-environment/docs/zh-CN.md) | [Dev Environment](phases/00-setup-and-tooling/01-dev-environment/) | 已完成 |
| 02 | [Git 与协作](phases/00-setup-and-tooling/02-git-and-collaboration/docs/zh-CN.md) | [Git & Collaboration](phases/00-setup-and-tooling/02-git-and-collaboration/) | 已完成 |
| 03 | [GPU 设置与云端](phases/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/zh-CN.md) | [GPU Setup & Cloud](phases/00-setup-and-tooling/03-gpu-setup-and-cloud/) | 已完成 |
| 04 | [APIs 与 Keys](phases/00-setup-and-tooling/04-apis-and-keys/docs/zh-CN.md) | [APIs & Keys](phases/00-setup-and-tooling/04-apis-and-keys/) | 已完成 |
| 05 | [Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks/docs/zh-CN.md) | [Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks/) | 已完成 |
| 06 | [Python 环境](phases/00-setup-and-tooling/06-python-environments/docs/zh-CN.md) | [Python Environments](phases/00-setup-and-tooling/06-python-environments/) | 已完成 |
| 07 | [面向 AI 的 Docker](phases/00-setup-and-tooling/07-docker-for-ai/docs/zh-CN.md) | [Docker for AI](phases/00-setup-and-tooling/07-docker-for-ai/) | 已完成 |
| 08 | [编辑器设置](phases/00-setup-and-tooling/08-editor-setup/docs/zh-CN.md) | [Editor Setup](phases/00-setup-and-tooling/08-editor-setup/) | 已完成 |
| 09 | [数据管理](phases/00-setup-and-tooling/09-data-management/docs/zh-CN.md) | [Data Management](phases/00-setup-and-tooling/09-data-management/) | 已完成 |
| 10 | [终端与 Shell](phases/00-setup-and-tooling/10-terminal-and-shell/docs/zh-CN.md) | [Terminal & Shell](phases/00-setup-and-tooling/10-terminal-and-shell/) | 已完成 |
| 11 | [面向 AI 的 Linux](phases/00-setup-and-tooling/11-linux-for-ai/docs/zh-CN.md) | [Linux for AI](phases/00-setup-and-tooling/11-linux-for-ai/) | 已完成 |
| 12 | [调试与 Profiling](phases/00-setup-and-tooling/12-debugging-and-profiling/docs/zh-CN.md) | [Debugging and Profiling](phases/00-setup-and-tooling/12-debugging-and-profiling/) | 已完成 |

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
| 02 | [线性回归](phases/02-ml-fundamentals/02-linear-regression/docs/zh-CN.md) | [Linear Regression](phases/02-ml-fundamentals/02-linear-regression/) | 已完成 |
| 03 | [逻辑回归](phases/02-ml-fundamentals/03-logistic-regression/docs/zh-CN.md) | [Logistic Regression](phases/02-ml-fundamentals/03-logistic-regression/) | 已完成 |
| 04 | [决策树与随机森林](phases/02-ml-fundamentals/04-decision-trees/docs/zh-CN.md) | [Decision Trees and Random Forests](phases/02-ml-fundamentals/04-decision-trees/) | 已完成 |
| 05 | [支持向量机](phases/02-ml-fundamentals/05-support-vector-machines/docs/zh-CN.md) | [Support Vector Machines](phases/02-ml-fundamentals/05-support-vector-machines/) | 已完成 |
| 06 | [K 近邻与距离](phases/02-ml-fundamentals/06-knn-and-distances/docs/zh-CN.md) | [K-Nearest Neighbors and Distances](phases/02-ml-fundamentals/06-knn-and-distances/) | 已完成 |
| 07 | [无监督学习](phases/02-ml-fundamentals/07-unsupervised-learning/docs/zh-CN.md) | [Unsupervised Learning](phases/02-ml-fundamentals/07-unsupervised-learning/) | 已完成 |
| 08 | [特征工程与选择](phases/02-ml-fundamentals/08-feature-engineering/docs/zh-CN.md) | [Feature Engineering & Selection](phases/02-ml-fundamentals/08-feature-engineering/) | 已完成 |
| 09 | [模型评估](phases/02-ml-fundamentals/09-model-evaluation/docs/zh-CN.md) | [Model Evaluation](phases/02-ml-fundamentals/09-model-evaluation/) | 已完成 |
| 10 | [偏差-方差权衡](phases/02-ml-fundamentals/10-bias-variance/docs/zh-CN.md) | [Bias-Variance Tradeoff](phases/02-ml-fundamentals/10-bias-variance/) | 已完成 |
| 11 | [集成方法](phases/02-ml-fundamentals/11-ensemble-methods/docs/zh-CN.md) | [Ensemble Methods](phases/02-ml-fundamentals/11-ensemble-methods/) | 已完成 |
| 12 | [超参数调优](phases/02-ml-fundamentals/12-hyperparameter-tuning/docs/zh-CN.md) | [Hyperparameter Tuning](phases/02-ml-fundamentals/12-hyperparameter-tuning/) | 已完成 |
| 13 | [机器学习流水线](phases/02-ml-fundamentals/13-ml-pipelines/docs/zh-CN.md) | [ML Pipelines](phases/02-ml-fundamentals/13-ml-pipelines/) | 已完成 |
| 14 | [朴素贝叶斯](phases/02-ml-fundamentals/14-naive-bayes/docs/zh-CN.md) | [Naive Bayes](phases/02-ml-fundamentals/14-naive-bayes/) | 已完成 |
| 15 | [时间序列基础](phases/02-ml-fundamentals/15-time-series/docs/zh-CN.md) | [Time Series Fundamentals](phases/02-ml-fundamentals/15-time-series/) | 已完成 |
| 16 | [异常检测](phases/02-ml-fundamentals/16-anomaly-detection/docs/zh-CN.md) | [Anomaly Detection](phases/02-ml-fundamentals/16-anomaly-detection/) | 已完成 |
| 17 | [处理不平衡数据](phases/02-ml-fundamentals/17-imbalanced-data/docs/zh-CN.md) | [Handling Imbalanced Data](phases/02-ml-fundamentals/17-imbalanced-data/) | 已完成 |
| 18 | [特征选择](phases/02-ml-fundamentals/18-feature-selection/docs/zh-CN.md) | [Feature Selection](phases/02-ml-fundamentals/18-feature-selection/) | 已完成 |

### Phase 3：深度学习核心

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [感知机](phases/03-deep-learning-core/01-the-perceptron/docs/zh-CN.md) | [The Perceptron](phases/03-deep-learning-core/01-the-perceptron/) | 已完成 |
| 02 | [多层网络与前向传播](phases/03-deep-learning-core/02-multi-layer-networks/docs/zh-CN.md) | [Multi-Layer Networks and Forward Pass](phases/03-deep-learning-core/02-multi-layer-networks/) | 已完成 |
| 03 | [从零实现反向传播](phases/03-deep-learning-core/03-backpropagation/docs/zh-CN.md) | [Backpropagation from Scratch](phases/03-deep-learning-core/03-backpropagation/) | 已完成 |
| 04 | [激活函数](phases/03-deep-learning-core/04-activation-functions/docs/zh-CN.md) | [Activation Functions](phases/03-deep-learning-core/04-activation-functions/) | 已完成 |
| 05 | [损失函数](phases/03-deep-learning-core/05-loss-functions/docs/zh-CN.md) | [Loss Functions](phases/03-deep-learning-core/05-loss-functions/) | 已完成 |
| 06 | [优化器](phases/03-deep-learning-core/06-optimizers/docs/zh-CN.md) | [Optimizers](phases/03-deep-learning-core/06-optimizers/) | 已完成 |
| 07 | [正则化](phases/03-deep-learning-core/07-regularization/docs/zh-CN.md) | [Regularization](phases/03-deep-learning-core/07-regularization/) | 已完成 |
| 08 | [权重初始化与训练稳定性](phases/03-deep-learning-core/08-weight-initialization/docs/zh-CN.md) | [Weight Initialization and Training Stability](phases/03-deep-learning-core/08-weight-initialization/) | 已完成 |
| 09 | [学习率调度与 Warmup](phases/03-deep-learning-core/09-learning-rate-schedules/docs/zh-CN.md) | [Learning Rate Schedules and Warmup](phases/03-deep-learning-core/09-learning-rate-schedules/) | 已完成 |
| 10 | [构建你自己的迷你框架](phases/03-deep-learning-core/10-mini-framework/docs/zh-CN.md) | [Build Your Own Mini Framework](phases/03-deep-learning-core/10-mini-framework/) | 已完成 |
| 11 | [PyTorch 入门](phases/03-deep-learning-core/11-intro-to-pytorch/docs/zh-CN.md) | [Introduction to PyTorch](phases/03-deep-learning-core/11-intro-to-pytorch/) | 已完成 |
| 12 | [JAX 入门](phases/03-deep-learning-core/12-intro-to-jax/docs/zh-CN.md) | [Introduction to JAX](phases/03-deep-learning-core/12-intro-to-jax/) | 已完成 |
| 13 | [调试神经网络](phases/03-deep-learning-core/13-debugging-neural-networks/docs/zh-CN.md) | [Debugging Neural Networks](phases/03-deep-learning-core/13-debugging-neural-networks/) | 已完成 |

### Phase 4：计算机视觉

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [图像基础：像素、通道与色彩空间](phases/04-computer-vision/01-image-fundamentals/docs/zh-CN.md) | [Image Fundamentals — Pixels, Channels, Color Spaces](phases/04-computer-vision/01-image-fundamentals/) | 已完成 |
| 02 | [从零实现卷积](phases/04-computer-vision/02-convolutions-from-scratch/docs/zh-CN.md) | [Convolutions from Scratch](phases/04-computer-vision/02-convolutions-from-scratch/) | 已完成 |
| 03 | [CNN：从 LeNet 到 ResNet](phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/zh-CN.md) | [CNNs — LeNet to ResNet](phases/04-computer-vision/03-cnns-lenet-to-resnet/) | 已完成 |
| 04 | [图像分类](phases/04-computer-vision/04-image-classification/docs/zh-CN.md) | [Image Classification](phases/04-computer-vision/04-image-classification/) | 已完成 |
| 05 | [迁移学习与微调](phases/04-computer-vision/05-transfer-learning/docs/zh-CN.md) | [Transfer Learning & Fine-Tuning](phases/04-computer-vision/05-transfer-learning/) | 已完成 |
| 06 | [目标检测：从零理解 YOLO](phases/04-computer-vision/06-object-detection-yolo/docs/zh-CN.md) | [Object Detection — YOLO from Scratch](phases/04-computer-vision/06-object-detection-yolo/) | 已完成 |
| 07 | [语义分割：U-Net](phases/04-computer-vision/07-semantic-segmentation-unet/docs/zh-CN.md) | [Semantic Segmentation — U-Net](phases/04-computer-vision/07-semantic-segmentation-unet/) | 已完成 |
| 08 | [实例分割：Mask R-CNN](phases/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/zh-CN.md) | [Instance Segmentation — Mask R-CNN](phases/04-computer-vision/08-instance-segmentation-mask-rcnn/) | 已完成 |
| 09 | [图像生成：GANs](phases/04-computer-vision/09-image-generation-gans/docs/zh-CN.md) | [Image Generation — GANs](phases/04-computer-vision/09-image-generation-gans/) | 已完成 |
| 10 | [图像生成：扩散模型](phases/04-computer-vision/10-image-generation-diffusion/docs/zh-CN.md) | [Image Generation — Diffusion Models](phases/04-computer-vision/10-image-generation-diffusion/) | 已完成 |
| 11 | [Stable Diffusion：架构与微调](phases/04-computer-vision/11-stable-diffusion/docs/zh-CN.md) | [Stable Diffusion — Architecture & Fine-Tuning](phases/04-computer-vision/11-stable-diffusion/) | 已完成 |
| 12 | [视频理解：时间建模](phases/04-computer-vision/12-video-understanding/docs/zh-CN.md) | [Video Understanding — Temporal Modeling](phases/04-computer-vision/12-video-understanding/) | 已完成 |
| 13 | [3D 视觉：点云与 NeRF](phases/04-computer-vision/13-3d-vision-nerf/docs/zh-CN.md) | [3D Vision — Point Clouds & NeRFs](phases/04-computer-vision/13-3d-vision-nerf/) | 已完成 |
| 14 | [视觉 Transformer (ViT)](phases/04-computer-vision/14-vision-transformers/docs/zh-CN.md) | [Vision Transformers (ViT)](phases/04-computer-vision/14-vision-transformers/) | 已完成 |
| 15 | [实时视觉：边缘部署](phases/04-computer-vision/15-real-time-edge/docs/zh-CN.md) | [Real-Time Vision — Edge Deployment](phases/04-computer-vision/15-real-time-edge/) | 已完成 |
| 16 | [构建完整视觉流水线：Capstone](phases/04-computer-vision/16-vision-pipeline-capstone/docs/zh-CN.md) | [Build a Complete Vision Pipeline — Capstone](phases/04-computer-vision/16-vision-pipeline-capstone/) | 已完成 |
| 17 | [自监督视觉：SimCLR、DINO、MAE](phases/04-computer-vision/17-self-supervised-vision/docs/zh-CN.md) | [Self-Supervised Vision — SimCLR, DINO, MAE](phases/04-computer-vision/17-self-supervised-vision/) | 已完成 |
| 18 | [开放词表视觉：CLIP](phases/04-computer-vision/18-open-vocab-clip/docs/zh-CN.md) | [Open-Vocabulary Vision — CLIP](phases/04-computer-vision/18-open-vocab-clip/) | 已完成 |
| 19 | [OCR 与文档理解](phases/04-computer-vision/19-ocr-document-understanding/docs/zh-CN.md) | [OCR & Document Understanding](phases/04-computer-vision/19-ocr-document-understanding/) | 已完成 |
| 20 | [图像检索与度量学习](phases/04-computer-vision/20-image-retrieval-metric/docs/zh-CN.md) | [Image Retrieval & Metric Learning](phases/04-computer-vision/20-image-retrieval-metric/) | 已完成 |
| 21 | [关键点检测与姿态估计](phases/04-computer-vision/21-keypoint-pose/docs/zh-CN.md) | [Keypoint Detection & Pose Estimation](phases/04-computer-vision/21-keypoint-pose/) | 已完成 |
| 22 | [从零理解 3D Gaussian Splatting](phases/04-computer-vision/22-3d-gaussian-splatting/docs/zh-CN.md) | [3D Gaussian Splatting from Scratch](phases/04-computer-vision/22-3d-gaussian-splatting/) | 已完成 |
| 23 | [Diffusion Transformers 与 Rectified Flow](phases/04-computer-vision/23-diffusion-transformers-rectified-flow/docs/zh-CN.md) | [Diffusion Transformers & Rectified Flow](phases/04-computer-vision/23-diffusion-transformers-rectified-flow/) | 已完成 |
| 24 | [SAM 3 与开放词表分割](phases/04-computer-vision/24-sam3-open-vocab-segmentation/docs/zh-CN.md) | [SAM 3 & Open-Vocabulary Segmentation](phases/04-computer-vision/24-sam3-open-vocab-segmentation/) | 已完成 |
| 25 | [视觉语言模型：ViT-MLP-LLM 模式](phases/04-computer-vision/25-vision-language-models/docs/zh-CN.md) | [Vision-Language Models — The ViT-MLP-LLM Pattern](phases/04-computer-vision/25-vision-language-models/) | 已完成 |
| 26 | [单目深度与几何估计](phases/04-computer-vision/26-monocular-depth/docs/zh-CN.md) | [Monocular Depth & Geometry Estimation](phases/04-computer-vision/26-monocular-depth/) | 已完成 |
| 27 | [多目标跟踪与视频记忆](phases/04-computer-vision/27-multi-object-tracking/docs/zh-CN.md) | [Multi-Object Tracking & Video Memory](phases/04-computer-vision/27-multi-object-tracking/) | 已完成 |
| 28 | [世界模型与视频扩散](phases/04-computer-vision/28-world-models-video-diffusion/docs/zh-CN.md) | [World Models & Video Diffusion](phases/04-computer-vision/28-world-models-video-diffusion/) | 已完成 |

### Phase 5：NLP：从基础到进阶

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [文本处理：分词, Stemming, Lemmatization](phases/05-nlp-foundations-to-advanced/01-text-processing/docs/zh-CN.md) | [Text Processing — Tokenization, Stemming, Lemmatization](phases/05-nlp-foundations-to-advanced/01-text-processing/) | 已完成 |
| 02 | [Bag of Words, TF-IDF,与Text Representation](phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/docs/zh-CN.md) | [Bag of Words, TF-IDF, and Text Representation](phases/05-nlp-foundations-to-advanced/02-bag-of-words-tfidf/) | 已完成 |
| 03 | [Word 嵌入：Word2Vec 从零实现](phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/docs/zh-CN.md) | [Word Embeddings — Word2Vec from Scratch](phases/05-nlp-foundations-to-advanced/03-word-embeddings-word2vec/) | 已完成 |
| 04 | [GloVe, FastText,与Subword 嵌入](phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/docs/zh-CN.md) | [GloVe, FastText, and Subword Embeddings](phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/) | 已完成 |
| 05 | [Sentiment Analysis](phases/05-nlp-foundations-to-advanced/05-sentiment-analysis/docs/zh-CN.md) | [Sentiment Analysis](phases/05-nlp-foundations-to-advanced/05-sentiment-analysis/) | 已完成 |
| 06 | [命名实体识别](phases/05-nlp-foundations-to-advanced/06-named-entity-recognition/docs/zh-CN.md) | [Named Entity Recognition](phases/05-nlp-foundations-to-advanced/06-named-entity-recognition/) | 已完成 |
| 07 | [POS Tagging与Syntactic Parsing](phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing/docs/zh-CN.md) | [POS Tagging and Syntactic Parsing](phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing/) | 已完成 |
| 08 | [CNNs与RNNs for Text](phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text/docs/zh-CN.md) | [CNNs and RNNs for Text](phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text/) | 已完成 |
| 09 | [Sequence-to-Sequence Models](phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/zh-CN.md) | [Sequence-to-Sequence Models](phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/) | 已完成 |
| 10 | [注意力 Mechanism：The Breakthrough](phases/05-nlp-foundations-to-advanced/10-attention-mechanism/docs/zh-CN.md) | [Attention Mechanism — The Breakthrough](phases/05-nlp-foundations-to-advanced/10-attention-mechanism/) | 已完成 |
| 11 | [机器翻译](phases/05-nlp-foundations-to-advanced/11-machine-translation/docs/zh-CN.md) | [Machine Translation](phases/05-nlp-foundations-to-advanced/11-machine-translation/) | 已完成 |
| 12 | [文本摘要](phases/05-nlp-foundations-to-advanced/12-text-summarization/docs/zh-CN.md) | [Text Summarization](phases/05-nlp-foundations-to-advanced/12-text-summarization/) | 已完成 |
| 13 | [问答 系统](phases/05-nlp-foundations-to-advanced/13-question-answering/docs/zh-CN.md) | [Question Answering Systems](phases/05-nlp-foundations-to-advanced/13-question-answering/) | 已完成 |
| 14 | [Information 检索与搜索](phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/docs/zh-CN.md) | [Information Retrieval and Search](phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/) | 已完成 |
| 15 | [Topic Modeling：LDA与BERTopic](phases/05-nlp-foundations-to-advanced/15-topic-modeling/docs/zh-CN.md) | [Topic Modeling — LDA and BERTopic](phases/05-nlp-foundations-to-advanced/15-topic-modeling/) | 已完成 |
| 16 | [文本生成 Before Transformer：N-gram 语言模型](phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/docs/zh-CN.md) | [Text Generation Before Transformers — N-gram Language Models](phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer/) | 已完成 |
| 17 | [Chatbots：Rule-Based to Neural to LLM 智能体](phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/docs/zh-CN.md) | [Chatbots — Rule-Based to Neural to LLM Agents](phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/) | 已完成 |
| 18 | [Multilingual NLP](phases/05-nlp-foundations-to-advanced/18-multilingual-nlp/docs/zh-CN.md) | [Multilingual NLP](phases/05-nlp-foundations-to-advanced/18-multilingual-nlp/) | 已完成 |
| 19 | [Subword 分词：BPE, WordPiece, Unigram, SentencePiece](phases/05-nlp-foundations-to-advanced/19-subword-tokenization/docs/zh-CN.md) | [Subword Tokenization — BPE, WordPiece, Unigram, SentencePiece](phases/05-nlp-foundations-to-advanced/19-subword-tokenization/) | 已完成 |
| 20 | [结构化输出与Constrained Decoding](phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding/docs/zh-CN.md) | [Structured Outputs & Constrained Decoding](phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding/) | 已完成 |
| 21 | [Natural Language 推理：Textual Entailment](phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment/docs/zh-CN.md) | [Natural Language Inference — Textual Entailment](phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment/) | 已完成 |
| 22 | [嵌入模型：The 2026 深入解析](phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/docs/zh-CN.md) | [Embedding Models — The 2026 Deep Dive](phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/) | 已完成 |
| 23 | [Chunking Strategies for RAG](phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/docs/zh-CN.md) | [Chunking Strategies for RAG](phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag/) | 已完成 |
| 24 | [共指消解](phases/05-nlp-foundations-to-advanced/24-coreference-resolution/docs/zh-CN.md) | [Coreference Resolution](phases/05-nlp-foundations-to-advanced/24-coreference-resolution/) | 已完成 |
| 25 | [实体链接与Disambiguation](phases/05-nlp-foundations-to-advanced/25-entity-linking/docs/zh-CN.md) | [Entity Linking & Disambiguation](phases/05-nlp-foundations-to-advanced/25-entity-linking/) | 已完成 |
| 26 | [关系抽取与知识图谱 Construction](phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/docs/zh-CN.md) | [Relation Extraction & Knowledge Graph Construction](phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/) | 已完成 |
| 27 | [LLM 评估：RAGAS, DeepEval, G-评估](phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks/docs/zh-CN.md) | [LLM Evaluation — RAGAS, DeepEval, G-Eval](phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks/) | 已完成 |
| 28 | [Long-Context 评估：NIAH, RULER, LongBench, MRCR](phases/05-nlp-foundations-to-advanced/28-long-context-evaluation/docs/zh-CN.md) | [Long-Context Evaluation — NIAH, RULER, LongBench, MRCR](phases/05-nlp-foundations-to-advanced/28-long-context-evaluation/) | 已完成 |
| 29 | [Dialogue State Tracking](phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking/docs/zh-CN.md) | [Dialogue State Tracking](phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking/) | 已完成 |

### Phase 6：语音与音频

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [音频 基础：Waveforms, Sampling, Fourier Transform](phases/06-speech-and-audio/01-audio-fundamentals/docs/zh-CN.md) | [Audio Fundamentals — Waveforms, Sampling, Fourier Transform](phases/06-speech-and-audio/01-audio-fundamentals/) | 已完成 |
| 02 | [声谱图, Mel Scale与音频 Features](phases/06-speech-and-audio/02-spectrograms-mel-features/docs/zh-CN.md) | [Spectrograms, Mel Scale & Audio Features](phases/06-speech-and-audio/02-spectrograms-mel-features/) | 已完成 |
| 03 | [音频 Classification：From k-NN on MFCCs to AST与BEATs](phases/06-speech-and-audio/03-audio-classification/docs/zh-CN.md) | [Audio Classification — From k-NN on MFCCs to AST and BEATs](phases/06-speech-and-audio/03-audio-classification/) | 已完成 |
| 04 | [语音 Recognition (ASR)：CTC, RNN-T, 注意力](phases/06-speech-and-audio/04-speech-recognition-asr/docs/zh-CN.md) | [Speech Recognition (ASR) — CTC, RNN-T, Attention](phases/06-speech-and-audio/04-speech-recognition-asr/) | 已完成 |
| 05 | [Whisper：Architecture与微调](phases/06-speech-and-audio/05-whisper-architecture-finetuning/docs/zh-CN.md) | [Whisper — Architecture & Fine-Tuning](phases/06-speech-and-audio/05-whisper-architecture-finetuning/) | 已完成 |
| 06 | [Speaker Recognition与Verification](phases/06-speech-and-audio/06-speaker-recognition-verification/docs/zh-CN.md) | [Speaker Recognition & Verification](phases/06-speech-and-audio/06-speaker-recognition-verification/) | 已完成 |
| 07 | [Text-to-语音 (TTS)：From Tacotron to F5与Kokoro](phases/06-speech-and-audio/07-text-to-speech/docs/zh-CN.md) | [Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro](phases/06-speech-and-audio/07-text-to-speech/) | 已完成 |
| 08 | [语音 Cloning与语音 Conversion](phases/06-speech-and-audio/08-voice-cloning-conversion/docs/zh-CN.md) | [Voice Cloning & Voice Conversion](phases/06-speech-and-audio/08-voice-cloning-conversion/) | 已完成 |
| 09 | [音乐 Generation：MusicGen, Stable 音频, Suno,与the Licensing Earthquake](phases/06-speech-and-audio/09-music-generation/docs/zh-CN.md) | [Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake](phases/06-speech-and-audio/09-music-generation/) | 已完成 |
| 10 | [音频-语言模型：Qwen2.5-Omni, 音频 Flamingo, GPT-4o 音频](phases/06-speech-and-audio/10-audio-language-models/docs/zh-CN.md) | [Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio](phases/06-speech-and-audio/10-audio-language-models/) | 已完成 |
| 11 | [Real-Time 音频 Processing](phases/06-speech-and-audio/11-real-time-audio-processing/docs/zh-CN.md) | [Real-Time Audio Processing](phases/06-speech-and-audio/11-real-time-audio-processing/) | 已完成 |
| 12 | [Build a 语音 Assistant Pipeline：The Phase 6 毕业项目](phases/06-speech-and-audio/12-voice-assistant-pipeline/docs/zh-CN.md) | [Build a Voice Assistant Pipeline — The Phase 6 Capstone](phases/06-speech-and-audio/12-voice-assistant-pipeline/) | 已完成 |
| 13 | [Neural 音频 Codecs：EnCodec, SNAC, Mimi, DAC与the Semantic-Acoustic Split](phases/06-speech-and-audio/13-neural-audio-codecs/docs/zh-CN.md) | [Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split](phases/06-speech-and-audio/13-neural-audio-codecs/) | 已完成 |
| 14 | [语音 Activity Detection与Turn-Taking：Silero, Cobra,与the Flush Trick](phases/06-speech-and-audio/14-voice-activity-detection-turn-taking/docs/zh-CN.md) | [Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick](phases/06-speech-and-audio/14-voice-activity-detection-turn-taking/) | 已完成 |
| 15 | [Streaming 语音-to-语音：Moshi, Hibiki,与Full-Duplex Dialogue](phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki/docs/zh-CN.md) | [Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue](phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki/) | 已完成 |
| 16 | [语音 Anti-Spoofing与音频 水印：ASVspoof 5, AudioSeal, WaveVerify](phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking/docs/zh-CN.md) | [Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify](phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking/) | 已完成 |
| 17 | [音频 评估：WER, MOS, UTMOS, MMAU, FAD,与the Open Leaderboards](phases/06-speech-and-audio/17-audio-evaluation-metrics/docs/zh-CN.md) | [Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards](phases/06-speech-and-audio/17-audio-evaluation-metrics/) | 已完成 |

### Phase 7：Transformer 深入解析

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [Why Transformer：The Problems with RNNs](phases/07-transformers-deep-dive/01-why-transformers/docs/zh-CN.md) | [Why Transformers — The Problems with RNNs](phases/07-transformers-deep-dive/01-why-transformers/) | 已完成 |
| 02 | [Self-注意力 从零实现](phases/07-transformers-deep-dive/02-self-attention-from-scratch/docs/zh-CN.md) | [Self-Attention from Scratch](phases/07-transformers-deep-dive/02-self-attention-from-scratch/) | 已完成 |
| 03 | [Multi-Head 注意力](phases/07-transformers-deep-dive/03-multi-head-attention/docs/zh-CN.md) | [Multi-Head Attention](phases/07-transformers-deep-dive/03-multi-head-attention/) | 已完成 |
| 04 | [Positional Encoding：Sinusoidal, RoPE, ALiBi](phases/07-transformers-deep-dive/04-positional-encoding/docs/zh-CN.md) | [Positional Encoding — Sinusoidal, RoPE, ALiBi](phases/07-transformers-deep-dive/04-positional-encoding/) | 已完成 |
| 05 | [The Full Transformer：Encoder + Decoder](phases/07-transformers-deep-dive/05-full-transformer/docs/zh-CN.md) | [The Full Transformer — Encoder + Decoder](phases/07-transformers-deep-dive/05-full-transformer/) | 已完成 |
| 06 | [BERT：Masked Language Modeling](phases/07-transformers-deep-dive/06-bert-masked-language-modeling/docs/zh-CN.md) | [BERT — Masked Language Modeling](phases/07-transformers-deep-dive/06-bert-masked-language-modeling/) | 已完成 |
| 07 | [GPT：Causal Language Modeling](phases/07-transformers-deep-dive/07-gpt-causal-language-modeling/docs/zh-CN.md) | [GPT — Causal Language Modeling](phases/07-transformers-deep-dive/07-gpt-causal-language-modeling/) | 已完成 |
| 08 | [T5, BART：Encoder-Decoder Models](phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder/docs/zh-CN.md) | [T5, BART — Encoder-Decoder Models](phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder/) | 已完成 |
| 09 | [视觉 Transformer (ViT)](phases/07-transformers-deep-dive/09-vision-transformers/docs/zh-CN.md) | [Vision Transformers (ViT)](phases/07-transformers-deep-dive/09-vision-transformers/) | 已完成 |
| 10 | [音频 Transformer：Whisper Architecture](phases/07-transformers-deep-dive/10-audio-transformers-whisper/docs/zh-CN.md) | [Audio Transformers — Whisper Architecture](phases/07-transformers-deep-dive/10-audio-transformers-whisper/) | 已完成 |
| 11 | [Mixture of Experts (MoE)](phases/07-transformers-deep-dive/11-mixture-of-experts/docs/zh-CN.md) | [Mixture of Experts (MoE)](phases/07-transformers-deep-dive/11-mixture-of-experts/) | 已完成 |
| 12 | [KV 缓存, Flash 注意力与推理 Optimization](phases/07-transformers-deep-dive/12-kv-cache-flash-attention/docs/zh-CN.md) | [KV Cache, Flash Attention & Inference Optimization](phases/07-transformers-deep-dive/12-kv-cache-flash-attention/) | 已完成 |
| 13 | [扩展 Laws](phases/07-transformers-deep-dive/13-scaling-laws/docs/zh-CN.md) | [Scaling Laws](phases/07-transformers-deep-dive/13-scaling-laws/) | 已完成 |
| 14 | [Build a Transformer 从零实现：The 毕业项目](phases/07-transformers-deep-dive/14-build-a-transformer-capstone/docs/zh-CN.md) | [Build a Transformer from Scratch — The Capstone](phases/07-transformers-deep-dive/14-build-a-transformer-capstone/) | 已完成 |
| 15 | [注意力 Variants：Sliding Window, Sparse, Differential](phases/07-transformers-deep-dive/15-attention-variants/docs/zh-CN.md) | [Attention Variants — Sliding Window, Sparse, Differential](phases/07-transformers-deep-dive/15-attention-variants/) | 已完成 |
| 16 | [Speculative Decoding：Draft, Verify, Repeat](phases/07-transformers-deep-dive/16-speculative-decoding/docs/zh-CN.md) | [Speculative Decoding — Draft, Verify, Repeat](phases/07-transformers-deep-dive/16-speculative-decoding/) | 已完成 |

### Phase 8：生成式 AI

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [Generative Models：Taxonomy与History](phases/08-generative-ai/01-generative-models-taxonomy-history/docs/zh-CN.md) | [Generative Models — Taxonomy & History](phases/08-generative-ai/01-generative-models-taxonomy-history/) | 已完成 |
| 02 | [自编码器与Variational 自编码器 (VAE)](phases/08-generative-ai/02-autoencoders-vae/docs/zh-CN.md) | [Autoencoders & Variational Autoencoders (VAE)](phases/08-generative-ai/02-autoencoders-vae/) | 已完成 |
| 03 | [GAN：Generator vs Discriminator](phases/08-generative-ai/03-gans-generator-discriminator/docs/zh-CN.md) | [GANs — Generator vs Discriminator](phases/08-generative-ai/03-gans-generator-discriminator/) | 已完成 |
| 04 | [Conditional GAN与Pix2Pix](phases/08-generative-ai/04-conditional-gans-pix2pix/docs/zh-CN.md) | [Conditional GANs & Pix2Pix](phases/08-generative-ai/04-conditional-gans-pix2pix/) | 已完成 |
| 05 | [StyleGAN](phases/08-generative-ai/05-stylegan/docs/zh-CN.md) | [StyleGAN](phases/08-generative-ai/05-stylegan/) | 已完成 |
| 06 | [扩散模型：DDPM 从零实现](phases/08-generative-ai/06-diffusion-ddpm-from-scratch/docs/zh-CN.md) | [Diffusion Models — DDPM from Scratch](phases/08-generative-ai/06-diffusion-ddpm-from-scratch/) | 已完成 |
| 07 | [Latent 扩散与Stable 扩散](phases/08-generative-ai/07-latent-diffusion-stable-diffusion/docs/zh-CN.md) | [Latent Diffusion & Stable Diffusion](phases/08-generative-ai/07-latent-diffusion-stable-diffusion/) | 已完成 |
| 08 | [ControlNet, LoRA与Conditioning](phases/08-generative-ai/08-controlnet-lora-conditioning/docs/zh-CN.md) | [ControlNet, LoRA & Conditioning](phases/08-generative-ai/08-controlnet-lora-conditioning/) | 已完成 |
| 09 | [Inpainting, Outpainting与图像 Editing](phases/08-generative-ai/09-inpainting-outpainting-editing/docs/zh-CN.md) | [Inpainting, Outpainting & Image Editing](phases/08-generative-ai/09-inpainting-outpainting-editing/) | 已完成 |
| 10 | [视频 Generation](phases/08-generative-ai/10-video-generation/docs/zh-CN.md) | [Video Generation](phases/08-generative-ai/10-video-generation/) | 已完成 |
| 11 | [音频 Generation](phases/08-generative-ai/11-audio-generation/docs/zh-CN.md) | [Audio Generation](phases/08-generative-ai/11-audio-generation/) | 已完成 |
| 12 | [3D Generation](phases/08-generative-ai/12-3d-generation/docs/zh-CN.md) | [3D Generation](phases/08-generative-ai/12-3d-generation/) | 已完成 |
| 13 | [Flow Matching与Rectified Flows](phases/08-generative-ai/13-flow-matching-rectified-flows/docs/zh-CN.md) | [Flow Matching & Rectified Flows](phases/08-generative-ai/13-flow-matching-rectified-flows/) | 已完成 |
| 14 | [评估：FID, CLIP Score, Human Preference](phases/08-generative-ai/14-evaluation-fid-clip-score/docs/zh-CN.md) | [Evaluation — FID, CLIP Score, Human Preference](phases/08-generative-ai/14-evaluation-fid-clip-score/) | 已完成 |
| 19 | [Visual Autoregressive Modeling (VAR)：Next-Scale Prediction](phases/08-generative-ai/19-visual-autoregressive-var/docs/zh-CN.md) | [Visual Autoregressive Modeling (VAR): Next-Scale Prediction](phases/08-generative-ai/19-visual-autoregressive-var/) | 已完成 |

### Phase 9：强化学习

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [MDPs, States, Actions与Rewards](phases/09-reinforcement-learning/01-mdps-states-actions-rewards/docs/zh-CN.md) | [MDPs, States, Actions & Rewards](phases/09-reinforcement-learning/01-mdps-states-actions-rewards/) | 已完成 |
| 02 | [Dynamic Programming：Policy Iteration与Value Iteration](phases/09-reinforcement-learning/02-dynamic-programming/docs/zh-CN.md) | [Dynamic Programming — Policy Iteration & Value Iteration](phases/09-reinforcement-learning/02-dynamic-programming/) | 已完成 |
| 03 | [Monte Carlo Methods：Learning from Complete Episodes](phases/09-reinforcement-learning/03-monte-carlo-methods/docs/zh-CN.md) | [Monte Carlo Methods — Learning from Complete Episodes](phases/09-reinforcement-learning/03-monte-carlo-methods/) | 已完成 |
| 04 | [Temporal Difference：Q-Learning与SARSA](phases/09-reinforcement-learning/04-q-learning-sarsa/docs/zh-CN.md) | [Temporal Difference — Q-Learning & SARSA](phases/09-reinforcement-learning/04-q-learning-sarsa/) | 已完成 |
| 05 | [Deep Q-Networks (DQN)](phases/09-reinforcement-learning/05-dqn/docs/zh-CN.md) | [Deep Q-Networks (DQN)](phases/09-reinforcement-learning/05-dqn/) | 已完成 |
| 06 | [Policy Gradient：REINFORCE 从零实现](phases/09-reinforcement-learning/06-policy-gradients-reinforce/docs/zh-CN.md) | [Policy Gradient — REINFORCE from Scratch](phases/09-reinforcement-learning/06-policy-gradients-reinforce/) | 已完成 |
| 07 | [Actor-Critic：A2C与A3C](phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/docs/zh-CN.md) | [Actor-Critic — A2C and A3C](phases/09-reinforcement-learning/07-actor-critic-a2c-a3c/) | 已完成 |
| 08 | [Proximal Policy Optimization (PPO)](phases/09-reinforcement-learning/08-ppo/docs/zh-CN.md) | [Proximal Policy Optimization (PPO)](phases/09-reinforcement-learning/08-ppo/) | 已完成 |
| 09 | [奖励 Modeling与RLHF](phases/09-reinforcement-learning/09-reward-modeling-rlhf/docs/zh-CN.md) | [Reward Modeling & RLHF](phases/09-reinforcement-learning/09-reward-modeling-rlhf/) | 已完成 |
| 10 | [多智能体 RL](phases/09-reinforcement-learning/10-multi-agent-rl/docs/zh-CN.md) | [Multi-Agent RL](phases/09-reinforcement-learning/10-multi-agent-rl/) | 已完成 |
| 11 | [Sim-to-Real Transfer](phases/09-reinforcement-learning/11-sim-to-real-transfer/docs/zh-CN.md) | [Sim-to-Real Transfer](phases/09-reinforcement-learning/11-sim-to-real-transfer/) | 已完成 |
| 12 | [RL for Games：AlphaZero, MuZero,与the LLM-推理 Era](phases/09-reinforcement-learning/12-rl-for-games/docs/zh-CN.md) | [RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era](phases/09-reinforcement-learning/12-rl-for-games/) | 已完成 |

### Phase 10：从零构建 LLM

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [分词器：BPE, WordPiece, SentencePiece](phases/10-llms-from-scratch/01-tokenizers/docs/zh-CN.md) | [Tokenizers: BPE, WordPiece, SentencePiece](phases/10-llms-from-scratch/01-tokenizers/) | 已完成 |
| 02 | [Building a 分词器 从零实现](phases/10-llms-from-scratch/02-building-a-tokenizer/docs/zh-CN.md) | [Building a Tokenizer from Scratch](phases/10-llms-from-scratch/02-building-a-tokenizer/) | 已完成 |
| 03 | [数据 Pipelines for Pre-训练](phases/10-llms-from-scratch/03-data-pipelines/docs/zh-CN.md) | [Data Pipelines for Pre-Training](phases/10-llms-from-scratch/03-data-pipelines/) | 已完成 |
| 04 | [Pre-训练 a Mini GPT (124M Parameters)](phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/zh-CN.md) | [Pre-Training a Mini GPT (124M Parameters)](phases/10-llms-from-scratch/04-pre-training-mini-gpt/) | 已完成 |
| 05 | [扩展：Distributed 训练, FSDP, DeepSpeed](phases/10-llms-from-scratch/05-scaling-distributed/docs/zh-CN.md) | [Scaling: Distributed Training, FSDP, DeepSpeed](phases/10-llms-from-scratch/05-scaling-distributed/) | 已完成 |
| 06 | [Instruction Tuning (SFT)](phases/10-llms-from-scratch/06-instruction-tuning-sft/docs/zh-CN.md) | [Instruction Tuning (SFT)](phases/10-llms-from-scratch/06-instruction-tuning-sft/) | 已完成 |
| 07 | [RLHF：奖励 Model + PPO](phases/10-llms-from-scratch/07-rlhf/docs/zh-CN.md) | [RLHF: Reward Model + PPO](phases/10-llms-from-scratch/07-rlhf/) | 已完成 |
| 08 | [DPO：Direct Preference Optimization](phases/10-llms-from-scratch/08-dpo/docs/zh-CN.md) | [DPO: Direct Preference Optimization](phases/10-llms-from-scratch/08-dpo/) | 已完成 |
| 09 | [Constitutional AI与Self-Improvement](phases/10-llms-from-scratch/09-constitutional-ai-self-improvement/docs/zh-CN.md) | [Constitutional AI and Self-Improvement](phases/10-llms-from-scratch/09-constitutional-ai-self-improvement/) | 已完成 |
| 10 | [评估：基准, Evals, LM Harness](phases/10-llms-from-scratch/10-evaluation/docs/zh-CN.md) | [Evaluation: Benchmarks, Evals, LM Harness](phases/10-llms-from-scratch/10-evaluation/) | 已完成 |
| 11 | [量化：Making Models Fit](phases/10-llms-from-scratch/11-quantization/docs/zh-CN.md) | [Quantization: Making Models Fit](phases/10-llms-from-scratch/11-quantization/) | 已完成 |
| 12 | [推理 Optimization](phases/10-llms-from-scratch/12-inference-optimization/docs/zh-CN.md) | [Inference Optimization](phases/10-llms-from-scratch/12-inference-optimization/) | 已完成 |
| 13 | [Building a Complete LLM Pipeline](phases/10-llms-from-scratch/13-building-complete-llm-pipeline/docs/zh-CN.md) | [Building a Complete LLM Pipeline](phases/10-llms-from-scratch/13-building-complete-llm-pipeline/) | 已完成 |
| 14 | [Open Models：Architecture Walkthroughs](phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs/docs/zh-CN.md) | [Open Models: Architecture Walkthroughs](phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs/) | 已完成 |
| 15 | [Speculative Decoding与EAGLE-3](phases/10-llms-from-scratch/15-speculative-decoding-eagle3/docs/zh-CN.md) | [Speculative Decoding and EAGLE-3](phases/10-llms-from-scratch/15-speculative-decoding-eagle3/) | 已完成 |
| 16 | [Differential 注意力 (V2)](phases/10-llms-from-scratch/16-differential-attention-v2/docs/zh-CN.md) | [Differential Attention (V2)](phases/10-llms-from-scratch/16-differential-attention-v2/) | 已完成 |
| 17 | [Native Sparse 注意力 (DeepSeek NSA)](phases/10-llms-from-scratch/17-native-sparse-attention/docs/zh-CN.md) | [Native Sparse Attention (DeepSeek NSA)](phases/10-llms-from-scratch/17-native-sparse-attention/) | 已完成 |
| 18 | [Multi-Token Prediction (MTP)](phases/10-llms-from-scratch/18-multi-token-prediction/docs/zh-CN.md) | [Multi-Token Prediction (MTP)](phases/10-llms-from-scratch/18-multi-token-prediction/) | 已完成 |
| 19 | [DualPipe Parallelism](phases/10-llms-from-scratch/19-dualpipe-parallelism/docs/zh-CN.md) | [DualPipe Parallelism](phases/10-llms-from-scratch/19-dualpipe-parallelism/) | 已完成 |
| 20 | [DeepSeek-V3 Architecture Walkthrough](phases/10-llms-from-scratch/20-deepseek-v3-walkthrough/docs/zh-CN.md) | [DeepSeek-V3 Architecture Walkthrough](phases/10-llms-from-scratch/20-deepseek-v3-walkthrough/) | 已完成 |
| 21 | [Jamba：Hybrid SSM-Transformer](phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer/docs/zh-CN.md) | [Jamba — Hybrid SSM-Transformer](phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer/) | 已完成 |
| 22 | [Async与Hogwild! 推理](phases/10-llms-from-scratch/22-async-hogwild-inference/docs/zh-CN.md) | [Async and Hogwild! Inference](phases/10-llms-from-scratch/22-async-hogwild-inference/) | 已完成 |
| 25 | [Speculative Decoding与EAGLE](phases/10-llms-from-scratch/25-speculative-decoding/docs/zh-CN.md) | [Speculative Decoding and EAGLE](phases/10-llms-from-scratch/25-speculative-decoding/) | 已完成 |
| 34 | [Gradient Checkpointing与Activation Recomputation](phases/10-llms-from-scratch/34-gradient-checkpointing/docs/zh-CN.md) | [Gradient Checkpointing and Activation Recomputation](phases/10-llms-from-scratch/34-gradient-checkpointing/) | 已完成 |

### Phase 11：LLM 工程

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [提示工程：Techniques与Patterns](phases/11-llm-engineering/01-prompt-engineering/docs/zh-CN.md) | [Prompt Engineering: Techniques & Patterns](phases/11-llm-engineering/01-prompt-engineering/) | 已完成 |
| 02 | [Few-Shot, Chain-of-Thought, Tree-of-Thought](phases/11-llm-engineering/02-few-shot-cot/docs/zh-CN.md) | [Few-Shot, Chain-of-Thought, Tree-of-Thought](phases/11-llm-engineering/02-few-shot-cot/) | 已完成 |
| 03 | [结构化输出：JSON, Schema Validation, Constrained Decoding](phases/11-llm-engineering/03-structured-outputs/docs/zh-CN.md) | [Structured Outputs: JSON, Schema Validation, Constrained Decoding](phases/11-llm-engineering/03-structured-outputs/) | 已完成 |
| 04 | [嵌入与Vector Representations](phases/11-llm-engineering/04-embeddings/docs/zh-CN.md) | [Embeddings & Vector Representations](phases/11-llm-engineering/04-embeddings/) | 已完成 |
| 05 | [上下文工程：Windows, Budgets, 记忆,与检索](phases/11-llm-engineering/05-context-engineering/docs/zh-CN.md) | [Context Engineering: Windows, Budgets, Memory, and Retrieval](phases/11-llm-engineering/05-context-engineering/) | 已完成 |
| 06 | [RAG (检索-Augmented Generation)](phases/11-llm-engineering/06-rag/docs/zh-CN.md) | [RAG (Retrieval-Augmented Generation)](phases/11-llm-engineering/06-rag/) | 已完成 |
| 07 | [进阶 RAG (Chunking, Reranking, Hybrid 搜索)](phases/11-llm-engineering/07-advanced-rag/docs/zh-CN.md) | [Advanced RAG (Chunking, Reranking, Hybrid Search)](phases/11-llm-engineering/07-advanced-rag/) | 已完成 |
| 08 | [微调 with LoRA与QLoRA](phases/11-llm-engineering/08-fine-tuning-lora/docs/zh-CN.md) | [Fine-Tuning with LoRA & QLoRA](phases/11-llm-engineering/08-fine-tuning-lora/) | 已完成 |
| 09 | [函数调用与Tool Use](phases/11-llm-engineering/09-function-calling/docs/zh-CN.md) | [Function Calling & Tool Use](phases/11-llm-engineering/09-function-calling/) | 已完成 |
| 10 | [评估与Testing LLM Applications](phases/11-llm-engineering/10-evaluation/docs/zh-CN.md) | [Evaluation & Testing LLM Applications](phases/11-llm-engineering/10-evaluation/) | 已完成 |
| 11 | [缓存, Rate Limiting与Cost Optimization](phases/11-llm-engineering/11-caching-cost/docs/zh-CN.md) | [Caching, Rate Limiting & Cost Optimization](phases/11-llm-engineering/11-caching-cost/) | 已完成 |
| 12 | [Guardrails, 安全与Content Filtering](phases/11-llm-engineering/12-guardrails/docs/zh-CN.md) | [Guardrails, Safety & Content Filtering](phases/11-llm-engineering/12-guardrails/) | 已完成 |
| 13 | [Building a 生产 LLM Application](phases/11-llm-engineering/13-production-app/docs/zh-CN.md) | [Building a Production LLM Application](phases/11-llm-engineering/13-production-app/) | 已完成 |
| 14 | [模型上下文协议 (MCP)](phases/11-llm-engineering/14-model-context-protocol/docs/zh-CN.md) | [Model Context Protocol (MCP)](phases/11-llm-engineering/14-model-context-protocol/) | 已完成 |
| 15 | [Prompt 缓存与Context 缓存](phases/11-llm-engineering/15-prompt-caching/docs/zh-CN.md) | [Prompt Caching and Context Caching](phases/11-llm-engineering/15-prompt-caching/) | 已完成 |
| 16 | [LangGraph：State Machines for 智能体](phases/11-llm-engineering/16-langgraph-state-machines/docs/zh-CN.md) | [LangGraph — State Machines for Agents](phases/11-llm-engineering/16-langgraph-state-machines/) | 已完成 |
| 17 | [智能体 框架 Tradeoffs：LangGraph vs CrewAI vs AutoGen vs Agno](phases/11-llm-engineering/17-agent-framework-tradeoffs/docs/zh-CN.md) | [Agent Framework Tradeoffs — LangGraph vs CrewAI vs AutoGen vs Agno](phases/11-llm-engineering/17-agent-framework-tradeoffs/) | 已完成 |

### Phase 12：多模态 AI

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [视觉 Transformer与the Patch-Token Primitive](phases/12-multimodal-ai/01-vision-transformer-patch-tokens/docs/zh-CN.md) | [Vision Transformers and the Patch-Token Primitive](phases/12-multimodal-ai/01-vision-transformer-patch-tokens/) | 已完成 |
| 02 | [CLIP与Contrastive 视觉-Language Pretraining](phases/12-multimodal-ai/02-clip-contrastive-pretraining/docs/zh-CN.md) | [CLIP and Contrastive Vision-Language Pretraining](phases/12-multimodal-ai/02-clip-contrastive-pretraining/) | 已完成 |
| 03 | [From CLIP to BLIP-2：Q-Former as Modality Bridge](phases/12-multimodal-ai/03-blip2-qformer-bridge/docs/zh-CN.md) | [From CLIP to BLIP-2 — Q-Former as Modality Bridge](phases/12-multimodal-ai/03-blip2-qformer-bridge/) | 已完成 |
| 04 | [Flamingo与Gated Cross-注意力 for Few-Shot VLMs](phases/12-multimodal-ai/04-flamingo-gated-cross-attention/docs/zh-CN.md) | [Flamingo and Gated Cross-Attention for Few-Shot VLMs](phases/12-multimodal-ai/04-flamingo-gated-cross-attention/) | 已完成 |
| 05 | [LLaVA与Visual Instruction Tuning](phases/12-multimodal-ai/05-llava-visual-instruction-tuning/docs/zh-CN.md) | [LLaVA and Visual Instruction Tuning](phases/12-multimodal-ai/05-llava-visual-instruction-tuning/) | 已完成 |
| 06 | [Any-Resolution 视觉：Patch-n'-Pack与NaFlex](phases/12-multimodal-ai/06-any-resolution-patch-n-pack/docs/zh-CN.md) | [Any-Resolution Vision: Patch-n'-Pack and NaFlex](phases/12-multimodal-ai/06-any-resolution-patch-n-pack/) | 已完成 |
| 07 | [Open-Weight VLM Recipes：What Actually Matters](phases/12-multimodal-ai/07-open-weight-vlm-recipes/docs/zh-CN.md) | [Open-Weight VLM Recipes: What Actually Matters](phases/12-multimodal-ai/07-open-weight-vlm-recipes/) | 已完成 |
| 08 | [LLaVA-OneVision：Single-图像, Multi-图像, 视频 in One Model](phases/12-multimodal-ai/08-llava-onevision-single-multi-video/docs/zh-CN.md) | [LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model](phases/12-multimodal-ai/08-llava-onevision-single-multi-video/) | 已完成 |
| 09 | [Qwen-VL Family与Dynamic-FPS 视频](phases/12-multimodal-ai/09-qwen-vl-family-dynamic-fps/docs/zh-CN.md) | [Qwen-VL Family and Dynamic-FPS Video](phases/12-multimodal-ai/09-qwen-vl-family-dynamic-fps/) | 已完成 |
| 10 | [InternVL3：Native 多模态 Pretraining](phases/12-multimodal-ai/10-internvl3-native-multimodal/docs/zh-CN.md) | [InternVL3: Native Multimodal Pretraining](phases/12-multimodal-ai/10-internvl3-native-multimodal/) | 已完成 |
| 11 | [Chameleon与Early-Fusion Token-Only 多模态 Models](phases/12-multimodal-ai/11-chameleon-early-fusion-tokens/docs/zh-CN.md) | [Chameleon and Early-Fusion Token-Only Multimodal Models](phases/12-multimodal-ai/11-chameleon-early-fusion-tokens/) | 已完成 |
| 12 | [Emu3：Next-Token Prediction for 图像与视频 Generation](phases/12-multimodal-ai/12-emu3-next-token-for-generation/docs/zh-CN.md) | [Emu3: Next-Token Prediction for Image and Video Generation](phases/12-multimodal-ai/12-emu3-next-token-for-generation/) | 已完成 |
| 13 | [Transfusion：Autoregressive Text + 扩散 图像 in One Transformer](phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion/docs/zh-CN.md) | [Transfusion: Autoregressive Text + Diffusion Image in One Transformer](phases/12-multimodal-ai/13-transfusion-autoregressive-diffusion/) | 已完成 |
| 14 | [Show-o与Discrete-扩散 Unified Models](phases/12-multimodal-ai/14-show-o-discrete-diffusion-unified/docs/zh-CN.md) | [Show-o and Discrete-Diffusion Unified Models](phases/12-multimodal-ai/14-show-o-discrete-diffusion-unified/) | 已完成 |
| 15 | [Janus-Pro：Decoupled Encoders for Unified 多模态 Models](phases/12-multimodal-ai/15-janus-pro-decoupled-encoders/docs/zh-CN.md) | [Janus-Pro: Decoupled Encoders for Unified Multimodal Models](phases/12-multimodal-ai/15-janus-pro-decoupled-encoders/) | 已完成 |
| 16 | [MIO与Any-to-Any Streaming 多模态 Models](phases/12-multimodal-ai/16-mio-any-to-any-streaming/docs/zh-CN.md) | [MIO and Any-to-Any Streaming Multimodal Models](phases/12-multimodal-ai/16-mio-any-to-any-streaming/) | 已完成 |
| 17 | [视频-语言模型：Temporal Tokens与Grounding](phases/12-multimodal-ai/17-video-language-temporal-grounding/docs/zh-CN.md) | [Video-Language Models: Temporal Tokens and Grounding](phases/12-multimodal-ai/17-video-language-temporal-grounding/) | 已完成 |
| 18 | [Long-视频 Understanding at Million-Token Context](phases/12-multimodal-ai/18-long-video-million-token/docs/zh-CN.md) | [Long-Video Understanding at Million-Token Context](phases/12-multimodal-ai/18-long-video-million-token/) | 已完成 |
| 19 | [音频-语言模型：the Whisper to 音频 Flamingo 3 Arc](phases/12-multimodal-ai/19-audio-language-whisper-to-af3/docs/zh-CN.md) | [Audio-Language Models: the Whisper to Audio Flamingo 3 Arc](phases/12-multimodal-ai/19-audio-language-whisper-to-af3/) | 已完成 |
| 20 | [Omni Models：Qwen2.5-Omni与the Thinker-Talker Split](phases/12-multimodal-ai/20-omni-models-thinker-talker/docs/zh-CN.md) | [Omni Models: Qwen2.5-Omni and the Thinker-Talker Split](phases/12-multimodal-ai/20-omni-models-thinker-talker/) | 已完成 |
| 21 | [Embodied VLAs：RT-2, OpenVLA, π0, GR00T](phases/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot/docs/zh-CN.md) | [Embodied VLAs: RT-2, OpenVLA, π0, GR00T](phases/12-multimodal-ai/21-embodied-vlas-openvla-pi0-groot/) | 已完成 |
| 22 | [Document与Diagram Understanding](phases/12-multimodal-ai/22-document-diagram-understanding/docs/zh-CN.md) | [Document and Diagram Understanding](phases/12-multimodal-ai/22-document-diagram-understanding/) | 已完成 |
| 23 | [ColPali与视觉-Native Document RAG](phases/12-multimodal-ai/23-colpali-vision-native-rag/docs/zh-CN.md) | [ColPali and Vision-Native Document RAG](phases/12-multimodal-ai/23-colpali-vision-native-rag/) | 已完成 |
| 24 | [多模态 RAG与Cross-Modal 检索](phases/12-multimodal-ai/24-multimodal-rag-cross-modal/docs/zh-CN.md) | [Multimodal RAG and Cross-Modal Retrieval](phases/12-multimodal-ai/24-multimodal-rag-cross-modal/) | 已完成 |
| 25 | [多模态 智能体与Computer-Use (毕业项目)](phases/12-multimodal-ai/25-multimodal-agents-computer-use/docs/zh-CN.md) | [Multimodal Agents and Computer-Use (Capstone)](phases/12-multimodal-ai/25-multimodal-agents-computer-use/) | 已完成 |

### Phase 13：工具与协议

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [The Tool Interface：Why 智能体 Need Structured I/O](phases/13-tools-and-protocols/01-the-tool-interface/docs/zh-CN.md) | [The Tool Interface — Why Agents Need Structured I/O](phases/13-tools-and-protocols/01-the-tool-interface/) | 已完成 |
| 02 | [函数调用 深入解析：OpenAI, Anthropic, Gemini](phases/13-tools-and-protocols/02-function-calling-deep-dive/docs/zh-CN.md) | [Function Calling Deep Dive — OpenAI, Anthropic, Gemini](phases/13-tools-and-protocols/02-function-calling-deep-dive/) | 已完成 |
| 03 | [Parallel Tool Calls与Streaming with 工具](phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls/docs/zh-CN.md) | [Parallel Tool Calls and Streaming with Tools](phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls/) | 已完成 |
| 04 | [Structured Output：JSON Schema, Pydantic, Zod, Constrained Decoding](phases/13-tools-and-protocols/04-structured-output/docs/zh-CN.md) | [Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding](phases/13-tools-and-protocols/04-structured-output/) | 已完成 |
| 05 | [Tool Schema Design：Naming, Descriptions, Parameter Constraints](phases/13-tools-and-protocols/05-tool-schema-design/docs/zh-CN.md) | [Tool Schema Design — Naming, Descriptions, Parameter Constraints](phases/13-tools-and-protocols/05-tool-schema-design/) | 已完成 |
| 06 | [MCP 基础：Primitives, Lifecycle, JSON-RPC Base](phases/13-tools-and-protocols/06-mcp-fundamentals/docs/zh-CN.md) | [MCP Fundamentals — Primitives, Lifecycle, JSON-RPC Base](phases/13-tools-and-protocols/06-mcp-fundamentals/) | 已完成 |
| 07 | [Building an MCP Server：Python + TypeScript SDKs](phases/13-tools-and-protocols/07-building-an-mcp-server/docs/zh-CN.md) | [Building an MCP Server — Python + TypeScript SDKs](phases/13-tools-and-protocols/07-building-an-mcp-server/) | 已完成 |
| 08 | [Building an MCP Client：Discovery, Invocation, Session Management](phases/13-tools-and-protocols/08-building-an-mcp-client/docs/zh-CN.md) | [Building an MCP Client — Discovery, Invocation, Session Management](phases/13-tools-and-protocols/08-building-an-mcp-client/) | 已完成 |
| 09 | [MCP Transports：stdio vs Streamable HTTP vs SSE Migration](phases/13-tools-and-protocols/09-mcp-transports/docs/zh-CN.md) | [MCP Transports — stdio vs Streamable HTTP vs SSE Migration](phases/13-tools-and-protocols/09-mcp-transports/) | 已完成 |
| 10 | [MCP Resources与Prompts：Context Exposure Beyond 工具](phases/13-tools-and-protocols/10-mcp-resources-and-prompts/docs/zh-CN.md) | [MCP Resources and Prompts — Context Exposure Beyond Tools](phases/13-tools-and-protocols/10-mcp-resources-and-prompts/) | 已完成 |
| 11 | [MCP Sampling：Server-Requested LLM Completions与智能体 Loops](phases/13-tools-and-protocols/11-mcp-sampling/docs/zh-CN.md) | [MCP Sampling — Server-Requested LLM Completions and Agent Loops](phases/13-tools-and-protocols/11-mcp-sampling/) | 已完成 |
| 12 | [Roots与Elicitation：Scoping与Mid-Flight User Input](phases/13-tools-and-protocols/12-mcp-roots-and-elicitation/docs/zh-CN.md) | [Roots and Elicitation — Scoping and Mid-Flight User Input](phases/13-tools-and-protocols/12-mcp-roots-and-elicitation/) | 已完成 |
| 13 | [Async Tasks (SEP-1686)：Call-Now, Fetch-Later for Long-Running Work](phases/13-tools-and-protocols/13-mcp-async-tasks/docs/zh-CN.md) | [Async Tasks (SEP-1686) — Call-Now, Fetch-Later for Long-Running Work](phases/13-tools-and-protocols/13-mcp-async-tasks/) | 已完成 |
| 14 | [MCP Apps：Interactive UI Resources via `ui://`](phases/13-tools-and-protocols/14-mcp-apps/docs/zh-CN.md) | [MCP Apps — Interactive UI Resources via `ui://`](phases/13-tools-and-protocols/14-mcp-apps/) | 已完成 |
| 15 | [MCP 安全 I：Tool Poisoning, Rug Pulls, Cross-Server Shadowing](phases/13-tools-and-protocols/15-mcp-security-tool-poisoning/docs/zh-CN.md) | [MCP Security I — Tool Poisoning, Rug Pulls, Cross-Server Shadowing](phases/13-tools-and-protocols/15-mcp-security-tool-poisoning/) | 已完成 |
| 16 | [MCP 安全 II：OAuth 2.1, Resource Indicators, Incremental Scopes](phases/13-tools-and-protocols/16-mcp-security-oauth-2-1/docs/zh-CN.md) | [MCP Security II — OAuth 2.1, Resource Indicators, Incremental Scopes](phases/13-tools-and-protocols/16-mcp-security-oauth-2-1/) | 已完成 |
| 17 | [MCP 网关与Registries：Enterprise Control Planes](phases/13-tools-and-protocols/17-mcp-gateways-and-registries/docs/zh-CN.md) | [MCP Gateways and Registries — Enterprise Control Planes](phases/13-tools-and-protocols/17-mcp-gateways-and-registries/) | 已完成 |
| 18 | [MCP Auth in 生产：Enrollment, JWKS Refresh, Audience-Pinned Tokens](phases/13-tools-and-protocols/18-mcp-auth-production/docs/zh-CN.md) | [MCP Auth in Production — Enrollment, JWKS Refresh, Audience-Pinned Tokens](phases/13-tools-and-protocols/18-mcp-auth-production/) | 已完成 |
| 19 | [A2A：智能体-to-智能体 协议](phases/13-tools-and-protocols/19-a2a-protocol/docs/zh-CN.md) | [A2A — Agent-to-Agent Protocol](phases/13-tools-and-protocols/19-a2a-protocol/) | 已完成 |
| 20 | [OpenTelemetry GenAI：Tracing Tool Calls End-to-End](phases/13-tools-and-protocols/20-opentelemetry-genai/docs/zh-CN.md) | [OpenTelemetry GenAI — Tracing Tool Calls End-to-End](phases/13-tools-and-protocols/20-opentelemetry-genai/) | 已完成 |
| 21 | [LLM 路由 Layer：LiteLLM, OpenRouter, Portkey](phases/13-tools-and-protocols/21-llm-routing-layer/docs/zh-CN.md) | [LLM Routing Layer — LiteLLM, OpenRouter, Portkey](phases/13-tools-and-protocols/21-llm-routing-layer/) | 已完成 |
| 22 | [Skills与智能体 SDKs：Anthropic Skills, AGENTS.md, OpenAI Apps SDK](phases/13-tools-and-protocols/22-skills-and-agent-sdks/docs/zh-CN.md) | [Skills and Agent SDKs — Anthropic Skills, AGENTS.md, OpenAI Apps SDK](phases/13-tools-and-protocols/22-skills-and-agent-sdks/) | 已完成 |
| 23 | [毕业项目：Build a Complete Tool Ecosystem](phases/13-tools-and-protocols/23-capstone-tool-ecosystem/docs/zh-CN.md) | [Capstone — Build a Complete Tool Ecosystem](phases/13-tools-and-protocols/23-capstone-tool-ecosystem/) | 已完成 |

### Phase 14：智能体工程

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [The 智能体 Loop：Observe, Think, Act](phases/14-agent-engineering/01-the-agent-loop/docs/zh-CN.md) | [The Agent Loop: Observe, Think, Act](phases/14-agent-engineering/01-the-agent-loop/) | 已完成 |
| 02 | [ReWOO与Plan-and-Execute：Decoupled 规划](phases/14-agent-engineering/02-rewoo-plan-and-execute/docs/zh-CN.md) | [ReWOO and Plan-and-Execute: Decoupled Planning](phases/14-agent-engineering/02-rewoo-plan-and-execute/) | 已完成 |
| 03 | [Reflexion：Verbal 强化学习](phases/14-agent-engineering/03-reflexion-verbal-rl/docs/zh-CN.md) | [Reflexion: Verbal Reinforcement Learning](phases/14-agent-engineering/03-reflexion-verbal-rl/) | 已完成 |
| 04 | [Tree of Thoughts与LATS：Deliberate 搜索](phases/14-agent-engineering/04-tree-of-thoughts-lats/docs/zh-CN.md) | [Tree of Thoughts and LATS: Deliberate Search](phases/14-agent-engineering/04-tree-of-thoughts-lats/) | 已完成 |
| 05 | [Self-Refine与CRITIC：Iterative Output Improvement](phases/14-agent-engineering/05-self-refine-and-critic/docs/zh-CN.md) | [Self-Refine and CRITIC: Iterative Output Improvement](phases/14-agent-engineering/05-self-refine-and-critic/) | 已完成 |
| 06 | [Tool Use与函数调用](phases/14-agent-engineering/06-tool-use-and-function-calling/docs/zh-CN.md) | [Tool Use and Function Calling](phases/14-agent-engineering/06-tool-use-and-function-calling/) | 已完成 |
| 07 | [记忆：Virtual Context与MemGPT](phases/14-agent-engineering/07-memory-virtual-context-memgpt/docs/zh-CN.md) | [Memory: Virtual Context and MemGPT](phases/14-agent-engineering/07-memory-virtual-context-memgpt/) | 已完成 |
| 08 | [记忆 Blocks与Sleep-Time Compute (Letta)](phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/zh-CN.md) | [Memory Blocks and Sleep-Time Compute (Letta)](phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/) | 已完成 |
| 09 | [Hybrid 记忆：Vector + Graph + KV (Mem0)](phases/14-agent-engineering/09-hybrid-memory-mem0/docs/zh-CN.md) | [Hybrid Memory: Vector + Graph + KV (Mem0)](phases/14-agent-engineering/09-hybrid-memory-mem0/) | 已完成 |
| 10 | [Skill Libraries与Lifelong Learning (Voyager)](phases/14-agent-engineering/10-skill-libraries-voyager/docs/zh-CN.md) | [Skill Libraries and Lifelong Learning (Voyager)](phases/14-agent-engineering/10-skill-libraries-voyager/) | 已完成 |
| 11 | [规划 with HTN与Evolutionary 搜索](phases/14-agent-engineering/11-planning-htn-and-evolutionary/docs/zh-CN.md) | [Planning with HTN and Evolutionary Search](phases/14-agent-engineering/11-planning-htn-and-evolutionary/) | 已完成 |
| 12 | [Anthropic's Workflow Patterns：Simple Over Complex](phases/14-agent-engineering/12-anthropic-workflow-patterns/docs/zh-CN.md) | [Anthropic's Workflow Patterns: Simple Over Complex](phases/14-agent-engineering/12-anthropic-workflow-patterns/) | 已完成 |
| 13 | [LangGraph：Stateful Graphs与Durable Execution](phases/14-agent-engineering/13-langgraph-stateful-graphs/docs/zh-CN.md) | [LangGraph: Stateful Graphs and Durable Execution](phases/14-agent-engineering/13-langgraph-stateful-graphs/) | 已完成 |
| 14 | [AutoGen v0.4：Actor Model与智能体 框架](phases/14-agent-engineering/14-autogen-actor-model/docs/zh-CN.md) | [AutoGen v0.4: Actor Model and Agent Framework](phases/14-agent-engineering/14-autogen-actor-model/) | 已完成 |
| 15 | [CrewAI：Role-Based Crews与Flows](phases/14-agent-engineering/15-crewai-role-based-crews/docs/zh-CN.md) | [CrewAI: Role-Based Crews and Flows](phases/14-agent-engineering/15-crewai-role-based-crews/) | 已完成 |
| 16 | [OpenAI 智能体 SDK：Handoffs, Guardrails, Tracing](phases/14-agent-engineering/16-openai-agents-sdk/docs/zh-CN.md) | [OpenAI Agents SDK: Handoffs, Guardrails, Tracing](phases/14-agent-engineering/16-openai-agents-sdk/) | 已完成 |
| 17 | [Claude 智能体 SDK：Subagents与Session Store](phases/14-agent-engineering/17-claude-agent-sdk/docs/zh-CN.md) | [Claude Agent SDK: Subagents and Session Store](phases/14-agent-engineering/17-claude-agent-sdk/) | 已完成 |
| 18 | [Agno与Mastra：生产 Runtimes](phases/14-agent-engineering/18-agno-and-mastra-runtimes/docs/zh-CN.md) | [Agno and Mastra: Production Runtimes](phases/14-agent-engineering/18-agno-and-mastra-runtimes/) | 已完成 |
| 19 | [基准：SWE-bench, GAIA, AgentBench](phases/14-agent-engineering/19-benchmarks-swebench-gaia/docs/zh-CN.md) | [Benchmarks: SWE-bench, GAIA, AgentBench](phases/14-agent-engineering/19-benchmarks-swebench-gaia/) | 已完成 |
| 20 | [基准：WebArena与OSWorld](phases/14-agent-engineering/20-benchmarks-webarena-osworld/docs/zh-CN.md) | [Benchmarks: WebArena and OSWorld](phases/14-agent-engineering/20-benchmarks-webarena-osworld/) | 已完成 |
| 21 | [计算机使用：Claude, OpenAI CUA, Gemini](phases/14-agent-engineering/21-computer-use-agents/docs/zh-CN.md) | [Computer Use: Claude, OpenAI CUA, Gemini](phases/14-agent-engineering/21-computer-use-agents/) | 已完成 |
| 22 | [语音 智能体：Pipecat与LiveKit](phases/14-agent-engineering/22-voice-agents-pipecat-livekit/docs/zh-CN.md) | [Voice Agents: Pipecat and LiveKit](phases/14-agent-engineering/22-voice-agents-pipecat-livekit/) | 已完成 |
| 23 | [OpenTelemetry GenAI Semantic Conventions](phases/14-agent-engineering/23-otel-genai-conventions/docs/zh-CN.md) | [OpenTelemetry GenAI Semantic Conventions](phases/14-agent-engineering/23-otel-genai-conventions/) | 已完成 |
| 24 | [智能体 可观测性：Langfuse, Phoenix, Opik](phases/14-agent-engineering/24-agent-observability-platforms/docs/zh-CN.md) | [Agent Observability: Langfuse, Phoenix, Opik](phases/14-agent-engineering/24-agent-observability-platforms/) | 已完成 |
| 25 | [多智能体 Debate与Collaboration](phases/14-agent-engineering/25-multi-agent-debate/docs/zh-CN.md) | [Multi-Agent Debate and Collaboration](phases/14-agent-engineering/25-multi-agent-debate/) | 已完成 |
| 26 | [Failure Modes：Why 智能体 Break](phases/14-agent-engineering/26-failure-modes-agentic/docs/zh-CN.md) | [Failure Modes: Why Agents Break](phases/14-agent-engineering/26-failure-modes-agentic/) | 已完成 |
| 27 | [提示注入与the PVE Defense](phases/14-agent-engineering/27-prompt-injection-defense/docs/zh-CN.md) | [Prompt Injection and the PVE Defense](phases/14-agent-engineering/27-prompt-injection-defense/) | 已完成 |
| 28 | [Orchestration Patterns：Supervisor, Swarm, Hierarchical](phases/14-agent-engineering/28-orchestration-patterns/docs/zh-CN.md) | [Orchestration Patterns: Supervisor, Swarm, Hierarchical](phases/14-agent-engineering/28-orchestration-patterns/) | 已完成 |
| 29 | [生产 Runtimes：Queue, Event, Cron](phases/14-agent-engineering/29-production-runtimes/docs/zh-CN.md) | [Production Runtimes: Queue, Event, Cron](phases/14-agent-engineering/29-production-runtimes/) | 已完成 |
| 30 | [评估-Driven 智能体 Development](phases/14-agent-engineering/30-eval-driven-agent-development/docs/zh-CN.md) | [Eval-Driven Agent Development](phases/14-agent-engineering/30-eval-driven-agent-development/) | 已完成 |
| 31 | [智能体 Workbench 工程：Why Capable Models Still Fail](phases/14-agent-engineering/31-agent-workbench-why-models-fail/docs/zh-CN.md) | [Agent Workbench Engineering: Why Capable Models Still Fail](phases/14-agent-engineering/31-agent-workbench-why-models-fail/) | 已完成 |
| 32 | [The Minimal 智能体 Workbench](phases/14-agent-engineering/32-minimal-agent-workbench/docs/zh-CN.md) | [The Minimal Agent Workbench](phases/14-agent-engineering/32-minimal-agent-workbench/) | 已完成 |
| 33 | [智能体 Instructions as Executable Constraints](phases/14-agent-engineering/33-instructions-as-executable-constraints/docs/zh-CN.md) | [Agent Instructions as Executable Constraints](phases/14-agent-engineering/33-instructions-as-executable-constraints/) | 已完成 |
| 34 | [Repo 记忆与Durable State](phases/14-agent-engineering/34-repo-memory-and-state/docs/zh-CN.md) | [Repo Memory and Durable State](phases/14-agent-engineering/34-repo-memory-and-state/) | 已完成 |
| 35 | [Initialization Scripts for 智能体](phases/14-agent-engineering/35-initialization-scripts/docs/zh-CN.md) | [Initialization Scripts for Agents](phases/14-agent-engineering/35-initialization-scripts/) | 已完成 |
| 36 | [Scope Contracts与Task Boundaries](phases/14-agent-engineering/36-scope-contracts/docs/zh-CN.md) | [Scope Contracts and Task Boundaries](phases/14-agent-engineering/36-scope-contracts/) | 已完成 |
| 37 | [Runtime Feedback Loops](phases/14-agent-engineering/37-runtime-feedback-loops/docs/zh-CN.md) | [Runtime Feedback Loops](phases/14-agent-engineering/37-runtime-feedback-loops/) | 已完成 |
| 38 | [Verification Gates](phases/14-agent-engineering/38-verification-gates/docs/zh-CN.md) | [Verification Gates](phases/14-agent-engineering/38-verification-gates/) | 已完成 |
| 39 | [Reviewer 智能体：Separate Builder from Marker](phases/14-agent-engineering/39-reviewer-agent/docs/zh-CN.md) | [Reviewer Agent: Separate Builder from Marker](phases/14-agent-engineering/39-reviewer-agent/) | 已完成 |
| 40 | [Multi-Session Handoff](phases/14-agent-engineering/40-multi-session-handoff/docs/zh-CN.md) | [Multi-Session Handoff](phases/14-agent-engineering/40-multi-session-handoff/) | 已完成 |
| 41 | [The Workbench on a Real Repo](phases/14-agent-engineering/41-workbench-for-real-repos/docs/zh-CN.md) | [The Workbench on a Real Repo](phases/14-agent-engineering/41-workbench-for-real-repos/) | 已完成 |
| 42 | [毕业项目：Ship a Reusable 智能体 Workbench Pack](phases/14-agent-engineering/42-agent-workbench-capstone/docs/zh-CN.md) | [Capstone: Ship a Reusable Agent Workbench Pack](phases/14-agent-engineering/42-agent-workbench-capstone/) | 已完成 |

### Phase 15：自主系统

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [The Shift from Chatbots to Long-Horizon 智能体](phases/15-autonomous-systems/01-long-horizon-agents/docs/zh-CN.md) | [The Shift from Chatbots to Long-Horizon Agents](phases/15-autonomous-systems/01-long-horizon-agents/) | 已完成 |
| 02 | [STaR, V-STaR, Quiet-STaR：Self-Taught 推理](phases/15-autonomous-systems/02-star-family-reasoning/docs/zh-CN.md) | [STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning](phases/15-autonomous-systems/02-star-family-reasoning/) | 已完成 |
| 03 | [AlphaEvolve：Evolutionary Coding 智能体](phases/15-autonomous-systems/03-alphaevolve-evolutionary-coding/docs/zh-CN.md) | [AlphaEvolve — Evolutionary Coding Agents](phases/15-autonomous-systems/03-alphaevolve-evolutionary-coding/) | 已完成 |
| 04 | [Darwin Godel Machine：Open-Ended Self-Modifying 智能体](phases/15-autonomous-systems/04-darwin-godel-machine/docs/zh-CN.md) | [Darwin Godel Machine — Open-Ended Self-Modifying Agents](phases/15-autonomous-systems/04-darwin-godel-machine/) | 已完成 |
| 05 | [AI Scientist v2：Workshop-Level 自主 Research](phases/15-autonomous-systems/05-ai-scientist-v2/docs/zh-CN.md) | [AI Scientist v2 — Workshop-Level Autonomous Research](phases/15-autonomous-systems/05-ai-scientist-v2/) | 已完成 |
| 06 | [Automated 对齐 Research (Anthropic AAR)](phases/15-autonomous-systems/06-automated-alignment-research/docs/zh-CN.md) | [Automated Alignment Research (Anthropic AAR)](phases/15-autonomous-systems/06-automated-alignment-research/) | 已完成 |
| 07 | [Recursive Self-Improvement：Capability vs 对齐](phases/15-autonomous-systems/07-recursive-self-improvement/docs/zh-CN.md) | [Recursive Self-Improvement — Capability vs Alignment](phases/15-autonomous-systems/07-recursive-self-improvement/) | 已完成 |
| 08 | [Bounded Self-Improvement Designs](phases/15-autonomous-systems/08-bounded-self-improvement/docs/zh-CN.md) | [Bounded Self-Improvement Designs](phases/15-autonomous-systems/08-bounded-self-improvement/) | 已完成 |
| 09 | [The 自主 Coding 智能体 Landscape (2026)](phases/15-autonomous-systems/09-coding-agent-landscape/docs/zh-CN.md) | [The Autonomous Coding Agent Landscape (2026)](phases/15-autonomous-systems/09-coding-agent-landscape/) | 已完成 |
| 10 | [Claude Code as an 自主 智能体：Permission Modes与Auto Mode](phases/15-autonomous-systems/10-claude-code-permission-modes/docs/zh-CN.md) | [Claude Code as an Autonomous Agent: Permission Modes and Auto Mode](phases/15-autonomous-systems/10-claude-code-permission-modes/) | 已完成 |
| 11 | [Browser 智能体与Long-Horizon Web Tasks](phases/15-autonomous-systems/11-browser-agents/docs/zh-CN.md) | [Browser Agents and Long-Horizon Web Tasks](phases/15-autonomous-systems/11-browser-agents/) | 已完成 |
| 12 | [Long-Running Background 智能体：Durable Execution](phases/15-autonomous-systems/12-durable-execution/docs/zh-CN.md) | [Long-Running Background Agents: Durable Execution](phases/15-autonomous-systems/12-durable-execution/) | 已完成 |
| 13 | [Action Budgets, Iteration Caps,与Cost Governors](phases/15-autonomous-systems/13-cost-governors/docs/zh-CN.md) | [Action Budgets, Iteration Caps, and Cost Governors](phases/15-autonomous-systems/13-cost-governors/) | 已完成 |
| 14 | [Kill Switches, Circuit Breakers,与Canary Tokens](phases/15-autonomous-systems/14-kill-switches-canaries/docs/zh-CN.md) | [Kill Switches, Circuit Breakers, and Canary Tokens](phases/15-autonomous-systems/14-kill-switches-canaries/) | 已完成 |
| 15 | [Human-in-the-Loop：Propose-Then-Commit](phases/15-autonomous-systems/15-propose-then-commit/docs/zh-CN.md) | [Human-in-the-Loop: Propose-Then-Commit](phases/15-autonomous-systems/15-propose-then-commit/) | 已完成 |
| 16 | [Checkpoints与Rollback](phases/15-autonomous-systems/16-checkpoints-rollback/docs/zh-CN.md) | [Checkpoints and Rollback](phases/15-autonomous-systems/16-checkpoints-rollback/) | 已完成 |
| 17 | [Constitutional AI与Rule Overrides](phases/15-autonomous-systems/17-constitutional-ai/docs/zh-CN.md) | [Constitutional AI and Rule Overrides](phases/15-autonomous-systems/17-constitutional-ai/) | 已完成 |
| 18 | [Llama Guard与Input/Output Classification](phases/15-autonomous-systems/18-llama-guard/docs/zh-CN.md) | [Llama Guard and Input/Output Classification](phases/15-autonomous-systems/18-llama-guard/) | 已完成 |
| 19 | [Anthropic Responsible 扩展 Policy v3.0](phases/15-autonomous-systems/19-anthropic-rsp/docs/zh-CN.md) | [Anthropic Responsible Scaling Policy v3.0](phases/15-autonomous-systems/19-anthropic-rsp/) | 已完成 |
| 20 | [OpenAI Preparedness 框架与DeepMind Frontier 安全 框架](phases/15-autonomous-systems/20-openai-preparedness-deepmind-fsf/docs/zh-CN.md) | [OpenAI Preparedness Framework and DeepMind Frontier Safety Framework](phases/15-autonomous-systems/20-openai-preparedness-deepmind-fsf/) | 已完成 |
| 21 | [METR Time Horizons与External Capability 评估](phases/15-autonomous-systems/21-metr-external-evaluation/docs/zh-CN.md) | [METR Time Horizons and External Capability Evaluation](phases/15-autonomous-systems/21-metr-external-evaluation/) | 已完成 |
| 22 | [CAIS, CAISI,与Societal-Scale Risk](phases/15-autonomous-systems/22-cais-caisi-societal-risk/docs/zh-CN.md) | [CAIS, CAISI, and Societal-Scale Risk](phases/15-autonomous-systems/22-cais-caisi-societal-risk/) | 已完成 |

### Phase 16：多智能体与群体智能

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [Why 多智能体?](phases/16-multi-agent-and-swarms/01-why-multi-agent/docs/zh-CN.md) | [Why Multi-Agent?](phases/16-multi-agent-and-swarms/01-why-multi-agent/) | 已完成 |
| 02 | [Heritage of FIPA-ACL与语音 Acts](phases/16-multi-agent-and-swarms/02-fipa-acl-heritage/docs/zh-CN.md) | [Heritage of FIPA-ACL and Speech Acts](phases/16-multi-agent-and-swarms/02-fipa-acl-heritage/) | 已完成 |
| 03 | [Communication 协议](phases/16-multi-agent-and-swarms/03-communication-protocols/docs/zh-CN.md) | [Communication Protocols](phases/16-multi-agent-and-swarms/03-communication-protocols/) | 已完成 |
| 04 | [The 多智能体 Primitive Model](phases/16-multi-agent-and-swarms/04-primitive-model/docs/zh-CN.md) | [The Multi-Agent Primitive Model](phases/16-multi-agent-and-swarms/04-primitive-model/) | 已完成 |
| 05 | [Supervisor / Orchestrator-Worker Pattern](phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/docs/zh-CN.md) | [Supervisor / Orchestrator-Worker Pattern](phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/) | 已完成 |
| 06 | [Hierarchical Architecture与Its Failure Mode](phases/16-multi-agent-and-swarms/06-hierarchical-architecture/docs/zh-CN.md) | [Hierarchical Architecture and Its Failure Mode](phases/16-multi-agent-and-swarms/06-hierarchical-architecture/) | 已完成 |
| 07 | [Society of Mind与多智能体 Debate](phases/16-multi-agent-and-swarms/07-society-of-mind-debate/docs/zh-CN.md) | [Society of Mind and Multi-Agent Debate](phases/16-multi-agent-and-swarms/07-society-of-mind-debate/) | 已完成 |
| 08 | [Role Specialization：Planner, Critic, Executor, Verifier](phases/16-multi-agent-and-swarms/08-role-specialization/docs/zh-CN.md) | [Role Specialization — Planner, Critic, Executor, Verifier](phases/16-multi-agent-and-swarms/08-role-specialization/) | 已完成 |
| 09 | [Parallel / Swarm / Networked Architectures](phases/16-multi-agent-and-swarms/09-parallel-swarm-networks/docs/zh-CN.md) | [Parallel / Swarm / Networked Architectures](phases/16-multi-agent-and-swarms/09-parallel-swarm-networks/) | 已完成 |
| 10 | [Group Chat与Speaker Selection](phases/16-multi-agent-and-swarms/10-group-chat-speaker-selection/docs/zh-CN.md) | [Group Chat and Speaker Selection](phases/16-multi-agent-and-swarms/10-group-chat-speaker-selection/) | 已完成 |
| 11 | [Handoffs与Routines：Stateless Orchestration](phases/16-multi-agent-and-swarms/11-handoffs-and-routines/docs/zh-CN.md) | [Handoffs and Routines — Stateless Orchestration](phases/16-multi-agent-and-swarms/11-handoffs-and-routines/) | 已完成 |
| 12 | [A2A：The 智能体-to-智能体 协议](phases/16-multi-agent-and-swarms/12-a2a-protocol/docs/zh-CN.md) | [A2A — The Agent-to-Agent Protocol](phases/16-multi-agent-and-swarms/12-a2a-protocol/) | 已完成 |
| 13 | [Shared 记忆与Blackboard Patterns](phases/16-multi-agent-and-swarms/13-shared-memory-blackboard/docs/zh-CN.md) | [Shared Memory and Blackboard Patterns](phases/16-multi-agent-and-swarms/13-shared-memory-blackboard/) | 已完成 |
| 14 | [Consensus与Byzantine Fault Tolerance for 智能体](phases/16-multi-agent-and-swarms/14-consensus-and-bft/docs/zh-CN.md) | [Consensus and Byzantine Fault Tolerance for Agents](phases/16-multi-agent-and-swarms/14-consensus-and-bft/) | 已完成 |
| 15 | [Voting, Self-Consistency,与Debate Topology](phases/16-multi-agent-and-swarms/15-voting-debate-topology/docs/zh-CN.md) | [Voting, Self-Consistency, and Debate Topology](phases/16-multi-agent-and-swarms/15-voting-debate-topology/) | 已完成 |
| 16 | [Negotiation与Bargaining](phases/16-multi-agent-and-swarms/16-negotiation-bargaining/docs/zh-CN.md) | [Negotiation and Bargaining](phases/16-multi-agent-and-swarms/16-negotiation-bargaining/) | 已完成 |
| 17 | [Generative 智能体与Emergent Simulation](phases/16-multi-agent-and-swarms/17-generative-agents-simulation/docs/zh-CN.md) | [Generative Agents and Emergent Simulation](phases/16-multi-agent-and-swarms/17-generative-agents-simulation/) | 已完成 |
| 18 | [Theory of Mind与Emergent Coordination](phases/16-multi-agent-and-swarms/18-theory-of-mind-coordination/docs/zh-CN.md) | [Theory of Mind and Emergent Coordination](phases/16-multi-agent-and-swarms/18-theory-of-mind-coordination/) | 已完成 |
| 19 | [Swarm Optimization for LLM (PSO, ACO)](phases/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco/docs/zh-CN.md) | [Swarm Optimization for LLMs (PSO, ACO)](phases/16-multi-agent-and-swarms/19-swarm-optimization-pso-aco/) | 已完成 |
| 20 | [MARL：MADDPG, QMIX, MAPPO](phases/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo/docs/zh-CN.md) | [MARL — MADDPG, QMIX, MAPPO](phases/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo/) | 已完成 |
| 21 | [智能体 Economies, Token Incentives, Reputation](phases/16-multi-agent-and-swarms/21-agent-economies/docs/zh-CN.md) | [Agent Economies, Token Incentives, Reputation](phases/16-multi-agent-and-swarms/21-agent-economies/) | 已完成 |
| 22 | [生产 扩展：Queues, Checkpoints, Durability](phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints/docs/zh-CN.md) | [Production Scaling — Queues, Checkpoints, Durability](phases/16-multi-agent-and-swarms/22-production-scaling-queues-checkpoints/) | 已完成 |
| 23 | [Failure Modes：MAST, Groupthink, Monoculture, Cascading Errors](phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink/docs/zh-CN.md) | [Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors](phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink/) | 已完成 |
| 24 | [评估与Coordination 基准](phases/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks/docs/zh-CN.md) | [Evaluation and Coordination Benchmarks](phases/16-multi-agent-and-swarms/24-evaluation-coordination-benchmarks/) | 已完成 |
| 25 | [Case Studies与the 2026 State of the Art](phases/16-multi-agent-and-swarms/25-case-studies-2026-sota/docs/zh-CN.md) | [Case Studies and the 2026 State of the Art](phases/16-multi-agent-and-swarms/25-case-studies-2026-sota/) | 已完成 |

### Phase 17：基础设施与生产部署

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [Managed LLM Platforms：Bedrock, Vertex AI, Azure OpenAI](phases/17-infrastructure-and-production/01-managed-llm-platforms/docs/zh-CN.md) | [Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI](phases/17-infrastructure-and-production/01-managed-llm-platforms/) | 已完成 |
| 02 | [推理 Platform Economics：Fireworks, Together, Baseten, Modal, Replicate, Anyscale](phases/17-infrastructure-and-production/02-inference-platform-economics/docs/zh-CN.md) | [Inference Platform Economics — Fireworks, Together, Baseten, Modal, Replicate, Anyscale](phases/17-infrastructure-and-production/02-inference-platform-economics/) | 已完成 |
| 03 | [GPU Autoscaling on Kubernetes：Karpenter, KAI Scheduler, Gang Scheduling](phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes/docs/zh-CN.md) | [GPU Autoscaling on Kubernetes — Karpenter, KAI Scheduler, Gang Scheduling](phases/17-infrastructure-and-production/03-gpu-autoscaling-kubernetes/) | 已完成 |
| 04 | [vLLM 服务部署 Internals：PagedAttention, Continuous Batching, Chunked Prefill](phases/17-infrastructure-and-production/04-vllm-serving-internals/docs/zh-CN.md) | [vLLM Serving Internals: PagedAttention, Continuous Batching, Chunked Prefill](phases/17-infrastructure-and-production/04-vllm-serving-internals/) | 已完成 |
| 05 | [EAGLE-3 Speculative Decoding in 生产](phases/17-infrastructure-and-production/05-eagle3-speculative-decoding/docs/zh-CN.md) | [EAGLE-3 Speculative Decoding in Production](phases/17-infrastructure-and-production/05-eagle3-speculative-decoding/) | 已完成 |
| 06 | [SGLang与RadixAttention for Prefix-Heavy Workloads](phases/17-infrastructure-and-production/06-sglang-radixattention/docs/zh-CN.md) | [SGLang and RadixAttention for Prefix-Heavy Workloads](phases/17-infrastructure-and-production/06-sglang-radixattention/) | 已完成 |
| 07 | [TensorRT-LLM on Blackwell with FP8与NVFP4](phases/17-infrastructure-and-production/07-tensorrt-llm-blackwell/docs/zh-CN.md) | [TensorRT-LLM on Blackwell with FP8 and NVFP4](phases/17-infrastructure-and-production/07-tensorrt-llm-blackwell/) | 已完成 |
| 08 | [推理 指标：TTFT, TPOT, ITL, Goodput, P99](phases/17-infrastructure-and-production/08-inference-metrics-goodput/docs/zh-CN.md) | [Inference Metrics — TTFT, TPOT, ITL, Goodput, P99](phases/17-infrastructure-and-production/08-inference-metrics-goodput/) | 已完成 |
| 09 | [生产 量化：AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4](phases/17-infrastructure-and-production/09-production-quantization/docs/zh-CN.md) | [Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4](phases/17-infrastructure-and-production/09-production-quantization/) | 已完成 |
| 10 | [Cold Start Mitigation for Serverless LLM](phases/17-infrastructure-and-production/10-cold-start-mitigation/docs/zh-CN.md) | [Cold Start Mitigation for Serverless LLMs](phases/17-infrastructure-and-production/10-cold-start-mitigation/) | 已完成 |
| 11 | [Multi-Region LLM 服务部署与KV 缓存 Locality](phases/17-infrastructure-and-production/11-multi-region-kv-locality/docs/zh-CN.md) | [Multi-Region LLM Serving and KV Cache Locality](phases/17-infrastructure-and-production/11-multi-region-kv-locality/) | 已完成 |
| 12 | [Edge 推理：Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson](phases/17-infrastructure-and-production/12-edge-inference/docs/zh-CN.md) | [Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson](phases/17-infrastructure-and-production/12-edge-inference/) | 已完成 |
| 13 | [LLM 可观测性 Stack Selection](phases/17-infrastructure-and-production/13-llm-observability/docs/zh-CN.md) | [LLM Observability Stack Selection](phases/17-infrastructure-and-production/13-llm-observability/) | 已完成 |
| 14 | [Prompt 缓存与Semantic 缓存 Economics](phases/17-infrastructure-and-production/14-prompt-semantic-caching/docs/zh-CN.md) | [Prompt Caching and Semantic Caching Economics](phases/17-infrastructure-and-production/14-prompt-semantic-caching/) | 已完成 |
| 15 | [Batch API：the 50% Discount as Industry Standard](phases/17-infrastructure-and-production/15-batch-apis/docs/zh-CN.md) | [Batch APIs — the 50% Discount as Industry Standard](phases/17-infrastructure-and-production/15-batch-apis/) | 已完成 |
| 16 | [Model 路由 as a Cost-Reduction Primitive](phases/17-infrastructure-and-production/16-model-routing/docs/zh-CN.md) | [Model Routing as a Cost-Reduction Primitive](phases/17-infrastructure-and-production/16-model-routing/) | 已完成 |
| 17 | [Disaggregated Prefill/Decode：NVIDIA Dynamo与llm-d](phases/17-infrastructure-and-production/17-disaggregated-prefill-decode/docs/zh-CN.md) | [Disaggregated Prefill/Decode — NVIDIA Dynamo and llm-d](phases/17-infrastructure-and-production/17-disaggregated-prefill-decode/) | 已完成 |
| 18 | [vLLM 生产 Stack with LMCache KV Offloading](phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache/docs/zh-CN.md) | [vLLM Production Stack with LMCache KV Offloading](phases/17-infrastructure-and-production/18-vllm-production-stack-lmcache/) | 已完成 |
| 19 | [AI 网关：LiteLLM, Portkey, Kong AI 网关, Bifrost](phases/17-infrastructure-and-production/19-ai-gateways/docs/zh-CN.md) | [AI Gateways — LiteLLM, Portkey, Kong AI Gateway, Bifrost](phases/17-infrastructure-and-production/19-ai-gateways/) | 已完成 |
| 20 | [Shadow Traffic, Canary Rollout,与Progressive Deployment for LLM](phases/17-infrastructure-and-production/20-shadow-canary-progressive/docs/zh-CN.md) | [Shadow Traffic, Canary Rollout, and Progressive Deployment for LLMs](phases/17-infrastructure-and-production/20-shadow-canary-progressive/) | 已完成 |
| 21 | [A/B Testing LLM Features：GrowthBook, Statsig,与the Vibes Problem](phases/17-infrastructure-and-production/21-ab-testing-llm-features/docs/zh-CN.md) | [A/B Testing LLM Features — GrowthBook, Statsig, and the Vibes Problem](phases/17-infrastructure-and-production/21-ab-testing-llm-features/) | 已完成 |
| 22 | [Load Testing LLM API：Why k6与Locust Lie](phases/17-infrastructure-and-production/22-load-testing-llm-apis/docs/zh-CN.md) | [Load Testing LLM APIs — Why k6 and Locust Lie](phases/17-infrastructure-and-production/22-load-testing-llm-apis/) | 已完成 |
| 23 | [SRE for AI：多智能体 Incident Response, Runbooks, Predictive Detection](phases/17-infrastructure-and-production/23-sre-for-ai/docs/zh-CN.md) | [SRE for AI — Multi-Agent Incident Response, Runbooks, Predictive Detection](phases/17-infrastructure-and-production/23-sre-for-ai/) | 已完成 |
| 24 | [Chaos 工程 for LLM 生产](phases/17-infrastructure-and-production/24-chaos-engineering-llm/docs/zh-CN.md) | [Chaos Engineering for LLM Production](phases/17-infrastructure-and-production/24-chaos-engineering-llm/) | 已完成 |
| 25 | [安全：Secrets, API Key Rotation, Audit Logs, Guardrails](phases/17-infrastructure-and-production/25-security-secrets-audit/docs/zh-CN.md) | [Security — Secrets, API Key Rotation, Audit Logs, Guardrails](phases/17-infrastructure-and-production/25-security-secrets-audit/) | 已完成 |
| 26 | [合规：SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001](phases/17-infrastructure-and-production/26-compliance-frameworks/docs/zh-CN.md) | [Compliance — SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, ISO 42001](phases/17-infrastructure-and-production/26-compliance-frameworks/) | 已完成 |
| 27 | [FinOps for LLM：Unit Economics与Multi-Tenant Attribution](phases/17-infrastructure-and-production/27-finops-llms/docs/zh-CN.md) | [FinOps for LLMs — Unit Economics and Multi-Tenant Attribution](phases/17-infrastructure-and-production/27-finops-llms/) | 已完成 |
| 28 | [Self-Hosted 服务部署 Selection：llama.cpp, Ollama, TGI, vLLM, SGLang](phases/17-infrastructure-and-production/28-self-hosted-serving-selection/docs/zh-CN.md) | [Self-Hosted Serving Selection — llama.cpp, Ollama, TGI, vLLM, SGLang](phases/17-infrastructure-and-production/28-self-hosted-serving-selection/) | 已完成 |

### Phase 18：伦理、安全与对齐

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [Instruction-Following as 对齐 Signal](phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal/docs/zh-CN.md) | [Instruction-Following as Alignment Signal](phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal/) | 已完成 |
| 02 | [奖励 Hacking与Goodhart's Law](phases/18-ethics-safety-alignment/02-reward-hacking-goodhart/docs/zh-CN.md) | [Reward Hacking and Goodhart's Law](phases/18-ethics-safety-alignment/02-reward-hacking-goodhart/) | 已完成 |
| 03 | [The Direct Preference Optimization Family](phases/18-ethics-safety-alignment/03-direct-preference-optimization-family/docs/zh-CN.md) | [The Direct Preference Optimization Family](phases/18-ethics-safety-alignment/03-direct-preference-optimization-family/) | 已完成 |
| 04 | [Sycophancy as RLHF Amplification](phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification/docs/zh-CN.md) | [Sycophancy as RLHF Amplification](phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification/) | 已完成 |
| 05 | [Constitutional AI与RLAIF](phases/18-ethics-safety-alignment/05-constitutional-ai-rlaif/docs/zh-CN.md) | [Constitutional AI and RLAIF](phases/18-ethics-safety-alignment/05-constitutional-ai-rlaif/) | 已完成 |
| 06 | [Mesa-Optimization与Deceptive 对齐](phases/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment/docs/zh-CN.md) | [Mesa-Optimization and Deceptive Alignment](phases/18-ethics-safety-alignment/06-mesa-optimization-deceptive-alignment/) | 已完成 |
| 07 | [Sleeper 智能体：Persistent Deception](phases/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception/docs/zh-CN.md) | [Sleeper Agents — Persistent Deception](phases/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception/) | 已完成 |
| 08 | [In-Context Scheming in Frontier Models](phases/18-ethics-safety-alignment/08-in-context-scheming-frontier-models/docs/zh-CN.md) | [In-Context Scheming in Frontier Models](phases/18-ethics-safety-alignment/08-in-context-scheming-frontier-models/) | 已完成 |
| 09 | [对齐 Faking](phases/18-ethics-safety-alignment/09-alignment-faking/docs/zh-CN.md) | [Alignment Faking](phases/18-ethics-safety-alignment/09-alignment-faking/) | 已完成 |
| 10 | [AI Control：安全 Despite Subversion](phases/18-ethics-safety-alignment/10-ai-control-subversion/docs/zh-CN.md) | [AI Control — Safety Despite Subversion](phases/18-ethics-safety-alignment/10-ai-control-subversion/) | 已完成 |
| 11 | [Scalable Oversight与Weak-to-Strong Generalization](phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong/docs/zh-CN.md) | [Scalable Oversight and Weak-to-Strong Generalization](phases/18-ethics-safety-alignment/11-scalable-oversight-weak-to-strong/) | 已完成 |
| 12 | [Red-Teaming：PAIR与Automated Attacks](phases/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks/docs/zh-CN.md) | [Red-Teaming: PAIR and Automated Attacks](phases/18-ethics-safety-alignment/12-red-teaming-pair-automated-attacks/) | 已完成 |
| 13 | [Many-Shot 越狱](phases/18-ethics-safety-alignment/13-many-shot-jailbreaking/docs/zh-CN.md) | [Many-Shot Jailbreaking](phases/18-ethics-safety-alignment/13-many-shot-jailbreaking/) | 已完成 |
| 14 | [ASCII Art与Visual Jailbreaks](phases/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks/docs/zh-CN.md) | [ASCII Art and Visual Jailbreaks](phases/18-ethics-safety-alignment/14-ascii-art-visual-jailbreaks/) | 已完成 |
| 15 | [Indirect 提示注入：生产 Attack Surface](phases/18-ethics-safety-alignment/15-indirect-prompt-injection/docs/zh-CN.md) | [Indirect Prompt Injection — Production Attack Surface](phases/18-ethics-safety-alignment/15-indirect-prompt-injection/) | 已完成 |
| 16 | [Red-Team Tooling：Garak, Llama Guard, PyRIT](phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit/docs/zh-CN.md) | [Red-Team Tooling — Garak, Llama Guard, PyRIT](phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit/) | 已完成 |
| 17 | [WMDP与Dual-Use Capability 评估](phases/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation/docs/zh-CN.md) | [WMDP and Dual-Use Capability Evaluation](phases/18-ethics-safety-alignment/17-wmdp-dual-use-evaluation/) | 已完成 |
| 18 | [Frontier 安全 框架：RSP, PF, FSF](phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf/docs/zh-CN.md) | [Frontier Safety Frameworks — RSP, PF, FSF](phases/18-ethics-safety-alignment/18-frontier-safety-frameworks-rsp-pf-fsf/) | 已完成 |
| 19 | [Anthropic's Model Welfare Program](phases/18-ethics-safety-alignment/19-model-welfare-research/docs/zh-CN.md) | [Anthropic's Model Welfare Program](phases/18-ethics-safety-alignment/19-model-welfare-research/) | 已完成 |
| 20 | [偏见与Representational Harm in LLM](phases/18-ethics-safety-alignment/20-bias-representational-harm/docs/zh-CN.md) | [Bias and Representational Harm in LLMs](phases/18-ethics-safety-alignment/20-bias-representational-harm/) | 已完成 |
| 21 | [公平性 Criteria：Group, Individual, Counterfactual](phases/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual/docs/zh-CN.md) | [Fairness Criteria — Group, Individual, Counterfactual](phases/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual/) | 已完成 |
| 22 | [Differential 隐私 for LLM](phases/18-ethics-safety-alignment/22-differential-privacy-for-llms/docs/zh-CN.md) | [Differential Privacy for LLMs](phases/18-ethics-safety-alignment/22-differential-privacy-for-llms/) | 已完成 |
| 23 | [水印：SynthID, Stable Signature, C2PA](phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/docs/zh-CN.md) | [Watermarking — SynthID, Stable Signature, C2PA](phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/) | 已完成 |
| 24 | [Regulatory 框架：EU, US, UK, Korea](phases/18-ethics-safety-alignment/24-regulatory-frameworks-eu-us-uk-korea/docs/zh-CN.md) | [Regulatory Frameworks — EU, US, UK, Korea](phases/18-ethics-safety-alignment/24-regulatory-frameworks-eu-us-uk-korea/) | 已完成 |
| 25 | [EchoLeak与the Emergence of CVEs for AI](phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai/docs/zh-CN.md) | [EchoLeak and the Emergence of CVEs for AI](phases/18-ethics-safety-alignment/25-echoleak-cves-for-ai/) | 已完成 |
| 26 | [Model, 系统,与数据集 Cards](phases/18-ethics-safety-alignment/26-model-system-dataset-cards/docs/zh-CN.md) | [Model, System, and Dataset Cards](phases/18-ethics-safety-alignment/26-model-system-dataset-cards/) | 已完成 |
| 27 | [数据 Provenance与训练-数据 治理](phases/18-ethics-safety-alignment/27-data-provenance-training-governance/docs/zh-CN.md) | [Data Provenance and Training-Data Governance](phases/18-ethics-safety-alignment/27-data-provenance-training-governance/) | 已完成 |
| 28 | [对齐 Research Ecosystem：MATS, Redwood, Apollo, METR](phases/18-ethics-safety-alignment/28-alignment-research-ecosystem/docs/zh-CN.md) | [Alignment Research Ecosystem — MATS, Redwood, Apollo, METR](phases/18-ethics-safety-alignment/28-alignment-research-ecosystem/) | 已完成 |
| 29 | [内容审核 系统：OpenAI, Perspective, Llama Guard](phases/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard/docs/zh-CN.md) | [Moderation Systems — OpenAI, Perspective, Llama Guard](phases/18-ethics-safety-alignment/29-moderation-systems-openai-perspective-llamaguard/) | 已完成 |
| 30 | [Dual-Use Risk：Cyber, Bio, Chem, Nuclear Uplift](phases/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear/docs/zh-CN.md) | [Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift](phases/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear/) | 已完成 |

### Phase 19：毕业项目

| # | 中文入口 | 英文课程目录 | 状态 |
|:---:|---|---|---|
| 01 | [毕业项目 01：Terminal-Native Coding 智能体](phases/19-capstone-projects/01-terminal-native-coding-agent/docs/zh-CN.md) | [Capstone 01 — Terminal-Native Coding Agent](phases/19-capstone-projects/01-terminal-native-coding-agent/) | 已完成 |
| 02 | [毕业项目 02：RAG over Codebase (Cross-Repo Semantic 搜索)](phases/19-capstone-projects/02-rag-over-codebase/docs/zh-CN.md) | [Capstone 02 — RAG over Codebase (Cross-Repo Semantic Search)](phases/19-capstone-projects/02-rag-over-codebase/) | 已完成 |
| 03 | [毕业项目 03：Real-Time 语音 Assistant (ASR to LLM to TTS)](phases/19-capstone-projects/03-realtime-voice-assistant/docs/zh-CN.md) | [Capstone 03 — Real-Time Voice Assistant (ASR to LLM to TTS)](phases/19-capstone-projects/03-realtime-voice-assistant/) | 已完成 |
| 04 | [毕业项目 04：多模态 Document QA (视觉-First PDF, Tables, Charts)](phases/19-capstone-projects/04-multimodal-document-qa/docs/zh-CN.md) | [Capstone 04 — Multimodal Document QA (Vision-First PDF, Tables, Charts)](phases/19-capstone-projects/04-multimodal-document-qa/) | 已完成 |
| 05 | [毕业项目 05：自主 Research 智能体 (AI-Scientist Class)](phases/19-capstone-projects/05-autonomous-research-agent/docs/zh-CN.md) | [Capstone 05 — Autonomous Research Agent (AI-Scientist Class)](phases/19-capstone-projects/05-autonomous-research-agent/) | 已完成 |
| 06 | [毕业项目 06：DevOps Troubleshooting 智能体 for Kubernetes](phases/19-capstone-projects/06-devops-troubleshooting-agent/docs/zh-CN.md) | [Capstone 06 — DevOps Troubleshooting Agent for Kubernetes](phases/19-capstone-projects/06-devops-troubleshooting-agent/) | 已完成 |
| 07 | [毕业项目 07：End-to-End 微调 Pipeline (数据 to SFT to DPO to Serve)](phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline/docs/zh-CN.md) | [Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)](phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline/) | 已完成 |
| 08 | [毕业项目 08：生产 RAG Chatbot for a Regulated Vertical](phases/19-capstone-projects/08-production-rag-chatbot/docs/zh-CN.md) | [Capstone 08 — Production RAG Chatbot for a Regulated Vertical](phases/19-capstone-projects/08-production-rag-chatbot/) | 已完成 |
| 09 | [毕业项目 09：Code Migration 智能体 (Repo-Level Language / Runtime Upgrade)](phases/19-capstone-projects/09-code-migration-agent/docs/zh-CN.md) | [Capstone 09 — Code Migration Agent (Repo-Level Language / Runtime Upgrade)](phases/19-capstone-projects/09-code-migration-agent/) | 已完成 |
| 10 | [毕业项目 10：多智能体 Software 工程 Team](phases/19-capstone-projects/10-multi-agent-software-team/docs/zh-CN.md) | [Capstone 10 — Multi-Agent Software Engineering Team](phases/19-capstone-projects/10-multi-agent-software-team/) | 已完成 |
| 11 | [毕业项目 11：LLM 可观测性与评估 Dashboard](phases/19-capstone-projects/11-llm-observability-dashboard/docs/zh-CN.md) | [Capstone 11 — LLM Observability & Eval Dashboard](phases/19-capstone-projects/11-llm-observability-dashboard/) | 已完成 |
| 12 | [毕业项目 12：视频 Understanding Pipeline (Scene, QA, 搜索)](phases/19-capstone-projects/12-video-understanding-pipeline/docs/zh-CN.md) | [Capstone 12 — Video Understanding Pipeline (Scene, QA, Search)](phases/19-capstone-projects/12-video-understanding-pipeline/) | 已完成 |
| 13 | [毕业项目 13：MCP Server with Registry与治理](phases/19-capstone-projects/13-mcp-server-with-registry/docs/zh-CN.md) | [Capstone 13 — MCP Server with Registry and Governance](phases/19-capstone-projects/13-mcp-server-with-registry/) | 已完成 |
| 14 | [毕业项目 14：Speculative-Decoding 推理 Server](phases/19-capstone-projects/14-speculative-decoding-server/docs/zh-CN.md) | [Capstone 14 — Speculative-Decoding Inference Server](phases/19-capstone-projects/14-speculative-decoding-server/) | 已完成 |
| 15 | [毕业项目 15：Constitutional 安全 Harness + Red-Team Range](phases/19-capstone-projects/15-constitutional-safety-harness/docs/zh-CN.md) | [Capstone 15 — Constitutional Safety Harness + Red-Team Range](phases/19-capstone-projects/15-constitutional-safety-harness/) | 已完成 |
| 16 | [毕业项目 16：GitHub Issue-to-PR 自主 智能体](phases/19-capstone-projects/16-github-issue-to-pr-agent/docs/zh-CN.md) | [Capstone 16 — GitHub Issue-to-PR Autonomous Agent](phases/19-capstone-projects/16-github-issue-to-pr-agent/) | 已完成 |
| 17 | [毕业项目 17：Personal AI Tutor (Adaptive, 多模态, with 记忆)](phases/19-capstone-projects/17-personal-ai-tutor/docs/zh-CN.md) | [Capstone 17 — Personal AI Tutor (Adaptive, Multimodal, with Memory)](phases/19-capstone-projects/17-personal-ai-tutor/) | 已完成 |
| 20 | [智能体 Harness Loop Contract](phases/19-capstone-projects/20-agent-harness-loop-contract/docs/zh-CN.md) | [Agent Harness Loop Contract](phases/19-capstone-projects/20-agent-harness-loop-contract/) | 已完成 |
| 21 | [Tool Registry with Schema Validation](phases/19-capstone-projects/21-tool-registry-schema-validation/docs/zh-CN.md) | [Tool Registry with Schema Validation](phases/19-capstone-projects/21-tool-registry-schema-validation/) | 已完成 |
| 22 | [JSON-RPC 2.0 Over Newline-Delimited Stdio](phases/19-capstone-projects/22-jsonrpc-stdio-transport/docs/zh-CN.md) | [JSON-RPC 2.0 Over Newline-Delimited Stdio](phases/19-capstone-projects/22-jsonrpc-stdio-transport/) | 已完成 |
| 23 | [Function Call Dispatcher](phases/19-capstone-projects/23-function-call-dispatcher/docs/zh-CN.md) | [Function Call Dispatcher](phases/19-capstone-projects/23-function-call-dispatcher/) | 已完成 |
| 24 | [Plan-Execute Control Flow](phases/19-capstone-projects/24-plan-execute-control-flow/docs/zh-CN.md) | [Plan-Execute Control Flow](phases/19-capstone-projects/24-plan-execute-control-flow/) | 已完成 |
| 25 | [毕业项目 Lesson 25：Verification Gates与the Observation Budget](phases/19-capstone-projects/25-verification-gates-observation-budget/docs/zh-CN.md) | [Capstone Lesson 25: Verification Gates and the Observation Budget](phases/19-capstone-projects/25-verification-gates-observation-budget/) | 已完成 |
| 26 | [毕业项目 Lesson 26：Sandbox Runner with Denylist与Path Jail](phases/19-capstone-projects/26-sandbox-runner-denylist/docs/zh-CN.md) | [Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail](phases/19-capstone-projects/26-sandbox-runner-denylist/) | 已完成 |
| 27 | [毕业项目 Lesson 27：评估 Harness with Fixture Tasks](phases/19-capstone-projects/27-eval-harness-fixture-tasks/docs/zh-CN.md) | [Capstone Lesson 27: Eval Harness with Fixture Tasks](phases/19-capstone-projects/27-eval-harness-fixture-tasks/) | 已完成 |
| 28 | [毕业项目 Lesson 28：可观测性 with OTel GenAI Spans与Prometheus 指标](phases/19-capstone-projects/28-observability-otel-traces/docs/zh-CN.md) | [Capstone Lesson 28: Observability with OTel GenAI Spans and Prometheus Metrics](phases/19-capstone-projects/28-observability-otel-traces/) | 已完成 |
| 29 | [毕业项目 Lesson 29：End-to-End Coding 智能体 on the Harness](phases/19-capstone-projects/29-end-to-end-coding-task-demo/docs/zh-CN.md) | [Capstone Lesson 29: End-to-End Coding Agent on the Harness](phases/19-capstone-projects/29-end-to-end-coding-task-demo/) | 已完成 |
| 30 | [BPE 分词器 从零实现](phases/19-capstone-projects/30-bpe-tokenizer-from-scratch/docs/zh-CN.md) | [BPE Tokenizer From Scratch](phases/19-capstone-projects/30-bpe-tokenizer-from-scratch/) | 已完成 |
| 31 | [Tokenized 数据集 with Sliding Window](phases/19-capstone-projects/31-tokenized-dataset-sliding-window/docs/zh-CN.md) | [Tokenized Dataset with Sliding Window](phases/19-capstone-projects/31-tokenized-dataset-sliding-window/) | 已完成 |
| 32 | [Token与Positional 嵌入](phases/19-capstone-projects/32-token-positional-embeddings/docs/zh-CN.md) | [Token and Positional Embeddings](phases/19-capstone-projects/32-token-positional-embeddings/) | 已完成 |
| 33 | [Multi-Head Self-注意力](phases/19-capstone-projects/33-multihead-self-attention/docs/zh-CN.md) | [Multi-Head Self-Attention](phases/19-capstone-projects/33-multihead-self-attention/) | 已完成 |
| 34 | [Transformer Block 从零实现](phases/19-capstone-projects/34-transformer-block/docs/zh-CN.md) | [Transformer Block from Scratch](phases/19-capstone-projects/34-transformer-block/) | 已完成 |
| 35 | [GPT Model Assembly](phases/19-capstone-projects/35-gpt-model-assembly/docs/zh-CN.md) | [GPT Model Assembly](phases/19-capstone-projects/35-gpt-model-assembly/) | 已完成 |
| 36 | [训练 Loop与评估](phases/19-capstone-projects/36-training-loop-eval/docs/zh-CN.md) | [Training Loop and Evaluation](phases/19-capstone-projects/36-training-loop-eval/) | 已完成 |
| 37 | [Loading Pretrained Weights](phases/19-capstone-projects/37-loading-pretrained-weights/docs/zh-CN.md) | [Loading Pretrained Weights](phases/19-capstone-projects/37-loading-pretrained-weights/) | 已完成 |
| 38 | [毕业项目 Lesson 38：分类器 微调 by Head Swap](phases/19-capstone-projects/38-classifier-finetuning/docs/zh-CN.md) | [Capstone Lesson 38: Classifier Fine-Tuning by Head Swap](phases/19-capstone-projects/38-classifier-finetuning/) | 已完成 |
| 39 | [毕业项目 Lesson 39：Instruction Tuning by Supervised 微调](phases/19-capstone-projects/39-instruction-tuning-sft/docs/zh-CN.md) | [Capstone Lesson 39: Instruction Tuning by Supervised Fine-Tuning](phases/19-capstone-projects/39-instruction-tuning-sft/) | 已完成 |
| 40 | [毕业项目 Lesson 40：Direct Preference Optimization 从零实现](phases/19-capstone-projects/40-dpo-from-scratch/docs/zh-CN.md) | [Capstone Lesson 40: Direct Preference Optimization from Scratch](phases/19-capstone-projects/40-dpo-from-scratch/) | 已完成 |
| 41 | [毕业项目 Lesson 41：Full 评估 Pipeline](phases/19-capstone-projects/41-eval-pipeline/docs/zh-CN.md) | [Capstone Lesson 41: Full Evaluation Pipeline](phases/19-capstone-projects/41-eval-pipeline/) | 已完成 |
| 42 | [Large Corpus Downloader](phases/19-capstone-projects/42-large-corpus-downloader/docs/zh-CN.md) | [Large Corpus Downloader](phases/19-capstone-projects/42-large-corpus-downloader/) | 已完成 |
| 43 | [HDF5 Tokenized Corpus](phases/19-capstone-projects/43-hdf5-tokenized-corpus/docs/zh-CN.md) | [HDF5 Tokenized Corpus](phases/19-capstone-projects/43-hdf5-tokenized-corpus/) | 已完成 |
| 44 | [Cosine LR with Linear Warmup](phases/19-capstone-projects/44-cosine-lr-warmup/docs/zh-CN.md) | [Cosine LR with Linear Warmup](phases/19-capstone-projects/44-cosine-lr-warmup/) | 已完成 |
| 45 | [Gradient Clipping与Mixed Precision](phases/19-capstone-projects/45-gradient-clipping-amp/docs/zh-CN.md) | [Gradient Clipping and Mixed Precision](phases/19-capstone-projects/45-gradient-clipping-amp/) | 已完成 |
| 46 | [Gradient Accumulation](phases/19-capstone-projects/46-gradient-accumulation/docs/zh-CN.md) | [Gradient Accumulation](phases/19-capstone-projects/46-gradient-accumulation/) | 已完成 |
| 47 | [Checkpoint Save与Resume](phases/19-capstone-projects/47-checkpoint-save-resume/docs/zh-CN.md) | [Checkpoint Save and Resume](phases/19-capstone-projects/47-checkpoint-save-resume/) | 已完成 |
| 48 | [Distributed 数据 Parallel与FSDP 从零实现](phases/19-capstone-projects/48-distributed-fsdp-ddp/docs/zh-CN.md) | [Distributed Data Parallel and FSDP from Scratch](phases/19-capstone-projects/48-distributed-fsdp-ddp/) | 已完成 |
| 49 | [语言模型 评估 Harness](phases/19-capstone-projects/49-lm-eval-harness/docs/zh-CN.md) | [Language Model Evaluation Harness](phases/19-capstone-projects/49-lm-eval-harness/) | 已完成 |
| 50 | [Hypothesis Generator](phases/19-capstone-projects/50-hypothesis-generator/docs/zh-CN.md) | [Hypothesis Generator](phases/19-capstone-projects/50-hypothesis-generator/) | 已完成 |
| 51 | [Literature 检索](phases/19-capstone-projects/51-literature-retrieval/docs/zh-CN.md) | [Literature Retrieval](phases/19-capstone-projects/51-literature-retrieval/) | 已完成 |
| 52 | [Experiment Runner](phases/19-capstone-projects/52-experiment-runner/docs/zh-CN.md) | [Experiment Runner](phases/19-capstone-projects/52-experiment-runner/) | 已完成 |
| 53 | [Result Evaluator](phases/19-capstone-projects/53-result-evaluator/docs/zh-CN.md) | [Result Evaluator](phases/19-capstone-projects/53-result-evaluator/) | 已完成 |
| 54 | [Paper Writer](phases/19-capstone-projects/54-paper-writer/docs/zh-CN.md) | [Paper Writer](phases/19-capstone-projects/54-paper-writer/) | 已完成 |
| 55 | [Critic Loop](phases/19-capstone-projects/55-critic-loop/docs/zh-CN.md) | [Critic Loop](phases/19-capstone-projects/55-critic-loop/) | 已完成 |
| 56 | [Iteration Scheduler](phases/19-capstone-projects/56-iteration-scheduler/docs/zh-CN.md) | [Iteration Scheduler](phases/19-capstone-projects/56-iteration-scheduler/) | 已完成 |
| 57 | [End-to-End Research Demo](phases/19-capstone-projects/57-end-to-end-research-demo/docs/zh-CN.md) | [End-to-End Research Demo](phases/19-capstone-projects/57-end-to-end-research-demo/) | 已完成 |
| 58 | [视觉 Encoder Patches](phases/19-capstone-projects/58-vision-encoder-patches/docs/zh-CN.md) | [Vision Encoder Patches](phases/19-capstone-projects/58-vision-encoder-patches/) | 已完成 |
| 59 | [视觉 Transformer Encoder](phases/19-capstone-projects/59-vit-transformer/docs/zh-CN.md) | [Vision Transformer Encoder](phases/19-capstone-projects/59-vit-transformer/) | 已完成 |
| 60 | [Projection Layer for Modality 对齐](phases/19-capstone-projects/60-projection-layer-modality-align/docs/zh-CN.md) | [Projection Layer for Modality Alignment](phases/19-capstone-projects/60-projection-layer-modality-align/) | 已完成 |
| 61 | [Cross-注意力 Fusion](phases/19-capstone-projects/61-cross-attention-fusion/docs/zh-CN.md) | [Cross-Attention Fusion](phases/19-capstone-projects/61-cross-attention-fusion/) | 已完成 |
| 62 | [视觉-Language Pretraining](phases/19-capstone-projects/62-vision-language-pretraining/docs/zh-CN.md) | [Vision-Language Pretraining](phases/19-capstone-projects/62-vision-language-pretraining/) | 已完成 |
| 63 | [多模态 评估](phases/19-capstone-projects/63-multimodal-eval/docs/zh-CN.md) | [Multimodal Evaluation](phases/19-capstone-projects/63-multimodal-eval/) | 已完成 |
| 64 | [Chunking Strategies, Compared](phases/19-capstone-projects/64-chunking-strategies-advanced/docs/zh-CN.md) | [Chunking Strategies, Compared](phases/19-capstone-projects/64-chunking-strategies-advanced/) | 已完成 |
| 65 | [Hybrid 检索 with BM25与Dense 嵌入](phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense/docs/zh-CN.md) | [Hybrid Retrieval with BM25 and Dense Embeddings](phases/19-capstone-projects/65-hybrid-retrieval-bm25-dense/) | 已完成 |
| 66 | [Cross-Encoder Reranker](phases/19-capstone-projects/66-reranker-cross-encoder/docs/zh-CN.md) | [Cross-Encoder Reranker](phases/19-capstone-projects/66-reranker-cross-encoder/) | 已完成 |
| 67 | [Query Rewriting：HyDE, Multi-Query,与Decomposition](phases/19-capstone-projects/67-query-rewriting-hyde/docs/zh-CN.md) | [Query Rewriting: HyDE, Multi-Query, and Decomposition](phases/19-capstone-projects/67-query-rewriting-hyde/) | 已完成 |
| 68 | [RAG 评估：Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance](phases/19-capstone-projects/68-rag-eval-precision-recall/docs/zh-CN.md) | [RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance](phases/19-capstone-projects/68-rag-eval-precision-recall/) | 已完成 |
| 69 | [End-to-End RAG 系统](phases/19-capstone-projects/69-end-to-end-rag-system/docs/zh-CN.md) | [End-to-End RAG System](phases/19-capstone-projects/69-end-to-end-rag-system/) | 已完成 |
| 70 | [Task Spec Format](phases/19-capstone-projects/70-task-spec-format/docs/zh-CN.md) | [Task Spec Format](phases/19-capstone-projects/70-task-spec-format/) | 已完成 |
| 71 | [Classical 指标](phases/19-capstone-projects/71-classical-metrics/docs/zh-CN.md) | [Classical Metrics](phases/19-capstone-projects/71-classical-metrics/) | 已完成 |
| 72 | [Code Exec Metric](phases/19-capstone-projects/72-code-exec-metric/docs/zh-CN.md) | [Code Exec Metric](phases/19-capstone-projects/72-code-exec-metric/) | 已完成 |
| 73 | [Perplexity与Calibration](phases/19-capstone-projects/73-perplexity-calibration/docs/zh-CN.md) | [Perplexity and Calibration](phases/19-capstone-projects/73-perplexity-calibration/) | 已完成 |
| 74 | [Leaderboard Aggregation](phases/19-capstone-projects/74-leaderboard-aggregation/docs/zh-CN.md) | [Leaderboard Aggregation](phases/19-capstone-projects/74-leaderboard-aggregation/) | 已完成 |
| 75 | [End-to-End 评估 Runner](phases/19-capstone-projects/75-end-to-end-eval-runner/docs/zh-CN.md) | [End-to-End Eval Runner](phases/19-capstone-projects/75-end-to-end-eval-runner/) | 已完成 |
| 76 | [Collective Ops 从零实现](phases/19-capstone-projects/76-collective-ops-from-scratch/docs/zh-CN.md) | [Collective Ops From Scratch](phases/19-capstone-projects/76-collective-ops-from-scratch/) | 已完成 |
| 77 | [数据 Parallel DDP 从零实现](phases/19-capstone-projects/77-data-parallel-ddp/docs/zh-CN.md) | [Data Parallel DDP From Scratch](phases/19-capstone-projects/77-data-parallel-ddp/) | 已完成 |
| 78 | [ZeRO Optimizer State Sharding](phases/19-capstone-projects/78-zero-parameter-sharding/docs/zh-CN.md) | [ZeRO Optimizer State Sharding](phases/19-capstone-projects/78-zero-parameter-sharding/) | 已完成 |
| 79 | [Pipeline Parallel与Bubble Analysis](phases/19-capstone-projects/79-pipeline-parallel/docs/zh-CN.md) | [Pipeline Parallel and Bubble Analysis](phases/19-capstone-projects/79-pipeline-parallel/) | 已完成 |
| 80 | [Sharded Checkpoint与Atomic Resume](phases/19-capstone-projects/80-checkpoint-sharded-resume/docs/zh-CN.md) | [Sharded Checkpoint and Atomic Resume](phases/19-capstone-projects/80-checkpoint-sharded-resume/) | 已完成 |
| 81 | [End-to-End Distributed 训练](phases/19-capstone-projects/81-end-to-end-distributed-train/docs/zh-CN.md) | [End-to-End Distributed Training](phases/19-capstone-projects/81-end-to-end-distributed-train/) | 已完成 |
| 82 | [毕业项目 82：越狱 Taxonomy](phases/19-capstone-projects/82-jailbreak-taxonomy/docs/zh-CN.md) | [Capstone 82 — Jailbreak Taxonomy](phases/19-capstone-projects/82-jailbreak-taxonomy/) | 已完成 |
| 83 | [毕业项目 83：提示注入 Detector](phases/19-capstone-projects/83-prompt-injection-detector/docs/zh-CN.md) | [Capstone 83 — Prompt Injection Detector](phases/19-capstone-projects/83-prompt-injection-detector/) | 已完成 |
| 84 | [毕业项目 84：Refusal 评估](phases/19-capstone-projects/84-refusal-evaluation/docs/zh-CN.md) | [Capstone 84 — Refusal Evaluation](phases/19-capstone-projects/84-refusal-evaluation/) | 已完成 |
| 85 | [毕业项目 85：Content 分类器 Integration](phases/19-capstone-projects/85-content-classifier-integration/docs/zh-CN.md) | [Capstone 85 — Content Classifier Integration](phases/19-capstone-projects/85-content-classifier-integration/) | 已完成 |
| 86 | [毕业项目 86：Constitutional Rules Engine](phases/19-capstone-projects/86-constitutional-rules-engine/docs/zh-CN.md) | [Capstone 86 — Constitutional Rules Engine](phases/19-capstone-projects/86-constitutional-rules-engine/) | 已完成 |
| 87 | [毕业项目 87：End-to-End 安全 Gate](phases/19-capstone-projects/87-end-to-end-safety-gate/docs/zh-CN.md) | [Capstone 87 — End-to-End Safety Gate](phases/19-capstone-projects/87-end-to-end-safety-gate/) | 已完成 |

每课都包含：

- `docs/zh-CN.md`：中文正文
- `quiz.zh-CN.json`：中文测验
- `outputs/*.zh-CN.md`：中文 prompt / skill / artifact

查看中文化进度：

```bash
python3 scripts/audit_translations.py --limit 0
```

查看原仓库课程结构是否仍然有效：

```bash
python3 scripts/audit_lessons.py
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

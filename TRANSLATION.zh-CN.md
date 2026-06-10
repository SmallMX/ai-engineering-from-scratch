# 中文翻译维护指南

这个 fork 的目标是把课程完整中文化，同时保留英文上游的可同步性。英文文件是来源，中文文件是旁路译本；除非专门做中文站点改造，不直接覆盖 `docs/en.md`、`quiz.json` 或已有 `outputs/*.md`。

## 文件约定

每个 lesson 按下面的结构新增中文文件：

```text
phases/<NN>-<phase>/<MM>-<lesson>/
├── docs/
│   ├── en.md
│   └── zh-CN.md
├── quiz.json
├── quiz.zh-CN.json
└── outputs/
    ├── skill-example.md
    └── skill-example.zh-CN.md
```

顶层和 phase 级入口使用同样的旁路命名：

```text
README.md
README.zh-CN.md
ROADMAP.md
ROADMAP.zh-CN.md
glossary/terms.md
glossary/terms.zh-CN.md
```

## 翻译原则

- 保留目录名、文件名、命令、代码标识符、包名和 API 名称。
- 技术术语首次出现时写成“中文术语 (English term)”，后文使用中文术语。
- 代码块只翻译周围说明，不翻译代码本身；所有 fenced code block 必须保留语言标签。
- Mermaid 图可以翻译节点文字，但不要改 Mermaid 语法、方向或结构。
- 数学公式、变量名和伪代码中的符号保持原样；必要时在公式后补一句中文解释。
- 练习题、测验题和解释需要自然中文化，不要逐词直译。
- 引用论文、RFC、官方规范和书名时保留英文标题，可以在后面补中文说明。

## 风格

中文译文面向正在学习 AI 工程的读者。优先准确、清楚、可操作。

- 英文原文很短促时，中文可以适当合并，让语气更顺。
- 英文比喻如果直译别扭，改成中文读者自然理解的表达。
- 对初学者关键的概念，不压缩到只剩术语。
- 对已经熟悉代码的人，不重复解释代码逐行做了什么。

## 术语统一

跨 lesson 重复出现的术语放进 `glossary/terms.zh-CN.md`。新增翻译前先查术语表；如果发现更好的译法，更新术语表并同步修正已翻译 lesson。

常见约定：

| English | 中文 |
|---|---|
| activation function | 激活函数 |
| agent loop | 智能体循环 |
| attention | 注意力 |
| backpropagation | 反向传播 |
| bias | 偏置 |
| decision boundary | 决策边界 |
| embedding | 嵌入 |
| gradient descent | 梯度下降 |
| hyperplane | 超平面 |
| linearly separable | 线性可分 |
| loss function | 损失函数 |
| perceptron | 感知机 |
| tokenization | 分词 |
| weight | 权重 |

## 测验翻译

`quiz.zh-CN.json` 必须保持和英文测验相同的 JSON 结构：

- `stage` 保持英文枚举值，例如 `pre`、`check`、`post`。
- `correct` 保持原来的零基索引。
- `options` 的顺序不要改变。
- `question`、`options`、`explanation` 翻译成中文。

## 产物翻译

`outputs/*.md` 是课程交付物，中文 fork 应提供对应的 `*.zh-CN.md`。如果产物是 agent skill 或 prompt：

- YAML frontmatter 的机器字段保持英文键名。
- `name` 可以保持英文，避免影响工具识别。
- `description` 可以翻译成中文，除非某个工具要求英文。
- 正文翻译成中文。

## 审计

查看整体翻译缺口：

```bash
python3 scripts/audit_translations.py
```

默认只显示前 50 个缺口。查看全部缺口：

```bash
python3 scripts/audit_translations.py --limit 0
```

只看某个 phase：

```bash
python3 scripts/audit_translations.py --phase 3
```

输出 JSON：

```bash
python3 scripts/audit_translations.py --json
```

完整中文化完成前，这个脚本会返回非零退出码。它的作用是追踪进度，不替代 `scripts/audit_lessons.py`。

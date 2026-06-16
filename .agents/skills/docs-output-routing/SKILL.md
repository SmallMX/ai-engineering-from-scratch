---
name: docs-output-routing
version: 1.0.0
description: 文档输出规范：所有生成的学习文档或辅助指南自动输出到对应章节的 docs/ 文件夹下。在生成文档类内容时自动生效。
---

# 文档输出路由规范

生成任何学习文档、辅助指南、深度解析、速查手册等文档类内容时，**必须将文件写入对应课时的 `docs/` 文件夹**，而非 artifacts 目录或其他位置。

## 激活条件

此规范在以下场景自动生效：
- 为某个课时生成补充学习文档时
- 为某个课时生成辅助指南、速查手册时
- 为某个课时生成深度解析、概念图解时
- 为某个课时翻译或创建多语言版本的文档时
- 用户要求"写一份指南"、"生成文档"、"补充说明"等与文档创作相关的请求时

无需手动触发，只要生成的内容属于课程文档范畴，始终遵守。

## 规则

### 1. 输出路径

所有生成的文档必须写入目标课时的 `docs/` 文件夹：

```
phases/NN-phase-slug/MM-lesson-slug/docs/<filename>.md
```

**不得**将课程文档输出到以下位置：
- Artifacts 目录（`~/.gemini/antigravity-ide/brain/...`）
- 项目根目录
- `outputs/` 文件夹（仅用于 Skill / Prompt / Agent / MCP Server 等可复用产物）
- 临时目录

### 2. 目标课时定位

根据用户请求的上下文确定目标课时：

- **用户明确指定**：如"给第 05 课写一份指南"，则输出到该课时的 `docs/`
- **基于当前打开的文件**：如用户正在编辑 `phases/00-setup-and-tooling/05-jupyter-notebooks/code/main.py`，则对应课时为 `phases/00-setup-and-tooling/05-jupyter-notebooks/`
- **基于对话上下文**：如果对话中一直在讨论某个课时的内容，则沿用该课时

### 3. 文件命名

- 使用小写英文单词，以下划线分隔：`detailed_jupyter_guide.md`
- 名称应准确反映文档内容，而非泛泛的 `guide.md` 或 `notes.md`
- 中文翻译版使用 `zh-CN.md` 后缀：`en.md` → `zh-CN.md`

### 4. 文件格式

生成的文档必须遵守以下格式要求：

- 使用 Markdown 格式（`.md`）
- 图表使用 Mermaid 或 SVG（不使用 ASCII 框图）
- 每个代码块必须标注语言标签
- 数学公式使用 LaTeX 语法（`$...$` 或 `$$...$$`）

### 5. 与现有文件的关系

- `en.md`：课时的主文档（英文），遵循 AGENTS.md 中定义的 frontmatter 格式
- `zh-CN.md`：中文翻译版本
- 其他 `.md` 文件：补充材料、深度指南、速查手册等

生成新文档时，不得覆盖已有的 `en.md` 或 `zh-CN.md`，除非用户明确要求修改。

## 示例

### 场景 1：用户请求"给 Jupyter Notebooks 课写一份深度指南"

```
输出路径：phases/00-setup-and-tooling/05-jupyter-notebooks/docs/detailed_jupyter_guide.md
```

### 场景 2：用户正在编辑某课时代码，要求"解释一下这个概念"

```
输出路径：phases/<当前课时>/docs/<概念名称>_explained.md
```

### 场景 3：用户要求"把 en.md 翻译成中文"

```
输出路径：phases/<当前课时>/docs/zh-CN.md
```

### 场景 4：用户要求生成与课程无关的通用文档

此规范**不适用**。通用文档按正常流程输出到 artifacts 目录或用户指定位置。

## 不适用范围

以下内容**不受此规范影响**：
- 与特定课时无关的通用分析报告或调研文档
- 实现计划（`implementation_plan.md`）、任务清单（`task.md`）等工作流文档
- `outputs/` 文件夹中的可复用产物（Skill、Prompt、Agent 等）
- 代码文件（应放入 `code/` 目录）
- 测验文件（`quiz.json` / `quiz.zh-CN.json`，放在课时根目录）

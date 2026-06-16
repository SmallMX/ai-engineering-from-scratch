---
name: chinese-comments
version: 1.0.0
description: 编码规范：所有代码注释和文档字符串使用中文书写。在编写或修改代码时自动生效。
---

# 中文注释规范

所有代码中的注释和文档字符串（docstring）必须使用**中文**书写。

## 激活条件

此规范在以下场景自动生效：
- 编写新代码文件时
- 修改现有代码文件时
- 代码审查时

无需手动触发，编写代码时始终遵守。

## 规则

### 1. 行内注释

```python
# 从环境变量或配置文件中读取 API 密钥
api_key = os.environ.get("ANTHROPIC_API_KEY")
```

```typescript
// 从环境变量或配置文件中读取 API 密钥
const apiKey = process.env.ANTHROPIC_API_KEY;
```

### 2. 文档字符串 / JSDoc

**Python docstring：**
```python
def load_dotenv(path: str | None = None) -> dict[str, str]:
    """读取 .env 文件并返回键值对。

    支持 KEY=VALUE 格式，支持 # 注释行，支持可选的引号包裹值。
    若 *path* 为 None，则在当前工作目录下查找 .env 文件。
    """
```

**TypeScript JSDoc：**
```typescript
/**
 * 读取 .env 文件并返回键值对。
 *
 * @param path - 配置文件路径，默认为当前目录下的 .env
 * @returns 解析后的键值对字典
 */
function loadDotenv(path?: string): Record<string, string> {
```

### 3. 块注释

```python
# ===========================
# 模型配置
# ===========================
```

### 4. TODO / FIXME / HACK

```python
# TODO: 添加对嵌套引号的支持
# FIXME: 当文件编码非 UTF-8 时会抛出异常
# HACK: 临时方案，等上游修复后移除
```

## 不适用范围

以下内容**不受此规范影响**，保持英文：
- 变量名、函数名、类名等标识符
- Git commit message（遵循 Conventional Commits 规范）
- `docs/en.md` 等英文文档文件
- 日志输出和用户提示信息（按目标受众决定语言）
- 已有的英文注释，除非主动修改该代码段

## 示例

修改前：
```python
def get_api_key() -> str | None:
    """Return the API key from env var or .env config file.

    Environment variables take precedence so users can override the file
    without editing it.
    """
    # Check environment variable first
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        return api_key
    # Fall back to .env file
    dotenv = load_dotenv()
    return dotenv.get("ANTHROPIC_API_KEY")
```

修改后：
```python
def get_api_key() -> str | None:
    """从环境变量或 .env 配置文件中获取 API 密钥。

    环境变量优先，用户无需修改文件即可覆盖配置。
    """
    # 优先检查环境变量
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        return api_key
    # 回退到 .env 配置文件
    dotenv = load_dotenv()
    return dotenv.get("ANTHROPIC_API_KEY")
```

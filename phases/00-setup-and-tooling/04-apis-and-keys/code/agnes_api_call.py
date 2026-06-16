# 阶段 0 · 课时 04 — API 与密钥（Agnes AI 版本）
# 从 .env 配置文件读取 AGNES_API_KEY，通过 HTTP 调用 Agnes AI 的
# OpenAI 兼容接口 /v1/chat/completions。
# 参考：https://docs.agnes-ai.com

import os
import json
import urllib.request
from pathlib import Path


def load_dotenv(path: str | None = None) -> dict[str, str]:
    """读取 .env 文件并返回键值对。

    支持 KEY=VALUE 格式、# 注释行和可选的引号包裹值。
    若 *path* 为 None，则在当前工作目录下查找 .env 文件。
    """
    if path is None:
        path = str(Path.cwd() / ".env")
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    env: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        eq = stripped.find("=")
        if eq <= 0:
            continue
        key = stripped[:eq].strip()
        value = stripped[eq + 1 :].strip()
        if (
            (value.startswith('"') and value.endswith('"'))
            or (value.startswith("'") and value.endswith("'"))
        ):
            value = value[1:-1]
        env[key] = value
    return env


def get_api_key() -> str | None:
    """从环境变量或 .env 配置文件中获取 API 密钥。

    环境变量优先，用户无需修改文件即可覆盖配置。
    """
    api_key = os.environ.get("AGNES_API_KEY")
    if api_key:
        return api_key
    dotenv = load_dotenv()
    return dotenv.get("AGNES_API_KEY")


def call_agnes_api():
    """通过原始 HTTP 请求调用 Agnes AI 的 chat completions 接口。"""
    api_key = get_api_key()
    if not api_key:
        print("请先在环境变量或 .env 配置文件中设置 AGNES_API_KEY")
        return

    url = "https://apihub.agnes-ai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    body = json.dumps({
        "model": "agnes-2.0-flash",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    }).encode()

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        text = result["choices"][0]["message"]["content"]
        usage = result["usage"]
        print(f"响应内容：{text}")
        print(f"Token 用量：{usage['prompt_tokens']} 输入, {usage['completion_tokens']} 输出")


if __name__ == "__main__":
    print("=== Agnes AI API 调用 ===\n")
    call_agnes_api()

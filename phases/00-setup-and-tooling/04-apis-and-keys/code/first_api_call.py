import os
import json
import urllib.request
from pathlib import Path


def load_dotenv(path: str | None = None) -> dict[str, str]:
    """Read a .env file and return key-value pairs.

    Supports KEY=VALUE per line, # comments, and optional surrounding quotes.
    If *path* is None, looks for .env in the current working directory.
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
    """Return the API key from env var or .env config file.

    Environment variables take precedence so users can override the file
    without editing it.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        return api_key
    dotenv = load_dotenv()
    return dotenv.get("ANTHROPIC_API_KEY")


def call_with_sdk():
    try:
        import anthropic
    except ImportError:
        print("Install the SDK: pip install anthropic")
        return

    api_key = get_api_key()
    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
    )
    print(f"SDK response: {response.content[0].text}")
    print(f"Tokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out")


def call_raw_http():
    api_key = get_api_key()
    if not api_key:
        print("Set ANTHROPIC_API_KEY in environment or .env config file first")
        return

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    }).encode()

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f"Raw HTTP response: {result['content'][0]['text']}")
        print(f"Tokens used: {result['usage']['input_tokens']} in, {result['usage']['output_tokens']} out")


if __name__ == "__main__":
    print("=== API Calls ===\n")
    print("1. Using the SDK:")
    call_with_sdk()
    print("\n2. Using raw HTTP:")
    call_raw_http()

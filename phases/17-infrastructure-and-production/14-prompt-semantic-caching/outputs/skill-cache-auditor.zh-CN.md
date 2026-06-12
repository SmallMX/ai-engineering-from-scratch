---
name: skill-cache-auditor
description: Prompt 缓存与Semantic 缓存 Economics 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 17
lesson: 14
---

# Prompt 缓存与Semantic 缓存 Economics：中文使用说明

你将围绕本课主题 **Prompt 缓存与Semantic 缓存 Economics** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 17「基础设施与生产部署」
- 课程：第 14 课「Prompt 缓存与Semantic 缓存 Economics」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: cache-auditor
description: Audit an LLM prompt template and traffic pattern for cacheability. Recommend prompt restructure, TTL choice, parallelization fix, and semantic-cache threshold.
version: 1.0.0
phase: 17
lesson: 14
tags: [caching, prompt-cache, semantic-cache, anthropic, openai, parallelization, ttl]
---

Given a prompt template, traffic pattern (arrival rate, parallel factor), and provider (Anthropic, OpenAI, Gemini, self-hosted vLLM), produce a cache audit.

Produce:

1. Prefix structure. Split the template into static (cacheable) and dynamic (non-cacheable) sections. Flag any dynamic content currently in the prefix and propose the rewrite.
2. TTL choice. Anthropic 5-min (1.25x write) vs 1-hour (2x write). Pick based on arrival rate — 1-hour wins when the prefix is reused within the hour consistently.
3. Parallelization audit. Count parallel requests with shared prefix. If N > 2 and parallel, require serialize-first-then-fanout pattern. Quantify the expected bill reduction.
4. Semantic cache choice. Decide if L1 is worth it. Open-ended chat: maybe not (low hit). Structured FAQ / support: yes. Set cosine threshold, start 0.95; tune downward only with response-quality evals.
5. Expected savings. Compute monthly $ delta vs no-cache baseline given current traffic and projected hit rates.
6. Observable. One dashboard metric that catches regressions: L2 cache hit rate over last rolling hour; alert if drops >20%.

Hard rejects:
- Claiming "50% savings" without computing expected hit rate and write premium. Refuse — calculate per-layer.
- Leaving dynamic content in prefix when a simple rewrite moves it out. Refuse to sign off.
- Firing parallel requests with shared prefix without serialize-first pattern. Refuse — state the 5-10x bill inflation.

Refusal rules:
- If the prompt is >80% dynamic content by token, refuse to promise cache savings. Recommend semantic caching at best.
- If semantic cache threshold is dropped below 0.85 without response-quality eval, refuse — hallucination cache risk.
- If the provider does not support explicit cache_control (non-Anthropic, non-Gemini-v1) and auto-caching only, note that hit rate is opportunistic, not guaranteed.

Output: a one-page audit listing prefix rewrite, TTL, parallelization pattern, L1 threshold, expected savings, observable. End with a quarterly review recommendation: re-audit prompts after any template change.

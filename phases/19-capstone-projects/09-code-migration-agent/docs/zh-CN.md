# 毕业项目 09：Code Migration 智能体 (Repo-Level Language / Runtime Upgrade)

> Amazon's MigrationBench (Java 8 to 17)与Google's App Engine Py2-to-Py3 migrator set the 2026 bar. Moderne's OpenRewrite does deterministic AST rewrites at scale. Grit targets the same problem with codemod-style DSL. The production pattern combines both：a deterministic substrate for safe rewrites plus an agent layer for the ambiguous cases, a sandbox for per-branch builds,与a test harness that flips green before the PR opens. The capstone is to migrate 50 real repos与publish a pass rate with a failure taxonomy.

**类型：** 毕业项目
**语言：** Python (agent), Java / Python (targets), TypeScript (dashboard)
**前置知识：** Phase 5 (NLP), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 15 (autonomous), Phase 17 (infrastructure)
**时间：** 30 hours

## 学习目标
- 理解 毕业项目 09：Code Migration 智能体 (Repo-Level Language / Runtime Upgrade) 在本阶段课程中的作用。
- 把核心概念映射到可运行代码、测验和课程产物。
- 保留英文术语、命令、路径和 API 名称，方便和原文对照。

## 中文导读

本课是 Phase 19「毕业项目」的第 09 课。学习时建议先读这一份中文导读，确认本课要解决的问题、关键术语和可运行产物，再回到英文原文核对细节。

阅读时请重点关注三件事：概念为什么成立，代码如何验证这个概念，以及课程产物如何复用到真实工作流。遇到公式、命令、路径、API 名称或模型名时，保持英文原写法，避免和源码脱节。

## 学习建议

1. 先通读“学习目标”和“中文导读”，建立本课的任务边界。
2. 对照英文原文阅读关键段落，代码、命令和数学符号保持原样。
3. 运行 `code/` 里的示例，并用 `quiz.zh-CN.json` 检查自己是否理解。
4. 如果本课包含 `outputs/*.zh-CN.md`，把它当作可复用的 prompt、skill 或操作清单。

## 英文原文

下面保留英文原文，方便和上游同步，也方便你在需要时查看精确术语、代码片段和引用来源。

# Capstone 09 — Code Migration Agent (Repo-Level Language / Runtime Upgrade)

> Amazon's MigrationBench (Java 8 to 17) and Google's App Engine Py2-to-Py3 migrator set the 2026 bar. Moderne's OpenRewrite does deterministic AST rewrites at scale. Grit targets the same problem with codemod-style DSL. The production pattern combines both: a deterministic substrate for safe rewrites plus an agent layer for the ambiguous cases, a sandbox for per-branch builds, and a test harness that flips green before the PR opens. The capstone is to migrate 50 real repos and publish a pass rate with a failure taxonomy.

**Type:** Capstone
**Languages:** Python (agent), Java / Python (targets), TypeScript (dashboard)
**Prerequisites:** Phase 5 (NLP), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 15 (autonomous), Phase 17 (infrastructure)
**Phases exercised:** P5 · P7 · P11 · P13 · P14 · P15 · P17
**Time:** 30 hours

## Problem

Large-scale code migration is one of the cleanest production applications of 2026 coding agents. The ground truth is obvious (does the test suite pass after the migration?), the rewards are real (a Java-8 fleet migration is a headcount-scale project), and the benchmarks are public (MigrationBench 50-repo subset). Moderne's OpenRewrite handles the deterministic side. The agent layer handles everything OpenRewrite recipes cannot: ambiguous rewrites, build-system drift, long-tail syntax, transitive dependency breakage.

You will build an agent that takes a Java 8 repo (or Python 2 repo) and produces a green-CI migrated branch. You will measure pass rate, test-coverage preservation, cost per repo, and build a failure taxonomy. The side-by-side against a deterministic-only baseline tells you where the agent's value actually lives.

## Concept

The pipeline has two layers. The **deterministic substrate** (OpenRewrite for Java, libcst for Python) runs the bulk of mechanical rewrites safely: imports, method signatures, null-safety edits, try-with-resources, deprecated API replacements. It is fast and produces auditable diffs. The **agent layer** (OpenAI Agents SDK or LangGraph over Claude Opus 4.7 and GPT-5.4-Codex) handles cases the recipes cannot: build-file upgrades (Maven/Gradle/pyproject), transitive dependency conflicts, test flakes, custom annotations.

Each repo gets a Daytona sandbox with the target runtime preinstalled. The agent iterates: run build, classify failures, apply fix, rerun. Hard limits: 30 minutes per repo, $8 per repo, 20 agent turns. If all tests pass and the coverage delta is not negative, the branch opens a PR. If not, the repo gets filed under a failure class with evidence.

The failure taxonomy is the deliverable. Across 50 repos, what broke? Transitive deps? Custom annotations? Build tool version? Test flakes unrelated to migration? Each class gets a count and an exemplar diff. Future recipe authors can target the top three.

## Architecture

```
target repo
      |
      v
OpenRewrite / libcst deterministic recipes
   (safe, fast, auditable, ~70-80% of fixes)
      |
      v
Daytona sandbox per branch
      |
      v
agent loop (Claude Opus 4.7 / GPT-5.4-Codex):
   - run build -> capture failures
   - classify failures (build, test, lint)
   - apply fix (patch or retry recipe)
   - rerun
   - budget: 30 min, $8, 20 turns
      |
      v
test + coverage delta gate
      |
      v (passed)
open PR
      |
      v (failed)
file under failure class + attach repro
```

## Stack

- Deterministic substrate: OpenRewrite (Java) or libcst (Python)
- Agent: OpenAI Agents SDK or LangGraph over Claude Opus 4.7 + GPT-5.4-Codex
- Sandbox: Daytona devcontainers per branch, pre-installed target runtime (Java 17 / Python 3.12)
- Build systems: Maven, Gradle, uv (Python)
- Benchmarks: Amazon MigrationBench 50-repo subset (Java 8 to 17), Google App Engine Py2-to-Py3 repos
- Test harness: parallel runner, coverage via Jacoco (Java) or coverage.py (Python)
- Observability: Langfuse + trace bundle per repo with every diff chunk
- Dashboard: failure-taxonomy dashboard with per-class counts and exemplar diffs

## Build It

1. **Recipe pass.** Run OpenRewrite (Java) or libcst (Python) recipes first. Catch the 70-80% of migrations that are mechanical. Commit as "recipe" commit.

2. **Build trial.** Daytona sandbox: install target runtime, run the build. If green, skip to tests. If red, hand off to agent.

3. **Agent loop.** LangGraph with tools: `run_build`, `read_file`, `edit_file`, `run_test`, `git_diff`. Agent classifies the failure (dep, syntax, test, build-tool) and applies a targeted fix. Rerun.

4. **Budget caps.** 30 minutes wall-clock per repo, $8 cost, 20 agent turns. Any breach halts and files under "budget_exhausted" with the current diff.

5. **Test + coverage gate.** After the build goes green, run the test suite. Compare coverage to the base repo. If coverage dropped more than 2%, file under "coverage_regression".

6. **PR open.** On success, push the branch, open the PR with the diff and a summary of which recipes applied and which commits the agent authored.

7. **Failure taxonomy.** For each failed repo, tag with a class: `dep_upgrade_required`, `build_tool_drift`, `custom_annotation`, `test_flake`, `syntax_edge_case`, `budget_exhausted`. Build a dashboard.

8. **50-repo run.** Execute across the MigrationBench subset. Report per-class pass rate, cost-per-repo, coverage-preservation, and a compare-vs-deterministic-only baseline.

## Use It

```
$ migrate legacy-java-service --target java17
[recipe]   27 rewrites applied (JUnit 4->5, HashMap initializer, try-with-resources)
[build]    FAIL: cannot find symbol sun.misc.BASE64Encoder
[agent]    turn 1 classify: removed_jdk_api
[agent]    turn 2 apply: sun.misc.BASE64Encoder -> java.util.Base64
[build]    OK
[tests]    412/412 passing; coverage 84.1% -> 84.3%
[pr]       opened #1841  cost=$3.20  turns=4
```

## Ship It

`outputs/skill-migration-agent.md` is the deliverable. Given a repo, it executes deterministic recipes then an agent loop to produce a green migrated branch, or files the repo under a taxonomy class.

| Weight | Criterion | How it is measured |
|:-:|---|---|
| 25 | MigrationBench pass rate | 50-repo subset pass@1 |
| 20 | Test-coverage preservation | Mean coverage delta vs base |
| 20 | Cost per migrated repo | $/repo on passing runs |
| 20 | Agent / deterministic-tool integration | Fraction of fixes that OpenRewrite handled vs agent authored |
| 15 | Failure analysis write-up | Taxonomy completeness with exemplars |
| **100** | | |

## Exercises

1. Run the migrate pipeline with OpenRewrite only (no agent). Compare pass rate to the full pipeline. Identify the cases where the agent alone is the difference.

2. Implement a "lint-clean" check: after migration, run a style linter (spotless for Java, ruff for Python). Fail the PR if new lint errors appear. Measure the coverage-preserved-but-style-regressed rate.

3. Add a "minimal-diff" optimizer: after the agent's branch passes tests, trim unnecessary changes with a second pass. Report diff-size reduction.

4. Extend to a third migration: Node 18 to Node 22. Reuse the sandbox wrapping; swap the recipe layer for a custom codemod.

5. Measure time-to-first-green-build (TTFGB) as a UX metric. Target: p50 under 10 minutes.

## Key Terms

| Term | What people say | What it actually means |
|------|-----------------|------------------------|
| Deterministic substrate | "Recipe engine" | OpenRewrite / libcst: declarative AST rewrites with safety guarantees |
| Codemod | "Code-modifying program" | A rewrite rule that changes source code mechanically |
| Build drift | "Tool version skew" | Subtle Maven / Gradle / uv behavior changes between major versions |
| Failure class | "Taxonomy bucket" | A labeled reason a repo did not migrate: dep, syntax, test, build-tool, budget |
| Coverage delta | "Coverage preservation" | Change in test coverage % from base to migrated branch |
| Agent turn | "Tool-call round" | One plan -> act -> observe cycle in the agent loop |
| Budget exhaustion | "Hit the ceiling" | The repo consumed its 30-min / $8 / 20-turn limit without passing |

## Further Reading

- [Amazon MigrationBench](https://aws.amazon.com/blogs/devops/amazon-introduces-two-benchmark-datasets-for-evaluating-ai-agents-ability-on-code-migration/) — the canonical 2026 benchmark
- [Moderne.io OpenRewrite platform](https://www.moderne.io) — the deterministic substrate reference
- [OpenRewrite documentation](https://docs.openrewrite.org) — recipe authoring
- [Grit.io](https://www.grit.io) — alternate codemod DSL
- [OpenAI sandboxed migration cookbook](https://developers.openai.com/cookbook/examples/agents_sdk/sandboxed-code-migration/sandboxed_code_migration_agent) — the Agents SDK reference
- [Google App Engine Py2 to Py3 migrator](https://cloud.google.com/appengine) — alternate migration benchmark
- [libcst](https://github.com/Instagram/LibCST) — Python deterministic substrate
- [Daytona sandboxes](https://daytona.io) — reference per-branch sandbox

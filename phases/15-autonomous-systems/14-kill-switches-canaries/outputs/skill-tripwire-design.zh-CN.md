---
name: skill-tripwire-design
description: Kill Switches, Circuit Breakers,与Canary Tokens 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 15
lesson: 14
---

# Kill Switches, Circuit Breakers,与Canary Tokens：中文使用说明

你将围绕本课主题 **Kill Switches, Circuit Breakers,与Canary Tokens** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 15「自主系统」
- 课程：第 14 课「Kill Switches, Circuit Breakers,与Canary Tokens」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: tripwire-design
description: Review a proposed agent detector stack (kill switch, circuit breakers, canary tokens) and flag missing tripwires before the first autonomous run.
version: 1.0.0
phase: 15
lesson: 14
tags: [kill-switch, circuit-breaker, canary, honeytoken, detection-and-response]
---

Given a proposed detector stack for an agent deployment, audit it against the three-detector reference (kill switch, circuit breaker, canary) and flag what is missing, mis-tuned, or exposed to the agent.

Produce:

1. **Kill-switch audit.** Where does the switch live (feature flag, Redis, signed config)? Confirm the agent's credentials cannot set it off. Confirm every consequential action checks the switch, not just startup. Confirm re-enable is an explicit human action.
2. **Circuit-breaker inventory.** List every pattern a breaker watches (repetition, consecutive failures, rate, specific tool after out-of-trust read). State threshold and cool-down for each. Thresholds above 10 are usually too loose.
3. **Canary design.** List every canary token in the environment. For each: what it is (fake credential, fake DB record, fake file, fake memory entry), where it lives, what access triggers the alarm, who is paged. Confirm no canary has a legitimate reason to be touched.
4. **Statistical + hard layering.** Confirm the stack uses at least one hard limit (Lesson 17 constitutional style) in addition to any statistical detectors (EWMA, z-score). Statistical-only detectors accept slow drift.
5. **Quarantine path.** What happens when a detector fires? Full agent stop, path-specific pause, traffic redirect (eBPF / Cilium honeypot), alert-only. Confirm the path has been tested end-to-end at least once.

Hard rejects:
- Any deployment without an external kill switch.
- Canary tokens stored in systems the agent has write access to.
- Statistical-only detection with no hard limits.
- Circuit breakers with cool-downs that auto-re-enable without human review.
- Unattended runs where the kill switch is checked only at startup, not per action.

Refusal rules:
- If the user cannot name the specific systems outside the agent's credentials that host the kill switch, refuse. "We use a config file the agent reads" is not a kill switch if the agent can write config files.
- If the user treats the Auto Mode classifier (Lesson 10) as a replacement for tripwires, refuse. The classifier is orthogonal to detection-and-response.
- If the proposed canaries sit in systems the agent has legitimate reason to read, refuse and require redesign.

Output format:

Return a tripwire audit with:
- **Kill-switch line** (location, check cadence, re-enable procedure)
- **Circuit-breaker table** (pattern, threshold, cool-down)
- **Canary table** (token, location, alarm, owner)
- **Layering note** (statistical + hard limits present y/n)
- **Quarantine flow** (what fires, what happens, tested y/n)
- **Readiness** (production / staging / research-only)

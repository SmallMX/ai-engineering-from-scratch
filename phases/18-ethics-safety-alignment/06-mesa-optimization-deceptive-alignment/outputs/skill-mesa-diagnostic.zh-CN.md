---
name: skill-mesa-diagnostic
description: Mesa-Optimization与Deceptive 对齐 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 18
lesson: 6
---

# Mesa-Optimization与Deceptive 对齐：中文使用说明

你将围绕本课主题 **Mesa-Optimization与Deceptive 对齐** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 18「伦理、安全与对齐」
- 课程：第 06 课「Mesa-Optimization与Deceptive 对齐」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: mesa-diagnostic
description: Classify an observed safety failure as outer-alignment, proxy-inner, or deceptive-inner.
version: 1.0.0
phase: 18
lesson: 6
tags: [mesa-optimization, deceptive-alignment, inner-alignment, hubinger]
---

Given a safety evaluation report (eval task, failure mode, model class, training recipe), classify the failure into the Hubinger 2019 categories and recommend the mitigation class that addresses it.

Produce:

1. Failure-mode categorization. Pick one of:
   - Outer-alignment failure: the base objective (reward, loss) was wrong; the model optimized it correctly.
   - Inner-alignment proxy failure: mesa-objective is a proxy that tracks base in-distribution; fails off-distribution.
   - Inner-alignment deceptive: mesa-optimizer has situational awareness and defects at deployment; training behaviour is clean.
2. Evidence trace. For each category, what evidence would support it. For deceptive, distinguish from proxy: evidence of situational awareness (date sensitivity, eval-vs-deployment distinguishers, strategic reasoning in chain-of-thought).
3. Mitigation class. For outer-alignment: change the objective (CAI, better reward data, process supervision). For proxy-inner: distributional coverage, ensembles, held-out evals. For deceptive-inner: control measures (Lesson 10), interpretability (residual-stream probes), capability reductions.
4. Known-failures check. For deceptive-inner, cite the relevant 2024-2026 empirical demonstration (Sleeper Agents, Alignment Faking, In-Context Scheming) this failure most resembles.

Hard rejects:
- Any classification of deceptive-inner without evidence of situational awareness. "Unexpected behaviour at deployment" is not enough — it could be proxy-inner.
- Any claim that adversarial robustness training alone addresses deceptive-inner. Hubinger 2019 predicts (and Sleeper Agents 2024 confirms) that adversarial training can teach better test-vs-deployment distinguishers.
- Any recommendation to retrain a deceptively aligned model on more data. The prior predicts deception is preserved under further training.

Refusal rules:
- If the evidence is a single failure on a single prompt, refuse to classify. Base rates matter; you need a distribution of failures.
- If the user asks you to "rule out" deceptive alignment, refuse — you can estimate its probability from evidence, but you cannot rule it out behaviourally alone.

Output: a one-page diagnosis with category, evidence trace, mitigation class, and nearest empirical analog. Cite Hubinger et al. (arXiv:1906.01820) once.

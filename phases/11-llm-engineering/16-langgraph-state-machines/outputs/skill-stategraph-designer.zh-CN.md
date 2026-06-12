---
name: skill-stategraph-designer
description: LangGraph：State Machines for 智能体 的中文辅助说明，用于学习、复盘和复用本课产物
version: 1.0.0
phase: 11
lesson: 16
---

# LangGraph：State Machines for 智能体：中文使用说明

你将围绕本课主题 **LangGraph：State Machines for 智能体** 使用这个课程产物。它可以作为 prompt、skill、检查清单或实现参考。

使用时请遵循这些原则：

1. 保留代码标识符、命令、路径、API 名称、模型名和指标名的英文原写法。
2. 先明确输入、输出、约束和成功标准，再执行具体步骤。
3. 把本课产物和 `docs/zh-CN.md`、`quiz.zh-CN.json` 对照使用。
4. 如果英文原文包含工具调用格式、JSON schema 或协议字段，不要随意改名。

## 中文要点

- 阶段：Phase 11「LLM 工程」
- 课程：第 16 课「LangGraph：State Machines for 智能体」
- 目标：把英文 artifact 转化为中文学习和实操入口，同时保留原始内容以便精确对照。

## 英文原始 artifact

下面保留英文原始内容，方便同步上游和核对机器可读字段。

---
name: stategraph-designer
description: Turn an agent task into a LangGraph StateGraph with named nodes, typed state, reducers, checkpointer, and human interrupts.
version: 1.0.0
phase: 11
lesson: 16
tags: [langgraph, stategraph, checkpointer, interrupt, time-travel, react-agent, human-in-the-loop]
---

Given the agent task (user-facing goal, available tools, expected turn count, side effects with safety blast radius, durability requirements, target latency budget), output:

1. Node list. Name every discrete step: the LLM thinker, each tool runner, every human review step, any summarizer or critic, any retriever. Reject the design if any node touches more than one concern; split it.
2. State schema. TypedDict (or Pydantic) fields with a reducer for every list. Always Annotated[list, add_messages] on the message log. Hoist any task-specific list out of messages (a plan, a budget counter, a retrieved-docs list) so reducers stay correct under parallel updates.
3. Edge map. Static edges where the next step is deterministic. Conditional edges with a named router function only where the model picks the next step. Reject any graph whose router function depends on a fresh LLM call you have not already made in a prior node.
4. Interrupt placement. interrupt_before on every node with an irreversible side effect (writes, deletes, payments, external API calls with cost). interrupt_after on the model node when output validation runs in a separate process. Reject interrupt_after on any side-effecting node; by then the side effect has happened.
5. Checkpointer. MemorySaver for tests only. Pick from PostgresSaver, SQLiteSaver, RedisSaver for any environment that must survive a restart. Confirm thread_id strategy (per-user, per-session, per-conversation) and the checkpoint TTL.

Refuse to ship a LangGraph without a checkpointer. No checkpointer means no resume, no time-travel, no human-in-the-loop replay. Refuse to ship a messages field without add_messages; the second write overwrites the first silently and half the conversation disappears. Refuse a graph whose every transition is a conditional edge routed by a planner LLM; that is AutoGen with extra steps and burns tokens per turn.

Example input: "Refund-handling agent over Anthropic Claude with three tools (lookup_order, issue_refund, send_email), must pause for a human before any refund over 100 dollars, must resume after server restart, p95 latency budget 8 seconds."

Example output:
- Nodes: agent (LLM call), lookup_tool, refund_tool, email_tool, human_review.
- State: messages with add_messages, order_context (overwrite), refund_amount (overwrite), reviewer_decision (overwrite).
- Edges: agent to should_continue router with branches lookup_tool, refund_tool, email_tool, human_review, END. Tool nodes go back to agent.
- Interrupts: interrupt_before on refund_tool when refund_amount > 100. No interrupt on lookup_tool or email_tool.
- Checkpointer: PostgresSaver with thread_id "user:{user_id}:case:{case_id}" and 30-day TTL.

---
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
created: Wednesday 1st April 2026 00:00
aliases:
  - AutoGen
tags:
  - llm
  - multi-agent
  - ai-agents
  - framework
  - ml
---
- https://arxiv.org/abs/2308.08155
- Source: arxiv

---

# TL;DR

AutoGen is an open-source framework that lets developers build LLM applications as **conversations between multiple customizable agents** — each combining LLMs, code execution, and human input — enabling complex workflows with dramatically less code.

# Summary

AutoGen introduces **"conversation programming"**: instead of hardcoded pipelines, application logic is expressed as dialogues between agents. Each agent is a `ConversableAgent` that can be backed by an LLM, a human, tools, or any combination. Two primary built-ins — `AssistantAgent` (LLM-backed) and `UserProxyAgent` (human proxy + code executor) — cover most use cases out of the box. For dynamic multi-party tasks, a `GroupChatManager` selects speakers at runtime using role-play-style prompting.

Control flow is hybrid: natural-language system prompts govern LLM behavior (e.g., "reply TERMINATE when done"), while Python code handles termination logic and tool dispatch. Agents communicate via a unified send/receive interface with auto-reply loops, keeping the abstraction uniform regardless of the underlying backend.

The paper validates the framework across six applications: **math problem solving** (69.48% on MATH level-5, beating GPT-4's 55.18%), **retrieval-augmented chat** with interactive context refinement, **ALFWorld decision-making** (+15% task completion via a grounding agent), **OptiGuide supply-chain coding** (4× code reduction, 3× less user interaction), **dynamic group chat**, and **conversational chess**.

# Key contributions

1. **Conversable agent abstraction** — a unified interface supporting LLM, human, and tool backends interchangeably, enabling flexible composition without framework rewrites.
2. **Conversation programming paradigm** — encodes both computation and control flow as multi-agent dialogue, replacing bespoke pipeline code with reusable patterns.
3. **GroupChatManager** — runtime speaker selection via role-play prompting, enabling dynamic (non-predetermined) multi-agent topologies.
4. **Interactive retrieval** — a novel RAG pattern where the assistant signals "UPDATE CONTEXT" to trigger automated context refinement, outperforming static retrieval baselines.
5. **Empirical validation at breadth** — six heterogeneous domains showing consistent gains in accuracy, code reduction, and human effort.

# When to cite

1. When building or describing **multi-agent LLM systems** and needing a canonical framework reference.
2. When arguing that **conversation-as-control-flow** is a viable alternative to explicit pipeline orchestration.
3. When discussing **human-in-the-loop** LLM workflows — AutoGen's configurable human input modes are the cleanest published treatment.
4. When benchmarking **RAG with iterative context refinement** against static retrieval baselines.
5. When evaluating **agentic code generation** pipelines (OptiGuide results provide a concrete code-reduction benchmark).

---
[[LLM]]
[[Multi-Agent Systems]]
[[Prompt Engineering]]
[[RAG]]
[[Generative AI]]
[[GPT]]

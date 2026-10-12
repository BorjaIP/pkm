---
title:  The End of Software Engineering - How AI Agents Are Fundamentally Restructuring the Software Paradigm
created: Monday 12th October 2026 19:10
aliases: 
tags:
  - agents
  - llm
  - code-generation
---
- https://arxiv.org/html/2606.05608v1
- Source: arxiv

---

# TL;DR

A position paper arguing that **AI agents**, where an LLM generates decision logic at runtime and code is only a temporary tool, restructure software delivery and give rise to **Agentic Engineering** as a new discipline.

# Summary

Traditional software engineering encodes every decision rule in static code, which hits a **complexity barrier** because human capacity is fixed while interaction paths grow combinatorially. The paper contrasts this with agent systems in which the LLM produces logic at runtime, replacing "AI → Software → Result" with **"Agent → Result"**, and traces delivery from licensed software to SaaS to **Agent-as-a-Service**. It proposes a four-stage roadmap (2023 to 2028+), names four open challenges (context drift, error propagation, weak technical-debt awareness, incomplete verification) and cites benchmark and pilot evidence reported by others; the superiority claim is theoretical and the main pilot is a single vendor-blog study.

# Key contributions

1. Argues from first principles that **agents scale better** than human-encoded software as complexity grows.
2. Frames agent-based delivery as a **paradigm shift** comparable to the move from on-premise software to SaaS.
3. Defines **Agentic Engineering**, where humans act as intent architects, coordinators and auditors, and contrasts it with traditional software engineering.
4. Lays out a **four-stage evolutionary roadmap** and practical recommendations for practitioners, researchers and organizations.
5. Collects reported evidence: **SWE-bench Verified** (an open 72B model resolving 30.2% of issues versus 31.8% for GPT-4o), a **LangChain multi-agent debugging pilot** (root-cause time down 93%), and **EvoClaw** (success falling from over 80% on isolated tasks to at most 38% in continuous software evolution).

# When to cite

1. When arguing that **software delivery is shifting from SaaS to agent-based services** and what that means for engineering roles.
2. When discussing why **long-horizon software evolution** is much harder for agents than isolated tasks (the EvoClaw gap).
3. When you need a **definition of Agentic Engineering** or a roadmap of how agent capabilities may mature.
4. When listing the **open problems of coding agents**: context drift, error propagation, technical debt and verification.

---
[[AI Agents]] [[LLM]] [[Artificial Intelligence|AI]] [[Harness Engineering]] [[Software Architecture]]
[[SWE-CI Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration]]
[[TDFlow Agentic Workflows for Test Driven Software Engineering]]
[[AutoGen - Enabling Next-Gen LLM Applications via Multi-Agent Conversation]]
[[REACT - SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS]]
[[How AI Impacts Skill Formation]]

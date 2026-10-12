---
title: State of prompting and reasoning
created: Monday 12th October 2026 18:45
aliases:
tags:
  - archived
  - agent
  - prompt-engineering
status: active
source: digest
query: What do I know about prompt engineering, reasoning models and tool-using agents?
---

> **Status: active** | Source: digest of vault notes
>
> Synthesis of what the vault says. Each claim cites the note it comes from.

# Question

What do I know about prompt engineering, reasoning models and tool-using agents?

# Answer

**Techniques.** Zero-, one- and few-shot, chain-of-thought, iterative, negative, hybrid prompting and prompt chaining are introduced with examples in [[8 Types of Prompt Engineering]]; a broader catalogue (self-consistency, ReAct, ART, PAL, RAG and more) is in [[Prompt-engineering-guide]]. Hub: [[Prompt Engineering]].

**Reasoning models.** They plan internally: keep prompts short, skip "think step by step", state constraints and success criteria, and use planner/doer splits between reasoning and GPT models ([[Reasoning best practices]]).

**Agents and tools.** Papers: [[REACT - SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS]], [[ART - Automatic multi-step reasoning and tool-use for large language models]], [[Toolformer - Language Models Can Teach Themselves to Use Tools]], [[Chameleon - Plug-and-Play Compositional Reasoning with Large Language Models]]; an overview of frameworks in [[Prompting Frameworks for Large Language Models - A Survey]]. Agent basics in [[AI Agents]] and the protocol layer in [[MCP]].

**Using LLMs as assistants.** An early experiment with ChatGPT writing Terraform and explaining Istio shows both the speed-up and the unsafe defaults ([[I tried… Using ChatGPT for FuNn as a DevOps Engineer]]).

**Evaluation and limits.** Evaluate prompts and systems with datasets and LLM-as-judge ([[Evaluating Large Language Model (LLM) systems - Metrics, challenges, and best practices]]); hallucination cannot be removed entirely ([[LLMs Will Always Hallucinate, and We Need to Live With This]]). Language matters for cost and limits ([[Why is GPT-3 15.77x more expensive for certain languages]]).

# Pages Consulted

[[Prompt Engineering]], [[AI Agents]], [[LLM]] and the notes cited above.

# Sources Cited

Original URLs are on each cited web note and paper note.

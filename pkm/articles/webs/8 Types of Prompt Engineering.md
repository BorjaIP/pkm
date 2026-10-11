---
title:  8 Types of Prompt Engineering
created: Saturday 12th April 2025 18:57
aliases: 
tags:
  - prompt-engineering
  - llm
---
- https://medium.com/@amiraryani/8-types-of-prompt-engineering-5322fff77bdf
- Type: article
- Source: Medium · Amir Aryani · Dec 2023

---

# TL;DR

Eight prompting styles, from zero-shot to prompt chaining, each demonstrated on Mistral by asking about Foundation Models.

# Summary

The article lists eight methods and runs one example prompt for each against the Mistral model. Zero-, one- and few-shot differ in how many examples accompany the task; chain-of-thought asks for step-by-step reasoning; iterative prompting refines a prompt based on the previous answer; negative prompting says what to avoid; hybrid prompting combines methods; prompt chaining feeds one output into the next prompt. It is an introductory survey with sample outputs rather than an evaluation.

# Key takeaways

1. **Zero-shot**: describe the task with no examples.
2. **One-shot and few-shot**: add one or a few (2-5) examples to fix format or context; the one-shot example also disambiguates (BERT the model vs a company).
3. **Chain-of-thought**: ask for the process step by step on multi-stage questions.
4. **Iterative prompting**: refine the question using the previous answer ("give more details on multimodal learning").
5. **Negative, hybrid and chained prompts**: exclude unwanted content, combine styles, or split a job into sequential prompts.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Prompt Engineering]] | Hub for all the techniques |
| [[LLM]] | Mistral used to generate the sample answers |
| [[Prompting Frameworks for Large Language Models - A Survey\|Prompting survey]] | Academic overview of prompting frameworks |

# When to use

1. When you need a **quick vocabulary of prompting methods**.
2. When choosing between **zero-shot, few-shot and chain-of-thought** for a task.
3. When teaching prompt basics with concrete example prompts.

# Caveats

- Introductory; no measurements, and one answer (few-shot robotics) shows the model ignoring the examples.

---
[[Prompt Engineering]] [[LLM]] [[Generative AI]]
[Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)
[[Prompt-engineering-guide]]
[[Reasoning best practices]]

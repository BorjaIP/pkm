---
title: Prompt Engineering
created: Saturday 12th April 2025 18:23
aliases:
  - Prompt
tags:
---
**Prompt Engineering** is the practice of **designing and refining input prompts** to optimize the output of generative AI models, especially large language models ([[LLM]]). It is a crucial skill that transforms raw model potential into useful, accurate, and task-specific results.
# Articles/Talks

- [[Awesome Prompt Engineering]]
- [[Awesome GPT Prompt Engineering]]
- [[8 Types of Prompt Engineering]]
- [[GPU optimized techniques for training transformer models at-scale]]
- [[Prompt-engineering-guide]]
# Prompt Types & Techniques

- [[Prompting Frameworks for Large Language Models - A Survey]]
## Zero-shot

This involves giving the AI a task without any prior examples. You describe what you want in detail, assuming the AI has no prior knowledge of the task.

> Prompt: “Explain what a large language model is.”
## One-shot

You provide one example along with your prompt. This helps the AI understand the context or format you’re expecting.

> Prompt: “A Foundation Model in AI refers to a model like GPT-3,  
> which is trained on a large dataset and can be adapted to various tasks.  
> Explain what BERT is in this context.”
## Few-shot

This involves providing a few examples (usually 2–5) to help the AI understand the pattern or style of the response you’re looking for.

> Prompt: “Foundation Models such as GPT-3 are used for natural language processing, while models like DALL-E are used for image generation.  
> How are Foundation Models used in the field of robotics?”
## Chain-of-thought (CoT)

Here, you ask the AI to detail its thought process step-by-step. This is particularly useful for complex reasoning tasks.

> Prompt: “Describe the process of developing a Foundation Model in AI, from data collection to model training.”
## Iterative Prompting

This is a process where you refine your prompt based on the outputs you get, slowly guiding the AI to the desired answer or style of answer.

> Initial Prompt: “Tell me about the latest developments in Foundation Models in AI.”
## Negative Prompting

In this method, you tell the AI what not to do. For instance, you might specify that you don’t want a certain type of content in the response.

> Prompt: “Explain the concept of Foundation Models in AI without mentioning natural language processing or NLP.”
## Hybrid Prompting

Combining different methods, like few-shot with chain-of-thought, to get more precise or creative outputs.

> Prompt: “Like GPT-3, which is a versatile model used in various language tasks, explain how Foundation Models are applied in other domains of AI, such as computer vision.”
## Prompt Chaining

Breaking down a complex task into smaller prompts and then chaining the outputs together to form a final response.

> First Prompt: “List some examples of Foundation Models in AI.”
> Second Prompt: “Choose one of these models and explain its foundational role in AI development.”
# Prompt management platforms
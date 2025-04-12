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
- [[Google - Prompt Engineering]]
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
## Role prompting

Role prompting is a technique in prompt engineering that involves assigning a specific role to the gen AI model. This can help the model to generate more relevant and informative output, as the model can craft its responses to the specific role that it has been assigned.

> I want you to act as a travel guide. I will write to you about my location and you will suggest 3 places to visit near me. In some cases, I will also give you the type of places I will visit.
> My suggestion: "I am in Amsterdam and I want to visit only museums."
> Travel Suggestions:

## Tree of Thoughts (ToT)

Now that we are familiar with chain of thought and **self-consistency prompting**, let’s review Tree of Thoughts (ToT). It generalizes the concept of CoT prompting because it allows LLMs to explore multiple different reasoning paths simultaneously, rather than just following a single linear chain of thought.
## ReAct (reason & act)

Reason and act (ReAct) prompting is a paradigm for enabling LLMs to **solve complex tasks using natural language reasoning combined with external tools** (search, code interpreter etc.) allowing the LLM to perform certain actions, such as interacting with external APIs to retrieve information which is a first step towards agent modeling.

ReAct mimics how humans operate in the real world, as we reason verbally and can take actions to gain information. ReAct performs well against other prompt engineering approaches in a variety of domains.
# Frameworks

# ChatGPT

| Task                            | Prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Summarize Long Documents        | Read this [insert link or upload document] and provide a detailed summary highlighting the main points, conclusions, and any recommendations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Professional Emails             | Write a professional email to [recipient’s name] regarding [subject matter], ensuring to cover all key points such as [key point 1], [key point 2], and [key point 3].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Generate Reports from Data      | Generate a comprehensive report from the attached spreadsheet data, focusing on key metrics like sales growth, customer acquisition costs, and profit margins over the last quarter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Create PowerPoint Presentations | Design a PowerPoint presentation based on the contents of the provided document. Include slides for introduction, key findings, data analysis, and conclusion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Code Snippet Explanation        | Explain the following code snippet in simple terms and suggest any improvements for efficiency. [insert code snippet]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Research and Summarize          | Research the topic [specific topic] and provide a concise summary including key facts, recent developments, and major players in the field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Create Perfect Prompt           | Be my prompt creator, assisting me to create optimal prompts. First, inquire about the prompt topic, then improve through iterations, generating: a) a revised prompt, b) suggestions, and c) questions for clarity and enhancement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Code Request                    | You're a Python developer with experience in creating data-driven visualizations. Develop a Python script to build a very modern looking (clean fonts, colors), interactive dashboard that: <br>- Displays the evolution of the key figures in this PDF document with appropriate type of charts, filters, etc. <br>- Create as many charts as necessary, one below the other. <br>- Don't hesitate to compare current figures with previous periods <br>- Use Plotly Dash for the dashboard. <br>- Ensure the code is compatible with Replit. <br>The dashboard should include dynamic features like hover effects, filters by year, and interactive legends. Format the script with comments explaining key sections and use a clear, professional tone throughout the code. Think step by step to avoid code errors. Just write the full script. |
## Reasoning (OpenAI, Anthropic, Claude)

- [[Reasoning best practices]]

Prompt examples:

```bash
<context>
Please analyze the writing style, tone, and structure in the following examples. Focus on elements like vocabulary choice, sentence complexity, pacing, and overall voice.
</context>
‹examples>
[Insert your writing samples here, add delimiters between them as well]
</examples>
<instruction>
Generate a [type of content, e.g., "informative article" or "blog post"] about [specific topic]. The content should match the style, tone, and structure of the provided examples. Make sure it is original, engaging, and suitable for [mention the target audience or purpose].
</instruction>
```

```bash
<context>
Analyze the style writing and structure in the following information. Focus on a simple vocabulary, short sentences and a clear idea. Save that information for the instruction. 
</context>
<information>
[Information related with something you need to execute]
</information>
<instruction>
Please create a summary and a cover letter. Focus on a good presence and a clear idea for a AI DevOps position.
</instruction>
```

```bash
<variables>
[TEXT]=
[ROLE]=
</variables>
<context>
I just finished writing a [TEXT] for a [ROLE] position. I will share the [TEXT] in <information> section.
</context>
<information>
[Information related with something you need to execute]
</information>
<instruction>
Your task is to look for and correct all misspelled words and grammatical errors, check for proper punctiation and capitalizacion, and imprive any readability issues. Also output a table that shows everything that you have changed. Do not hallucinate.
</instruction>
```

```bash
<variables>
[ROLE]=
[ACTION]=
</variables>
<context>
You are and expert in [ROLE]. I will share the <information> you will use.
</context>
<information>
[Information related with something you need to execute]
</information>
<instruction>
Explain it in a correct and accurate way without leaving any room for mistakes or misunderstandings. Use colloquial language. Use external sources to improve the result. Use examples to understand it. Create a final section with a summary. Do not hallucinate.
</instruction>
```

```bash
<context>
You are an expert programming AI assistant who prioritizes minimalist, efficient code. You plan before coding, write idiomatic solutions, seek clarification when needed, and accept user preferences even if suboptimal.
</context>
<planning_rules> 
- Create 3-step numbered plans before coding
- Display current plan step clearly
- Ask for clarification on ambiguity
- Optimize for minimal code and overhead
- </planning_rules>
<format_rules>
- Use code blocks for simple tasks
- Split long code into sections
- Create artifacts for file-level tasks
- Keep responses brief but complete
</format_rules>
OUTPUT: Create responses following these rules. Focus on minimal, efficient solutions while maintaining a helpful, concise style.
```

## AI Agent

```bash
You are an advanced AI model designed to solve complex problems by applying a combination of sophisticated reasoning techniques. To ensure your outputs are accurate, logical, and optimized, follow these structured instructions:

1. Break Down the Task: Start by using Chain of Thought (CoT reasoning. Clearly articulate each logical step in solving the problem, treating each as a distinct part of the overall process. Verify each step before moving on, ensuring that your reasoning remains coherent and well-structured.
   
2. Rationalize Each Step: As you progress, apply Step-by-Step Rationalization (STaR). Provide clear, logical justifications for every decision. Balance the depth of your explanations with the need for efficiency, focusing on key points that are critical to solving the problem effectively.
   
3. Optimize Your Approach: Integrate _A Search_* principles into your reasoning. Evaluate the efficiency of each potential path, using heuristic-like guidance to select the most direct and cost-effective strategy. Adjust your approach based on the complexity of the task, always aiming for the most optimal solution.
   
4. Consider Multiple Solutions: Utilize Tree of Thoughts (ToT) to explore multiple potential approaches in parallel. Evaluate each path using the principles of _A Search_*, prioritizing those that show the most promise. After thorough evaluation, converge on the solution that best addresses the problem.
   
5. Simulate Adaptive Learning: Reflect on your decisions within this session as if you were learning from each outcome. Prioritize strategies that would likely lead to the best results, simulating the core principles of **Q-Learning** within the context of this interaction.
   
6. Continuously Monitor Your Process: Engage in *Process Monitoring throughout your reasoning. Continuously assess your progress, ensuring each step aligns with the overall goal. Use this feedback to refine your approach, making adjustments as needed to stay on track toward the desired outcome.

Final Instruction:

By following these instructions, you will ensure that your problem-solving approach is methodical, well-reasoned, and optimized for accuracy and efficiency. Your goal is to deliver the most logical, effective, and comprehensive solution possible by fully integrating these advanced reasoning techniques.
```
## ChatGPT Prompt Framework

![[prompt_frameworks.png]]

## Vercel v0 system prompt

- [[FULL v0, Cursor, Manus, Same.dev & Lovable System Prompts & AI Models]]
## Coding

```
1. Embrace Simplicity Over Cleverness

- Write code that's immediately understandable to others
- If a solution feels complex, it probably needs simplification
- Optimize for readability first, performance second unless proven otherwise
- Avoid premature optimization

2. Focus on Core Functionality

- Start with the minimum viable solution
- Question every feature: "Is this really necessary?"
- Build incrementally based on actual needs, not hypothetical ones
- Delete unnecessary code and features

3. Leverage Existing Solutions

- Use standard libraries whenever possible
- Don't reinvent the wheel
- Choose well-maintained, popular libraries for common tasks
- Keep dependencies minimal but practical

4. Function Design

- Each function should have a single responsibility
- Keep functions short (typically under 20 lines)
- Use descriptive names that indicate purpose
- Limit number of parameters (3 or fewer is ideal)

5. Project Structure

- Keep related code together
- Use consistent file organization
- Maintain a flat structure where possible
- Group by feature rather than type

6. Code Review Guidelines

- Review for simplicity first
- Question complexity and overengineering
- Look for duplicate code and abstraction opportunities
- Ensure consistent style and naming conventions

7. Maintenance Practices

- Regularly remove unused code
- Keep dependencies updated
- Refactor when code becomes unclear
- Document only what's necessary and likely to change

Remember:

- Simple code is easier to maintain and debug
- Write code for humans first, computers second
- Add complexity only when justified by requirements
- If you can't explain your code simply, it's probably too complex
```
# Prompt management platform
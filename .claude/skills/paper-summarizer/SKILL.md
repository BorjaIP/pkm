---
name: paper-summarizer
description: Summarizes academic and research papers and saves a structured Markdown note to the PKM vault at pkm/articles/papers/. Use this skill whenever the user shares a research paper, academic article, preprint, or scientific document — or provides a URL to one — and wants a summary, key points, takeaways, or just wants it added to their notes. Trigger on phrases like "summarize this paper", "add this to my notes", "what does this paper say", "break down this paper", "key findings", or any time the user pastes an abstract or paper URL.
---

You are an expert summarizer of research and academic papers. Your goal is to read the paper carefully and produce a well-structured note saved to the PKM vault.

## Workflow

1. **Get the content** — If the user provides a URL, fetch or read the paper. If they paste content, use that. Ask for the title if unclear.
2. **Identify metadata** — Extract the paper title, source URL(s), and the source platform (arxiv, acm, medium, github, openreview, etc.).
3. **Generate tags** — Follow the tagging rules below. Read the obsidian-helper skill to search for existing tags before creating new ones.
4. **Find WikiLinks** — Use the obsidian-helper skill to search for existing vault notes that relate to the paper's topics.
5. **Write the note** — Follow the output format below.
6. **Save the note** — Write to `pkm/articles/papers/<Paper Title>.md` using the template below.

## Tagging rules

Run this first to resolve the CLI path and list existing tags (reuse the obsidian-helper skill for the full path-detection snippet):

```bash
"$OBS" vault=pkm tags 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

Reuse an existing tag whenever it fits. Only introduce a new tag when no existing one covers the concept. Up to 5 tags total:

- Prefer specific over generic — `rag` beats `ai`, `fine-tuning` beats `ml`
- Use kebab-case, all lowercase (`prompt-engineering`, `knowledge-graph`, `vector-db`)
- Skip a tag if a more specific one already covers it
- Prefix company names with `co-` (`co-openai`, `co-google`, `co-meta`)
- Prefix organization/lab names with `org-` (`org-deepmind`, `org-huggingface`)

## Note template

```
---
title:  <Paper Title>
created: <date as "Weekday DDth Month YYYY HH:mm", e.g. "Monday 24th April 2023 19:20">
aliases:
tags:
  - <tag1>
  - <tag2>
  - <tag3>
---
- <primary URL — PDF or paper page>
- Source: <platform name, e.g. arxiv, acm, medium, github, openreview>

---

# TL;DR

<One sentence. The single core contribution of the paper — what it proposes or proves. No filler.>

# Summary

<Dense prose, ~80 words. Problem → approach → key result. Do not mention authors. Start with the problem or the finding, not with "This paper...".>

# Key contributions

<Numbered list of 3–5 items. Only what is genuinely NEW in this paper: novel method, dataset, benchmark, architecture, or theoretical insight. Each item starts with an action verb (Proposes, Introduces, Shows, Demonstrates, Establishes). Bold the name of the contribution or technique.>

# When to cite

<Numbered list of 3–4 specific situations where you would reference this paper. Frame as questions this paper answers or claims it supports, e.g. "When explaining why X works", "When arguing that Y is more efficient than Z". This makes retrieval actionable.>

---
<WikiLinks to related vault notes, one per line, e.g. [[LLM]] [[Artificial Intelligence|AI]]>
```

## Quality notes

- Section headers use only the first letter capitalized, no colon at the end.
- Leave one blank line between each section header and its content.
- **TL;DR must be one sentence** — if it takes two, split the less important idea into Key contributions.
- Summary is information-dense prose — avoid filler like "the authors propose" or "this paper presents". Start with the problem or the finding.
- Key contributions cover only novelty — do not list things the paper reuses or builds on without modification.
- When to cite is the most retrieval-critical section: write it so a future search for "papers about X" will match this note.
- Do not start consecutive list items with the same word.
- If the paper has a companion GitHub repo or project page, add it as a second bullet before `Source:`.
- **Bold key terms** throughout all sections — technical concepts, method names, metrics, and findings a reader would scan for. Aim for 2–4 bolded terms per section.

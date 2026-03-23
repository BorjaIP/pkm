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
5. **Write the summary** — Follow the output format below.
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

# Summary

<A single paragraph of ~100 words. Explain what problem the paper addresses, the approach taken, and the key results. Do not mention authors by name. Write for a technical reader who wants the essence without reading the full paper.>

# Main points

<Numbered list of 5 points, max 16 words each. Cover: the core problem, the proposed method, key results, limitations or scope, and broader implications.>

# Takeaways

<Numbered list of 5 actionable or intellectual insights a reader should walk away with. Focus on what's useful or surprising, not just what was done.>

---
<WikiLinks to related vault notes, one per line, e.g. [[LLM]] [[Artificial Intelligence|AI]]>
```

## Quality notes

- Section headers use only the first letter capitalized, no colon at the end.
- Leave one blank line between each section header and its content.
- The Summary should be information-dense — avoid filler like "the authors propose" or "this paper presents". Start with the problem or the finding.
- Main points and Takeaways must not overlap — if a point is in one, rephrase or replace it in the other.
- Do not start consecutive list items with the same word.
- If the paper has a companion GitHub repo or project page, add it as a second bullet before `Source:`.
- **Bold key terms** throughout the Summary, Main points, and Takeaways — technical concepts, method names, metrics, and findings that a reader would want to scan for. Aim for 2–4 bolded terms per section, enough to aid skimming without saturating the text.

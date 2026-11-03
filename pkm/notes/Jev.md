---
title:  Jev
created: Sunday 1st November 2026 12:00
aliases:
  - Jev AI
  - TypeSafe Jev
tags:
  - llm
  - agents
  - ai
part_of:
  - "[[LLM]]"
uses:
  - "[[AI Agents]]"
---
**Jev** is a non-generative "decision model" from TypeSafe AI. It never writes text: you give it a state and a typed question (pick one option, score, or yes/no) and it returns an answer with a calibrated confidence. It is meant to sit next to a chat [[LLM]] and make the cheap, structured decisions around it, such as routing, relevance filtering and verification, so the large model only generates.

## How it works

- Input is context plus a question with a fixed set of possible answers; output is the chosen answer and a confidence.
- It is a cloud API (about 0.4 s per routing decision according to the Hermes skills repo). Eligible, redacted input leaves the machine, so check what each tool sends before using it on private code.
- Access goes through a TypeSafe key, or providers such as OpenRouter, Vercel AI Gateway and OpenCode Zen.
- When the key is missing, the call times out or confidence is low, the tools below fall back to safe defaults (keep the current model, return the original list).

## Typical uses

| Use | What Jev decides |
| --- | --- |
| Model routing | Which model is good enough for each turn |
| Memory | Which retrieved passages are worth reading, and which hide instructions |
| Compaction | Which turns to keep when a transcript must be cut |
| Skill selection | Which installed skill a turn needs, if any |
| Code search | Which folders, files and declarations are relevant to a question |

## Tools built on Jev

| Tool | Description | Install |
| --- | --- | --- |
| [jevgrep](https://github.com/dzhng/jevgrep) | CLI (`jg`) that finds relevant files and source excerpts for natural-language code questions; returns evidence for the calling agent, not an answer | `npm install -g @dzhng/jevgrep`, then `jg auth` and `jg skill` |
| [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) | Jev-powered routing, memory, compaction and skill selection for [[Hermes]], Claude Code and Codex; 13 plain `SKILL.md` files | `git clone`, then `python3 install.py` and `jev setup-key` |

- **jevgrep** needs Node.js 22+ and understands declarations in Python, TypeScript/JavaScript, Go and Rust. It skips hidden, dependency, build, binary and likely credential files by default.
- **hermes-jev-skills** integrates fully with [[Hermes]] through a plugin; for Claude Code and Codex it installs the skills and edits `~/.claude/CLAUDE.md` after backing it up (`--no-claude-md` skips that). Start routing in shadow mode (`/jev routing shadow`), which logs decisions without switching models.

## Caveats

- Most numbers (speed, cost cuts) come from TypeSafe and the tool authors; independent verification was not found.
- The hermes-jev-skills repo itself reports that a Jev-digest handoff recalled less than a plain transcript, so its default hands off the whole dialogue.
- Background: TypeSafe came out of stealth in September 2026 with a reported $40M seed ([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/09/jev-explained/)).

---
Related: [[Hermes]], [[AI Agents]], [[Agent Skills]], [[LLM]], [[Terminal]]

---
title: Agent Skills
created: Tuesday 13th October 2026 10:00
aliases:
  - Skills
tags:
  - agents
  - ai
part_of:
  - "[[AI Agents]]"
---
Agent Skills are self-contained folders (a `SKILL.md` plus scripts and resources) that an AI coding agent loads on demand for specialized tasks. They work across Claude Code, Codex, Cursor and others. Install with `npx skills add <repo>` or as a Claude Code plugin; see [[Claude]] for the marketplace flow and [[AI Agents]] for the wider tooling.

## Official and registries

| Skill | Description | Install |
| ----- | ----------- | ------- |
| [anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic repository of Agent Skills — self-contained skill folders Claude loads dynamically for specialized tasks. |  |
| [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | Curated collection of 5,400+ OpenClaw skills filtered and categorized from the official OpenClaw Skills Registry. |  |

## Development workflow

| Skill | Description | Install |
| ----- | ----------- | ------- |
| [create-agentsmd](https://skills.sh/github/awesome-copilot/create-agentsmd) | Generates standardized AGENTS.md files to help AI coding agents understand and work with your repository. Covers setup, workflow, testing, code style, and deployment. Compatible with 20+ AI coding tools. | `npx skills add https://github.com/github/awesome-copilot --skill create-agentsmd` |
| [agent-governance](https://skills.sh/github/awesome-copilot/agent-governance) | Declarative policies, intent classification, and audit trails for controlling AI agent tool access and behavior. Includes threat detection, rate limiting, trust scoring, and immutable audit logs. | `npx skills add https://github.com/github/awesome-copilot --skill agent-governance` |
| [agentic-eval](https://skills.sh/github/awesome-copilot/agentic-eval) | Iterative evaluation and refinement patterns for improving AI agent outputs through self-critique loops. Supports reflection, evaluator-optimizer architecture, and test-driven refinement. | `npx skills add https://github.com/github/awesome-copilot --skill agentic-eval` |
| [team-communication-protocols](https://skills.sh/wshobson/agents/team-communication-protocols) | Structured messaging protocols for coordinating agent teams through direct messages, broadcasts, plan approvals, and graceful shutdown. Includes teammate discovery and anti-pattern documentation. | `npx skills add https://github.com/wshobson/agents --skill team-communication-protocols` |
| [code-reviewer](https://skills.sh/google-gemini/gemini-cli/code-reviewer) | Automated code review for local changes and remote PRs with structured analysis across correctness, maintainability, security, efficiency, and test coverage. Supports GitHub CLI checkout. | `npx skills add https://github.com/google-gemini/gemini-cli --skill code-reviewer` |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Claude Code skill that implements persistent markdown-based planning using a three-file pattern (task_plan.md, findings.md, progress.md) to maintain structured task tracking across context resets. |  |
| [eidos](https://github.com/agenticnotetaking/eidos) | Claude Code plugin that keeps Markdown specs and code in sync for spec-driven development | `/plugin marketplace add agenticnotetaking/eidos` then `/plugin install eidos@eidos` |

## Design and frontend

| Skill                                                               | Description                                                                                                           | Install                                                                                                                          |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [impeccable](https://github.com/pbakaus/impeccable)                 | Design skill system for AI coding assistants; teaches typography, color, and UX anti-patterns via 20+ slash commands. |                                                                                                                                  |
| [taste-skill](https://github.com/Leonxlnx/taste-skill)              | Portable skills that steer AI coding agents away from generic frontend design                                         | `npx skills add https://github.com/Leonxlnx/taste-skill`                                                                         |
| [ai-design-skills](https://github.com/elayadesign/ai-design-skills) | Design skills for AI coding tools, currently a landing-page-design skill                                              | Copy the skill folder into `.claude/skills`                                                                                      |
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides)  | Skill that generates HTML slide presentations from scratch or converts PowerPoint files                               | `/plugin marketplace add https://github.com/zarazhangrui/frontend-slides` then `/plugin install frontend-slides@frontend-slides` |
| [anatomy](https://github.com/wheresryan22/anatomy)                  | Agent skill that explains a technical idea as an interactive isometric figure (SVG, WebGL)                            | `npx skills add wheresryan22/anatomy -g -a claude-code`                                                                          |
| [archify](https://github.com/tt-a1i/archify)                        | Agent skill that turns an idea, plan or codebase into an interactive architecture diagram                             | `npx skills add tt-a1i/archify -g`                                                                                               |

## Domain-specific

| Skill | Description | Install |
| ----- | ----------- | ------- |
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 142 ready-to-use scientific research skills for AI coding agents covering bioinformatics, genomics, drug discovery, proteomics, and multi-omics. | `npx skills add https://github.com/K-Dense-AI/scientific-agent-skills` |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | 40+ marketing skills for Claude Code and other AI coding agents: conversion optimization, copywriting, SEO, paid ads, analytics, A/B testing, retention, and growth engineering. |  |
| [Data-engineering-skills](https://github.com/AltimateAI/data-engineering-skills) | A curated list of skills and resources for data engineers |  |
| [obsidian-skills](https://github.com/kepano/obsidian-skills) | Agent skills (by Obsidian's CEO) for Claude Code to read, write, and navigate Obsidian vaults. |  |
| [Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Claude Code skill bundle for bug hunting and red-team work | `/plugin install claude-bughunter@elementalsouls` |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Claude Code skills for academic research, writing, peer review and revision | `/plugin install academic-research-skills` |
| [personal-os-skills](https://github.com/ArtemXTech/personal-os-skills) | Claude Code skills linking Obsidian with meeting notes, voice dictation, tasks and NotebookLM | `/plugin marketplace add ArtemXTech/personal-os-skills` |

---
Related: [[AI Agents]], [[Claude]], [[OpenClaw]], [[Data Engineering]], [[Software Design Methodology]], [[Obsidian]]

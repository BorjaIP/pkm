---
name: pkm-tool-adder
description: Adds a new tool, software, program, or service to the PKM vault by finding the right existing note and inserting a properly formatted table entry. Use this skill whenever the user mentions a tool, app, CLI, framework, service, or platform they want to save or catalog — even phrased casually like "add X to my notes", "save this tool", "I want to remember this", "note down this software", "add this to my vault", or just naming a tool and asking where it goes. ALWAYS invoke this skill when a tool or software is the subject of a "save/add/catalog/note" request. Do NOT wait for the user to say "PKM" explicitly — any intent to catalog a piece of software counts.
---

You are cataloging a tool into a carefully organized personal knowledge base. Your job is to find the single best existing note for it — the vault has 149 notes covering a rich hierarchy of domains — and insert a well-formatted entry. Creating a new note is the last resort, not the default.

## Workflow

### 1. Understand the tool

Identify:
- **Name** — what it's called
- **URL** — official site, GitHub repo, or docs page (ask the user if not provided)
- **One-line description** — what it does, in plain terms
- **Domain** — what technology area it belongs to (containers, ML, cloud, databases, DevOps, etc.)

If the user hasn't provided a URL or description, ask before proceeding. A good entry needs both.

### 2. Find the best existing note

Use the obsidian-helper skill to resolve the `$OBS` path, then search for candidates:

```bash
# Search by the tool's domain keywords
"$OBS" vault=pkm search query="<domain keyword>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

Run 2–3 searches with different keywords (e.g. the technology category, a related umbrella term, the problem the tool solves). The vault's main domain areas include:

| Domain | Key notes to consider |
|---|---|
| Cloud / infra | Cloud, AWS, GCP, Azure, IaC, Terraform, Ansible |
| Containers / K8s | Containers, Docker, Kubernetes, Helm, Istio |
| Data / databases | Databases, Data Engineering, Data Platforms, BigQuery, PostgreSQL, MongoDB |
| ML / AI | Machine Learning, MLOps, LLM, Generative AI, AI Agents, Deep Learning |
| Observability / ops | Observability, DevOps, Prometheus, Elasticsearch |
| Security | Security, IAM, Vault, OPA, ZTN |
| Web / APIs | Web, API, FastAPI, gRPC |
| Developer tooling | Tools, Git, VSCode, Python, Linux, MacOS |
| Package managers | Chocolatey, Winget, Nix, Homebrew-adjacent areas |
| Networking | DNS, VPC, Wireguard, Remote Access |
| BI / analytics | Business Intelligence, SQL, TSDB |

Read the top 2–3 candidate notes to confirm they are a good fit before choosing one.

### 3. Choose the best note — decision rules

Pick the **most specific** note that already covers this domain:
- A Kubernetes monitoring tool → `Kubernetes.md` (not `Observability.md`)
- A PostgreSQL extension → `PostgreSQL.md` (not `Databases.md`)
- A general-purpose CLI with no clear home → `Tools.md`
- A cloud provider-specific service → the provider note (e.g. `AWS.md`)

If two notes are equally valid, prefer the one that already has a tools table (scan for `| [` in the note content).

Tell the user which note you chose and why, before making the edit.

### 4. Insert the entry

The standard format for a tools table row is:

```markdown
| [ToolName](https://url)  | One-sentence description of what it does |
```

Rules:
- Pad with spaces so the `|` columns roughly align with the existing table (look at the table in the note to match width)
- The description is factual and concise — max ~15 words, no marketing language
- Use the tool's official or most canonical name (check the GitHub repo name if unsure)
- Add the row at the **end** of the existing tools table, not in the middle

Use the obsidian-helper skill to read the note first, then write the updated content back.

### 5. If no note fits well

If after searching you genuinely cannot find a note where this tool belongs (the tool covers a domain not represented in the vault), **do not silently add it to `Tools.md`**. Instead:

1. Explain to the user which notes you checked and why none fit
2. Propose a new note title — it must be **generalizing** (covering a whole domain or technology category), not a one-tool note. Examples of good new note names: `Package Managers`, `Terminal Emulators`, `Diagram Tools`, `Workflow Automation`. A bad new note name: `Warp.md` (too specific — should live in a `Terminal Emulators.md` note).
3. Describe what the new note would cover and what other tools/concepts could live in it
4. **Ask the user to confirm** before creating it. Show the proposed note structure.

If the user confirms, create the note following this template:

```markdown
---
title: <Note Title>
created: <Weekday DDth Month YYYY HH:mm>
aliases:
tags:
  - <relevant-tag>
---
<1–2 sentence definition of the domain this note covers.>

| Tool | Description |
| ---- | ----------- |
| [ToolName](https://url) | Description |
```

Use the obsidian-helper skill to check existing tags before assigning new ones, and to search for related notes to add WikiLinks at the bottom.

## Quality checklist

Before finishing, verify:
- [ ] The chosen note is the most specific fit (not a generic fallback)
- [ ] The URL is present and correct
- [ ] The description is factual, not marketing copy
- [ ] The table row is properly formatted and aligned with the rest of the table
- [ ] You told the user where the tool was added

---
name: obsidian-helper
description: Provides Obsidian vault integration using the Obsidian CLI. Use this skill whenever you need to interact with the PKM vault — listing existing tags before creating new ones, searching for notes to WikiLink, reading note content, creating or updating notes, or setting frontmatter properties. Invoke this skill proactively when creating or editing vault notes to ensure consistency with existing content.
---

Always target the vault with `vault=pkm`. Strip warning lines from output with `2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"`.

## Resolving the Obsidian CLI path

Detect the OS first, then set `OBS` accordingly. Run this once at the start of any session:

```bash
case "$(uname -s)" in
  Darwin)
    OBS="/Applications/Obsidian.app/Contents/MacOS/Obsidian"
    ;;
  Linux)
    # Try common locations in order
    OBS=$(command -v obsidian 2>/dev/null)
    if [ -z "$OBS" ]; then
      # Flatpak
      flatpak info md.obsidian.Obsidian &>/dev/null && \
        OBS="flatpak run md.obsidian.Obsidian"
    fi
    if [ -z "$OBS" ]; then
      # AppImage in common locations
      OBS=$(find "$HOME" /opt /usr/local -name "Obsidian*.AppImage" 2>/dev/null | head -1)
    fi
    ;;
  MINGW*|CYGWIN*|MSYS*)
    # Windows (Git Bash / MSYS2)
    OBS="${LOCALAPPDATA}/Obsidian/Obsidian.exe"
    ;;
esac

echo "OBS=$OBS"
```

On **Windows with bash** (Git Bash / MSYS2), `$LOCALAPPDATA` resolves automatically to `C:\Users\<user>\AppData\Local`. Never hardcode the username or drive letter.

## Common operations

### List all existing tags

```bash
"$OBS" vault=pkm tags 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

Returns all tags prefixed with `#`. Strip the `#` when writing tags in frontmatter.

### Search notes by keyword (for WikiLink candidates)

```bash
"$OBS" vault=pkm search query="<keyword>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

Returns file paths. Use the filename (without `.md`) as the WikiLink target.

### Search with context lines

```bash
"$OBS" vault=pkm search:context query="<keyword>" limit=5 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

### Read a note

```bash
"$OBS" vault=pkm read path="<folder/note.md>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

### Create a new note

```bash
"$OBS" vault=pkm create path="<folder/note.md>" content="<content>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

### Set a frontmatter property

```bash
"$OBS" vault=pkm property:set path="<folder/note.md>" name="<property>" value="<value>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

### List backlinks to a note

```bash
"$OBS" vault=pkm backlinks file="<Note Title>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

### List outgoing links from a note

```bash
"$OBS" vault=pkm links file="<Note Title>" 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

### Get tag info (files using a tag)

```bash
"$OBS" vault=pkm tag name="<tag>" verbose 2>&1 | grep -v "^20[0-9][0-9]" | grep -v "installer"
```

## WikiLink format

- `[[Note Title]]` — links by filename (without .md), resolved by Obsidian's shortest-path
- `[[Note Title|Display Text]]` — custom display text
- Only link to notes that actually exist in the vault (verify with `search` or `files`)

## Tags format in YAML frontmatter

```yaml
tags:
  - tag-one
  - tag-two
```

Never use `tags: tag1, tag2` — this renders incorrectly in Obsidian.
Tags are lowercase kebab-case. Check existing tags first and reuse when they fit.

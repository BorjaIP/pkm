---
title:  Browser Automation
created: Thursday 12th November 2026 19:46
aliases:
  - Browsers for agents
  - Agent browsers
tags:
  - agents
  - web-automation
  - scraping
---
**Browser automation for agents** means driving a real browser (click, type, read the page) from code or from an LLM. The tool you pick on top of the browser is rarely the bottleneck; **the browser's fingerprint and where its state lives** are. Related notes: [[Data Extraction]], [[AI Agents]], [[MCP]], [[Testing]].

## Choosing a browser

| Option | Kind | Use it for | Limit |
| ------ | ---- | ---------- | ----- |
| [Playwright](https://playwright.dev) | Library (Chromium, Firefox, WebKit) | Deterministic flows on sites without strict bot protection; `storage_state` keeps a login | Stock Chromium is fingerprinted and blocked by strict WAFs |
| [Patchright](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright) | Patched Playwright | Stealth with the same API | Still Chromium: tested blocked on an Akamai-protected shop |
| [Camoufox](https://camoufox.com) | Firefox anti-detect build | Strict anti-bot sites; persistent profile on disk | Firefox: **no CDP**, use the Playwright API |
| [Lightpanda](https://github.com/lightpanda-io/browser) / [Obscura](https://github.com/h4ckf0r0day/obscura) | Light headless engines | Fast public reads, no Chromium | Obscura opens a new context per CDP connection, so no state survives between processes |
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP over Chrome (Puppeteer) | Debugging, network and performance traces, attaching to a running Chrome | Needs a Chrome to attach to |
| [Browser-use](https://github.com/browser-use/browser-use) | LLM agent layer | Open-ended goals on unfamiliar sites | LLM cost per task, still blocked by WAFs |
| Browserbase, Steel, Kernel | Hosted browser infrastructure | Anti-bot at scale, session Contexts/Profiles | Paid and external |
| [agent-browser](https://agent-browser.dev) | CLI browser | Persistent profiles, reuse of a Chrome profile | |

## What decides it

1. **Fingerprint, not IP.** A strict WAF checks TLS and JS fingerprints. On one retail site stock Chromium and Patchright were blocked, while Camoufox and Obscura passed. Test the real target before choosing.
2. **State must outlive the process.** A logged-in session or cart needs a persistent profile directory (cookies, localStorage, IndexedDB). The whole industry converges on this: Browserbase Contexts, Steel and Kernel Profiles, Browser-use `persist_profile`, agent-browser `--profile`, Playwright `storage_state` or a persistent context.
3. **Keep the browser alive for polling.** A fresh browser per poll is slow; one persistent page removes start-up cost.
4. **Do not bypass what a site forbids.** Read-only work and carts prepared for a human fit; logins go through a vault or the person, and paying is always human.

## Camoufox pattern

```python
from camoufox.sync_api import Camoufox

with Camoufox(headless=True, locale="es-ES", humanize=True,
              persistent_context=True, user_data_dir="profile-dir") as ctx:
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.goto("https://example.com", wait_until="domcontentloaded")
```

Use one profile directory per site or project so sessions never mix. Pass `i_know_what_im_doing=True` to silence the canvas warning once you accept it.

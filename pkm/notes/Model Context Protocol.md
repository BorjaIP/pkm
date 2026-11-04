---
title: Model Context Protocol
created: Wednesday 4th November 2026 17:10
aliases:
  - MCP
tags:
  - mcp
  - data-fever-mcp
  - fever
---

Review triggered by: comparing [data-fever-mcp](https://github.com/Feverup/data-fever-mcp) against
the current MCP spec docs (`https://modelcontextprotocol.io/docs/2026-07-28/...`), looking for
what's genuinely adoptable now vs. aspirational.

## Where we actually stand

- `data-fever-mcp` pins `fastmcp>=3.4.8,<4` (root `pyproject.toml`). The official Python SDK
  (`mcp` on PyPI) is already at **2.3.0** and `fastmcp` at **4.1.6** (4.2.0 in alpha) — we're a
  full major version behind the SDKs that would even let us touch most of what's below. This
  context should gate every recommendation here: most of the exciting stuff needs an SDK major
  bump first, and 4.2.0 isn't stable yet.
- We already independently arrived at two of the newer spec ideas before reading this:
  - **CIMD (Client ID Metadata Documents)** as the preferred DCR alternative — our own
    `auth_provider.py` already treats CIMD as primary and plain DCR (`/register`) as a fallback.
    The spec (2026-07-28) now **deprecates classic DCR entirely** in favor of CIMD
    (earliest removal: first revision on/after 2027-07-28). We're ahead of the curve here, not
    behind — worth tracking the CIMD migration docs as the removal date approaches, since Gemini
    Enterprise's current `/register` hit (DP-2702/data-charts#3406) is exactly the fallback path
    that's being phased out industry-wide.
  - **MCP Apps** (interactive HTML widgets in a host's chat, `ui://` resources +
    `_meta.ui.resourceUri`) — `src/mcp_shared/mcp_apps/` (`register_widget_resource`, `AppConfig`,
    `structuredContent`) is a full, working implementation already wired into ~18 `mcp_business_ops`
    tool families (pricing, time slots, plan creation, coupons, channel publication, ...). This
    isn't a gap, it's a strength: the spec's `extensions/apps/overview` page describes exactly
    what we built. No action needed beyond keeping it current with the official extension repo.

## What's new in spec 2026-07-28 (vs. 2025-11-25) — and fit for us

The 2026-07-28 revision is a **sweeping, breaking rewrite** (`specification/2026-07-28/changelog`),
not an incremental bump. Before we can adopt most of it, fastmcp/mcp-python need to ship it — as of
now neither has (4.1.x / 2.3.0 are both pre-stateless-era). Treat the items below as "watch", not
"backlog", except where noted.

| Change | What it means | Fit for Fever |
|---|---|---|
| Protocol made **stateless**: no `initialize` handshake, no `Mcp-Session-Id`, every request self-describes its version/capabilities in `_meta` | Removes the session model our gateway's Keycloak/OAuth layer and Redis-backed state implicitly assume | Needs careful design once fastmcp ships it — our `OAuthProxy`/session persistence (Redis) was built session-first. Not actionable yet; worth a design doc when fastmcp 4.2+ stabilizes. |
| New mandatory `server/discover` RPC | Servers advertise supported versions/capabilities/identity up front | Low effort once SDK supports it — mostly free from fastmcp |
| `subscriptions/listen` replaces GET+`resources/subscribe` | Single long-lived stream, opt-in per notification type | We don't currently use `resources/subscribe` anywhere in this repo (checked) — no migration debt, just future capability if we ever want live `toolsListChanged` push (e.g. for a tool catalog that changes mid-session, like BYOT-gated tools) |
| **Sampling and Roots deprecated** | Servers asking the client's LLM to complete a prompt, or declaring filesystem roots, are on their way out (earliest removal 2027-07-28) | We don't use either today (grep confirms no `sampling/createMessage` or `roots/list` call sites) — nothing to migrate, and a good reason to keep not using them |
| **DCR deprecated**, CIMD is the replacement | See above | Already positioned correctly; just don't invest further in `/register`-based flows (like the Gemini Enterprise workaround) as a long-term pattern — flag to the partner-integrations team that CIMD is where new clients should land once their vendor supports it |
| Multi Round-Trip Requests (MRTR) replaces server-initiated requests (`elicitation/create` et al.) | `InputRequiredResult` / `resultType` on every result | We don't currently use Elicitation anywhere (no interactive mid-tool-call prompts) — this would matter most for `mcp_business_ops` write flows that today do confirm/commit as two separate tool calls instead of one elicited round-trip. Worth a second look once MRTR ships: could simplify the "preview then confirm" pattern used by Sales Agent writes and fever2 writes. |
| `tasks` moved out of core into an extension (`io.modelcontextprotocol/tasks`), polling-based (`tasks/get`/`tasks/update`) replacing blocking `tasks/result` | Standardized async/long-running tool pattern | We already hand-roll this ourselves: `snf_bulk_export_to_s3` + `snf_check_export_status` (fire-and-forget export + poll) is literally the pattern this extension formalizes. Once the extension ships in fastmcp, worth evaluating whether to re-platform the Snowflake export tools (and similar) onto the standard extension instead of our bespoke in-memory `export_statuses` dict — would also give us the status pattern "for free" on any new long-running tool instead of re-inventing it each time. |
| `CacheableResult` (`ttlMs`, `cacheScope`) required on list/read results | Client-side caching hints | Cheap win once available — our `tools/list` surface is large (hundreds of tools across sub-MCPs) and mostly static per deployment; a `ttlMs` hint could reduce redundant `tools/list` calls from clients that re-list often |
| Deterministic `tools/list` ordering (SHOULD) | Helps client-side prompt caching | Already effectively true for us (registry-driven, stable iteration order) — verify once we touch `tools/registry.py` next, don't need a dedicated task |

## Recommendations, ranked

1. **Don't chase 2026-07-28 features directly** — fastmcp/mcp-python haven't shipped the stateless
   rewrite yet (4.2.0 alpha only). Revisit this note when `fastmcp>=4.2` is stable and re-run the
   gap analysis against whatever subset they actually implement (SDKs historically lag the spec
   by 1-2 revisions and sometimes skip features).
2. **Do** keep an eye on the CIMD deprecation timeline for DCR — any new partner integration
   (after Gemini Enterprise) should be pointed at CIMD if their platform supports it, since classic
   `/register` becomes a dead end after 2027-07-28.
3. **Worth a real design spike**: re-platforming `snf_bulk_export_to_s3`/`snf_check_export_status`
   (and any future long-running tool) onto the official `tasks` extension once fastmcp ships it —
   we're already solving the exact problem it standardizes, just with our own vocabulary.
4. **No action, just awareness**: Sampling/Roots deprecation doesn't affect us (we never adopted
   them); MCP Apps is already a mature strength, not a gap.
5. **Low priority, cheap when available**: `server/discover` and `CacheableResult` ttl hints — small
   wins, no design risk, just wait for SDK support.

## References

- Spec changelog (2025-11-25 → 2026-07-28): `https://modelcontextprotocol.io/specification/2026-07-28/changelog.md`
- Deprecated features registry: `https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md`
- MRTR pattern: `https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md`
- MCP Apps overview: `https://modelcontextprotocol.io/extensions/apps/overview.md`
- Our MCP Apps implementation: `src/mcp_shared/mcp_apps/` (repository.py, widgets.py, state_tools.py, models.py)
- Our CIMD/DCR fallback: `src/mcp_data_fever/security/auth_provider.py`
- Our bespoke async-export pattern (candidate for the `tasks` extension later): `src/mcp_data_fever/tools/snowflake/export.py`

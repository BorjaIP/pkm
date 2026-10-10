#!/usr/bin/env bash
# Checks a Quartz build of the CI fixture for presentation, build and deploy regressions.
# Usage: ci/check-output.sh <output-dir> [build-log]
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: $0 <output-dir> [build-log]" >&2
  exit 2
fi

out="${1%/}"
log="${2:-}"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
config="$script_dir/../quartz/quartz.config.ts"

failures=0
pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; failures=$((failures + 1)); }
check() { # check <description> <command...>
  local desc="$1"; shift
  if "$@" >/dev/null 2>&1; then pass "$desc"; else fail "$desc"; fi
}
nonempty() { [[ -s "$1" ]]; }

base_url="$(sed -n 's/^[[:space:]]*baseUrl:[[:space:]]*"\([^"]*\)".*/\1/p' "$config" | head -n 1)"
if [[ -z "$base_url" ]]; then
  fail "baseUrl found in quartz/quartz.config.ts"
else
  pass "baseUrl found in quartz/quartz.config.ts ($base_url)"
fi

# Required files
for f in index.html 404.html sitemap.xml; do
  check "$f exists and is non-empty" nonempty "$out/$f"
done

# Base URL
if [[ -n "$base_url" ]]; then
  check "sitemap.xml contains https://$base_url" grep -qF "https://$base_url" "$out/sitemap.xml"
  check "index.html og:url contains https://$base_url" \
    grep -Eq "<meta[^>]*property=\"og:url\"[^>]*https://${base_url//./\\.}|<meta[^>]*https://${base_url//./\\.}[^>]*property=\"og:url\"" "$out/index.html"
fi

# Sample note page
note=""
if [[ -d "$out" ]]; then
  note="$(find "$out" -type f -iname 'sample-note.html' | head -n 1 || true)"
fi
if [[ -n "$note" ]]; then
  pass "sample note page exists ($note)"
else
  fail "sample note page exists"
fi

# Excluded content
if [[ -d "$out" ]]; then
  leaked="$(find "$out" -type f \( -iname '*secret*' -o -iname '*template*' -o -iname '*draft*' \) | head -n 5 || true)"
else
  leaked=""
fi
if [[ -d "$out" && -z "$leaked" ]]; then pass "no output file for excluded content"; else fail "no output file for excluded content ${leaked:+($leaked)}"; fi
if [[ -s "$out/sitemap.xml" ]] && ! grep -Eiq 'secret|template|draft' "$out/sitemap.xml"; then
  pass "sitemap.xml does not list excluded content"
else
  fail "sitemap.xml does not list excluded content"
fi

# Custom components on the sample note page
if [[ -n "$note" ]]; then
  check "breadcrumbs component rendered" grep -q 'breadcrumb-container' "$note"
  check "recent notes component rendered" grep -q 'recent-notes' "$note"
  sidebar_hr() {
    # Quartz output is not line-oriented: join lines, then slice out the left sidebar (up to the center column) before matching.
    local left
    left="$(tr '\n' ' ' <"$note" | sed -e 's/.*class="left sidebar"//' -e 's/class="center".*//')"
    grep -q '<hr' <<<"$left"
  }
  check "divider (<hr) rendered in the left sidebar" sidebar_hr
else
  fail "breadcrumbs component rendered"
  fail "recent notes component rendered"
  fail "divider (<hr) rendered in the left sidebar"
fi

# Build log
if [[ -n "$log" ]]; then
  if [[ ! -s "$log" ]]; then
    fail "build log exists and is non-empty"
  elif grep -qi 'invalid date' "$log"; then
    fail "build log has no 'invalid date' messages"
  else
    pass "build log has no 'invalid date' messages"
  fi
fi

echo
if [[ $failures -gt 0 ]]; then
  echo "SUMMARY: $failures check(s) failed"
  exit 1
fi
echo "SUMMARY: all checks passed"

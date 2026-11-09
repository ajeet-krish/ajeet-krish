# ajeet-krish Reviews

Last updated: 2026-11-08

## 2026-11-08 - Phase 1: README.md Profile Redesign Review

Verdict: FAIL (1 minor item, waivable)

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Low | README.md:199,238,248,267 | New thumbnail img tags (talon, gearflow, stormfund, cybersend) have no alt text | Add alt attributes, e.g. alt="Talon thumbnail", or waive for row-format parity (pre-existing rows also omit alt) |

Notes: All other checks PASS. Diff is 86 insertions / 5 deletions; all 5 deletions map to intentional changes (Flight Dynamics count 3 to 4, ParaView removal, GNC and Orbital row delete, HPC row delete, ML/AI row rewrite). No em dashes or double hyphens introduced; separators use middot (U+00B7). Recurring pattern: thumbnail img tags across all catalog rows (old and new) omit alt text; consider a repo-wide accessibility pass in a later phase.

## 2026-11-08 - Phase 1: Security Review

Verdict: PASS (no Critical/High/Medium findings)

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Low | README.md:330 | www.linkedin.com link is outside the stated URL allowlist; pre-existing intentional contact link to the owner's own LinkedIn profile | Waive as owner-profile link, or add linkedin.com to the allowlist |
| Low | README.md:336-337 | Owner email exposed in mailto: link and shields.io badge label (intentional public contact info; harvestable by spambots) | Accept as intentional; obfuscate only if spam becomes a concern |
| Info | README.md:2 | git.io shortener link (allowlisted, but git.io is deprecated/frozen by GitHub) | Optional: point directly at the readme-typing-svg.demolab.com target |
| Info | README.md:199,238,248,267 | New thumbnails now carry alt attributes (supersedes the accessibility item in the prior review entry) | None |

Check summary: URL allowlist PASS for all Phase 1 additions (github.com/ajeet-krish/*, skillicons.dev, img.shields.io, readme-typing-svg.demolab.com, git.io, raw.githubusercontent.com/ajeet-krish/*). No script/iframe/event-handler/javascript:/data: content. No hidden tracking pixels. All four new PNGs (talon-thumb, gearflow-thumb, stormfund-thumb, cybersend-thumb) decode as valid PNGs matching their subjects. All asset references are simple relative paths (no traversal). No secrets or credentials.

Limitations: git diff/git status/file commands were unavailable in the review session; the change set was reconstructed from README old.md vs README.md comparison plus a full README.md read; PNG validation was by image decode rather than byte-level `file` output.

## 2026-11-08 - Phase 2: Header Title Block & Drawing Stamp Review

Verdict: PASS

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Info | assets/src/build.py (untracked) | Out-of-scope untracked generator script (builds fig-01/fig-02 SVGs, not the title block); not listed in Phase 2 intended changes | Confirm intent: commit, gitignore, or remove |
| Info | README.md:281-282 | Double blank line left where the SHEET 03 kicker was removed | Optional: collapse to one blank line |

Check summary: Both title block SVGs (assets/header-titleblock-dark.svg, assets/header-titleblock-light.svg; 800x200, monospace, self-contained) are well-formed XML with a single root, balanced tags, valid entities, and no external fonts, images, or scripts (only internal url(#grid) and the SVG xmlns URI). README structure intact: details 6/6 (README.md:84-276), HTML tables 7/7 balanced, two markdown tables with matching column counts (README.md:287-292, 310-316), both picture elements well formed (README.md:2-6, 295-299). The header picture (README.md:1-7) sits above the typing SVG (README.md:9-13). srcset paths resolve to existing files (README.md:3-4). Footer monospace stamp present (README.md:338) with middot separators; contact badge block (README.md:326-336) unchanged. Alt text accurate for the header image (README.md:5) and skillicons (README.md:298, Linux removed from both the icon URL and the alt string). No em dashes or double hyphens in new text content; only --- rules, XML/HTML comment delimiters, and markdown table separators appear (all exempt). Diff is 13 insertions / 18 deletions; all deletions map to approved removals (spec block, SHEET 01-05 kickers, linux skillicons icon, italic footer line replaced by the stamp).

## 2026-11-08 - Phase 2: Security Review

Verdict: PASS (no Critical/High/Medium findings)

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Info | assets/header-titleblock-dark.svg:1, assets/header-titleblock-light.svg:1 | xmlns="http://www.w3.org/2000/svg" is a namespace identifier, not a fetched external reference | None; expected and required |
| Info | README.md:332-333 | Owner email exposed in mailto: link and shields.io badge label (pre-existing, intentional contact info; already noted in Phase 1 security review) | Accept as intentional |
| Info | README.md:10 | git.io shortener link (allowlisted but deprecated/frozen by GitHub; pre-existing) | Optional: point directly at the readme-typing-svg.demolab.com target |

Check summary: SVG content safety PASS for both title-block files (assets/header-titleblock-dark.svg, assets/header-titleblock-light.svg; 69 lines each, fully read): only svg/title/defs/pattern/path/rect/line/circle/polygon/g/text elements; no script, foreignObject, event handlers (on*), href/xlink:href, use, image, animate, a, textPath, or style attributes; no data:/javascript: URIs; no DOCTYPE (no XXE surface); only URI-like references are the SVG xmlns namespace and internal url(#grid) paint-server refs (dark:13, light:13). Self-contained: local font stack only, no external fonts/images/stylesheets. URL allowlist PASS: all 43 external URL occurrences in README.md resolve to allowlisted hosts (git.io:10, readme-typing-svg.demolab.com:11, img.shields.io:20-24/32/81/283/306/322/327/330/333, github.com:41-315, skillicons.dev:295-297, www.linkedin.com:326, raw.githubusercontent.com:329, mailto:332); Phase 2 additions reference only relative asset paths (README.md:3-5). Hidden/obfuscated content PASS: no zero-width (U+200B-200D, U+2060), bidi override/isolate (U+200E-200F, U+202A-202E, U+2066-2069), BOM (U+FEFF), or soft hyphen (U+00AD) characters in README.md or either SVG; only visible U+00B7 middle dots. Injected HTML attributes PASS: new/changed markup (README.md:1-7 picture block, 297 skillicons alt, 337 footer stamp) uses only standard attributes (align, media, srcset, src, alt, width); no attribute breakout or event handlers. Secrets PASS: SVGs contain only public portfolio metadata (name, drawing fields); no keys/tokens/credentials.

Limitations: no shell/git tool available in the security-review session; git status/git diff could not be executed. Review performed against working-tree state (full reads of README.md and both SVGs plus regex pattern scans); observed content matches the declared Phase 2 scope (picture block README.md:1-7, skillicons alt text README.md:297, footer stamp README.md:337).

Recurring patterns: none new; mailto/git.io infos are carried over from Phase 1 and remain accepted as intentional.

## 2026-11-08 - Phase 3: Figures Build System, Output Workflow & README Picture Blocks Review

Verdict: PASS (1 Low non-blocking finding, 1 Info)

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Low | assets/src/build.py:361,429-430 vs 505-514 | BuildError raised in the render stage (invalid contribution date at 361, non-positive language total at 429-430) escapes the try/except in main() and surfaces as an uncaught traceback instead of the intended clean `error: ...` message; still exits nonzero so failure remains loud | Extend the try/except BuildError to also wrap the render/write loop (build.py:516-533) |
| Info | .github/workflows/output.yml:42-43 | GITHUB_TOKEN passed to crazy-max/ghaction-github-pages@v4 via `env:` is the legacy pattern; v4 also accepts a `token` input defaulting to github.token, so this works either way with contents: write | Optional: switch to `token: ${{ secrets.GITHUB_TOKEN }}` input for clarity |

Check summary: build.py (538 lines) passes all Python checks: full type hints on every signature, stdlib only, snake_case/PascalCase/SCREAMING_SNAKE conventions, no CLI flags, no hardcoded secrets (ghp_... at build.py:14 is a docstring placeholder), env handling correct (GITHUB_TOKEN preferred then GH_TOKEN at build.py:497, whitespace-only treated as unset at 113-116, OUT_DIR/GH_USER defaulted). GraphQL parsing robust: require_mapping/require_list with precise error paths, null repo nodes skipped (build.py:241-242), contributionLevel fully validated against all 5 GitHub enum values (build.py:55-61,215-219), size validated int >= 0. Date/week math correct: Sunday=0 row mapping via (weekday()+1)%7 (build.py:362), partial edge weeks placed by real weekday so cells stay aligned, month labels from ISO substring labeled once per month (build.py:341-348), 53-column grid geometry consistent (54 vertical / 8 horizontal rules). Donut arc math correct: single-segment full circle via two circles when sweep reaches 360 with gap 0 (build.py:441-454), degenerate segments clamped to 0.1 deg (456-457), symmetric gap/2 margins, large-arc flag modulo 360. XML escaping complete: escape_xml on all text (via text_element, build.py:290) and all API-derived colors (452,460,477); theme constants and numerics safe. Workflow correct: step order checkout > snk@v3 > setup-python 3.12 > build.py > ghaction-github-pages (dist/ accumulates snk artifacts plus 4 figs, makedirs exist_ok does not wipe), snk@v3 `outputs` multi-line with `#mode:dark` fragment matches documented snk syntax, cron "23 */12 * * *" + workflow_dispatch as approved, permissions contents: write minimal and sufficient, concurrency group output-publish with cancel-in-progress false serializes publishes. Deleted snake.yml leaves zero dangling references (repo-wide grep clean); README snake URLs match snk output names. README additions pass: 3 picture blocks after skillicons before Let's Connect (README.md:301-329), all URLs match generated filenames on output branch exactly, alt text on all 3 new imgs (305,313,325), details balanced 7/7, no em dashes or double hyphens in new prose (only exempt --- rules, <!-- comments -->, and the markdown table separator). .gitignore:9 has dist/.

Limitations: no shell/git tool in the review session; git status/git diff could not be executed (same limitation as Phase 1/2 sessions). Review performed against working-tree state (full reads of build.py, output.yml, README.md, .gitignore) plus repo-wide grep sweeps; cross-checked README structure against the Phase 2 review record (second markdown table at old 310-316 correctly absent per approved spec-block removal; details count 6/6 to 7/7 as scoped). Unintended-change verification is therefore observational: everything visible matches the declared Phase 3 scope and the approved removals.

Recurring patterns: BuildError message-quality should cover all stages, not just the fetch/extract stage; legacy `env: GITHUB_TOKEN` idiom for ghaction-github-pages carried by convention.

## 2026-11-08 - Phase 3: Security Review

Verdict: PASS (no Critical/High/Medium findings)

| Severity | File:Line | Issue | Fix |
|----------|-----------|-------|-----|
| Low | .github/workflows/output.yml:19,21,28,38 | All four actions pinned to mutable version tags (actions/checkout@v4, Platane/snk@v3, actions/setup-python@v5, crazy-max/ghaction-github-pages@v4) rather than immutable commit SHAs; consistent with the repo's established snk/ghaction convention | Optional hardening: pin to full commit SHAs with version comments |
| Low | assets/src/build.py:148-149 | Raw GitHub API HTTP error body echoed verbatim into the BuildError message and CI logs; cannot contain the token (GitHub does not echo Authorization headers) but passes unfiltered API-returned content into logs | Optional: truncate or sanitize error detail before printing |
| Info | assets/src/build.py:262-263,447,473 | API-derived color values are XML-escaped (attribute breakout prevented) but not format-validated (e.g. hex pattern); language colors come from GitHub Linguist and are not attacker-controlled | Optional: validate color against a hex pattern before use |

Check summary: Token handling PASS - token read only from env (build.py:497), never printed (only output paths logged at build.py:534), never embedded in SVG output (SVG content derives solely from parsed API data and constants), never written to files, and no error message interpolates the token (HTTPError detail at build.py:148-149 and URLError reason at build.py:150-151 carry response bodies/reasons only; GraphQL errors at build.py:159 are API-returned). Token sent only in the Authorization header over TLS to the fixed api.github.com/graphql endpoint (build.py:29,133-143); urllib does not log headers. Workflow security PASS - permissions block scopes GITHUB_TOKEN to contents: write only (output.yml:8-9; no packages/write, pull-requests/write, or id-token); triggers are schedule + workflow_dispatch only (output.yml:3-6), no pull_request_target/pull_request/issue_comment, so no fork-exposed secret surface; the only secret used is the auto-provisioned secrets.GITHUB_TOKEN (output.yml:34,43), never a PAT; snk/ghaction third-party pattern consistent with the deleted snake.yml convention. Injection surface PASS - GRAPHQL_QUERY is a fixed module constant (build.py:81-110) with GH_USER passed exclusively as a JSON-serialized GraphQL variable (build.py:132), never interpolated into query text (confirmed safe); SVG output escapes all API-derived strings via escape_xml (build.py:119-127) covering ampersand, angle brackets, and both quote characters, applied to language names via text_element (build.py:290) and to all API-derived colors in attribute context (build.py:452,460,477), so a malicious language name or color cannot break out of text or attribute context; contribution dates validated via datetime.date.fromisoformat (build.py:358-361); all geometry values are numeric format strings. Path safety PASS - output filenames are fixed literals (build.py:520-525) with no API-derived path components (no traversal or absolute components possible); OUT_DIR comes from trusted env (build.py:503) and the workflow pins OUT_DIR: dist (output.yml:35). README PASS - the three new picture blocks (README.md:301-330) reference only raw.githubusercontent.com/ajeet-krish/ajeet-krish/output/*.svg (allowlisted host, owner-scoped paths, README.md:303-305,311-313,323-325); no new external hosts, no query strings or tracking parameters, no tracking pixels, alt text present on all three img tags. Secrets PASS - repo-wide grep for ghp_/gho_/github_pat_ patterns finds only env-var references and the docstring placeholder at build.py:14; workflow uses secrets template references (correct), not literal values.

Limitations: no shell/git tool in the review session; git diff/git status could not be executed (same limitation as prior phase reviews). Review performed against working-tree state (full reads of build.py, output.yml, README.md, .gitignore) plus repo-wide grep sweeps. The deleted snake.yml could not be inspected from history; the established snk/ghaction action-pinning convention was assessed as stated in the phase brief.

Recurring patterns: mutable-tag action pinning is the repo-wide convention (carried from snake.yml); legacy env: GITHUB_TOKEN idiom for ghaction-github-pages carried over from the Phase 3 code review; the BuildError message-quality item from the Phase 3 code review (render-stage errors escaping main's handler) has no security impact (messages contain API data only, no token).

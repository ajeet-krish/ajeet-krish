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

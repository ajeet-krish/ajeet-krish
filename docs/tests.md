# ajeet-krish Test Results
Last updated: 2026-11-08

## 2026-11-08 - Phase 1: README Structural & Link Test Report

| Test | Verdict | Notes |
|------|---------|-------|
| T1: `<details>` balance | PASS | 6 open, 6 close (expected 6 each) |
| T2: Summary counts vs row counts | PASS | CFD 5/5, FEA 1/1, CAD 1/1, Flight Dynamics & GNC 4/4, Competitions 2/2, Hobbies 1/1 |
| T3: `src="assets/..."` refs resolve | PASS | All 14 unique refs exist with exact case; 3 markdown-style `](assets/...)` refs also verified |
| T4: No em/en dashes or double hyphens in prose | PASS | 0 issues; global U+2014=0, U+2013=0; all `--` occurrences confined to `---` rules, `<!--` comments, and table delimiter rows |
| T5: Project repo links return 200 | PASS | Talon 200, gearflow 200, stormfund 200, cybersend 200 |
| T6: External images return 200 | PASS | skillicons.dev 200; readme-typing-svg.demolab.com (first 100 chars of URL) 200 |
| T7: SHEET kickers 01-05 above badges | PASS | SHEET 01 (L29), 02 (L79), 03 (L282), 04 (L306), 05 (L323); each immediately followed by its `for-the-badge` paragraph |
| T8: Tech stack table shape | PASS | Exactly 4 data rows: CAD/CFD, Languages, ML/AI, Manufacturing; no "GNC & Orbital", no "HPC", no "ParaView" anywhere in README |
| T9: HTML tag balance | PASS | `<table>` 7 = `</table>` 7; `<tr>` 15 = `</tr>` 15 |

### Coverage Summary
- Structural checks: HTML tag balance, details/summary integrity, per-section row counts
- Asset integrity: 17/17 local asset references resolve (exact case)
- External dependencies: 6/6 HTTP checks return 200 (4 repo links, 2 image URLs)
- Content policy: dash hygiene, tech stack constraints, sheet kicker placement

### Failure Analysis
- None. All 9 tests PASS.

### Recurring Patterns / Notes for Other Agents
- Markdown table delimiter rows (`|---|---|`) contain `--` and must be excluded from dash-hygiene checks; filter with a `[|:\-\s]+` full-line match before flagging double hyphens.

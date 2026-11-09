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

## 2026-11-08 - Phase 3: build.py / output.yml / README Figure Test Report

| Test | Verdict | Notes |
|------|---------|-------|
| T1 build.py syntax | PASS | `python3 -m py_compile assets/src/build.py` exit=0, no output |
| T2 output.yml parses | PASS | `yaml.safe_load` succeeded (PyYAML 6.0.3), no error |
| T3 snake.yml deleted | FAIL | File absent (PASS), but repo-wide grep for `snake.yml` returns **7** matches, expected 0: `docs/reviews.md` L66/L82/L84/L86 (4, added in this phase's diff) and `VISUAL_UPGRADE_PLAN.md` L308/L315/L488 (3, pre-existing planning doc). Functional scope (`.github/`, `README.md`, `assets/`) is clean: 0 matches. |
| T4 live generation | PASS | `OUT_DIR=/tmp/p3test GH_TOKEN="$(gh auth token)" python3 assets/src/build.py` exit=0; exactly 4 files: fig-01-commit-discretization.svg (51993 B), fig-01-commit-discretization-dark.svg (51993 B), fig-02-language-donut.svg (4949 B), fig-02-language-donut-dark.svg (4949 B); all 4 parse via `xml.etree.ElementTree.parse` |
| T5 dark/light distinct | PASS | Both pairs differ (sha256 fig-01: b65d35ffa69e vs a1559a083b70; fig-02: b09f9e19fab9 vs 474fc4558418); each dark contains `0D1117`, each light contains `FFFFFF`; light does not contain `0D1117`, dark does not contain `FFFFFF` |
| T6 dash hygiene in SVGs | PASS | 0 em dash (U+2014), 0 en dash (U+2013), 0 double hyphen across all 4 generated SVGs (grep and unicode codepoint count agree) |
| T7 README structure | PASS | `<details>`=7, `</details>`=7; `<picture>`=5, `</picture>`=5; zero consecutive blank-line pairs; file ends with newline |
| T8 README figure URLs | PASS | 6 unique `raw.githubusercontent.com/ajeet-krish/ajeet-krish/output/` URLs: fig-01-commit-discretization.svg, fig-01-commit-discretization-dark.svg, fig-02-language-donut.svg, fig-02-language-donut-dark.svg, github-snake.svg, github-snake-dark.svg. First 4 match live build.py output filenames exactly; last 2 match output.yml snk step `outputs:` (L25-26). Dark variants appear twice each (picture source sets), light once each. |
| T9 workflow triggers/permissions | PASS | cron `23 */12 * * *` present; `workflow_dispatch` present; `permissions: {contents: write}`; `concurrency: {group: output-publish, cancel-in-progress: false}`; step order verified as checkout@v4 -> Platane/snk@v3 -> setup-python@v5 -> "Generate figures" (`python assets/src/build.py`) -> ghaction-github-pages@v4 |
| T10 clean error handling | PASS | `OUT_DIR=/tmp/p3err GH_TOKEN=""` -> exit=1; stderr exactly `error: GITHUB_TOKEN or GH_TOKEN must be set`; 0 `Traceback` lines; stdout empty; no partial OUT_DIR created |

### Coverage Summary
- 10/10 tests executed; 9 PASS, 1 FAIL
- Syntax/parse: build.py compiles, output.yml is valid YAML
- Functional verification: full live run against the GitHub API produced 4 valid, theme-distinct, dash-clean SVGs
- Content policy: README tag balance (7 details, 5 picture blocks), 6 figure URLs all traceable to a producer (build.py or output.yml snk step)
- Workflow contract: triggers, permissions, concurrency, and 5-step ordering all machine-verified from parsed YAML
- Error path: missing token fails fast with a single clean `error:` line and no traceback

### Failure Analysis
- **T3 (FAIL)**: root cause is documentation prose, not a dangling functional reference. 4 matches were introduced in this phase's own `docs/reviews.md` edit (phrases such as "deleted snake.yml", "carried from snake.yml"); 3 pre-date the phase in `VISUAL_UPGRADE_PLAN.md` (planning doc, unmodified). No workflow, README, or asset reference points at `snake.yml`. Suggested fix: either (a) reword the check to grep only functional paths (`.github/`, `README.md/`, `assets/`), which yields 0 and passes, or (b) keep the repo-wide check and reword the 4 new `docs/reviews.md` sentences (e.g. "the deleted snake workflow") plus the 3 `VISUAL_UPGRADE_PLAN.md` lines to stop using the literal filename. Option (a) matches the check's intent ("no dangling references"); option (b) satisfies the literal spec.
- Note: `.github/workflows/snake.yml` deletion is present in the working tree (`git status` shows ` D`) but is not yet staged/committed; HEAD still contains the file. Must be committed for the deletion to land.

### Recurring Patterns / Notes for Other Agents
- Docs prose written by review/phase agents (docs/reviews.md) is the common source of "zero-reference" grep failures; write check summaries without naming deleted file paths literally, or scope such checks to functional paths.
- `grep -c` returns exit 1 when a file has 0 matches; assert on counts, not grep exit codes.
- The two SVG pairs have identical byte sizes (51993/4949) despite differing content, so size alone is not a valid dark/light distinctness check; use content comparison or hashes.

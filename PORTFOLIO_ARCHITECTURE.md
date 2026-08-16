# Portfolio Architecture: GitHub as Single Source of Truth

> Design document for `ajeet-krish/ajeet-krish` — the primary portfolio and GitHub profile.
> Researched and designed 2026-08-16.

---

## Context

This repo (`ajeet-krish/ajeet-krish`) is the **primary portfolio**. A separate portfolio website exists at `/Users/ajeet/Projects/Digital CV` but is paused — not deleted. The GitHub profile is the single source of truth for all recruiter/manager interactions.

### User Profile

- **Name**: Ajeet Krishnasamy
- **Degree**: BASc Biomedical Mechanical Engineering, University of Ottawa (May 2026)
- **Target roles**: Entry-level mechanical / aerospace / flight dynamics engineering
- **Specialization**: CFD, FEA, spacecraft GNC, orbital mechanics
- **Key languages**: C++20, Python, Rust, MATLAB
- **Work authorization**: Canadian citizen + U.S. work authorization (TN-eligible)

### Current Project Inventory

| # | Project | Domain | Primary Lang | Status |
|---|---------|--------|-------------|--------|
| 1 | AK-Vortex | CFD | C++20 | Active |
| 2 | Crucible-FEA | FEA | C++20 | Active |
| 3 | Zenith | Orbital Mechanics | C++20 | Active |
| 4 | AstroSim | ADCS / GNC | C++17 | Active |
| 5 | SwarmGNC | UAV GNC | C++ / Python / Rust | Active |
| 6 | Airfoil CFD Explorer | CFD | Python / SU2 | Standby |
| 7 | Soccer CFD | CFD | Python / PhiFlow | Standby |
| 8 | F1 Aerodynamics Dashboard | CFD | Python / SU2 | Standby |
| 9 | The Stack (Capstone) | Mechanical Design | SolidWorks / MATLAB | Standby |
| 10 | 3D Orbital Animator | Astrodynamics | Python | Standby |

---

## Design Principles

| Principle | Rationale |
|-----------|-----------|
| **Progressive disclosure** | 30-second scan gets the headline; 5-minute deep-dive gets the evidence |
| **Category-first, not list-first** | Recruiters think in domains ("I need a CFD person"), not chronological order |
| **Validation in-context** | Benchmark tables appear next to the project, not in a separate section |
| **Single source of truth** | Every description traces back to `PROJECTS.md` in the Resume_Builder repo |
| **Engineering maturity signals** | CI badges, test counts, validation tables prove rigor without click-through |

---

## Profile README Architecture (9 Sections)

```
┌─────────────────────────────────────────────────────────┐
│  §1  HEADER (5 lines max)                               │
│      Name, one-line role, work authorization             │
├─────────────────────────────────────────────────────────┤
│  §2  QUICK STATS (badges, inline)                       │
│      Languages · Projects · Tests · CI                   │
├─────────────────────────────────────────────────────────┤
│  §3  WHAT I BUILD (3-sentence elevator pitch)           │
│      CFD solvers · FEA tools · Flight dynamics           │
├─────────────────────────────────────────────────────────┤
│  §4  FEATURED PROJECTS (3 cards, role-targeted)         │
│      Hero image + 1-line description + key metric        │
│      "30-second hook" — these are the resume projects    │
├─────────────────────────────────────────────────────────┤
│  §5  PROJECT CATALOG (categorized table)                │
│      CFD · FEA · GNC · CAD/Mechanical · Tools            │
│      Each row: name + tech tags + 1-line summary         │
│      "5-minute deep-dive" — full inventory               │
├─────────────────────────────────────────────────────────┤
│  §6  VALIDATION EVIDENCE (compact table)                │
│      Solver · Benchmark · Error — across all projects    │
│      Proves rigor without requiring click-through        │
├─────────────────────────────────────────────────────────┤
│  §7  TECH STACK (visual grid)                           │
│      Grouped by domain, not alphabet                     │
├─────────────────────────────────────────────────────────┤
│  §8  ENGINEERING SIGNALS (badges)                       │
│      CI status · Test counts · Build status per project  │
├─────────────────────────────────────────────────────────┤
│  §9  CONTACT (badges + resume link)                     │
│      LinkedIn · Resume PDF · Email                       │
└─────────────────────────────────────────────────────────┘
```

### Section Details

#### §1 — Header

```markdown
# Ajeet Krishnasamy

**Mechanical Engineer · CFD / FEA / Flight Dynamics**

🇨🇦 Canadian Citizen · 🇺🇸 U.S. Work Authorization (TN-eligible)
```

The role title comes first because recruiters scan left-to-right on the first line. "CFD / FEA / Flight Dynamics" is the keyword string that maps to job descriptions. Work authorization is critical for aerospace/defense.

#### §2 — Quick Stats

Badges showing: language proficiency, project count with domain breakdown, total test count, CI status. These are the first quantitative signals. "400+ Tests" immediately differentiates from typical new-grad projects.

#### §3 — What I Build

3-sentence elevator pitch using exact job description language (Lattice Boltzmann, SGP4, ADCS, FEA, validated against benchmarks). Last sentence is the differentiator: validated + tested + packaged = engineering maturity.

#### §4 — Featured Projects (3 cards)

Three cards covering all target domains (CFD, FEA, GNC). Each card has: hero image/GIF, key capabilities, a validation metric table, and links to both portfolio site and source code. Three is the maximum before cognitive overload.

**Why inline validation tables:** The benchmark table is the single most differentiating element a new-grad portfolio can have. Putting it in the card means a recruiter sees proof of rigor without clicking anything.

#### §5 — Project Catalog

Categorized tables (CFD, FEA, GNC, Tools). Each row: project name (linked), tech tags (inline code), 1-line summary, portfolio link. Tables are scannable in 10 seconds. Categories map to how recruiters filter.

#### §6 — Validation Evidence

Cross-project table showing: solver, case, metric, result, reference, error. This is the "proof wall." It answers "did you actually validate this, or just claim you did?" Every row is a specific metric with a specific reference.

#### §7 — Tech Stack

Grouped by domain (Languages, Numerics, HPC, Desktop, CAD/CFD, ML/AI, Testing, Manufacturing). Not alphabetical — grouped by how the recruiter thinks about skills.

#### §8 — Build Status

Live CI badges per repo. A green checkmark next to every project is a trust signal: "This code compiles and tests pass right now."

#### §9 — Contact

Badges for LinkedIn, Resume PDF (direct download), Email. One-click access from any page.

---

## Recruiter Journey Optimization

### 30-Second Scan

```
Ajeet Krishnasamy
Mechanical Engineer · CFD / FEA / Flight Dynamics

[C++20] [Python] [Rust] [10+ Projects] [400+ Tests]

"I build engineering physics tools from first principles..."

┌─────────┐  ┌─────────┐  ┌─────────┐
│AK-Vortex│  │Crucible │  │SwarmGNC │
│  CFD    │  │  FEA    │  │  GNC    │
│Cd=1.536 │  │ <1% err │  │ 96 tests│
└─────────┘  └─────────┘  └─────────┘
```

In 30 seconds, a recruiter knows:
- **Who**: Ajeet Krishnasamy, mechanical engineer
- **What**: CFD, FEA, flight dynamics (three distinct domains)
- **Proof**: 400+ tests, 10+ projects, benchmark validation
- **Stack**: C++20, Python, Rust

### 5-Minute Deep-Dive

After the 30-second scan, a hiring manager who scrolls further finds:
1. Full project catalog across 4 categories — proves breadth
2. Validation evidence table (11 benchmark comparisons) — proves rigor
3. CI status table with green badges — proves maintenance
4. Tech stack grid organized by domain — proves depth
5. Links to portfolio sites — proves documentation skill

### Engineering Maturity Signals

| Signal | Where | What It Proves |
|--------|-------|---------------|
| CI badges (green) | §8, each repo header | Code compiles and tests pass right now |
| Test counts (400+) | §2, each repo | Automated verification, not manual |
| Validation tables with error % | §6, each repo | Engineering discipline |
| Quick Start sections | Each repo README | Reproducible builds |
| References | Each repo README | Academic rigor |

---

## CAD Project Presentation on GitHub

### The Problem

CAD work (crankshaft assemblies, mechanical designs) is inherently visual and spatial. GitHub READMEs render static images. How do you show a 3D assembly?

### Layered Strategy

| Layer | Where | Format | What It Shows |
|-------|-------|--------|---------------|
| **Layer 1** | README | GIF rotation (600px, 5-8 MB) + 2-3 static PNGs | 360° form, exploded view, detail |
| **Layer 2** | GitHub Pages | Three.js interactive viewer (orbit, zoom) | Full interactivity |
| **Layer 3** | YouTube (optional) | 60-second narrated walkthrough | Complex assemblies |

### GIF Pipeline (SolidWorks)

```bash
# 1. SolidWorks: View → Orientation → Save as .mov (turntable animation)
# 2. Convert to optimized GIF:
ffmpeg -i crankshaft.mov -vf "fps=15,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 crankshaft.gif

# 3. Optimize for GitHub (target < 10 MB):
gifsicle -O3 --lossy=80 crankshaft.gif -o crankshaft_optimized.gif
```

### README Integration Pattern

```markdown
<table>
<tr>
<td width="50%">
  ![Rotation](crankshaft_rotation.gif)
  *360° turntable view*
</td>
<td width="50%">
  ![Exploded](crankshaft_exploded.png)
  *Exploded view, 12 components*
</td>
</tr>
</table>

| Component | Material | Tolerance | Manufacturing |
|-----------|----------|-----------|---------------|
| Crankshaft body | 4340 Steel | ±0.025 mm | CNC turning |
```

### Three.js Viewer Pipeline

```
SolidWorks Assembly
    ↓ Save As → eDrawings (.easm)
eDrawings
    ↓ Export → glTF/GLB (.glb)
Three.js Viewer (docs/viewer.html)
    ↓ Linked from GitHub Pages
Profile README links to Pages
```

---

## Project Repository Structure

### Standardized README Template

Every project repo follows this structure:

```markdown
# [Project Name]: [One-Line Description]

[![CI](badge)](link) [![Tests](badge)](link) [![C++20](badge)](link)

One-paragraph description: what it is, why it exists, what makes it notable.

**[Portfolio Site →](link)** | **[Source →](link)**

---

## Demo
![Hero image or GIF](path)

---

## Why [Project Name]
2-3 sentences: what problem does this solve?

---

## Key Capabilities
| Category | Details |
|----------|---------|
| Feature 1 | Details |

---

## Architecture
ASCII diagram or Mermaid showing component relationships.

---

## Validation
| Case | Metric | Solver | Reference | Error |
|------|--------|--------|-----------|-------|
| ... | ... | ... | ... | ... |

---

## Quick Start
### Prerequisites
### Build
### Test
### Run

---

## Tech Stack
## Project Structure
## References
```

### Content Split: README vs GitHub Pages

| Content | README | GitHub Pages |
|---------|--------|-------------|
| One-paragraph summary | Yes | Yes |
| Hero image/GIF | Yes | Yes |
| Key capabilities table | Yes | Yes |
| Validation table (compact) | Yes | Yes (expanded) |
| Quick start / build instructions | Yes | No |
| Architecture diagram | Yes | Yes (interactive) |
| Per-case deep-dive analysis | No | Yes |
| Interactive 3D viewers | No | Yes |
| Theory/math derivations | No | Yes |
| Desktop app screenshots | Yes (1-2) | Yes (full gallery) |

**Rule of thumb:** The README is the "executive summary" that compiles and runs. The portfolio site is the "technical report" that proves depth.

### Cross-Linking Strategy

```
Profile README (ajeet-krish/ajeet-krish)
    ├── §4 Featured Projects → links to each repo README
    ├── §5 Project Catalog → links to each repo README
    └── §9 Contact → links to resume PDF in this repo

Project Repo README (e.g., ajeet-krish/AK-Vortex)
    ├── Header badge → links to portfolio site
    └── Portfolio site → links back to repo

Portfolio Site (e.g., ajeet-krish.github.io/AK-Vortex)
    ├── Navigation → links to repo
    └── Footer → links to profile README
```

---

## Single Source of Truth

```
PROJECTS.md (Resume_Builder repo)
    ↓ propagate to:
    1. Profile README §5 (catalog row)
    2. Profile README §4 (featured card, if top 3)
    3. Repo README (one-paragraph description)
    4. Portfolio site (expanded description)
    5. Resume .tex files (if Active)
```

**Rule:** Edit `PROJECTS.md` first. Then propagate to all downstream locations. Never edit a description in a repo README without updating `PROJECTS.md` first.

---

## Maintenance Workflow

### Adding a New Project (5 steps)

1. **Add entry to `PROJECTS.md`** (Resume_Builder repo) — status, description, results
2. **Create repo** with standardized README template, CI workflow, GitHub Pages site
3. **Update profile README** — §4 if featured, §5 always, §6 if validation, §8 if CI
4. **Update resume** (if Active status)
5. **Verify all cross-links** — profile → repo → portfolio → profile

### Keeping Profile and Repos in Sync

**Quarterly sync checklist:**
- [ ] All repo URLs in profile README are valid
- [ ] All portfolio site URLs are valid
- [ ] All CI badges are green
- [ ] Test counts in profile README match actual counts
- [ ] Validation table rows match actual benchmarks
- [ ] Resume PDF link works
- [ ] Featured projects still reflect target role

### Automation

**GitHub Actions for link checking** (weekly):
- Uses `lychee-action` to check all URLs in README
- Checks portfolio site accessibility
- Fails on broken links

**GitHub Actions for stats** (monthly):
- Queries GitHub API for test counts
- Updates badge numbers in README
- Commits if changed

---

## Future-Proofing

### Project Retirement

| Action | When | How |
|--------|------|-----|
| **Move to Standby** | Still sound but not relevant to current target role | Change status in `PROJECTS.md`. Remove from §4 (featured). Keep in §5 (catalog). |
| **Archive repo** | Obsolete or broken | Set repo to "Archive" on GitHub. Remove from profile README. Keep in `PROJECTS.md` with `Status: Archived`. |
| **Delete repo** | Embarrassing or harmful | Delete on GitHub. Remove from `PROJECTS.md`. Rare — archiving is almost always better. |

**Rule:** Never delete a repo that has stars, forks, or external links. Archive it instead.

### Scaling to 20+ Projects

- Categorized tables (§5) grow independently per category
- Featured section stays at 3 (rotates based on target role)
- If catalog exceeds 20 rows, create `CATALOG_CFD.md` sub-pages linked from main README

### Adding Blog/Writing Later

**Recommended:** Separate repo (`ajeet-krish/blog`) with Jekyll/Hugo on GitHub Pages. Linked from profile README as a new section.

---

## File Structure

```
ajeet-krish/ajeet-krish/              (profile repo)
├── README.md                          (primary portfolio)
├── PORTFOLIO_ARCHITECTURE.md          (this document)
├── resume/
│   └── AjeetKrishResume.pdf           (direct download link target)
└── .github/
    └── workflows/
        ├── validate-links.yml         (weekly link checker)
        └── update-stats.yml           (monthly test count updater)

ajeet-krish/<project-repo>/            (each project repo)
├── README.md                          (standardized template)
├── .github/workflows/ci.yml           (build + test on push)
├── docs/
│   ├── index.html                     (GitHub Pages portfolio)
│   ├── assets/images/                 (hero images, GIFs)
│   └── viewer.html                    (Three.js viewer, optional)
└── src/                               (source code)
```

---

## Implementation Phases

| Phase | What | Effort |
|-------|------|--------|
| **Phase 1** | Restructure profile README with 9-section architecture | 2-3 hours |
| **Phase 1** | Add Experience + Education to profile README | 30 min |
| **Phase 1** | Add Validation Evidence table | 30 min |
| **Phase 1** | Add Build Status table | 30 min |
| **Phase 2** | Standardize top 3 repo READMEs (AK-Vortex, Crucible-FEA, SwarmGNC) | 2-3 hours each |
| **Phase 2** | Add CI workflows to repos missing them | 1 hour each |
| **Phase 3** | CAD GIF pipeline + Three.js viewer | 2-3 hours per project |
| **Phase 3** | GitHub Actions automation | 1-2 hours |
| **Future** | Blog/writing integration | Depends on frequency |

---

## References

- MIT Portfolio Guide: https://mitcommlab.mit.edu/meche/commkit/portfolio/
- GitHub Profile README Best Practices: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
- shields.io badge generation: https://shields.io/
- GitHub Actions link checking: https://github.com/lycheeverse/lychee-action

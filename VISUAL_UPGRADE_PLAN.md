# README Visual Upgrade Plan

> Implementation plan for 7 features + snake animation + SVG header banner.
> Target: `/Users/ajeet/Projects/ajeet-krish/README.md`

---

## Feature 1: Animated Typing SVG Header

**What**: Replace the plain `# Ajeet Krishnasamy` header with an animated typing SVG that cycles through name, title, and specialization.

**Implementation**:
```html
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=0A66C2&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=100&lines=Ajeet+Krishnasamy;Mechanical+%26+Aerospace+Engineer;CFD+%7C+FEA+%7C+Orbital+Mechanics" alt="Typing SVG" />
  </a>
</p>
```

**Parameters**:
- `font=Fira Code` — monospace, engineering aesthetic
- `color=0A66C2` — LinkedIn blue (trust/technical)
- `size=28` — readable on mobile
- `duration=3000` — 3 seconds per line
- `pause=1000` — 1 second pause between lines
- `lines` — URL-encoded, `;` separates lines, `%7C` is pipe character
- `width=700` — fits desktop, scales on mobile

**Replace**: Lines 1-5 (the current `# Ajeet Krishnasamy` header + intro paragraphs)

**Note**: The intro paragraphs ("I'm a Mechanical engineering graduate...") get removed. The typing SVG replaces the entire header section.

---

## Feature 2: Skills Badges Section (Separate from Tech Stack Table)

**What**: Add a new visual skills section using shields.io badges with tool logos and brand colors. Keep the existing Tech Stack table intact for approval.

**Implementation** (new section after the typing header):
```html
<p align="center">
  <!-- Languages -->
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" />
  <img src="https://img.shields.io/badge/MATLAB-FF8C00?style=flat-square&logo=mathworks&logoColor=white" />
  
  <!-- CFD & Simulation -->
  <img src="https://img.shields.io/badge/ANSYS-0A66C2?style=flat-square&logo=ansys&logoColor=white" />
  <img src="https://img.shields.io/badge/SU2-0A66C2?style=flat-square" />
  <img src="https://img.shields.io/badge/OpenFOAM-0A66C2?style=flat-square" />
  <img src="https://img.shields.io/badge/ParaView-0A66C2?style=flat-square" />
  
  <!-- CAD -->
  <img src="https://img.shields.io/badge/SolidWorks-E2231A?style=flat-square&logo=solidworks&logoColor=white" />
  <img src="https://img.shields.io/badge/Autodesk_Fusion-FF8C00?style=flat-square&logo=autodesk&logoColor=white" />
  
  <!-- GNC & Orbital -->
  <img src="https://img.shields.io/badge/SGP4--SDP4-8957E5?style=flat-square" />
  <img src="https://img.shields.io/badge/EKF-8957E5?style=flat-square" />
  <img src="https://img.shields.io/badge/LQR-8957E5?style=flat-square" />
  
  <!-- HPC & ML -->
  <img src="https://img.shields.io/badge/OpenMP-58A6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/Apple_Metal-58A6FF?style=flat-square" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  
  <!-- Testing -->
  <img src="https://img.shields.io/badge/Google_Test-238636?style=flat-square" />
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
</p>
```

**Style**: `flat-square` (clean, modern, square corners)

**Color strategy**:
- Languages: Tool brand colors (C++ blue, Python blue, Rust black, MATLAB orange)
- CFD: Blue `#0A66C2` (water/aero association)
- GNC: Purple `#8957E5` (space/innovation)
- HPC: Light blue `#58A6FF` (GitHub link color)
- ML: PyTorch orange `#EE4C2C`
- Testing: Green `#238636` (GitHub success)

**Note**: Some tools (SU2, OpenFOAM, ParaView, SGP4, EKF, LQR, OpenMP, Metal, Google Test) don't have official shields.io logos. They render as text-only badges with the specified background color. This is fine — the color coding still works.

---

## Feature 3: Collapsible Project Catalog

**What**: Wrap the Project Catalog tables in `<details>`/`<summary>` blocks so they're collapsed by default. Keeps the 30-second scan clean.

**Implementation**:
```html
<details>
<summary><b>CFD & Aerodynamics</b> (3 projects)</summary>
<br>

| Project | Tech | Summary |
|---------|------|---------|
| [AK-Vortex](https://github.com/ajeet-krish/AK-Vortex) | `C++` `Rust` `Python` | LBM CFD solver with MRT, LES, AMR, Rust desktop app, PINN surrogate |
| [Airfoil CFD Explorer](https://github.com/ajeet-krish/Airfoil_CFD) | `Python` `SU2` `Gmsh` | Automated RANS pipeline with NACA 0012 validation and CST shape optimization |
| [The Aerodynamics of Soccer](https://github.com/ajeet-krish/Soccer-CFD) | `Python` `PhiFlow` `SU2` | Magnus effect, vortex shedding, wake drafting, tactical formation flow |

</details>

<details>
<summary><b>FEA & Structural Analysis</b> (1 project)</summary>
<br>

| Project | Tech | Summary |
|---------|------|---------|
| [Crucible-FEA](https://github.com/ajeet-krish/Crucible-FEA) | `C++` `Python` | 6-element FEA solver with nonlinear dynamics, contact, desktop app |

</details>

<details>
<summary><b>Flight Dynamics & GNC</b> (3 projects)</summary>
<br>

| Project | Tech | Summary |
|---------|------|---------|
| [Zenith](https://github.com/ajeet-krish/zenith) | `C++` `Python` | SGP4/SDP4 propagation, force models, conjunction assessment, GPU acceleration |
| [AstroSim](https://github.com/ajeet-krish/AstroSim) | `C++` `Python` | ADCS simulator with sensor models, EKF attitude determination, FDIR |
| [SwarmGNC](https://github.com/ajeet-krish/SwarmGNC) | `C++` `Python` `Rust` | 7-drone swarm, LQR, APF, FDIR, Rust GCS |

</details>
```

**Replace**: Lines 48-71 (the entire Project Catalog section with its `##` header and 3 subsections)

**Key detail**: The `<br>` after `<summary>` is required — GitHub's markdown parser needs it to break out of the summary context.

---

## Feature 4: Featured Cards with GIF

**What**: Add project preview images to the 3 featured cards. Use the screenshots provided (AK-Vortex velocity field, Zenith 3D orbit view).

**Image assets needed**:
- AK-Vortex: The tandem cylinder velocity field screenshot (provided as Image 1)
- Zenith: The 3D orbital propagation view (provided as Image 2)
- Crucible-FEA: Need to find/creates a screenshot (FEA contour plot or desktop app)

**Image hosting**: Store in `assets/` directory of this repo, reference via relative path or raw GitHub URL.

**Implementation** (replacing the current featured cards table):
```html
<table>
<tr>
<td width="33%" align="center">

[AK-VORTEX GIF HERE]

### [AK-Vortex](https://github.com/ajeet-krish/AK-Vortex)
**C++ Lattice Boltzmann CFD Solver**

`C++` `Python` `Rust`

MRT collision · Smagorinsky LES · Bouzidi bounce-back · AMR

</td>
<td width="33%" align="center">

[CRUCIBLE-FEA IMAGE HERE]

### [Crucible-FEA](https://github.com/ajeet-krish/Crucible-FEA)
**C++ Finite Element Structural Solver**

`C++` `Python`

6 element types · Cholesky + CG solvers · Adaptive refinement

</td>
<td width="33%" align="center">

[ZENITH GIF HERE]

### [Zenith](https://github.com/ajeet-krish/zenith)
**Orbital Propagation & Flight Dynamics Engine**

`C++` `Python`

SGP4/SDP4 propagation · Force models · Conjunction assessment

</td>
</tr>
</table>
```

**Image format**: 
- Use `<img src="path" width="100%" />` for responsive sizing
- GIFs should be < 5 MB, 600-800px wide, 15-20 fps
- PNG screenshots are fine too (smaller file size)
- Add `border-radius: 8px` via inline style for polished look (GitHub supports this)

**Optimization**:
```bash
# Convert video to optimized GIF
ffmpeg -i input.mp4 -vf "fps=15,scale=700:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

# Further compress
gifsicle -O3 --lossy=80 output.gif -o optimized.gif
```

---

## Feature 5: Domain-Coded Color System

**What**: Apply consistent colors across all sections based on engineering domain.

**Color map**:
| Domain | Color | Hex | Applied To |
|--------|-------|-----|------------|
| CFD | Blue | `#0A66C2` | CFD project badges, CFD catalog header, AK-Vortex card accent |
| FEA | Green | `#238636` | FEA project badges, FEA catalog header, Crucible-FEA card accent |
| GNC | Purple | `#8957E5` | GNC project badges, GNC catalog header, Zenith card accent |
| General | Gray | `#8B949E` | Tools section, neutral elements |
| Contact | Red | `#DC3545` | Resume badge (already done) |

**Implementation locations**:
1. Skills badges (Feature 2) — already color-coded by domain
2. Section header badges (Feature 6) — each gets domain color
3. Featured card tech tags — use colored `<img>` badges instead of backtick code
4. Catalog table headers — no change needed (markdown tables don't support color)

---

## Feature 6: Color-Coded Section Headers

**What**: Replace plain `## Section Name` headers with shields.io badge headers in domain colors.

**Implementation**:
```html
<!-- Featured Projects -->
<p align="center">
  <img src="https://img.shields.io/badge/%F0%9F%94%A7_Featured_Projects-0A66C2?style=for-the-badge&labelColor=0D1117&color=0A66C2" />
</p>

<!-- Project Catalog -->
<p align="center">
  <img src="https://img.shields.io/badge/%F0%9F%93%96_Project_Catalog-238636?style=for-the-badge&labelColor=0D1117&color=238636" />
</p>

<!-- Tech Stack -->
<p align="center">
  <img src="https://img.shields.io/badge/%F0%9F%9B%A0_Tech_Stack-8957E5?style=for-the-badge&labelColor=0D1117&color=8957E5" />
</p>

<!-- Build Status -->
<p align="center">
  <img src="https://img.shields.io/badge/%E2%9C%85_Build_Status-238636?style=for-the-badge&labelColor=0D1117&color=238636" />
</p>

<!-- Contact -->
<p align="center">
  <img src="https://img.shields.io/badge/%F0%9F%93%AC_Let%27s_Connect-0A66C2?style=for-the-badge&labelColor=0D1117&color=0A66C2" />
</p>
```

**Parameters**:
- `style=for-the-badge` — large, uppercase, prominent
- `labelColor=0D1117` — matches GitHub dark background (seamless)
- `color` — section accent color
- `%F0%9F%94%A7` = 🔧, `%F0%9F%93%96` = 📖, `%F0%9F%9B%A0` = 🛠️, `%E2%9C%85` = ✅, `%F0%9F%93%AC` = 📬

**Replace**: Each `## Section Name` markdown header with the corresponding badge.

---

## Feature 7: GitHub Stats Cards

**What**: Add automated GitHub stats cards showing contribution activity, top languages, and streak.

**Implementation** (side by side using HTML table):
```html
<table>
  <tr>
    <td>
      <img src="https://github-readme-stats.vercel.app/api?username=ajeet-krish&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" />
    </td>
    <td>
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ajeet-krish&layout=compact&theme=tokyonight&hide_border=true" />
    </td>
  </tr>
</table>
```

**Theme**: `tokyonight` — dark blue/purple, professional, matches engineering aesthetic

**Placement**: After Tech Stack, before Build Status

**Note**: The `github-readme-stats` service was returning 503 earlier. If it's still down, these cards won't render. Alternative: use `github-readme-streak-stats` for streak-only, or skip if service is unreliable.

---

## Feature 8: Snake Animation (Expanded)

**What**: An animated snake that "eats" your contribution graph squares. Adds visual interest without being unprofessional.

### How It Works

The snake animation is a GIF generated by a GitHub Action that runs on a schedule. It reads your contribution graph data and animates a snake moving through the green squares.

### Setup Requirements

1. **GitHub Action workflow** in the profile repo (`.github/workflows/snake.yml`)
2. **Separate branch** (`output`) to store the generated SVG
3. **README references** the SVG from the `output` branch

### Workflow File

```yaml
# .github/workflows/snake.yml
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 */12 * * *"  # Every 12 hours
  workflow_dispatch:  # Manual trigger

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: Platane/snk@v3
        with:
          github_user_name: ajeet-krish
          outputs: dist/github-snake.svg

      # Dark mode variant
      - uses: Platane/snk@v3
        with:
          github_user_name: ajeet-krish
          svg_out: dist/github-snake-dark.svg
          color_scheme: dark

      - uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### README Integration

```html
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ajeet-krish/ajeet-krish/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ajeet-krish/ajeet-krish/output/github-snake.svg" />
    <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/ajeet-krish/ajeet-krish/output/github-snake.svg" />
  </picture>
</p>
```

### Placement

After the typing header, before the featured projects. The `<picture>` element with `prefers-color-scheme` works in GitHub — it shows the dark/light variant based on the viewer's GitHub theme.

### Considerations

| Aspect | Detail |
|--------|--------|
| **Privacy** | Shows public contribution graph only; no private repo data |
| **Maintenance** | GitHub Action runs automatically; no manual intervention |
| **File size** | SVG is ~10-50 KB (very lightweight) |
| **Fallback** | If Action fails, last generated SVG remains on `output` branch |
| **Frequency** | Every 12 hours is sufficient; daily is also fine |

---

## Feature 9: SVG Header Banner (Expanded)

**What**: A custom SVG banner with your name, title, and visual elements. Creates a branded identity that's more distinctive than the typing SVG.

### Design Concept

Engineering aesthetic: monospace font, subtle grid lines (technical drawing feel), dark background matching GitHub dark mode, one accent color.

### SVG Code

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0D1117;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#161B22;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="200" fill="url(#bg)" rx="8"/>
  
  <!-- Grid lines (subtle engineering aesthetic) -->
  <line x1="0" y1="50" x2="800" y2="50" stroke="#21262D" stroke-width="0.5"/>
  <line x1="0" y1="100" x2="800" y2="100" stroke="#21262D" stroke-width="0.5"/>
  <line x1="0" y1="150" x2="800" y2="150" stroke="#21262D" stroke-width="0.5"/>
  <line x1="200" y1="0" x2="200" y2="200" stroke="#21262D" stroke-width="0.5"/>
  <line x1="400" y1="0" x2="400" y2="200" stroke="#21262D" stroke-width="0.5"/>
  <line x1="600" y1="0" x2="600" y2="200" stroke="#21262D" stroke-width="0.5"/>
  
  <!-- Accent line -->
  <rect x="50" y="85" width="700" height="2" fill="#0A66C2" rx="1"/>
  
  <!-- Subtitle -->
  <text x="400" y="70" font-family="monospace" font-size="12" fill="#8B949E" text-anchor="middle">
    MECHANICAL &amp; AEROSPACE ENGINEERING
  </text>
  
  <!-- Name -->
  <text x="400" y="120" font-family="monospace" font-size="28" fill="#F0F6FC" font-weight="bold" text-anchor="middle">
    Ajeet Krishnasamy
  </text>
  
  <!-- Domain tags -->
  <text x="400" y="150" font-family="monospace" font-size="14" fill="#58A6FF" text-anchor="middle">
    CFD · FEA · Orbital Mechanics
  </text>
</svg>
```

### Hosting

Save as `header.svg` in the repo root. Reference in README:
```html
<img src="https://raw.githubusercontent.com/ajeet-krish/ajeet-krish/main/header.svg" width="100%" />
```

### Design Principles

| Element | Choice | Rationale |
|---------|--------|-----------|
| Font | Monospace | Engineering/terminal aesthetic |
| Background | `#0D1117` → `#161B22` gradient | Matches GitHub dark mode |
| Grid lines | `#21262D` at 0.5px | Subtle technical drawing feel |
| Accent | `#0A66C2` (blue) | Trust, technical depth |
| Text | `#F0F6FC` (off-white) | Primary text color |
| Subtitle | `#8B949E` (muted gray) | Secondary text |
| Domain tags | `#58A6FF` (light blue) | GitHub link color |

### SVG vs Typing SVG

| Aspect | SVG Banner | Typing SVG |
|--------|-----------|------------|
| Visual impact | High (custom design) | Medium (text animation) |
| Maintenance | Low (static file) | Low (external service) |
| Customization | Full control | Limited to parameters |
| File size | ~2 KB | ~10 KB |
| Animation | None (static) | Typing effect |
| Recommendation | Use as primary header | Use as fallback or combine |

**建议**: Use the SVG banner as the primary header. The typing SVG can be used as a secondary element or fallback.

---

## Implementation Order

| Phase | Features | Estimated Effort |
|-------|----------|-----------------|
| **1** | Typing SVG header + Skills badges | 30 min |
| **2** | Featured cards with GIFs + Domain colors | 2 hours |
| **3** | Collapsible catalog + Color-coded headers | 30 min |
| **4** | GitHub Stats cards | 10 min |
| **5** | Snake animation (GitHub Action setup) | 30 min |
| **6** | SVG header banner (design iteration) | 1-2 hours |

**Total estimated effort**: 5-6 hours

---

## File Structure After Implementation

```
ajeet-krish/ajeet-krish/
├── README.md                    (upgraded with all 9 features)
├── header.svg                   (custom SVG banner)
├── assets/
│   ├── ak-vortex-preview.gif    (CFD velocity field animation)
│   ├── zenith-preview.gif       (3D orbital propagation)
│   └── crucible-preview.png     (FEA contour plot)
├── .github/
│   └── workflows/
│       └── snake.yml            (contribution snake animation)
├── resume/
│   └── AjeetKrishResume.pdf
└── PORTFOLIO_ARCHITECTURE.md
```

---

## Verification Checklist

- [ ] Typing SVG renders correctly on desktop and mobile
- [ ] Skills badges display with correct colors and logos
- [ ] Collapsible sections open/close properly
- [ ] Featured card images load (check file sizes < 5 MB)
- [ ] Domain colors are consistent across all sections
- [ ] Section header badges render with correct colors
- [ ] GitHub Stats cards load (check service availability)
- [ ] Snake animation generates and displays
- [ ] SVG banner renders at correct dimensions
- [ ] All links point to correct repositories
- [ ] Mobile responsive (test at 375px width)
- [ ] No broken images or dead links

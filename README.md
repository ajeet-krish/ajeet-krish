# Ajeet Krishnasamy

**Mechanical Engineer · CFD / FEA / Flight Dynamics**

---

## At a Glance

| 📏 Lines of C++ | ✅ Benchmark Cases | 🧪 Google Test Cases | 📦 Portfolio Projects |
|:---:|:---:|:---:|:---:|
| **50K+** | **14+** | **400+** | **10** |

---

## What I Build

> I build engineering physics tools from first principles: C++ CFD solvers with Lattice
> Boltzmann and RANS methods, finite element structural solvers with adaptive refinement,
> and spacecraft flight dynamics pipelines with SGP4 propagation and ADCS simulation.
> Every project is validated against published benchmarks, tested with Google Test, and
> packaged as a desktop application or interactive portfolio.

---

## Featured Projects

<table>
<tr>
<td width="33%" align="center">

### [AK-Vortex](https://github.com/ajeet-krish/AK-Vortex)
**C++ Lattice Boltzmann CFD Solver**

`C++20` `Python` `Rust`

MRT collision · Smagorinsky LES · Bouzidi bounce-back · AMR · Tauri desktop app

| Case | Re | Error vs Literature |
|------|-----|-------------------|
| Cavity u_max | 100 | 1.0% vs Ghia |
| Cylinder Cd | 100 | 1.1% vs Mei |
| BFS Xr/H | 100 | 3.2% vs Armaly |

**[Source →](https://github.com/ajeet-krish/AK-Vortex)**

</td>
<td width="33%" align="center">

### [Crucible-FEA](https://github.com/ajeet-krish/Crucible-FEA)
**C++ Finite Element Structural Solver**

`C++20` `Python` `Qt 6`

6 element types · Cholesky + CG solvers · Adaptive refinement · Qt 6 desktop app

| Case | Metric | Error |
|------|--------|-------|
| Cantilever tip | PL³/3EI | < 1% |
| Cook's membrane | 13.68 mm | < 1% |
| Plate with hole | σ_max/σ_∞ = 3 | < 10% |

**[Source →](https://github.com/ajeet-krish/Crucible-FEA)**

</td>
<td width="33%" align="center">

### [SwarmGNC](https://github.com/ajeet-krish/SwarmGNC)
**UAV Formation Control & Flight Software**

`C++` `Python` `Rust` `MAVLink`

7-drone swarm · LQR · APF · FDIR · Rust GCS · React MOCR dashboard

| Metric | Value |
|--------|-------|
| Formation error | 1-3 m steady state |
| GTest tests | 96/96 passing |
| Min clearance | 0.52 m at 3 m/s |

**[Source →](https://github.com/ajeet-krish/SwarmGNC)**

</td>
</tr>
</table>

---

## Project Catalog

### CFD & Aerodynamics

| Project | Tech | Summary | Links |
|---------|------|---------|-------|
| [AK-Vortex](https://github.com/ajeet-krish/AK-Vortex) | `C++20` `Rust` `Python` | D2Q9 LBM solver with MRT, LES, AMR, Tauri desktop app, PINN surrogate | [Site](https://ajeet-krish.github.io/lbm-2d/) · [Source](https://github.com/ajeet-krish/AK-Vortex) |
| [Airfoil CFD Explorer](https://github.com/ajeet-krish/Airfoil_CFD) | `Python` `SU2` `Gmsh` | Automated RANS pipeline with NACA 0012 validation and CST shape optimization | [Site](https://ajeet-krish.github.io/Airfoil_CFD/) · [Source](https://github.com/ajeet-krish/Airfoil_CFD) |
| [Soccer CFD](https://github.com/ajeet-krish/Soccer-CFD) | `Python` `PhiFlow` `SU2` | Magnus effect, vortex shedding, wake drafting, tactical formation flow | [Site](https://ajeet-krish.github.io/Soccer-CFD/) · [Source](https://github.com/ajeet-krish/Soccer-CFD) |
| [F1 Aerodynamics Dashboard](https://github.com/ajeet-krish/F1_Telemetry_Dashboard) | `Python` `SU2` `Plotly` | Venturi ground effect, FastF1 telemetry, SU2 RANS validation | [Site](https://ajeet-krish.github.io/F1_Telemetry_Dashboard/) · [Source](https://github.com/ajeet-krish/F1_Telemetry_Dashboard) |

### FEA & Structural Analysis

| Project | Tech | Summary | Links |
|---------|------|---------|-------|
| [Crucible-FEA](https://github.com/ajeet-krish/Crucible-FEA) | `C++20` `Qt 6` `Python` | 6-element FEA solver with nonlinear dynamics, contact, Qt desktop app | [Site](https://ajeet-krish.github.io/fea-2d/) · [Source](https://github.com/ajeet-krish/Crucible-FEA) |

### Flight Dynamics & GNC

| Project | Tech | Summary | Links |
|---------|------|---------|-------|
| [Zenith](https://github.com/ajeet-krish/zenith) | `C++20` `Metal` `ImGui` | SGP4/SDP4 propagation, force models, conjunction assessment, GPU acceleration | [Site](https://ajeet-krish.github.io/zenith/) · [Source](https://github.com/ajeet-krish/zenith) |
| [AstroSim](https://github.com/ajeet-krish/AstroSim) | `C++17` `Eigen3` `OpenGL` | ADCS simulator with sensor models, EKF attitude determination, FDIR, ImGui GCS | [Site](https://ajeet-krish.github.io/AstroSim/) · [Source](https://github.com/ajeet-krish/AstroSim) |
| [SwarmGNC](https://github.com/ajeet-krish/SwarmGNC) | `C++` `Python` `Rust` | 7-drone swarm, LQR, APF, FDIR, Rust GCS, React MOCR dashboard | [Site](https://ajeet-krish.github.io/UAV_swarm/) · [Source](https://github.com/ajeet-krish/SwarmGNC) |

### Tools & Utilities

| Project | Tech | Summary | Links |
|---------|------|---------|-------|
| [3D Orbital Animator](https://github.com/ajeet-krish/orbital-animator) | `Python` `Matplotlib` | Kepler equation solver, 7 orbital regimes, Hohmann transfers, ground tracks | [Source](https://github.com/ajeet-krish/orbital-animator) |

---

## Validation Evidence

All solvers are validated against published experimental or numerical benchmarks.

| Solver | Case | Metric | Result | Reference | Error |
|--------|------|--------|--------|-----------|-------|
| AK-Vortex | Lid-driven cavity | u_max (Re=100) | 0.102 | Ghia 1982 | 1.0% |
| AK-Vortex | Cylinder drag | Cd (Re=100) | 1.536 | Mei 1999 | 1.1% |
| AK-Vortex | Backward-facing step | Xr/H (Re=100) | 3.2 | Armaly 1983 | 3.2% |
| AK-Vortex | Flat plate | Cf (Re=1000) | 0.070 | Blasius | 1.7% |
| Crucible-FEA | Cantilever beam | Tip deflection | PL³/3EI | Analytical | < 1% |
| Crucible-FEA | Cook's membrane | Tip displacement | 13.68 mm | Benchmark | < 1% |
| Crucible-FEA | Plate with hole | σ_max/σ_∞ | 3.0 | Kirsch | < 10% |
| Zenith | SGP4 LEO (ISS) | Position error, 7 days | < 1 km | Spacetrack Report #3 | — |
| Zenith | J2 acceleration | Relative error | < 0.01% | Analytical (Vallado Eq. 8-20) | — |
| AstroSim | EKF convergence | Time to true attitude | < 30 s | — | — |
| AstroSim | Pointing accuracy | Fine-point mode | < 1° | — | — |

---

## Tech Stack

| Domain | Technologies |
|--------|-------------|
| **Languages** | C++20 · Python · Rust · TypeScript · MATLAB |
| **Numerics** | Lattice Boltzmann · FEA · SGP4/SDP4 · EKF · LQR · Monte Carlo |
| **HPC** | OpenMP · Apple Metal GPU · Cache-aware data layouts |
| **Desktop** | Tauri 2 · Qt 6 · Dear ImGui · OpenGL · React |
| **CAD/CFD** | SolidWorks · ANSYS · SU2 · OpenFOAM · Gmsh · ParaView |
| **ML/AI** | PyTorch · ONNX Runtime · Physics-Informed Neural Networks |
| **Testing** | Google Test · pytest · GitHub Actions CI |
| **Manufacturing** | CNC Machining · 3D Printing · MIG Welding |

---

## Build Status

| Project | CI | Tests | Platform |
|---------|-----|-------|----------|
| AK-Vortex | ![](https://github.com/ajeet-krish/AK-Vortex/actions/workflows/ci.yml/badge.svg) | 26 | Ubuntu + macOS |
| Crucible-FEA | ![](https://github.com/ajeet-krish/Crucible-FEA/actions/workflows/ci.yml/badge.svg) | 57 | Ubuntu + macOS |
| Zenith | ![](https://github.com/ajeet-krish/zenith/actions/workflows/ci.yml/badge.svg) | 139 | Ubuntu + macOS |
| AstroSim | ![](https://github.com/ajeet-krish/AstroSim/actions/workflows/ci.yml/badge.svg) | 199 | Ubuntu + macOS |
| SwarmGNC | ![](https://github.com/ajeet-krish/SwarmGNC/actions/workflows/ci.yml/badge.svg) | 96 | Ubuntu + macOS |

---

## Let's Connect

<p align="center">
  <a href="https://www.linkedin.com/in/ajeetkrishnasamy">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/ajeet-krish/ajeet-krish/raw/main/resume/AjeetKrishResume.pdf">
    <img src="https://img.shields.io/badge/Resume-PDF-DC3545?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Resume" />
  </a>
  <a href="mailto:ajeetkrish@icloud.com">
    <img src="https://img.shields.io/badge/Email-ajeetkrish%40icloud.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

<p align="center">
  <i>Always open to discussing new opportunities, collaborations, or engineering problems.</i>
</p>

# EMPIRIC  
*Emulators of Pacific Island Risk to Infrastructure*

Welcome to the EMPIRIC GitHub Organization. EMPIRIC develops open‑source tools to improve climate model data accessibility and extreme‑event analysis for small island states—initially focusing on Pacific Island nations.

---

## Table of Contents

- [Overview](#overview)  
- [Objectives](#objectives)  
- [Repositories](#repositories)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [Citing EMPIRIC](#citing-empiric)  
- [License](#license)  
- [Contact](#contact)  

---

## Overview

Small island states face unique challenges in climate‑risk modelling: coarse general circulation models often omit island geographies, and extreme‑event detection with shifting baselines is non‑trivial. EMPIRIC provides:

- **Emulators** for rapid, high‑resolution hazard generation  
- **Transfer‑learning downscaling** of coarse reanalysis to island‑scale fields  
- **Statistically robust extreme‑event detection**  
- (Planned) **Spatial decision support** integrating health‑infrastructure data  

---

## Objectives

1. **Tropical Cyclone Emulation**  
   Rapid synthetic generation of site‑specific cyclone hazard using Fourier Neural Operators.  

2. **Climate Data Downscaling**  
   Transfer‑learning workflow (U‑Net) to map coarse reanalysis (∼30 km) to high‑resolution (∼2.5 km) meteorology.  

3. **Extreme Event Detection**  
   Implementation of the Optimal Path Threshold (OPT) method for multifactorial identification of extremes under a shifting climate baseline.  

4. **Spatial Decision Support (Goal)**  
   Interactive GIS‑based platform to visualise site‑specific risks and uncertainty alongside health‑facility data.  

---

## Repositories

All code lives under **[https://github.com/EMPIRIC2](https://github.com/EMPIRIC2)**. Key projects:

- **EMPIRIC-DS**  
  U‑Net downscaling models for island meteorology.  
  _Status: Prototype complete; actively maintained._  

- **EMPIRIC-TC**  
  Fourier Neural Operator‑based tropical cyclone hazard emulator.  
  _Status: Alpha release; core features available._  

- **EMPIRIC-OPT**  
  Python implementation of the Optimal Path Threshold method.  
  _Status: Stable reference implementation._  

- **EMPIRIC-SDS**  
  Spatial decision support system (GIS web platform).  
  _Status: Work in progress; planned features documented._  

---

## Installation

Each repository includes its own `README.md` with detailed setup instructions. In general:

```bash
git clone https://github.com/EMPIRIC2/EMPIRIC-DS.git
git clone https://github.com/EMPIRIC2/EMPIRIC-TC.git
git clone https://github.com/EMPIRIC2/EMPIRIC-OPT.git
# For the SDS platform, please refer to:
git clone https://github.com/EMPIRIC2/EMPIRIC-SDS.git

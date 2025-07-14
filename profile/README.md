# EMPIRIC  
*Emulators of Pacific Island Risk to Infrastructure*

Welcome to the EMPIRIC GitHub Organization. EMPIRIC develops open‑source tools to improve climate model data accessibility and extreme‑event analysis for small island states—with a focus on Pacific Island Countries and Territories (PICTs).

---

## Table of Contents

- [Overview](#overview)  
- [Objectives](#objectives)  
- [Repositories](#repositories)  
- [Citing EMPIRIC](#citing-empiric)  
- [Contact](#contact)  

---

## Overview

Small island states face unique challenges in climate‑risk modelling: coarse general circulation models often omit island geographies, and extreme‑event detection with shifting baselines is non‑trivial. EMPIRIC centers around building:

- **Emulators** for rapid, high‑resolution hazard generation  
- **Transfer‑learning downscaling** of coarse reanalysis to island‑scale fields  
- **Statistically robust extreme‑event detection methods**  
- (Planned) **Spatial decision support** integrating health‑infrastructure data  

---

## Objectives

1. **Tropical Cyclone Emulation**  
   Rapid synthetic generation of site‑specific cyclone hazard using Fourier Neural Operators.  

2. **Climate Data Downscaling**  
   Transfer‑learning procedures for one-shot mapping of coarse reanalysis (∼30 km) to high‑resolution (∼2.5 km) meteorological data.  

3. **Extreme Event Detection**  
   Implementation of the Optimal Path Threshold (OPT) method for multifactorial identification of extremes under a shifting climate baseline.  

4. **Spatial Decision Support (Goal)**  
   An interactive GIS‑based platform to visualise site‑specific risks and uncertainty alongside health‑facility data.  

---

## Repositories

All code lives under **[https://github.com/EMPIRIC2](https://github.com/EMPIRIC2)**. Key projects:

- **EMPIRIC-DS**  
  U‑Net downscaling models for island meteorology.  
  _Status: Work in progress._  

- **EMPIRIC-TC**  
  Fourier Neural Operator‑based tropical cyclone hazard emulator.  
  _Status: First release; core features available._  

- **EMPIRIC-OPT**  
  Python implementation of the Optimal Path Threshold method.  
  _Status: Stable Implementation of **[Zhao, Horvat, and Gao](https://iopscience.iop.org/article/10.1088/1748-9326/adae24)**._  

- **EMPIRIC-SDS**  
  Spatial decision support system (GIS web platform).  
  _Status: Work in progress; Initial pre-alpha release at **[https://empiric-tc-model.web.app/](https://empiric-tc-model.web.app/)**._  

---

If you make use of these tools in published research, kindly cite:

- **Zhao B., Horvat C., Gao H.** (2025). *An optimal path threshold method for rigorously identifying extreme climate events.* Environmental Research Letters, 20(2), 024048.  
- **Winkelman E. et al.** (2025). *EMPIRIC TC: A site‑specific AI‑based emulator for tropical cyclone hazards using Fourier Neural Operators.* Journal of Advances in Modeling Earth Systems. (In Review)

---

## Contact

**Dr. Christopher Horvat**  
Department of Earth, Environmental & Planetary Sciences  
Brown University  
[chhorvat@brown.edu](mailto:horvat@brown.edu)  

We welcome your questions and suggestions.  

## Support

This work has been made possible by the generous support of:

- **Climate Change AI**  
  - 2023 Innovation Grant: EMPIRIC_AI: AI-enabled Ensemble Projections of Cyclone Risk for Health Infrastructure in Pacific Island Countries and Territories

- **U.S. National Science Foundation (NSF)**  
  - NSF RISE 2528950: C2H2 EAGER: Site-specific Climate Risks to South Pacific Health and Health Infrastructure.  

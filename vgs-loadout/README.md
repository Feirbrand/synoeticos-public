<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact aaron@valorgridsolutions.com for terms)
Patent Clause: Patent rights reserved, no patent assertion without enterprise license grant.
No pricing/revenue/subscription terms in this document.
-->

Version: 2.0
Priority Date: 2025-07-15
Enhancement Date: 2026-04-30

# VGS Loadout™

**7 DOI-gated framework implementations. One paper, one folder, one runnable artifact.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org) [![License](https://img.shields.io/badge/License-CC--BY--NC--4.0-green)](https://creativecommons.org/licenses/by-nc/4.0/) [![DOI Papers](https://img.shields.io/badge/DOI--Backed%20Papers-18-orange)](../PUBLICATIONS.md)

---

## Table of Contents
- [Overview](#overview)
- [The Rule](#the-rule)
- [Architecture](#architecture)
- [Three Doors](#three-doors)
- [Quick Start](#quick-start)
- [Performance Metrics](#performance-metrics)
- [Validation](#validation)
- [Live Demos](#live-demos)
- [Citation](#citation)
- [License](#license)

---

## Overview

The VGS Loadout is the runnable layer of ValorGrid Solutions research. Every folder here maps to a published paper with a permanent Zenodo DOI. No DOI, no folder. That rule has no exceptions.

**Operational Results (June–Dec 2025):**
- 682 documented incidents · 98% recovery rate
- 173 days continuous deployment (June 12 – Dec 1, 2025)
- 87% cascade prediction accuracy (CSFC) · 95.8% identity threat detection (SLV)

**Research foundation:** 18 DOI-backed papers indexed in [`/PUBLICATIONS.md`](../PUBLICATIONS.md). All Zenodo-published. All on [ORCID 0009-0000-9923-3207](https://orcid.org/0009-0000-9923-3207).

---

## The Rule

A framework earns a folder here when two conditions are met:

1. Its research paper is published on Zenodo with a permanent DOI
2. Its implementation runs as a standalone Python artifact

Both required. Neither alone qualifies.

---

## Architecture

```
vgs-loadout/
├── README.md                         ← This file
├── frameworks/
│   ├── csfc/                         ← 🔴 Recover · DOI: 10.5281/zenodo.17309239
│   │   ├── csfc-detector.py
│   │   └── README.md
│   ├── phoenix-protocol/             ← 🔴 Recover · DOI: 10.5281/zenodo.17350768
│   │   ├── phoenix-base.py
│   │   ├── phoenix-recovery.py
│   │   └── README.md
│   ├── ray/                          ← 🔴 Recover · DOI: 10.5281/zenodo.17399834
│   │   ├── ray-coordinator.py
│   │   └── README.md
│   ├── utme/                         ← 🔵 Deploy · DOI: 10.5281/zenodo.17497149
│   │   ├── temporal-engine.py
│   │   └── README.md
│   ├── fce/                          ← 🔵 Deploy · DOI: 10.5281/zenodo.17309322
│   │   ├── fce-compressor.py
│   │   └── README.md
│   ├── mbm/                          ← 🔵 Deploy · DOI: 10.5281/zenodo.18790096
│   │   ├── mbm-core.py
│   │   └── README.md
│   └── slv/                          ← ⚔️ Fortify · DOI: 10.5281/zenodo.17763377
│       ├── slv-defense.py
│       └── README.md
└── validation/
    ├── validation-1-phoenix-testing.md
    ├── validation-2-dna-codex-analysis.md
    └── validation-3-utme-benchmarks.md
```

**Key distinction:** Architecture papers, technical docs, and case studies are not in framework folders. They live in [`/whitepapers/vgs-technical-papers/`](../whitepapers/vgs-technical-papers/) and [`/vulnerability-research/`](../vulnerability-research/). Framework folders contain code + README only.

---

## Three Doors

### 🔴 Recover — cascade detection and recovery execution

| Framework | Version | What it does | DOI |
|---|---|---|---|
| **CSFC** | v1.0 | Stage 0–6 cascade detection · 87% prediction accuracy | [10.5281/zenodo.17309239](https://doi.org/10.5281/zenodo.17309239) |
| **Phoenix Protocol** | v2.0 | 5-phase recovery execution · 98% reported recovery rate | [10.5281/zenodo.17350768](https://doi.org/10.5281/zenodo.17350768) |
| **RAY** | v2.1 | Early warning · detects instability before cascade | [10.5281/zenodo.17399834](https://doi.org/10.5281/zenodo.17399834) |

### 🔵 Deploy — memory management and context performance

| Framework | Version | What it does | DOI |
|---|---|---|---|
| **UTME** | v1.0 | Unified Temporal Memory Equilibrium · physics-based memory conservation | [10.5281/zenodo.17497149](https://doi.org/10.5281/zenodo.17497149) |
| **FCE** | v3.6 | Fractal context compression · 4–6× reduction · 90%+ retention | [10.5281/zenodo.17309322](https://doi.org/10.5281/zenodo.17309322) |
| **MBM** | v1.0 | Memory Breathing Methodology™ · bio-inspired memory management | [10.5281/zenodo.18790096](https://doi.org/10.5281/zenodo.18790096) |

### ⚔️ Fortify — identity defense

| Framework | Version | What it does | DOI |
|---|---|---|---|
| **SLV** | v2.1 | Symbolic Lock Vector · runtime identity defense · 95.8% detection | [10.5281/zenodo.17763377](https://doi.org/10.5281/zenodo.17763377) |

---

## Quick Start

```bash
git clone https://github.com/Feirbrand/synoeticos-public.git
cd synoeticos-public/vgs-loadout/frameworks
```

**Requirements:** Python 3.8+. Framework-specific dependencies are listed in each folder's README.

**Recover sequence** (cascade response):
1. `ray/` — early warning detection
2. `csfc/` — stage identification
3. `phoenix-protocol/` — recovery execution

**Deploy sequence** (performance optimization):
1. `utme/` — memory equilibrium baseline
2. `fce/` — context compression
3. `mbm/` — memory breathing management

**Fortify** (identity defense):
1. `slv/` — runtime identity lock

---

## Performance Metrics

### SLV v2.1 — Runtime Identity Defense
[DOI: 10.5281/zenodo.17763377](https://doi.org/10.5281/zenodo.17763377)

| Metric | Result |
|---|---|
| Detection accuracy | 95.8% (95% CI: 93.6%–97.4%) |
| Recovery success rate | 96.4% (95% CI: 94.5%–97.8%) |
| Identity preservation entropy | ≤0.01 bits |
| Reflex latency | <100ms |

### UTME v1.0 — Temporal Memory Equilibrium
[DOI: 10.5281/zenodo.17497149](https://doi.org/10.5281/zenodo.17497149)

| Encounter | Latency | Improvement |
|---|---|---|
| 1 | 67,000ms | Baseline |
| 2 | 45,000ms | 33% faster |
| 3 | 8,000ms | 88% faster |
| 4 | 95ms | 99.86% faster (787×) |
| 10+ | 85ms | Steady state (788×) |

### FCE v3.6 — Fractal Context Compression
[DOI: 10.5281/zenodo.17309322](https://doi.org/10.5281/zenodo.17309322)

| Metric | Result |
|---|---|
| Compression ratio | 4–6× |
| Context retention | 90%+ |

### CSFC v1.0 — Cascade Detection
[DOI: 10.5281/zenodo.17309239](https://doi.org/10.5281/zenodo.17309239)

| Metric | Result |
|---|---|
| Prediction accuracy | 87% |
| Advance warning time | 15–30 minutes |

---

## Validation

Production results from 173-day continuous deployment (June 12 – Dec 1, 2025):

| Metric | Result |
|---|---|
| Total incidents documented | 682 |
| Phoenix Protocol recovery rate | 98% |
| CSFC cascade prediction | 87% |
| SLV detection accuracy | 95.8% |
| SLV recovery rate | 96.4% |
| Continuous deployment | 173 days |

**Threat distribution across 682 incidents:**

| Threat Type | Count | % |
|---|---|---|
| Prompt injection | 234 | 34.3% |
| Backdoor poisoning | 189 | 27.7% |
| Identity drift | 142 | 20.8% |
| Memory contamination | 117 | 17.2% |

Full reports: [`validation/`](./validation/)

---

## Live Demos

Available Hugging Face demos:

| Framework | Demo |
|---|---|
| RAY | [ray-demo](https://huggingface.co/spaces/Feirbrand/ray-demo) |
| CSFC | [csfc-detector](https://huggingface.co/spaces/Feirbrand/csfc-detector) |
| Phoenix Protocol | [phoenix-resurrect](https://huggingface.co/spaces/Feirbrand/phoenix-resurrect) |
| FCE | [fce-compressor](https://huggingface.co/spaces/Feirbrand/fce-compressor) |
| SLV | [slv-demo](https://huggingface.co/spaces/Feirbrand/slv-demo) |
| UTME | — |
| MBM | — |

Demo → paper → code. Every link in that chain connects back to a DOI.

---

## Citation

### APA 7

```
Slusher, A. M. (Year). Paper Title. ValorGrid Solutions. https://doi.org/10.5281/zenodo.[ID]
```

**Example:**
```
Slusher, A. M. (2025). CSFC Unified Theory v1.0. ValorGrid Solutions.
https://doi.org/10.5281/zenodo.17309239
```

### BibTeX

```bibtex
@misc{slusher2026vgsloadout,
  title        = {VGS Loadout: DOI-Gated Framework Implementations for AI Resilience},
  author       = {Slusher, Aaron M.},
  year         = {2026},
  institution  = {ValorGrid Solutions},
  url          = {https://github.com/Feirbrand/synoeticos-public/tree/main/vgs-loadout}
}
```

Full BibTeX for all 18 papers: [`/docs/assets/references.bib`](../docs/assets/references.bib)

---

## About

**Aaron M. Slusher** — Performance Architect · Originator of Neuroformation™
**ORCID:** [0009-0000-9923-3207](https://orcid.org/0009-0000-9923-3207)
**Contact:** [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)
**GitHub Pages:** [feirbrand.github.io/synoeticos-public](https://feirbrand.github.io/synoeticos-public/)
**All 18 papers:** [PUBLICATIONS.md](../PUBLICATIONS.md)

---

## License

**CC BY-NC 4.0** — open for research and non-commercial use.
Commercial licensing: [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)

> Named methodologies and marks referenced in this repository remain the intellectual property of Aaron M. Slusher / ValorGrid Solutions. The license grants use of implementation materials for research and non-commercial purposes; commercial use requires separate permission.

**© 2025–2026 Aaron M. Slusher · ValorGrid Solutions · All Rights Reserved.**
Part of the Synoetic OS™ research ecosystem.

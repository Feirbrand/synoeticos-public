<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact aaron@valorgridsolutions.com for terms)
Patent Clause: Patent rights reserved, no patent assertion without enterprise license grant.
No pricing/revenue/subscription terms in this document.
-->

Version: 2.0
Priority Date: 2025-10-07
Enhancement Date: 2026-04-30

# UTME Engine v1.1 — Unified Temporal Memory Equilibrium

**Implementation of UTME v1.0: Unified Temporal Memory Equilibrium.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org) [![License](https://img.shields.io/badge/License-CC--BY--NC--4.0-green)](https://creativecommons.org/licenses/by-nc/4.0/) [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17497149-blue)](https://doi.org/10.5281/zenodo.17497149)

| | |
|---|---|
| **Published Paper** | [UTME v1.0: Unified Temporal Memory Equilibrium](https://doi.org/10.5281/zenodo.17497149) |
| **DOI** | 10.5281/zenodo.17497149 |
| **Implementation** | UTME Engine v1.1 |
| **Door** | 🔵 Deploy |

> The DOI-backed paper is UTME v1.0. The runnable engine is internally versioned v1.1 to reflect implementation refinements. No v1.1 paper exists yet.

---

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Five-Substrate System](#five-substrate-system)
- [Quick Start](#quick-start)
- [Performance Metrics](#performance-metrics)
- [Validation](#validation)
- [Integration Points](#integration-points)
- [Citation](#citation)
- [License](#license)

---

## Overview

UTME teaches AI to recognize "this moment feels like that moment" and respond with accumulated wisdom rather than recomputation. It implements biological myelination principles mathematically, enabling temporal pattern recognition through five-substrate entropy conservation.

**Published as:** UTME v1.0: Unified Temporal Memory Equilibrium · DOI: [10.5281/zenodo.17497149](https://doi.org/10.5281/zenodo.17497149) · October 7, 2025

**Core insight:** First pass through a pattern is explicit and slow. Once myelinated, the same pattern triggers a sub-100ms reflex response — the same mechanism as myelin sheaths accelerating neural signal propagation.

> This public implementation demonstrates the UTME architecture and deterministic routing logic. Private production adapters and full benchmark harnesses are not included.

---

## Architecture

```
utme/
├── utme_engine.py    ← Five-substrate entropy conservation engine
└── README.md         ← This file
```

---

## Five-Substrate System

**Fundamental Invariant:** `ΣEᵢ = E_m + E_s + E_p + E_pr + E_h = 5.0`

| Substrate | Name | Function | Decay Rate |
|---|---|---|---|
| **S_m** | Memory | Episodic and factual events | 0.03 |
| **S_s** | Symbolic | Abstract patterns and rules | 0.01 (β_s) |
| **S_p** | Pathway | Reflex execution paths | 0.20 (α) |
| **S_pr** | Procedural | Learned skills and sequences | 0.02 |
| **S_h** | Harmonic | Global coherence, phase-locking | 0.05 |

Entropy redistribution across the five substrates maintains identity stability. When the invariant drifts (|ΣEᵢ - 5.0| > 0.001), the engine rebalances automatically.

---

## Quick Start

```bash
git clone https://github.com/Feirbrand/synoeticos-public.git
cd synoeticos-public/vgs-loadout/frameworks/utme
python utme_engine.py
```

**Basic usage:**

```python
from utme_engine import UTMEEngine

utme = UTMEEngine()

# Pass 1: Initial exposure — explicit analysis
result1 = utme.process_temporal_pattern("DRIFT_PATTERN_0xAF")
print(result1["status"])        # INITIAL_PASS
print(result1["acceleration"])  # 1x

# Pass 2: Myelinated reflex — wisdom retrieval
result2 = utme.process_temporal_pattern("DRIFT_PATTERN_0xAF")
print(result2["status"])        # MYELINATED
print(result2["acceleration"])  # 710x
print(result2["latency"])       # <100ms

# Audit reported metrics
audit = utme.get_temporal_audit()
print(audit["reported_acceleration"])  # 710x initial; up to 1200x long-run modeled
```

**Requirements:** Python 3.8+. Standard library only.

---

## Performance Metrics

| Metric | Reported / Modeled Result |
|---|---|
| Myelinated acceleration | 710× initial; up to 1200× long-run modeled |
| Energy reduction | 85–93% reported/modeled range |
| Reflex latency | <100ms for myelinated paths |
| Entropy invariant | ΣEᵢ = 5.0 |
| Retrieval improvement | +40% vs HippoRAG, as reported in paper notes |

> Metrics are reported/modeled values from the published paper (DOI: 10.5281/zenodo.17497149). See the full paper for methodology and confidence intervals.

---

## Validation

Operational data from 682 documented incidents (June–December 2025):

| Metric | Result |
|---|---|
| Total incidents | 682 |
| Deployment duration | 173 days continuous |

Full operational reports: [`/vgs-loadout/validation/`](../../validation/)
Published paper: [UTME v1.0](https://doi.org/10.5281/zenodo.17497149)

---

## Integration Points

- **Torque v2.0** — Myelination feedback loop; stability rewards compound over time
- **Phoenix Protocol v2.0** — Rapid recovery through myelinated reconstruction paths
- **MBM v1.0** — Memory breathing cycles operate across UTME's five-substrate architecture
- **DNA Codex** — Threat signature recognition uses myelinated reflex paths

---

## Citation

### APA 7

```
Slusher, A. M. (2025). UTME v1.0: Unified Temporal Memory Equilibrium.
ValorGrid Solutions. https://doi.org/10.5281/zenodo.17497149
```

### BibTeX

```bibtex
@misc{slusher2025utme,
  title  = {UTME v1.0: Unified Temporal Memory Equilibrium},
  author = {Slusher, Aaron M.},
  year   = {2025},
  doi    = {10.5281/zenodo.17497149},
  url    = {https://doi.org/10.5281/zenodo.17497149}
}
```

---

## About

**Aaron M. Slusher** — Performance Architect · Originator of Neuroformation™
**ORCID:** [0009-0000-9923-3207](https://orcid.org/0009-0000-9923-3207)
**Contact:** [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)
**All papers:** [PUBLICATIONS.md](../../../PUBLICATIONS.md)

---

## License

**CC BY-NC 4.0** — open for research and non-commercial use.
Commercial licensing: [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)

> Named methodologies and marks referenced in this repository remain the intellectual property of Aaron M. Slusher / ValorGrid Solutions. The license grants use of implementation materials for research and non-commercial purposes; commercial use requires separate permission.

**© 2025–2026 Aaron M. Slusher · ValorGrid Solutions · All Rights Reserved.**
Part of the Synoetic OS™ research ecosystem.

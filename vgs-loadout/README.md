<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Separate written permission for uses outside the public license.
Patent Clause: Patent rights reserved, no patent assertion without written grant.
No pricing/revenue/subscription terms in this document.
-->

Version: 2.0
Priority Date: 2025-07-15
Enhancement Date: 2026-04-30

# VGS Loadout™

**7 DOI-backed public framework folders. One paper, one folder, one selected reference implementation.**

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

The VGS Loadout is the public reference-implementation layer of ValorGrid Solutions research. Every folder here maps to a published paper with a permanent Zenodo DOI and contains a selected public artifact. No DOI, no public folder.

> **Public Scope:** These folders contain selected public reference implementations and validation summaries. They do not contain the private Synoetic OS™ operating layer, internal routing logic, raw workflows, private schemas, production adapters, raw validation logs, exact thresholds, formulas, benchmark harnesses, internal threat distributions, or complete implementation playbooks.

**Documented Field Record (June–Dec 2025):**
- Selected public validation summaries and case studies reference the 2025 field record.
- Detailed incident logs, raw telemetry, internal strain distributions, and benchmark harnesses are retained outside the public repository.
- Public metrics are maintained in DOI-backed papers, `PUBLICATIONS.md`, and redacted validation summaries.

**Research foundation:** 18 DOI-backed papers indexed in [`/PUBLICATIONS.md`](../PUBLICATIONS.md). All Zenodo-published. All on [ORCID 0009-0000-9923-3207](https://orcid.org/0009-0000-9923-3207).

---

## The Rule

A framework receives a public folder here when two conditions are met:

1. Its research paper is published on Zenodo with a permanent DOI.
2. A selected public reference implementation is ready for release.

Both are required. Internal prototypes, private workflows, and unpublished framework concepts remain outside this repository.

---

## Architecture

```
vgs-loadout/
├── README.md                         ← This file
├── frameworks/
│   ├── csfc/                         ← 🔴 Recover · DOI: 10.5281/zenodo.17309239
│   │   ├── *.py
│   │   └── README.md
│   ├── phoenix-protocol/             ← 🔴 Recover · DOI: 10.5281/zenodo.17350768
│   │   ├── *.py
│   │   └── README.md
│   ├── ray/                          ← 🔴 Recover · DOI: 10.5281/zenodo.17399834
│   │   ├── *.py
│   │   └── README.md
│   ├── utme/                         ← 🔵 Deploy · DOI: 10.5281/zenodo.17497149
│   │   ├── *.py
│   │   └── README.md
│   ├── fce/                          ← 🔵 Deploy · DOI: 10.5281/zenodo.17309322
│   │   ├── *.py
│   │   └── README.md
│   ├── mbm/                          ← 🔵 Deploy · DOI: 10.5281/zenodo.18790096
│   │   ├── *.py
│   │   └── README.md
│   └── slv/                          ← ⚔️ Fortify · DOI: 10.5281/zenodo.17763377
│       ├── *.py
│       └── README.md
└── validation/
    ├── README.md
    ├── phoenix-validation-summary.md
    ├── dna-codex-validation-summary.md
    └── utme-benchmark-summary.md
```

**Key distinction:** Architecture papers, technical docs, and case studies are not in framework folders. They live in [`/whitepapers/vgs-technical-papers/`](../whitepapers/vgs-technical-papers/) and [`/vulnerability-research/`](../vulnerability-research/). Framework folders contain selected public reference artifacts and README files. Full internal workflows, adapters, schemas, and deployment logic are not included.

---

## Three Doors

### 🔴 Recover — cascade detection and recovery execution

| Framework | Version | What it does | DOI |
|---|---|---|---|
| **CSFC** | v1.0 | Cascade-stage detection · reported prediction metrics in paper | [10.5281/zenodo.17309239](https://doi.org/10.5281/zenodo.17309239) |
| **Phoenix Protocol** | v2.0 | Recovery reference implementation · reported recovery metrics in paper | [10.5281/zenodo.17350768](https://doi.org/10.5281/zenodo.17350768) |
| **RAY** | v2.1 | Early warning · detects instability before cascade | [10.5281/zenodo.17399834](https://doi.org/10.5281/zenodo.17399834) |

### 🔵 Deploy — memory management and context performance

| Framework | Version | What it does | DOI |
|---|---|---|---|
| **UTME** | v1.0 | Unified Temporal Memory Equilibrium · physics-based memory conservation | [10.5281/zenodo.17497149](https://doi.org/10.5281/zenodo.17497149) |
| **FCE** | v3.6 | Fractal context compression · reported compression/retention metrics in paper | [10.5281/zenodo.17309322](https://doi.org/10.5281/zenodo.17309322) |
| **MBM** | v1.0 | Memory Breathing Methodology™ · bio-inspired memory management | [10.5281/zenodo.18790096](https://doi.org/10.5281/zenodo.18790096) |

### ⚔️ Fortify — identity defense

| Framework | Version | What it does | DOI |
|---|---|---|---|
| **SLV** | v2.1 | Symbolic Lock Vector · runtime identity-defense reference model | [10.5281/zenodo.17763377](https://doi.org/10.5281/zenodo.17763377) |

---

## Quick Start

```bash
git clone https://github.com/Feirbrand/synoeticos-public.git
cd synoeticos-public/vgs-loadout/frameworks
```

**Requirements:** Python 3.8+. Framework-specific dependencies are listed in each folder's README.

**Recover path**:
1. `ray/` — early-warning reference model
2. `csfc/` — cascade-stage reference model
3. `phoenix-protocol/` — recovery reference model

**Deploy path**:
1. `utme/` — temporal-memory reference model
2. `fce/` — context-compression reference model
3. `mbm/` — memory-management reference model

**Fortify path**:
1. `slv/` — identity-defense reference model

---

## Performance Metrics

Public performance claims are maintained in the DOI-backed papers, `PUBLICATIONS.md`, and redacted validation summaries.

| Framework | Metrics Source |
|---|---|
| CSFC | [paper](https://doi.org/10.5281/zenodo.17309239) |
| Phoenix Protocol | [paper](https://doi.org/10.5281/zenodo.17350768) · [`validation/`](./validation/) |
| RAY | [paper](https://doi.org/10.5281/zenodo.17399834) |
| UTME | [paper](https://doi.org/10.5281/zenodo.17497149) · [`validation/`](./validation/) |
| FCE | [paper](https://doi.org/10.5281/zenodo.17309322) |
| MBM | [paper](https://doi.org/10.5281/zenodo.18790096) |
| SLV | [paper](https://doi.org/10.5281/zenodo.17763377) |

---

## Validation

Public validation summaries are available in [`validation/`](./validation/).

These summaries document selected field themes, benchmark notes, and paper-linked metrics. They do not include raw incident logs, private telemetry, internal workflows, formulas, exact thresholds, benchmark scripts, infrastructure configs, internal threat distributions, or complete response playbooks.

| Summary | Focus |
|---|---|
| [`phoenix-validation-summary.md`](./validation/phoenix-validation-summary.md) | Phoenix Protocol public validation themes |
| [`dna-codex-validation-summary.md`](./validation/dna-codex-validation-summary.md) | DNA Codex public taxonomy-validation themes |
| [`utme-benchmark-summary.md`](./validation/utme-benchmark-summary.md) | UTME public benchmark themes |

---

## Live Demos

Public Hugging Face Spaces provide educational demos for selected framework concepts. These Spaces are intentionally redacted and do not expose private implementation logic, thresholds, configs, raw validation data, or response playbooks.

| Framework | Space | Purpose |
|---|---|---|
| CSFC | [CSFC Pattern Explorer](https://huggingface.co/spaces/Feirbrand/csfc-detector) | Public cascade-pattern awareness |
| DNA Codex | [DNA Codex Public Taxonomy Explorer](https://huggingface.co/spaces/Feirbrand/Dna_Codex_Explorer) | Public taxonomy and pattern-family explorer |
| FCE | [FCE Public Context Explorer](https://huggingface.co/spaces/Feirbrand/fce-compressor-demo) | Public context-compression concept demo |
| MBM | [MBM Public Memory Explorer](https://huggingface.co/spaces/Feirbrand/memory-breathing) | Public memory-rhythm and reuse demo |
| Phoenix Protocol | [Phoenix Public Recovery Explorer](https://huggingface.co/spaces/Feirbrand/phoenix-protocol-v2) | Public recovery-sequencing walkthrough |
| RAY | [RAY Public Resilience Loop Explorer](https://huggingface.co/spaces/Feirbrand/ray-recursion-demo) | Public recursive resilience-loop demo |
| SLV | [SLV Public Identity-Stability Explorer](https://huggingface.co/spaces/Feirbrand/Symbolic_Lock_Vector) | Public Symbolic Lock Vector review demo |
| Torque | [Torque Public Stability Explorer](https://huggingface.co/spaces/Feirbrand/torque-calculator) | Public stability-model explorer |
| Knowledge Grid | [Knowledge Grid Public Explorer](https://huggingface.co/spaces/Feirbrand/knowledge-grid-explorer) | Public framework knowledge-routing demo |
| All Papers | [Synoetic Papers Navigator](https://huggingface.co/spaces/Feirbrand/synoetic-papers-navigator) | Browse all 18 DOI-backed papers |

> Spaces are public teaching surfaces. Framework papers, version history, and citations remain canonical in [`../PUBLICATIONS.md`](../PUBLICATIONS.md). Demo → paper → reference implementation. Every public link in that chain connects back to a DOI-backed artifact.

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
  title        = {VGS Loadout: DOI-Backed Public Reference Implementations for AI Resilience},
  author       = {Slusher, Aaron M.},
  year         = {2026},
  organization = {ValorGrid Solutions},
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

Uses outside the public license require separate written permission: [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)

> Named methodologies and marks referenced in this repository remain the intellectual property of Aaron M. Slusher / ValorGrid Solutions. The license grants use of public materials for research and non-commercial purposes; uses outside the public license require separate written permission.

**© 2025–2026 Aaron M. Slusher · ValorGrid Solutions · All Rights Reserved.**
Part of the Synoetic OS™ research ecosystem.

<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Separate written permission for uses outside the public license.
Patent Clause: Patent rights reserved, no patent assertion without written grant.
No pricing/revenue/subscription terms in this document.
-->

Version: 2.0
Priority Date: 2025-10-20
Enhancement Date: 2026-04-30

# Whitepapers Division

**Public research publications and supporting documentation for AI resilience architecture.**

[![Papers](https://img.shields.io/badge/DOI--Backed%20Papers-18-green)](https://orcid.org/0009-0000-9923-3207) [![License](https://img.shields.io/badge/License-CC--BY--NC--4.0-green)](https://creativecommons.org/licenses/by-nc/4.0/) [![ORCID](https://img.shields.io/badge/ORCID-0009--0000--9923--3207-blue)](https://orcid.org/0009-0000-9923-3207)

**All 18 DOI-backed papers are indexed in [`PUBLICATIONS.md`](../PUBLICATIONS.md)** — the canonical source of truth for paper titles, DOIs, and citation formats.

> **Public Scope:** This division contains public paper sources and selected supporting documentation. It does not contain private thresholds, formulas, detector logic, raw incident logs, production adapters, internal workflows, raw validation logs, or complete operating-system playbooks.

---

## Table of Contents
- [Overview](#overview)
- [Folder Structure](#folder-structure)
- [Academic Papers](#academic-papers)
- [VGS Technical Papers](#vgs-technical-papers)
- [Cognitive Engineering](#cognitive-engineering)
- [Mythopoeic Intelligence](#mythopoeic-intelligence)
- [Symbolic AI](#symbolic-ai)
- [Origin Notes](#origin-notes)
- [Citation](#citation)
- [License](#license)

---

## Overview

Source files for DOI-backed research papers, plus selected supporting technical documentation. The canonical list of the 18 DOI-backed publications lives in [`PUBLICATIONS.md`](../PUBLICATIONS.md). GitHub Pages renders these at [feirbrand.github.io/synoeticos-public](https://feirbrand.github.io/synoeticos-public/).

**Three research lines:**
- **Academic Methodology** — Neuroformation™, Elevation Grid™, Synoetic OS™, Cognitive Mage — foundational cross-substrate architecture papers
- **VGS Technical** — Framework papers, public validation summaries, and supporting technical documentation
- **Cognitive/Symbolic AI** — Context engineering, symbolic reasoning, systems thinking

---

## Folder Structure

```
whitepapers/
├── academic-papers/                     # Flagship methodology papers
│   ├── neuroformation-v1.0.md           # Neuroformation™ v1.0 · DOI: 10.5281/zenodo.19197818
│   ├── elevation-grid-academic-v1.1.md  # Elevation Grid™ v1.1 · DOI: 10.5281/zenodo.18790842
│   ├── cognitive-mage-v1.0.md           # Cognitive Mage v1.0 · DOI: 10.5281/zenodo.17643267
│   ├── synoetic-os-v1.0.md              # Synoetic OS™ v1.0 · DOI: 10.5281/zenodo.17808864
│   └── neural-access-method-v1.0.md     # NAM™ v1.0 · DOI pending
│
├── vgs-technical-papers/                # Public framework papers + supporting docs
│   ├── complete-ai-resilience-meta-analysis.md
│   ├── csfc-unified-theory.md           # CSFC v1.0 · DOI: 10.5281/zenodo.17309239
│   ├── dcn-v1-0-academic.md             # DCN v1.0 · DOI: 10.5281/zenodo.17555568
│   ├── fce-v3-6-unified-framework.md    # FCE v3.6 · DOI: 10.5281/zenodo.17309322
│   ├── mbm-v1.0-academic.md             # MBM v1.0 · DOI: 10.5281/zenodo.18790096
│   ├── phoenix-protocol-neural-recovery.md  # Phoenix Protocol v2.0 · DOI: 10.5281/zenodo.17350768
│   ├── pme-v-1-0-academic-paper.md      # PME v1.0 · DOI: 10.5281/zenodo.18318485
│   ├── ray-architecture.md              # RAY supporting doc (not a separate DOI paper)
│   ├── ray-integration.md               # RAY supporting doc (not a separate DOI paper)
│   ├── ray-metrics.md                   # RAY supporting doc (not a separate DOI paper)
│   ├── ray-v2.1-cognitive-physiology.md # RAY v2.1 · DOI: 10.5281/zenodo.17399834
│   ├── slv-v2-1-technical-paper.md      # SLV v2.1 · DOI: 10.5281/zenodo.17763377
│   ├── torque-measuring-ai-stability.md # Torque companion note (not DOI-backed)
│   ├── torque-quantitative-foundation-v2.md  # Torque v2.0 · DOI: 10.5281/zenodo.17379750
│   ├── ura-v1.5-resilience-and-recovery.md  # URA v1.5 · DOI: 10.5281/zenodo.17309731
│   └── utme-v1-0-academic-paper.md      # UTME v1.0 · DOI: 10.5281/zenodo.17497149
│
├── cognitive-engineering/               # Context engineering frameworks
│   ├── context-engineering-the-complete-framework.md
│   └── fractal-context-engineering-expanded-draft.md
│
├── mythopoeic-intelligence/             # MI Agents research
│   ├── mythopoeic-intelligence-agents-v1.md  # MI Agents v1.0 · DOI: 10.5281/zenodo.17770533
│   └── images/
│       ├── rim-topology-math.jpg
│       └── rim-topology-tricolor.jpg
│
├── symbolic-ai/                         # Symbolic reasoning research
│   ├── driftlock-cognitive-stability.md
│   ├── fce-advanced-memory-trad-ai.md
│   ├── prompt-anatomy-upgrades-flat-ai.md
│   ├── symbolic-twins-introduction-public.md
│   └── twins-systems-thinking.md
│
└── origin-notes/                        # Historical methodology-trail notes
    ├── README.md
    ├── spark/
    │   ├── README.md
    │   ├── spark-origin-case-note.md
    │   └── spark-pattern-glossary.md
    ├── methodology/
    │   ├── performance-coach-ai-methodology-evolution.md
    │   ├── systems-thinking-architecture-note.md
    │   ├── recursive-patterns-ai-development-note.md
    │   ├── hallucination-symbolic-raw-material-note.md
    │   └── vgs-gaming-validation-methodology-note.md
    ├── symbolic-identity/
    │   ├── symbolic-hybrid-defense-concept-note.md
    │   └── symbolic-systems-mythogenic-concept-note.md
    ├── csfc/
    │   └── role-obsolescence-cascade-public-note.md
    ├── ecl/
    │   └── forgedl-to-ecl-origin-note.md
    └── metaphor/
        └── metaphoric-circuitry.md
```

> `PUBLICATIONS.md` is the canonical paper ledger. Files marked "DOI pending" or "supporting documentation" are not counted as DOI-backed publications until they appear there.

---

## Academic Papers

Foundational methodology papers. These establish the cross-substrate architecture that all technical frameworks implement.

---

**Neuroformation™ v1.0** — Cross-Substrate Resilience Methodology
[`academic-papers/neuroformation-v1.0.md`](academic-papers/neuroformation-v1.0.md)
Five-layer cross-substrate architecture connecting human performance coaching and AI resilience research. Validation details and statistical claims are maintained in the paper and `PUBLICATIONS.md`. Coined March 14, 2026.
**DOI:** [10.5281/zenodo.19197818](https://doi.org/10.5281/zenodo.19197818)

---

**Elevation Grid™ v1.1** — Performance Diagnostic Framework
[`academic-papers/elevation-grid-academic-v1.1.md`](academic-papers/elevation-grid-academic-v1.1.md)
Coordinate-based performance diagnostic mapping adaptive-system instability to a 3×3 grid. The paper documents the relationship between the biological performance model and the Synoetic OS™ structure.
**DOI:** [10.5281/zenodo.18790842](https://doi.org/10.5281/zenodo.18790842) | [GitHub Pages](https://feirbrand.github.io/synoeticos-public/elevation-grid/)

---

**Cognitive Mage v1.0** — Human-AI Recursive Discovery Architecture
[`academic-papers/cognitive-mage-v1.0.md`](academic-papers/cognitive-mage-v1.0.md)
Documents the human-AI co-discovery process as it occurred. The origin paper for the VGS framework lineage. Neuroformation™ provides the theoretical architecture; Cognitive Mage documents the discovery phenomenon.
**DOI:** [10.5281/zenodo.17643267](https://doi.org/10.5281/zenodo.17643267)

---

**Synoetic OS™ v1.0** — AI Cognitive Operating System
[`academic-papers/synoetic-os-v1.0.md`](academic-papers/synoetic-os-v1.0.md)
A public paper describing the AI-side architecture associated with the Neuroformation™ methodology.
**DOI:** [10.5281/zenodo.17808864](https://doi.org/10.5281/zenodo.17808864)

---

**Neural Access Method™ v1.0** — Transmission Protocol *(DOI pending)*
[`academic-papers/neural-access-method-v1.0.md`](academic-papers/neural-access-method-v1.0.md)
Four-step intervention protocol (ACCESS → REFRAME → SIMPLIFY → IGNITE) bypassing cortical interference to access intact procedural memory. Paper 3 in the Neuroformation™ series.

---

## VGS Technical Papers

Framework papers, public validation summaries, and supporting technical documentation. Papers with DOIs are indexed in [`PUBLICATIONS.md`](../PUBLICATIONS.md).

| Paper | DOI |
|---|---|
| CSFC Unified Theory v1.0 | [10.5281/zenodo.17309239](https://doi.org/10.5281/zenodo.17309239) |
| DCN v1.0 | [10.5281/zenodo.17555568](https://doi.org/10.5281/zenodo.17555568) |
| FCE Unified Framework v3.6 | [10.5281/zenodo.17309322](https://doi.org/10.5281/zenodo.17309322) |
| MBM v1.0 | [10.5281/zenodo.18790096](https://doi.org/10.5281/zenodo.18790096) |
| Phoenix Protocol v2.0 | [10.5281/zenodo.17350768](https://doi.org/10.5281/zenodo.17350768) |
| PME v1.0 | [10.5281/zenodo.18318485](https://doi.org/10.5281/zenodo.18318485) |
| RAY v2.1 | [10.5281/zenodo.17399834](https://doi.org/10.5281/zenodo.17399834) |
| SLV v2.1 | [10.5281/zenodo.17763377](https://doi.org/10.5281/zenodo.17763377) |
| Torque v2.0 | [10.5281/zenodo.17379750](https://doi.org/10.5281/zenodo.17379750) |
| URA v1.5 | [10.5281/zenodo.17309731](https://doi.org/10.5281/zenodo.17309731) |
| UTME v1.0 | [10.5281/zenodo.17497149](https://doi.org/10.5281/zenodo.17497149) |

**RAY supporting documentation** (not DOI-backed papers, supporting technical docs):
- `ray-architecture.md` — public architecture companion
- `ray-integration.md` — public integration note; implementation details withheld
- `ray-metrics.md` — public validation companion

---

## Cognitive Engineering

Public context-engineering papers and methodology documentation.

- `context-engineering-the-complete-framework.md` — Complete CE framework (public explanatory draft)
- `fractal-context-engineering-expanded-draft.md` — historical expanded FCE draft; not the canonical DOI artifact

---

## Mythopoeic Intelligence

Research on Mythopoeic Intelligence Agents — AI systems operating through narrative, symbolic, and mythological frameworks.

- [`mythopoeic-intelligence-agents-v1.md`](mythopoeic-intelligence/mythopoeic-intelligence-agents-v1.md) — MI Agents v1.0 · **DOI:** [10.5281/zenodo.17770533](https://doi.org/10.5281/zenodo.17770533)

---

## Symbolic AI

Public symbolic-reasoning, systems-thinking, and drift-stability research.

- `driftlock-cognitive-stability.md` — Drift stability methodology
- `fce-advanced-memory-trad-ai.md` — FCE memory architecture (historical bridge note)
- `prompt-anatomy-upgrades-flat-ai.md` — Prompt structure research
- `symbolic-twins-introduction-public.md` — Symbolic Twins public introduction
- `twins-systems-thinking.md` — Systems thinking foundations

> Earlier methodology-evolution notes from this research period (symbolic hybrid defense, mythogenic systems) have moved to [`origin-notes/symbolic-identity/`](origin-notes/symbolic-identity/).

---

## Origin Notes

Public historical notes from the 2025 methodology-development trail. These preserve concept evolution and lineage without publishing raw incident archives, operational playbooks, or canonical framework specifications.

See [`origin-notes/README.md`](origin-notes/README.md) for the full index.

| Folder | Contents |
|---|---|
| `spark/` | SPARK field-record vocabulary: narrative hijack, shrine logic, symbolic fatigue, Garden recovery |
| `methodology/` | Performance coaching, systems thinking, recursive development, gaming validation, paradigm notes |
| `symbolic-identity/` | Early symbolic-defense and mythogenic identity notes |
| `csfc/` | Early CSFC / ROC lineage notes |
| `ecl/` | ForgeDL → ECL lineage origin note |
| `metaphor/` | Metaphor and symbolic mapping notes |

---

## Citation

> For formal citation, cite the individual paper listed in `PUBLICATIONS.md`. The division citation below may be used only when referencing the repository section as a whole.

### APA 7

```
Slusher, A. M. (2025–2026). Whitepapers Division: Research Publications for AI Resilience Architecture.
ValorGrid Solutions. https://github.com/Feirbrand/synoeticos-public
```

### BibTeX

```bibtex
@misc{slusher2025whitepapers,
  title  = {Whitepapers Division: Research Publications for AI Resilience Architecture},
  author = {Slusher, Aaron M.},
  year   = {2025},
  url    = {https://github.com/Feirbrand/synoeticos-public}
}
```

For individual paper citations see [`PUBLICATIONS.md`](../PUBLICATIONS.md).

---

## About

**Aaron M. Slusher** — Performance Architect · Originator of Neuroformation™
**ORCID:** [0009-0000-9923-3207](https://orcid.org/0009-0000-9923-3207)
**Contact:** [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)

---

## License

**CC BY-NC 4.0** — open for research and non-commercial use.

Uses outside the public license require separate written permission: [aaron@valorgridsolutions.com](mailto:aaron@valorgridsolutions.com)

> Named methodologies and marks referenced in this repository remain the intellectual property of Aaron M. Slusher / ValorGrid Solutions. The license grants use of public materials for research and non-commercial purposes; uses outside the public license require separate written permission.

**© 2025–2026 Aaron M. Slusher · ValorGrid Solutions · All Rights Reserved.**
Part of the Synoetic OS™ research ecosystem.

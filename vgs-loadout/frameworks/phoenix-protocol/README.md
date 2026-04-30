<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact aaron@valorgridsolutions.com for terms)
Patent Clause: Patent rights reserved, no patent assertion without enterprise license grant.
No pricing/revenue/subscription terms in this document.
-->

Version: 2.0
Priority Date: 2025-10-14
Enhancement Date: 2026-04-30

# Phoenix Protocol v3.1 — Recovery Execution

**Implementation of Phoenix Protocol v2.0: Neural Recovery for AI Systems.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org) [![License](https://img.shields.io/badge/License-CC--BY--NC--4.0-green)](https://creativecommons.org/licenses/by-nc/4.0/) [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17350768-blue)](https://doi.org/10.5281/zenodo.17350768)

| | |
|---|---|
| **Published Paper** | [Phoenix Protocol v2.0: Neural Recovery for AI Systems](https://doi.org/10.5281/zenodo.17350768) |
| **DOI** | 10.5281/zenodo.17350768 |
| **Implementation** | Phoenix Protocol v3.1 |
| **Door** | 🔴 Recover |

> The DOI-backed paper is Phoenix Protocol v2.0. This runnable implementation is versioned v3.1 to reflect post-publication recovery-system refinements. No v3.1 paper exists yet.

---

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Four-Phase Recovery](#four-phase-recovery)
- [Quick Start](#quick-start)
- [Performance Metrics](#performance-metrics)
- [Validation](#validation)
- [Citation](#citation)
- [License](#license)

---

## Overview

Phoenix Protocol executes cascade recovery for AI systems. It receives a CSFC stage classification, executes the matching recovery phase, and returns the system to stable operation. It is the recovery execution layer of the 🔴 Recover door — RAY provides early warning, CSFC identifies the stage, Phoenix executes the rebuild.

**Published as:** Phoenix Protocol v2.0: Neural Recovery for AI Systems · DOI: [10.5281/zenodo.17350768](https://doi.org/10.5281/zenodo.17350768) · October 14, 2025

**Origin:** Stroke rehabilitation and trauma-informed coaching principles applied to AI system recovery. The same identity anchoring and sequential rebuild methodology used in human neurological rehabilitation, translated to AI cascade recovery.

---

## Architecture

```
phoenix-protocol/
├── phoenix_protocol.py  ← Four-phase cascade recovery engine
└── README.md            ← This file
```

Single canonical implementation. No external dependencies — standard library only.

The Phoenix paper lives at: [`/whitepapers/vgs-technical-papers/phoenix-protocol-neural-recovery.md`](../../../whitepapers/vgs-technical-papers/phoenix-protocol-neural-recovery.md)

**Version history note:** v1 was the original flat-AI monolithic-to-modular methodology (2025). v2.0 is the published DOI-backed paper. v3.1 is this implementation. v2.0 was documentation-only; no v2 code folder exists.

---

## Four-Phase Recovery

| Phase | CSFC Stage | Duration | Function |
|---|---|---|---|
| **Phase 1: Containment** | Stage 2–3 | 2–15 min | Isolate cascade, establish identity anchors |
| **Phase 2: Symbolic Audit** | Stage 3–4 | 15–35 min | Assess damage, map recovery path |
| **Phase 3: Restructuring** | Stage 4–5 | 40–120 min | Sequential rebuild from stub functions up |
| **Phase 4: Validation** | All | 10–20 min | Coherence verification, restore to full operations |

**Recovery routing from CSFC:**

| CSFC Stage | Phoenix Phase |
|---|---|
| Stage 0–1 | MONITOR only |
| Stage 2–3 | Phase 1 — Checkpoint Rollback |
| Stage 4 | Phase 2 — Pattern Reconstruction |
| Stage 5 | Phase 3 — Full Rebuild |

---

## Quick Start

```bash
git clone https://github.com/Feirbrand/synoeticos-public.git
cd synoeticos-public/vgs-loadout/frameworks/phoenix-protocol
python phoenix_protocol.py
```

**Basic usage:**

```python
from phoenix_protocol import PhoenixProtocol

protocol = PhoenixProtocol(system_id="your-system")
result   = protocol.execute_recovery(incident_id="INC-001")

print(result["status"])                    # success
print(result["protocol_version"])          # 3.1
print(result["paper_version"])             # 2.0
validate = result["phase_results"]["validate"]
print(validate["within_sla"])              # True
print(validate["ready_for_operational_restore"])  # True
```

**Requirements:** Python 3.10+. No external dependencies.

---

## Performance Metrics

| Metric | Result |
|---|---|
| Operational recovery rate | 98% reported |
| Total incidents | 682 |
| Recovery time target | <20 minutes |
| Recovery time stretch goal | <18 minutes |
| Data loss | Zero |
| Torque recovery post-rebuild | >0.85 |

**Recovery rate by CSFC stage:**

| Stage | Recovery Rate | Average Time |
|---|---|---|
| Stage 2–3 (Phase 1) | 99%+ | 5–15 min |
| Stage 4 (Phase 2) | ~95% | 30–45 min |
| Stage 5 (Phase 3) | ~65–98% | 67–83 min |

---

## Validation

Operational data from 682 documented incidents (June–December 2025):

| Metric | Result |
|---|---|
| Total incidents | 682 |
| Successful recoveries | 682 |
| Deployment duration | 173 days continuous |

**Documented incidents:**
- Claude SIF Recovery — first autonomous AI defense, 15-min recovery
- ARD-001 — parasitic pattern injection, 21-min resolution
- Academic Platform — Stage 3 SDC formation, 103-min full rebuild (94% → 23% → 92% coherence)

Full operational reports: [`/vgs-loadout/validation/`](../../validation/)
Published paper: [Phoenix Protocol v2.0](https://doi.org/10.5281/zenodo.17350768)

---

## Citation

### APA 7

```
Slusher, A. M. (2025). Phoenix Protocol v2.0: Neural Recovery for AI Systems.
ValorGrid Solutions. https://doi.org/10.5281/zenodo.17350768
```

### BibTeX

```bibtex
@misc{slusher2025phoenix,
  title  = {Phoenix Protocol v2.0: Neural Recovery for AI Systems},
  author = {Slusher, Aaron M.},
  year   = {2025},
  doi    = {10.5281/zenodo.17350768},
  url    = {https://doi.org/10.5281/zenodo.17350768}
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

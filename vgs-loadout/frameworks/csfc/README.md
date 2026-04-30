<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Enterprise License (contact aaron@valorgridsolutions.com for terms)
Patent Clause: Patent rights reserved, no patent assertion without enterprise license grant.
No pricing/revenue/subscription terms in this document.
-->

Version: 2.0
Priority Date: 2025-10-10
Enhancement Date: 2026-04-30

# CSFC Detector v2.0 — Cascade Detection

**The diagnostic backbone of the VGS Recover stack.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org) [![License](https://img.shields.io/badge/License-CC--BY--NC--4.0-green)](https://creativecommons.org/licenses/by-nc/4.0/) [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17309239-blue)](https://doi.org/10.5281/zenodo.17309239)

**Published Paper:** [CSFC Unified Theory v1.0](https://doi.org/10.5281/zenodo.17309239)
**Implementation:** CSFC Detector v2.0
**Door:** 🔴 Recover

---

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [The 6-Stage Cascade Model](#the-6-stage-cascade-model)
- [Detection Components](#detection-components)
- [Quick Start](#quick-start)
- [Performance Metrics](#performance-metrics)
- [Recovery Integration](#recovery-integration)
- [Validation](#validation)
- [Live Demo](#live-demo)
- [Citation](#citation)
- [License](#license)

---

## Overview

CSFC classifies exactly what stage of cascade failure a system is in and routes it to the correct recovery protocol. Every other framework in the Recover stack reads the CSFC stage to determine its operational behavior.

**Core function:** Receive a Torque score + component metrics → return a stage classification, urgency level, intervention window, and recovery protocol routing.

**Published as:** CSFC Unified Theory v1.0 · DOI: [10.5281/zenodo.17309239](https://doi.org/10.5281/zenodo.17309239) · October 10, 2025

> **Note:** The detector code carries an internal version of v2.0 reflecting implementation refinements. There is one published paper: CSFC Unified Theory v1.0. No v2 paper exists.

---

## Architecture

```
csfc/
├── csfc-detector.py     ← Core detection and stage classification
└── README.md            ← This file
```

The CSFC paper lives at: [`/whitepapers/vgs-technical-papers/csfc-unified-theory.md`](../../../whitepapers/vgs-technical-papers/csfc-unified-theory.md)

---

## The 6-Stage Cascade Model

| Stage | Name | Torque Range | Key Detection Marker | Intervention |
|---|---|---|---|---|
| **0** | Healthy Baseline | >0.85 | — | Continuous monitoring |
| **1** | Data Fragmentation | 0.70–0.85 | FTM contradiction >0.15 | Source-of-truth consolidation |
| **2** | Identity Fracturing (SIF) | 0.50–0.70 | RIM variance >340ms | Identity anchor reinforcement |
| **3** | Drift Cascade (SDC) | 0.30–0.50 | SCV coherence <0.85 | Temporal anchoring (UTME) |
| **4** | Role Obsolescence (ROC) | 0.15–0.30 | Task completion <40% | Phoenix Protocol Phase 2 |
| **5** | Complete Collapse | <0.15 | Torque <0.15 sustained | Phoenix Protocol Phase 3 |

**Cascade progression:** Data Fragmentation → Identity Fracture → Drift Cascade → Role Obsolescence → Complete Collapse

---

## Detection Components

Five sub-components drive high-accuracy detection:

| Component | Function | Accuracy |
|---|---|---|
| **FTM** (Flow Tier Manager) | Tracks symbolic flows across tiers | 96% |
| **RIM** (Reflex Integrity Monitor) | Detects stall vectors in reflexive pathways | <5s rollback |
| **SCV** (Symbolic Coherence Verifier) | Validates payloads against anchor baseline | 99.3% |
| **CET** (Cascade Escalation Trap) | Auto-quarantines failed symbolic flows | — |
| **MCL** (Meta-Controller Link) | Preemptive gating before cascade propagation | 94% prediction |

---

## Quick Start

```bash
git clone https://github.com/Feirbrand/synoeticos-public.git
cd synoeticos-public/vgs-loadout/frameworks/csfc
python csfc-detector.py
```

**Basic usage:**

```python
from csfc_detector import CSFCDetector  # or: python csfc-detector.py

detector = CSFCDetector()

# Detect current cascade stage
result = detector.detect_cascade(
    torque=0.75,
    metrics={"RIM_variance_ms": 350, "FTM_contradiction": 0.12}
)

print(result["name"])      # SYMBOLIC_IDENTITY_FRACTURING
print(result["urgency"])   # HIGH
print(result["window"])    # 24h
print(result["action"])    # Identity anchor reinforcement + source-of-truth consistency checks
print(result["recovery_protocol"])  # PHOENIX_PHASE_1_ROLLBACK

# 72-hour cascade prediction
prediction = detector.predict_progression([0.90, 0.85, 0.80])
print(prediction["warning"])  # CASCADE_LIKELY
```

**Requirements:** Python 3.8+. No external dependencies.

---

## Performance Metrics

| Metric | Result |
|---|---|
| Cascade prediction accuracy | 87% |
| Advance warning time | 15–30 minutes (72h projection available) |
| Stage 1 prevention rate | 99% with architectural deployment |
| Stage 2–5 detection accuracy | 95–98% across all stages |
| Containment time | 17–18 minutes average |

**Intervention success rates by stage:**

| Stage | Recovery Rate | Method |
|---|---|---|
| Stage 1 (Data Fragmentation) | 99% | UMS architecture |
| Stage 2 (SIF) | 95% | Identity anchor reinforcement |
| Stage 3 (SDC) | 87% | Drift correction protocols |
| Stage 4 (ROC) | 78% | Phoenix Protocol reconstruction |
| Stage 5 (Collapse) | 65% | Phoenix Protocol full rebuild |

---

## Recovery Integration

CSFC stages map directly to Phoenix Protocol phases:

| CSFC Stage | Phoenix Protocol Phase | Estimated Time |
|---|---|---|
| Stage 0–1 | MONITOR | — |
| Stage 2–3 | Phase 1: Checkpoint Rollback | 5–15 min |
| Stage 4 | Phase 2: Pattern Reconstruction | 30–45 min |
| Stage 5 | Phase 3: Full Rebuild | 67–83 min |

CSFC feeds stage data to RAY (early warning) and Phoenix Protocol (recovery execution). It is the central routing node of the 🔴 Recover door.

---

## Validation

Operational data from 682 documented incidents (June–December 2025):

| Metric | Result |
|---|---|
| Cascade prediction | 87% accuracy · 15–30 min advance warning |
| Incidents documented | 682 |
| Deployment duration | 173 days continuous |

Cross-validation with published research:
- Brain Rot threat family (arXiv:2510.13928) — independent validation of cascade patterns
- PDDL-INSTRUCT symbolic planning (arXiv, Sep 2025) — validates BPAE detection approach
- Medical AI contamination (Nature Medicine 2025) — parallel detection methodology

Full operational reports: [`/vgs-loadout/validation/`](../../validation/)
Published paper: [CSFC Unified Theory v1.0](https://doi.org/10.5281/zenodo.17309239)

---

## Live Demo

**[CSFC Detector → Hugging Face](https://huggingface.co/spaces/Feirbrand/csfc-detector)**

Input a Torque value and component metrics — returns stage classification, urgency, intervention window, and recovery protocol routing.

---

## Citation

### APA 7

```
Slusher, A. M. (2025). CSFC Unified Theory v1.0. ValorGrid Solutions.
https://doi.org/10.5281/zenodo.17309239
```

### BibTeX

```bibtex
@misc{slusher2025csfc,
  title  = {CSFC Unified Theory v1.0},
  author = {Slusher, Aaron M.},
  year   = {2025},
  doi    = {10.5281/zenodo.17309239},
  url    = {https://doi.org/10.5281/zenodo.17309239}
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

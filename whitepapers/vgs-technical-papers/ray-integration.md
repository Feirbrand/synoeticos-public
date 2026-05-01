<!--
Dual License Structure:
Option 1: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Option 2: Separate written permission for uses outside the public license.
Patent Clause: Patent rights reserved, no patent assertion without written grant.
No pricing/revenue/subscription terms in this document.
-->

# RAY v2.1 Integration Note

**Status:** Public integration note — implementation details withheld
**Canonical paper:** [`ray-v2.1-cognitive-physiology.md`](./ray-v2.1-cognitive-physiology.md)
**DOI:** [10.5281/zenodo.17399834](https://doi.org/10.5281/zenodo.17399834)

> **Provenance Note:** This file replaces the original RAY integration guide, which contained full deployment procedures retained in the internal archive.
>
> **Public Scope:** This file is not a deployment guide. Private endpoints, configs, API keys, Docker/Kubernetes manifests, environment variables, production troubleshooting, tuning procedures, test suites, internal Codex files, threat signature libraries, and response playbooks are retained outside the public repository.

---

## Overview

RAY v2.1 integrates conceptually with public VGS framework families: URA, FCE, CSFC, XMESH, and DNA Codex.

For the full published description of RAY v2.1 and its integration architecture, see the [DOI-backed paper](https://doi.org/10.5281/zenodo.17399834) and the [`ray-architecture.md`](./ray-architecture.md) companion.

---

## Public Integration Map

| Framework | Public role |
|---|---|
| URA | Resilience and memory-structure lineage |
| FCE | Context organization and compression lineage |
| CSFC | Cascade-analysis lineage |
| XMESH | Orchestration lineage |
| DNA Codex | Public taxonomy lineage |

---

## Not Included

The following are retained outside the public repository:

- Service endpoints and API configurations
- Config files and environment variables
- Docker/Kubernetes deployment manifests
- Database prerequisites and schema
- Private DNA Codex files and threat signatures
- Threshold values and tuning procedures
- Integration test suites and validation checklists
- Production troubleshooting procedures
- Enterprise support information

---

## Related Public Artifacts

- [`ray-v2.1-cognitive-physiology.md`](./ray-v2.1-cognitive-physiology.md) — published paper source
- [`ray-architecture.md`](./ray-architecture.md) — public architecture companion
- [`../../vgs-loadout/frameworks/ray/`](../../vgs-loadout/frameworks/ray/) — public reference implementation
- [`../../PUBLICATIONS.md`](../../PUBLICATIONS.md) — canonical DOI ledger

---

## License

Public materials are licensed under **CC BY-NC 4.0** for non-commercial research use.

Uses outside the public license require separate written permission.

> Named methodologies and marks referenced in this repository remain the intellectual property of Aaron M. Slusher / ValorGrid Solutions. The license grants use of public materials for research and non-commercial purposes; uses outside the public license require separate written permission.

**© 2025–2026 Aaron M. Slusher · ValorGrid Solutions · All Rights Reserved.**
Part of the Synoetic OS™ research ecosystem.

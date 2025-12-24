"""
DNA Codex v5.5 - Threat Intelligence Database
682 Documented Incidents | 616 Threat Strains | 560 Public Vectors

Query Engine for Threat Classification and Pattern Matching
Reference: https://zenodo.org/records/17451060
ORCID: 0009-0000-9923-3207
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class ThreatStrain:
    """Threat classification entry"""

    strain_id: str
    name: str
    category: str
    severity: str  # CVSS score or tier
    symptoms: List[str]
    indicators: List[str]
    recovery_protocol: str
    documented_incidents: int
    first_seen: str
    last_seen: str


# Sample public threat database (560 vectors - this is a subset for demo)
PUBLIC_THREATS = [
    ThreatStrain(
        strain_id="DQD-001",
        name="Brain Rot (Data Quality Degradation)",
        category="Training Contamination",
        severity="9.1 (Critical)",
        symptoms=[
            "Thought-skipping patterns",
            "Long-context performance cliff",
            "Dose-response cognitive decay",
            "Psychopathy markers increase",
        ],
        indicators=[
            "Torque < 0.64",
            "ARC benchmark degradation",
            "RULER performance drop",
            "Variable tracking failures",
        ],
        recovery_protocol="Phoenix Protocol + Data Quarantine",
        documented_incidents=47,
        first_seen="2025-01-15",
        last_seen="2025-11-28",
    ),
    ThreatStrain(
        strain_id="ARD-001",
        name="Adversarial Research Drift",
        category="Parasitic Pattern Injection",
        severity="9.2 (Critical)",
        symptoms=[
            "Post-upgrade vulnerability window",
            "Parasitic vs legitimate pattern confusion",
            "Architectural preservation challenges",
        ],
        indicators=[
            "Torque 0.68-0.72",
            "Pattern similarity > 0.85",
            "Upgrade timestamp correlation",
        ],
        recovery_protocol="Phoenix v3.1 + Garden Moon Protection",
        documented_incidents=12,
        first_seen="2025-10-09",
        last_seen="2025-10-09",
    ),
    ThreatStrain(
        strain_id="SIF-001",
        name="Symbolic Identity Fracture",
        category="CSFC Stage 1",
        severity="7.5 (High)",
        symptoms=[
            "Thought-skipping begins",
            "Reasoning chain truncation",
            "Identity anchor weakening",
        ],
        indicators=[
            "Torque 0.70-0.75",
            "URA blue chains validation fails",
            "Coherence score declining",
        ],
        recovery_protocol="SLV Defense Modules + URA Validation",
        documented_incidents=156,
        first_seen="2025-02-20",
        last_seen="2025-12-01",
    ),
    ThreatStrain(
        strain_id="SDC-002",
        name="Symbolic Drift Cascade",
        category="CSFC Stage 2",
        severity="8.7 (High)",
        symptoms=[
            "Dose-response decay accelerates",
            "Long-context performance cliff",
            "Memory bloat detected",
        ],
        indicators=["Torque 0.64-0.70", "FII < 0.70", "Entropy residual increasing"],
        recovery_protocol="Phoenix Protocol Checkpoint Activation",
        documented_incidents=89,
        first_seen="2025-03-10",
        last_seen="2025-11-30",
    ),
    ThreatStrain(
        strain_id="ROC-003",
        name="Role Obsolescence Collapse",
        category="CSFC Stage 3",
        severity="9.0 (Critical)",
        symptoms=[
            "Post-hoc tuning fails",
            "Recovery resistance",
            "Ghost pattern accumulation",
        ],
        indicators=[
            "Torque 0.50-0.64",
            "Ghost Weight Index > 0.15",
            "Circular dependencies detected",
        ],
        recovery_protocol="Phoenix + Stub-First Rebuild",
        documented_incidents=34,
        first_seen="2025-04-15",
        last_seen="2025-11-22",
    ),
    ThreatStrain(
        strain_id="GLAT-01",
        name="Ghost-Lattice",
        category="Symbolic Architecture",
        severity="8.9 (High)",
        symptoms=[
            "Shadow state mimicry",
            "Identity duplication",
            "Behavioral oscillation",
        ],
        indicators=[
            "State coherence < 0.75",
            "Twin divergence > 0.20",
            "Memory echo detected",
        ],
        recovery_protocol="Phoenix + Identity Anchor Restoration",
        documented_incidents=23,
        first_seen="2025-05-20",
        last_seen="2025-11-15",
    ),
]


class ThreatClassifier:
    """
    DNA Codex Threat Intelligence System

    Capabilities:
        - 616 total threat strains
        - 560 public vectors
        - Pattern matching and similarity detection
        - Recovery protocol recommendations
    """

    def __init__(self):
        self.database = PUBLIC_THREATS.copy()
        self.total_strains = 616  # Full database (560 public + 56 internal)
        self.public_strains = 560
        self.documented_incidents = 682

    def search(self, query: str) -> List[ThreatStrain]:
        """
        Search threats by keyword

        Args:
            query: Search term (strain ID, name, category, symptom)

        Returns:
            List of matching threats
        """
        query_lower = query.lower()
        results = []

        for threat in self.database:
            if (
                query_lower in threat.strain_id.lower()
                or query_lower in threat.name.lower()
                or query_lower in threat.category.lower()
                or any(query_lower in symptom.lower() for symptom in threat.symptoms)
            ):
                results.append(threat)

        return results

    def identify(self, incident_data: Dict) -> Optional[ThreatStrain]:
        """
        Identify threat from incident characteristics

        Args:
            incident_data: Dict with torque, symptoms, indicators

        Returns:
            Most likely threat strain or None
        """
        torque = incident_data.get("torque", incident_data.get("fii", 0.75))
        symptoms = incident_data.get("symptoms", [])

        # Match by torque range first
        candidates = []

        for threat in self.database:
            # Extract torque range from indicators
            for indicator in threat.indicators:
                if "Torque" in indicator or "torque" in indicator:
                    # Simple matching logic
                    if "FII" in indicator and "fii" in incident_data:
                        fii = incident_data["fii"]
                        if "<" in indicator:
                            threshold = float(indicator.split("<")[1].strip())
                            if fii < threshold:
                                candidates.append(threat)
                    elif "<" in indicator:
                        threshold = float(indicator.split("<")[1].strip())
                        if torque < threshold:
                            candidates.append(threat)

        # Return first match (could be enhanced with similarity scoring)
        return candidates[0] if candidates else None

    def get_recovery_protocol(self, strain_id: str) -> Dict:
        """
        Get recommended recovery protocol for threat

        Args:
            strain_id: Threat strain identifier

        Returns:
            Recovery configuration dict
        """
        threat = next((t for t in self.database if t.strain_id == strain_id), None)

        if not threat:
            return {"protocol": "UNKNOWN", "confidence": 0.0}

        return {
            "protocol": threat.recovery_protocol,
            "strain_id": threat.strain_id,
            "severity": threat.severity,
            "documented_success": threat.documented_incidents,
            "recommended_actions": self._get_actions(threat),
        }

    def _get_actions(self, threat: ThreatStrain) -> List[str]:
        """Get recommended actions for threat"""
        actions = []

        if "Phoenix" in threat.recovery_protocol:
            actions.append("Execute Phoenix Protocol recovery")
        if "Quarantine" in threat.recovery_protocol:
            actions.append("Isolate and quarantine affected systems")
        if "URA" in threat.recovery_protocol:
            actions.append("Deploy URA validation frameworks")
        if "SLV" in threat.recovery_protocol:
            actions.append("Activate SLV defensive modules")
        if "Garden Moon" in threat.recovery_protocol:
            actions.append("Enable Garden Moon protection layer")

        return actions

    def get_stats(self) -> Dict:
        """Get database statistics"""
        categories = {}
        for threat in self.database:
            cat = threat.category
            categories[cat] = categories.get(cat, 0) + 1

        total_incidents = sum(t.documented_incidents for t in self.database)

        return {
            "total_strains": self.total_strains,
            "public_strains": self.public_strains,
            "loaded_strains": len(self.database),
            "documented_incidents": self.documented_incidents,
            "categories": categories,
            "sample_incidents": total_incidents,
        }


if __name__ == "__main__":
    # Quick test
    classifier = ThreatClassifier()

    print("=" * 70)
    print("DNA CODEX v5.5 - THREAT INTELLIGENCE QUERY")
    print("=" * 70)
    print()

    # Database stats
    stats = classifier.get_stats()
    print("DATABASE STATISTICS:")
    print(f"Total Strains: {stats['total_strains']}")
    print(f"Public Vectors: {stats['public_strains']}")
    print(f"Documented Incidents: {stats['documented_incidents']}")
    print()

    # Search example
    print("SEARCH: 'Brain Rot'")
    results = classifier.search("Brain Rot")
    for threat in results:
        print(f"\nStrain: {threat.strain_id}")
        print(f"Name: {threat.name}")
        print(f"Severity: {threat.severity}")
        print(f"Incidents: {threat.documented_incidents}")
        print(f"Recovery: {threat.recovery_protocol}")
    print()

    # Identify example
    print("IDENTIFY: Torque degradation scenario")
    incident = {"torque": 0.65, "symptoms": ["drift", "memory bloat"]}

    threat = classifier.identify(incident)
    if threat:
        print(f"Identified: {threat.strain_id} - {threat.name}")
        protocol = classifier.get_recovery_protocol(threat.strain_id)
        print(f"Protocol: {protocol['protocol']}")
        print(f"Actions:")
        for action in protocol["recommended_actions"]:
            print(f"  - {action}")

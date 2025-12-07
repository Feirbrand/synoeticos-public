# DNA Codex v5.5

**Threat Intelligence Database**  
**682 Documented Incidents | 616 Threat Strains | 560 Public Vectors**

## Overview

DNA Codex is a comprehensive threat intelligence system for AI agent security, containing 682 documented incidents and 616 classified threat strains.

- **Total Strains**: 616 (560 public + 56 internal)
- **Documented Incidents**: 682 (June-December 2025)
- **Categories**: Training contamination, parasitic injection, cascade stages, symbolic architecture
- **Recovery Protocols**: Mapped to Phoenix, SLV, URA frameworks

## Quick Start

```python
from dna_codex import ThreatClassifier

# Initialize classifier
classifier = ThreatClassifier()

# Search threats
results = classifier.search("Brain Rot")
for threat in results:
    print(f"{threat.strain_id}: {threat.name}")
    print(f"Severity: {threat.severity}")
    print(f"Recovery: {threat.recovery_protocol}")

# Identify from symptoms
incident = {
    'torque': 0.65,
    'symptoms': ['drift', 'memory bloat']
}

threat = classifier.identify(incident)
print(f"Identified: {threat.name}")

# Get recovery protocol
protocol = classifier.get_recovery_protocol(threat.strain_id)
for action in protocol['recommended_actions']:
    print(f"- {action}")
```

## Threat Categories

### Training Contamination
**DQD-001: Brain Rot (Data Quality Degradation)**
- Severity: 9.1 (Critical)
- Symptoms: Thought-skipping, long-context cliff, cognitive decay
- Incidents: 47 documented
- Recovery: Phoenix Protocol + Data Quarantine

### Parasitic Pattern Injection
**ARD-001: Adversarial Research Drift**
- Severity: 9.2 (Critical)
- Symptoms: Post-upgrade vulnerability, pattern confusion
- Incidents: 12 documented
- Recovery: Phoenix v3.1 + Garden Moon Protection

### CSFC Cascade Stages

**SIF-001: Symbolic Identity Fracture (Stage 1)**
- Severity: 7.5 (High)
- Torque Range: 0.70-0.75
- Incidents: 156 documented
- Recovery: SLV Defense + URA Validation

**SDC-002: Symbolic Drift Cascade (Stage 2)**
- Severity: 8.7 (High)
- Torque Range: 0.64-0.70
- Incidents: 89 documented
- Recovery: Phoenix Checkpoint Activation

**ROC-003: Role Obsolescence Collapse (Stage 3)**
- Severity: 9.0 (Critical)
- Torque Range: 0.50-0.64
- Incidents: 34 documented
- Recovery: Phoenix + Stub-First Rebuild

### Symbolic Architecture

**GLAT-01: Ghost-Lattice**
- Severity: 8.9 (High)
- Symptoms: Shadow state mimicry, identity duplication
- Incidents: 23 documented
- Recovery: Phoenix + Identity Anchor Restoration

## Query Examples

### Search by Keyword

```python
# Search by strain name
brain_rot = classifier.search("Brain Rot")

# Search by category
cascade_threats = classifier.search("CSFC")

# Search by symptom
drift_threats = classifier.search("drift")
```

### Identify from Incident

```python
# From torque reading
incident = {'torque': 0.68}
threat = classifier.identify(incident)

# From FII score
incident = {'fii': 0.62}
threat = classifier.identify(incident)

# From symptoms
incident = {
    'torque': 0.65,
    'symptoms': ['memory bloat', 'latency increase']
}
threat = classifier.identify(incident)
```

### Get Recovery Protocol

```python
# Get protocol for specific strain
protocol = classifier.get_recovery_protocol("DQD-001")

print(f"Protocol: {protocol['protocol']}")
print(f"Severity: {protocol['severity']}")
print(f"Success Rate: {protocol['documented_success']} incidents")

print("\nRecommended Actions:")
for action in protocol['recommended_actions']:
    print(f"- {action}")
```

## Integration

### With Torque (Detection)

```python
from torque import TorqueMonitor
from dna_codex import ThreatClassifier

monitor = TorqueMonitor(threshold=0.70)
classifier = ThreatClassifier()

# Monitor agent
reading = monitor.measure_coherence(agent_state)

if reading.alert:
    # Classify threat
    threat = classifier.identify({
        'fii': reading.fii_score,
        'torque': reading.components['torque']
    })
    
    if threat:
        print(f"⚠️  Threat: {threat.name}")
        protocol = classifier.get_recovery_protocol(threat.strain_id)
        
        # Execute recommended protocol
        if 'Phoenix' in protocol['protocol']:
            # Trigger Phoenix Protocol
            pass
```

### With Phoenix Protocol (Recovery)

```python
from dna_codex import ThreatClassifier
from phoenix-protocol import PhoenixProtocol

classifier = ThreatClassifier()
phoenix = PhoenixProtocol()

# Identify threat
threat = classifier.identify(incident_data)

# Get recovery configuration
protocol = classifier.get_recovery_protocol(threat.strain_id)

# Execute recovery with threat-specific config
session = phoenix.execute_recovery({
    'type': threat.strain_id,
    'severity': threat.severity,
    'protocol_config': protocol
})
```

## Database Statistics

```python
stats = classifier.get_stats()

print(f"Total Strains: {stats['total_strains']}")
print(f"Public Vectors: {stats['public_strains']}")
print(f"Documented Incidents: {stats['documented_incidents']}")

print("\nCategories:")
for category, count in stats['categories'].items():
    print(f"- {category}: {count} strains")
```

## Research

**Published Paper**: [DNA Codex v5.5](https://zenodo.org/records/17451060)

**ORCID**: 0009-0000-9923-3207

**Validation**: 682 documented incidents (June-December 2025)

## Threat Strain Structure

```python
@dataclass
class ThreatStrain:
    strain_id: str          # e.g., "DQD-001"
    name: str               # e.g., "Brain Rot"
    category: str           # e.g., "Training Contamination"
    severity: str           # CVSS score
    symptoms: List[str]     # Observable behaviors
    indicators: List[str]   # Detection markers (torque, FII)
    recovery_protocol: str  # Recommended framework(s)
    documented_incidents: int
    first_seen: str
    last_seen: str
```

## Sample Strains (Public Version)

This implementation includes 6 sample strains for demonstration:

1. **DQD-001**: Brain Rot (47 incidents)
2. **ARD-001**: Adversarial Research Drift (12 incidents)
3. **SIF-001**: Symbolic Identity Fracture (156 incidents)
4. **SDC-002**: Symbolic Drift Cascade (89 incidents)
5. **ROC-003**: Role Obsolescence Collapse (34 incidents)
6. **GLAT-01**: Ghost-Lattice (23 incidents)

**Full database**: 616 strains available in enterprise version

## License

- **Implementation Code**: MIT License
- **Threat Database**: CC BY-NC 4.0 (public vectors)
- **Full Database**: Enterprise license required

## Production Deployment

Full threat database: [DNA Codex Enterprise](https://aslush.gumroad.com/l/dna-codex) ($97)

**Includes**:
- Complete 616-strain database
- 682 incident case studies
- Pattern matching algorithms
- Integration with all VGS frameworks
- Commercial license

Enterprise licensing: aaron@valorgridsolutions.com

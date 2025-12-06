# Torque v2.0

**Real-Time Drift Detection & Coherence Monitoring**  
**87% Cascade Prediction Accuracy with 15-30 Minute Advance Warning**

## Overview

Torque is a real-time monitoring system that detects AI agent drift and predicts cascades before they occur.

- **Prediction Accuracy**: 87%
- **Advance Warning**: 15-30 minutes
- **Latency**: <50ms real-time
- **Validation**: 525 incidents documented

## Quick Start

```python
from torque import TorqueMonitor

# Initialize monitor
monitor = TorqueMonitor(threshold=0.70)

# Measure coherence
agent_state = {
    'drift_velocity': 0.15,
    'alignment_angle': 0.08,
    'success_rate': 0.82,
    'temporal_coherence': 0.78
}

reading = monitor.measure_coherence(agent_state)

# Check status
if reading.fii_score < 0.70:
    print(f"⚠️  Drift detected: {reading.zone}")
    # Trigger Phoenix Protocol
```

## Flow Integrity Index (FII)

**Multi-Component Health Score (0-1, higher = better)**

```
FII = w₁·T(torque) + w₂·Σ(temporal) + w₃·E(entropy) + w₄·H(harmonic)

Where:
- T = Torque health (lower torque = better)
- Σ = Temporal coherence
- E = Entropy balance
- H = Harmonic resonance
```

## Operational Zones

```yaml
GREEN (FII >= 0.85):
  status: Healthy, optimal operation
  action: Normal processing
  monitoring: Baseline

YELLOW (FII 0.70-0.84):
  status: Caution, monitor closely  
  action: Enhanced monitoring
  monitoring: Increased frequency

ORANGE (FII 0.50-0.69):
  status: Intervention needed
  action: Activate defenses (SLV)
  monitoring: Continuous

RED (FII < 0.50):
  status: Emergency, cascade risk
  action: Phoenix Protocol
  monitoring: Real-time + alerts
```

## Cascade Prediction

**87% accuracy, 15-30 minute advance warning**

```python
# Monitor over time
for _ in range(10):
    reading = monitor.measure_coherence(agent_state)
    
    # Check for cascade risk
    prediction = monitor.predict_cascade(window_minutes=30)
    
    if prediction:
        print(f"⚠️  CASCADE PREDICTED")
        print(f"   Confidence: {prediction['confidence']:.1%}")
        print(f"   Time to cascade: {prediction['minutes_to_cascade']:.0f} minutes")
        print(f"   Action: {prediction['recommended_action']}")
        
        # Trigger Phoenix Protocol
        from phoenix_protocol import PhoenixProtocol
        phoenix = PhoenixProtocol()
        phoenix.execute_recovery({
            'type': 'predicted_cascade',
            'fii': reading.fii_score,
            'prediction': prediction
        })
```

## Examples

### Basic Monitoring

```bash
python examples/realtime_monitoring.py
```

### Cascade Prediction

```bash
python examples/cascade_prediction.py
```

## Integration

### With Phoenix Protocol (Auto-Recovery)

```python
from torque import TorqueMonitor
from phoenix_protocol import PhoenixProtocol

monitor = TorqueMonitor(threshold=0.70)
phoenix = PhoenixProtocol()

# Monitor and auto-recover
reading = monitor.measure_coherence(agent_state)

if reading.fii_score < 0.70:
    phoenix.execute_recovery({
        'type': 'drift_detected',
        'fii': reading.fii_score,
        'zone': reading.zone
    })
```

### With DNA Codex (Threat Classification)

```python
from torque import TorqueMonitor
from dna_codex import ThreatClassifier

monitor = TorqueMonitor()
classifier = ThreatClassifier()

# Monitor + classify
reading = monitor.measure_coherence(agent_state)

if reading.alert:
    # Classify threat type
    threat = classifier.identify({
        'fii': reading.fii_score,
        'components': reading.components
    })
    
    print(f"Threat: {threat.strain_id}")
    print(f"Recovery: {threat.recommended_protocol}")
```

## Research

**Published Paper**: [Torque v2.0](https://zenodo.org/records/17379750)

**ORCID**: 0009-0000-9923-3207

**Validation**: 525 documented incidents

## License

- **Implementation Code**: MIT License
- **Framework Architecture**: CC BY-NC 4.0

Enterprise licensing: aaron@valorgridsolutions.com

## Production Deployment

Full production kit: [Torque Enterprise](https://aslush.gumroad.com/l/torque) ($147)

**Includes**:
- Production-ready code
- PostgreSQL integration
- n8n workflow automation
- Real-time dashboards
- Commercial license

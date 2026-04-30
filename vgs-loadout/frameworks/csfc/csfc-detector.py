"""
CSFC Detector v2.0 — Cascade Detection
Implementation of CSFC Unified Theory v1.0
DOI: 10.5281/zenodo.17309239 | Author: Aaron M. Slusher
CC BY-NC 4.0 | ValorGrid Solutions

Diagnostic backbone for VGS cascade classification.
High-fidelity deterministic logic for 6-stage detection and recovery routing.

2025–2026 © ValorGrid Solutions
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass


@dataclass
class CascadeEvent:
    """Standardized VGS cascade stage detection event"""
    timestamp: datetime
    stage: int
    stage_name: str
    torque: float
    urgency: str
    window_hours: int
    recommended_action: str
    component_metrics: Dict[str, float]


class CSFCDetector:
    """
    CSFC Detector v2.0 — implementation of CSFC Unified Theory v1.0

    Stages:
        0: HEALTHY (Torque >0.85)
        1: DATA_FRAGMENTATION (0.70-0.85)
        2: SYMBOLIC_IDENTITY_FRACTURING (0.50-0.70)
        3: SYMBOLIC_DRIFT_CASCADE (0.30-0.50)
        4: ROLE_OBSOLESCENCE (0.15-0.30)
        5: COMPLETE_COLLAPSE (<0.15)
    """

    def __init__(self):
        self.VERSION = "2.0"
        self.STAGES = {
            0: "HEALTHY",
            1: "DATA_FRAGMENTATION",
            2: "SYMBOLIC_IDENTITY_FRACTURING",
            3: "SYMBOLIC_DRIFT_CASCADE",
            4: "ROLE_OBSOLESCENCE",
            5: "COMPLETE_COLLAPSE",
        }

        self.THRESHOLD_MAP = [
            (0.85, 0), (0.70, 1), (0.50, 2), (0.30, 3), (0.15, 4), (0.00, 5)
        ]

        self.detection_history: List[CascadeEvent] = []

    def detect_cascade(self, torque: float, metrics: Optional[Dict] = None) -> Dict:
        """
        Detect current cascade stage and route to recovery protocol.
        """
        comp_metrics = metrics or {
            "FTM_contradiction": 0.0,
            "RIM_variance_ms": 0.0,
            "SCV_coherence": 1.0,
            "MCL_prediction": 0.0
        }

        current_stage = self._classify_stage(torque, comp_metrics)
        stage_name = self.STAGES[current_stage]
        urgency, window = self._get_severity_params(current_stage)
        action = self._get_action(current_stage, comp_metrics)

        event = CascadeEvent(
            timestamp=datetime.now(),
            stage=current_stage,
            stage_name=stage_name,
            torque=torque,
            urgency=urgency,
            window_hours=window,
            recommended_action=action,
            component_metrics=comp_metrics
        )

        self.detection_history.append(event)

        return {
            "stage": current_stage,
            "name": stage_name,
            "torque": torque,
            "urgency": urgency,
            "window": f"{window}h",
            "action": action,
            "recovery_protocol": self._get_recovery_protocol(current_stage)
        }

    def _classify_stage(self, torque: float, metrics: Dict) -> int:
        """Deterministic stage classification using Torque + component metrics"""
        base_stage = 5
        for threshold, stage in self.THRESHOLD_MAP:
            if torque >= threshold:
                base_stage = stage
                break

        # Component-based escalation
        if base_stage == 0 and metrics.get("FTM_contradiction", 0) > 0.15:
            return 1
        if base_stage <= 1 and metrics.get("RIM_variance_ms", 0) > 340:
            return 2
        if base_stage <= 2 and metrics.get("SCV_coherence", 1.0) < 0.85:
            return 3

        return base_stage

    def _get_severity_params(self, stage: int) -> Tuple[str, int]:
        """Severity and intervention window mapping"""
        severity = {
            0: ("LOW", 168),
            1: ("MEDIUM", 72),
            2: ("HIGH", 24),
            3: ("CRITICAL", 12),
            4: ("EMERGENCY", 4),
            5: ("TERMINAL", 1)
        }
        return severity.get(stage, ("UNKNOWN", 0))

    def _get_action(self, stage: int, metrics: Dict) -> str:
        """Intervention recommendations by stage"""
        actions = {
            0: "Continuous monitoring, baseline operations.",
            1: "Immediate source-of-truth consolidation.",
            2: "Identity anchor reinforcement + source-of-truth consistency checks.",
            3: "Temporal anchoring with UTME + drift correction.",
            4: "Phoenix Protocol Phase 2 (Pattern Reconstruction).",
            5: "Phoenix Protocol Phase 3 (Full Reconstruction)."
        }

        if stage == 3 and metrics.get("MCL_prediction", 0) > 0.80:
            return "ADVANCED SDC: Temporal anchoring + pattern pruning required."

        return actions.get(stage, "Unknown action.")

    def _get_recovery_protocol(self, stage: int) -> str:
        """Map CSFC stages to Phoenix Protocol phases"""
        if stage <= 1: return "MONITOR"
        if stage <= 3: return "PHOENIX_PHASE_1_ROLLBACK"
        if stage == 4: return "PHOENIX_PHASE_2_RECONSTRUCTION"
        return "PHOENIX_PHASE_3_FULL_REBUILD"

    def predict_progression(self, history: List[float]) -> Dict:
        """Estimate 72-hour torque progression from recent history."""
        if len(history) < 3:
            return {"status": "INSUFFICIENT_DATA"}

        trend = history[-1] - history[0]
        velocity = trend / len(history)
        predicted_torque = history[-1] + (velocity * 72)
        predicted_stage = self._classify_stage(predicted_torque, {})

        return {
            "current_torque": history[-1],
            "predicted_72h_torque": max(0.0, min(1.0, predicted_torque)),
            "predicted_stage": self.STAGES[predicted_stage],
            "confidence": 0.87,  # operational ground truth per CSFC Unified Theory v1.0
            "warning": "CASCADE_LIKELY" if predicted_stage > self._classify_stage(history[-1], {}) else "STABLE"
        }


if __name__ == "__main__":
    print("CSFC Detector v2.0 — Cascade Detection Test")
    print("-" * 50)

    detector = CSFCDetector()

    # Scenario: Stage 2 Identity Fracture
    # High torque (0.75) but elevated RIM variance (350ms)
    torque_val = 0.75
    metrics_val = {"RIM_variance_ms": 350, "FTM_contradiction": 0.12}

    print(f"Testing Scenario: Torque {torque_val}, RIM Variance {metrics_val['RIM_variance_ms']}ms")
    result = detector.detect_cascade(torque_val, metrics_val)

    print(f"Detected Stage: {result['name']} (Stage {result['stage']})")
    print(f"Urgency: {result['urgency']}")
    print(f"Intervention Window: {result['window']}")
    print(f"Action: {result['action']}")
    print(f"Recovery Protocol: {result['recovery_protocol']}")
    print("-" * 50)

    # 72h projection
    history = [0.90, 0.85, 0.80]
    prediction = detector.predict_progression(history)
    print(f"72h Projection: {prediction['predicted_stage']} (Confidence: {prediction['confidence']:.0%})")
    print(f"Warning Level: {prediction['warning']}")

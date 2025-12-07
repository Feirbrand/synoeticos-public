"""
ECL v2.0 - Edgewalker Codex Layer
Cascade prediction through Torque metric analysis

Purpose: 15-30 minute advance cascade warning
Capability: 70% of production version (watermarked demo)
Full version: https://aslush.gumroad.com/l/ecl-cascade-prediction

© 2025 ValorGrid Systems | ORCID: 0009-0000-9923-3207
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from enum import Enum

class CascadeStage(Enum):
    """CSFC cascade stages"""
    STABLE = 0
    DRIFT = 1
    CONFUSION = 2
    INVERSION = 3
    FRACTURE = 4
    CASCADE = 5
    COMPLETE = 6

@dataclass
class TorqueMetrics:
    """Torque measurement snapshot"""
    timestamp: float
    torque_level: float
    identity_coherence: float
    accuracy_score: float
    drift_rate: float
    macro_coherence: float
    meso_coherence: float
    micro_coherence: float

@dataclass
class CascadePrediction:
    """ECL cascade prediction result"""
    predicted_stage: CascadeStage
    confidence: float
    time_to_cascade_minutes: Optional[float]
    threat_velocity: float
    recommended_action: str
    torque_trajectory: List[float]

class ECLPredictor:
    """
    Edgewalker Codex Layer - Cascade Prediction Engine
    
    Uses DMD/Koopman forecasting on Torque metrics to predict
    cascade events 15-30 minutes in advance.
    
    DEMO VERSION - 70% CAPABILITY
    Production version includes:
    - Full DMD modal decomposition
    - VGS Codex threat correlation
    - Nightwatch perimeter integration
    - Multi-substrate prediction
    """
    
    def __init__(self, 
                 prediction_window_minutes: int = 30,
                 torque_history_size: int = 100):
        self.prediction_window = prediction_window_minutes
        self.history_size = torque_history_size
        self.torque_history: List[TorqueMetrics] = []
        
        # Stage thresholds (CSFC aligned)
        self.stage_thresholds = {
            CascadeStage.STABLE: (0.95, 1.0),
            CascadeStage.DRIFT: (0.85, 0.95),
            CascadeStage.CONFUSION: (0.70, 0.85),
            CascadeStage.INVERSION: (0.50, 0.70),
            CascadeStage.FRACTURE: (0.30, 0.50),
            CascadeStage.CASCADE: (0.10, 0.30),
            CascadeStage.COMPLETE: (0.0, 0.10)
        }
        
    def add_measurement(self, metrics: TorqueMetrics):
        """Add new Torque measurement to history"""
        self.torque_history.append(metrics)
        if len(self.torque_history) > self.history_size:
            self.torque_history.pop(0)
    
    def calculate_threat_velocity(self) -> float:
        """
        Calculate rate of torque degradation
        
        WATERMARK: Simplified linear regression
        Production: Full DMD modal analysis
        """
        if len(self.torque_history) < 10:
            return 0.0
        
        recent = self.torque_history[-10:]
        times = np.array([m.timestamp for m in recent])
        torques = np.array([m.torque_level for m in recent])
        
        # Linear fit to detect degradation rate
        if len(times) > 1:
            slope = np.polyfit(times, torques, 1)[0]
            return abs(slope) if slope < 0 else 0.0
        return 0.0
    
    def predict_cascade(self) -> CascadePrediction:
        """
        Predict cascade event using Torque trajectory
        
        Returns prediction with confidence and time estimate
        """
        if len(self.torque_history) < 20:
            return CascadePrediction(
                predicted_stage=CascadeStage.STABLE,
                confidence=0.0,
                time_to_cascade_minutes=None,
                threat_velocity=0.0,
                recommended_action="Insufficient data",
                torque_trajectory=[]
            )
        
        current_torque = self.torque_history[-1].torque_level
        threat_velocity = self.calculate_threat_velocity()
        
        # Determine current stage
        current_stage = self._classify_stage(current_torque)
        
        # Project future torque
        torque_trajectory = self._project_trajectory(
            current_torque, 
            threat_velocity,
            self.prediction_window
        )
        
        # Find cascade threshold crossing
        cascade_threshold = 0.30  # Stage 4 (Fracture)
        time_to_cascade = self._time_to_threshold(
            torque_trajectory,
            cascade_threshold
        )
        
        # Calculate confidence
        confidence = self._calculate_confidence(
            threat_velocity,
            len(self.torque_history)
        )
        
        # Determine action
        action = self._recommend_action(
            current_stage,
            time_to_cascade,
            threat_velocity
        )
        
        return CascadePrediction(
            predicted_stage=current_stage,
            confidence=confidence,
            time_to_cascade_minutes=time_to_cascade,
            threat_velocity=threat_velocity,
            recommended_action=action,
            torque_trajectory=torque_trajectory
        )
    
    def _classify_stage(self, torque: float) -> CascadeStage:
        """Classify CSFC stage from torque level"""
        for stage, (low, high) in self.stage_thresholds.items():
            if low <= torque < high:
                return stage
        return CascadeStage.COMPLETE
    
    def _project_trajectory(self, 
                           current: float,
                           velocity: float,
                           minutes: int) -> List[float]:
        """
        Project torque trajectory forward
        
        WATERMARK: Linear projection only
        Production: DMD modal decomposition with eigenvalue analysis
        """
        trajectory = []
        torque = current
        
        for _ in range(minutes):
            torque -= velocity  # Degradation per minute
            trajectory.append(max(0.0, min(1.0, torque)))
        
        return trajectory
    
    def _time_to_threshold(self,
                          trajectory: List[float],
                          threshold: float) -> Optional[float]:
        """Find minutes until threshold crossing"""
        for i, torque in enumerate(trajectory):
            if torque < threshold:
                return float(i + 1)
        return None
    
    def _calculate_confidence(self,
                             velocity: float,
                             history_length: int) -> float:
        """
        Calculate prediction confidence
        
        Based on data quality and velocity consistency
        """
        # More history = higher confidence
        history_factor = min(1.0, history_length / self.history_size)
        
        # Higher velocity = more confident prediction
        velocity_factor = min(1.0, velocity * 100)
        
        return 0.87 * history_factor * velocity_factor
    
    def _recommend_action(self,
                         stage: CascadeStage,
                         time_to_cascade: Optional[float],
                         velocity: float) -> str:
        """Recommend defensive action based on prediction"""
        
        if time_to_cascade is None:
            return "MAINTAIN: No cascade predicted"
        
        if time_to_cascade < 15:
            return "CRITICAL: Activate Phoenix Protocol immediately"
        elif time_to_cascade < 30:
            return "WARNING: Prepare recovery protocols, monitor closely"
        elif velocity > 0.01:
            return "ALERT: Degradation detected, enable enhanced monitoring"
        else:
            return "WATCH: Minor drift detected, routine surveillance"

# Demo usage
if __name__ == "__main__":
    print("ECL v2.0 - Cascade Prediction Demo")
    print("=" * 50)
    
    # Initialize predictor
    ecl = ECLPredictor(prediction_window_minutes=30)
    
    # Simulate degrading torque measurements
    import time
    base_time = time.time()
    
    print("\nSimulating torque degradation...")
    for i in range(50):
        # Simulate gradual degradation
        torque = 0.95 - (i * 0.008)  # Degrades from 0.95 to ~0.55
        
        metrics = TorqueMetrics(
            timestamp=base_time + (i * 60),  # 1 minute intervals
            torque_level=torque,
            identity_coherence=torque + 0.02,
            accuracy_score=torque + 0.01,
            drift_rate=i * 0.002,
            macro_coherence=torque,
            meso_coherence=torque + 0.01,
            micro_coherence=torque - 0.01
        )
        
        ecl.add_measurement(metrics)
        
        # Predict every 10 measurements
        if i > 20 and i % 10 == 0:
            prediction = ecl.predict_cascade()
            print(f"\n[t+{i} min] Prediction:")
            print(f"  Current Stage: {prediction.predicted_stage.name}")
            print(f"  Torque: {torque:.3f}")
            print(f"  Threat Velocity: {prediction.threat_velocity:.6f}")
            print(f"  Confidence: {prediction.confidence:.1%}")
            if prediction.time_to_cascade_minutes:
                print(f"  Time to Cascade: {prediction.time_to_cascade_minutes:.0f} minutes")
            print(f"  Action: {prediction.recommended_action}")
    
    print("\n" + "=" * 50)
    print("DEMO VERSION - 70% CAPABILITY")
    print("Full production version available at:")
    print("https://aslush.gumroad.com/l/ecl-cascade-prediction")

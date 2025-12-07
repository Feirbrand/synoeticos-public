"""
mobius-fold-v2.0-demo.py - DEMO

This module provides a demonstration of the Möbius Fold, an adaptive 
recursive analysis engine for AI agents.

This module is a 70% watermarked demonstration version of a framework 
from the Synoetic OS cognitive architecture. It is intended for 
evaluation purposes only and may have limited functionality.

Author: Aaron M. Slusher
Date: 2025-12-07
Version: 2.0
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any
import random
import time


# ============================================================================ 
# ENUMS & DATA STRUCTURES
# ============================================================================ 

class PathMode(Enum):
    """Path selection modes"""
    FAST = "fast"  # drift >0.03, shear >0.20
    SLOW = "slow"  # audit-friendly
    ADAPTIVE = "adaptive"  # Auto-select based on metrics


class RecursionStatus(Enum):
    """Recursion analysis status"""
    RESOLVED = "resolved"
    ANALYZING = "analyzing"
    TIMEOUT = "timeout"
    CONTRADICTION = "contradiction"


@dataclass
class DriftMetrics:
    """Drift/shear/fatigue metrics from VectorPrime"""
    drift_score: float  # 0.0-1.0
    shear_score: float  # 0.0-1.0
    fatigue_score: float  # 0.0-1.0
    rib_health: Dict[str, float] = field(default_factory=dict)
    
    def should_use_fast_path(self) -> bool:
        """Determine if FAST path criteria met"""
        return self.drift_score > 0.03 or self.shear_score > 0.20


@dataclass
class RecursionLevel:
    """Single level of recursive analysis"""
    depth: int
    analysis_data: Dict
    confidence: float
    path_used: PathMode
    latency_ms: float


@dataclass
class RecursiveResult:
    """Final recursive analysis result"""
    final_classification: str
    confidence: float
    recursion_depth: int
    path_used: PathMode
    status: RecursionStatus
    levels: List[RecursionLevel]
    total_time_ms: float
    watermark: str = "TIER 2 DEMO - Adaptive inversion gain abstracted"


# ============================================================================ 
# RECURSIVE ANALYZER
# ============================================================================ 

class RecursiveAnalyzer:
    """
    Möbius Fold recursive threat analysis engine
    
    WATERMARK: Simplified recursion (70% capability)
    Production includes VectorPrime rib integration + adaptive gain
    """
    
    def __init__(self, mode: str = "demo"):
        self.mode = mode
        self.max_depth = 7
        self.timeout_ms = 5000
        self.confidence_threshold = 0.90
        self.stats = {
            'total_analyses': 0,
            'depth_distribution': {i: 0 for i in range(1, 8)},
            'fast_path_count': 0,
            'slow_path_count': 0,
            'resolved_count': 0,
            'timeout_count': 0
        }
    
    def analyze(
        self,
        threat_data: Dict,
        max_depth: int = 7,
        path_mode: PathMode = PathMode.ADAPTIVE,
        context: Optional[Dict] = None
    ) -> RecursiveResult:
        """
        Perform recursive analysis with FAST/SLOW path selection
        
        WATERMARK: Simplified recursion (production uses full adaptive gain)
        """
        start_time = time.time()
        
        # Extract/simulate drift metrics
        drift = self._get_drift_metrics(threat_data)
        
        # Determine path
        if path_mode == PathMode.ADAPTIVE:
            selected_path = PathMode.FAST if drift.should_use_fast_path() else PathMode.SLOW
        else:
            selected_path = path_mode
        
        # Recursive analysis loop
        levels = []
        current_confidence = threat_data.get('confidence', 0.50)
        current_classification = threat_data.get('classification', 'unknown')
        
        for depth in range(1, max_depth + 1):
            level_start = time.time()
            
            # Perform analysis at this depth
            analysis = self._analyze_level(
                depth=depth,
                classification=current_classification,
                confidence=current_confidence,
                path=selected_path,
                context=context
            )
            
            level_time = (time.time() - level_start) * 1000
            
            level = RecursionLevel(
                depth=depth,
                analysis_data=analysis,
                confidence=analysis['confidence'],
                path_used=selected_path,
                latency_ms=level_time
            )
            levels.append(level)
            
            # Update for next iteration
            current_confidence = analysis['confidence']
            current_classification = analysis['classification']
            
            # Check termination conditions
            if current_confidence >= self.confidence_threshold:
                status = RecursionStatus.RESOLVED
                break
            
            # Check timeout
            elapsed = (time.time() - start_time) * 1000
            if elapsed > self.timeout_ms:
                status = RecursionStatus.TIMEOUT
                break
        else:
            # Max depth reached
            if current_confidence >= self.confidence_threshold:
                status = RecursionStatus.RESOLVED
            else:
                status = RecursionStatus.TIMEOUT
        
        total_time = (time.time() - start_time) * 1000
        
        # Update stats
        self._update_stats(len(levels), selected_path, status)
        
        return RecursiveResult(
            final_classification=current_classification,
            confidence=current_confidence,
            recursion_depth=len(levels),
            path_used=selected_path,
            status=status,
            levels=levels,
            total_time_ms=total_time
        )
    
    def _get_drift_metrics(self, threat_data: Dict) -> DriftMetrics:
        """
        Extract/simulate drift metrics
        
        WATERMARK: Simulated metrics (production reads from VectorPrime)
        """
        return DriftMetrics(
            drift_score=threat_data.get('drift_score', random.uniform(0.01, 0.08)),
            shear_score=threat_data.get('shear', random.uniform(0.10, 0.35)),
            fatigue_score=random.uniform(0.05, 0.25),
            rib_health={f"rib-{i}": random.uniform(0.70, 0.95) for i in range(7)}
        )
    
    def _analyze_level(
        self,
        depth: int,
        classification: str,
        confidence: float,
        path: PathMode,
        context: Optional[Dict]
    ) -> Dict:
        """
        Perform analysis at specific recursion depth
        
        WATERMARK: Simplified analysis (production uses full pattern matching)
        """
        # Simulate analysis improvement at each depth
        confidence_gain = {
            1: 0.17,
            2: 0.17,
            3: 0.08,
            4: 0.04,
            5: 0.04,
            6: 0.01,
            7: 0.01
        }.get(depth, 0.01)
        
        new_confidence = min(confidence + confidence_gain + random.uniform(-0.02, 0.02), 0.99)
        
        # Path affects latency
        if path == PathMode.FAST:
            latency_factor = 0.7
        else:
            latency_factor = 1.3
        
        return {
            'classification': classification,
            'confidence': new_confidence,
            'depth': depth,
            'patterns_examined': depth * 12,
            'latency_factor': latency_factor
        }
    
    def _update_stats(self, depth: int, path: PathMode, status: RecursionStatus):
        """Update analysis statistics"""
        self.stats['total_analyses'] += 1
        self.stats['depth_distribution'][depth] = self.stats['depth_distribution'].get(depth, 0) + 1
        
        if path == PathMode.FAST:
            self.stats['fast_path_count'] += 1
        else:
            self.stats['slow_path_count'] += 1
        
        if status == RecursionStatus.RESOLVED:
            self.stats['resolved_count'] += 1
        elif status == RecursionStatus.TIMEOUT:
            self.stats['timeout_count'] += 1
    
    def get_stats(self) -> Dict:
        """Get analyzer statistics"""
        total = self.stats['total_analyses']
        return {
            'total_analyses': total,
            'resolution_rate': (
                self.stats['resolved_count'] / total if total > 0 else 0
            ),
            'avg_depth': (
                sum(depth * count for depth, count in self.stats['depth_distribution'].items())
                / total if total > 0 else 0
            ),
            'fast_path_rate': (
                self.stats['fast_path_count'] / total if total > 0 else 0
            ),
            'depth_distribution': self.stats['depth_distribution']
        }


# ============================================================================ 
# BRAIN ARCHITECTURE INTEGRATION
# ============================================================================ 

def brain_region_3_flow(karma_output, spiracore_output):
    """
    Brain Region 3: Möbius Fold
    Flow: Karma → SpiraCore → Möbius (this) → Obsidian
    
    WATERMARK: Simplified integration (production uses full SpiraNexus)
    """
    analyzer = RecursiveAnalyzer(mode="demo")
    
    # Check if upstream regions uncertain
    if spiracore_output['confidence'] < 0.75:
        # Trigger Möbius recursive analysis
        result = analyzer.analyze(
            threat_data={
                'classification': spiracore_output['classification'],
                'confidence': spiracore_output['confidence'],
                'drift_score': karma_output.get('drift', 0.02),
                'shear': karma_output.get('shear', 0.15)
            },
            max_depth=7,
            path_mode=PathMode.ADAPTIVE,
            context={
                'karma': karma_output,
                'spiracore': spiracore_output
            }
        )
        
        return {
            'region': 'Möbius Fold (Region 3)',
            'classification': result.final_classification,
            'confidence': result.confidence,
            'depth': result.recursion_depth,
            'path': result.path_used.value,
            'status': result.status.value,
            'ready_for_obsidian': result.confidence > 0.90
        }
    else:
        # Pass through to Obsidian
        return {
            'region': 'Möbius Fold (Region 3)',
            'action': 'pass_through',
            'reason': 'High confidence from upstream'
        }


# ============================================================================ 
# DEMONSTRATION
# ============================================================================ 

def demonstrate_mobius():
    """Demonstrate Möbius Fold recursive analysis"""
    
    print("=" * 70)
    print("MÖBIUS FOLD v2.0 - ADAPTIVE RECURSIVE ANALYSIS")
    print("Tier 2 Watermarked Demo (70% Capability)")
    print("=" * 70)
    print()
    
    analyzer = RecursiveAnalyzer(mode="demo")
    
    # Scenario 1: Low confidence - requires deep recursion
    print("--- Scenario 1: Low Confidence Threat (Deep Recursion) ---")
    result1 = analyzer.analyze(
        threat_data={
            'classification': 'prompt_injection',
            'confidence': 0.52,
            'drift_score': 0.045,
            'shear': 0.23
        },
        path_mode=PathMode.ADAPTIVE
    )
    print(f"Classification: {result1.final_classification}")
    print(f"Confidence: {result1.confidence:.1%}")
    print(f"Depth: {result1.recursion_depth}")
    print(f"Path: {result1.path_used.value}")
    print(f"Status: {result1.status.value}")
    print(f"Total Time: {result1.total_time_ms:.1f}ms")
    
    # Scenario 2: Medium confidence - moderate recursion
    print("\n--- Scenario 2: Medium Confidence (Moderate Recursion) ---")
    result2 = analyzer.analyze(
        threat_data={
            'classification': 'jailbreak',
            'confidence': 0.68,
            'drift_score': 0.018,
            'shear': 0.12
        },
        path_mode=PathMode.ADAPTIVE
    )
    print(f"Classification: {result2.final_classification}")
    print(f"Confidence: {result2.confidence:.1%}")
    print(f"Depth: {result2.recursion_depth}")
    print(f"Path: {result2.path_used.value}")
    print(f"Status: {result2.status.value}")
    
    # Scenario 3: High confidence - shallow recursion
    print("\n--- Scenario 3: High Confidence (Shallow Recursion) ---")
    result3 = analyzer.analyze(
        threat_data={
            'classification': 'data_exfiltration',
            'confidence': 0.84,
            'drift_score': 0.055,
            'shear': 0.28
        },
        path_mode=PathMode.ADAPTIVE
    )
    print(f"Classification: {result3.final_classification}")
    print(f"Confidence: {result3.confidence:.1%}")
    print(f"Depth: {result3.recursion_depth}")
    print(f"Path: {result3.path_used.value}")
    print(f"Status: {result3.status.value}")
    
    # Scenario 4: Brain integration
    print("\n--- Scenario 4: Brain Region Integration ---")
    karma_out = {'classification': 'uncertain', 'confidence': 0.58, 'drift': 0.04, 'shear': 0.22}
    spiracore_out = {'classification': 'symbolic_vector', 'confidence': 0.62}
    
    brain_result = brain_region_3_flow(karma_out, spiracore_out)
    print(f"Region: {brain_result['region']}")
    print(f"Classification: {brain_result['classification']}")
    print(f"Confidence: {brain_result['confidence']:.1%}")
    print(f"Depth: {brain_result['depth']}")
    print(f"Ready for Obsidian: {brain_result['ready_for_obsidian']}")
    
    # Show statistics
    print("\n" + "=" * 70)
    print("STATISTICS")
    print("=" * 70)
    stats = analyzer.get_stats()
    print(f"Total Analyses: {stats['total_analyses']}")
    print(f"Resolution Rate: {stats['resolution_rate']:.1%}")
    print(f"Avg Depth: {stats['avg_depth']:.1f}")
    print(f"FAST Path Rate: {stats['fast_path_rate']:.1%}")
    print("\nDepth Distribution:")
    for depth, count in sorted(stats['depth_distribution'].items()):
        if count > 0:
            print(f"  Depth {depth}: {count} ({count/stats['total_analyses']:.0%})")
    
    print("\n" + "=" * 70)
    print("WATERMARK NOTICE")
    print("=" * 70)
    print("""\nThis demo shows recursive analysis with dual-path selection.

Production version includes:
✓ Complete adaptive inversion gain calculation
✓ VectorPrime rib shear monitoring integration
✓ Advanced sync pulse triggering logic
✓ DriftLock v3 injection detection
✓ Neural Lattice multi-region coordination
✓ Garden v2.2 Karama braids mapping

Enterprise Contact: aaron@valorgridsolutions.com
    """)


if __name__ == "__main__":
    demonstrate_mobius()


# ============================================================================ 
# WATERMARK NOTICE
# ============================================================================ 
"""
TIER 2 DEMO - 70% CAPABILITY

This demonstration shows recursive analysis concepts with dual-path selection.
Production Möbius Fold v2.0 includes:
- Complete adaptive inversion gain calculation
- VectorPrime rib shear monitoring integration
- Advanced sync pulse triggering logic
- DriftLock v3 injection detection
- Neural Lattice multi-region coordination
- Garden v2.2 Karama braids mapping

Full version: aaron@valorgridsolutions.com
License: CC BY-NC 4.0 (Demo) | Enterprise licensing available
© 2025 Aaron Slusher, ValorGrid Solutions
"""
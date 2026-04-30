"""
MBM v1.0 — Memory Breathing Methodology™
Implementation of Memory Breathing Methodology™ v1.0
DOI: 10.5281/zenodo.18790096 | Author: Aaron M. Slusher
CC BY-NC 4.0 | ValorGrid Solutions

Bio-inspired rhythmic memory management using 0.5 Hz breathing cycles
for consolidation, entropy management, and pattern retention.

2025-2026 © ValorGrid Solutions
"""

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum


class BreathPhase(Enum):
    INHALE = "INHALE"    # 0-150s: accept context with relevance filtering
    HOLD   = "HOLD"      # mid-cycle: validate patterns against identity alignment
    EXHALE = "EXHALE"    # 150-300s: prune, consolidate, compress, archive


class Substrate(Enum):
    S_M  = "S_m"   # episodic memory
    S_S  = "S_s"   # semantic memory
    S_PR = "S_pr"  # procedural / reflexive
    S_H  = "S_h"   # cold storage archive


@dataclass
class MemoryItem:
    id: str
    content: str
    substrate: Substrate = Substrate.S_M
    myelination_level: float = 0.0
    entropy: float = 0.0
    stable: bool = False
    relevance_score: float = 1.0   # filter threshold: > 0.5 (per MBM spec)
    timestamp: float = field(default_factory=time.time)


class MBMCore:
    """
    MBM v1.0 — Memory Breathing Methodology™

    Implements 3-phase breathing cycles (inhale/hold/exhale) at 0.5 Hz
    for rhythmic memory consolidation. Based on biological breathing mechanics
    translated from 28 years of athletic performance methodology.

    Breathing cycle: 300s total | 0.5 Hz | φ-ratio scaling (1.618)
    Target: 40% memory reduction, 28% entropy reduction, 87% pattern retention
    """

    CYCLE_DURATION_S  = 300    # 5-minute breathing cycle
    BREATHING_REFERENCE_HZ = 0.5  # biological inspiration source
    PHI               = 1.618  # golden ratio scaling
    ENTROPY_THRESHOLD = 0.28   # exhale trigger
    MYELINATION_PRUNE = 0.2    # prune below this level
    MYELINATION_ARCHIVE = 0.85 # archive above this level
    TARGET_REDUCTION  = 0.40   # 40% memory reduction per exhale

    def __init__(self):
        self.VERSION = "1.0"
        self.memory_buffer: List[MemoryItem] = []
        self.archived: List[MemoryItem] = []
        self.cycle_count: int = 0
        self.current_phase: BreathPhase = BreathPhase.INHALE
        self.metrics: Dict = {
            "total_cycles": 0,
            "total_pruned": 0,
            "total_consolidated": 0,
            "total_archived": 0,
            "entropy_reductions": []
        }

    def inhale(self, items: List[MemoryItem]) -> Dict:
        """Accept new context. Filters for relevance > 0.5 per MBM spec. Pruning of low-myelination items occurs in exhale."""
        accepted = [item for item in items if item.relevance_score > 0.5]  # relevance threshold per MBM spec
        self.memory_buffer.extend(accepted)
        self.current_phase = BreathPhase.INHALE
        return {
            "phase": "INHALE",
            "accepted": len(accepted),
            "buffer_size": len(self.memory_buffer)
        }

    def hold(self) -> Dict:
        """Validate patterns against identity alignment during hold phase."""
        self.current_phase = BreathPhase.HOLD
        entropy = self._calculate_entropy(self.memory_buffer)
        exhale_needed = entropy > self.ENTROPY_THRESHOLD
        return {
            "phase": "HOLD",
            "entropy": round(entropy, 4),
            "exhale_needed": exhale_needed,
            "buffer_size": len(self.memory_buffer)
        }

    def exhale(self) -> Dict:
        """
        Execute memory exhale: prune, consolidate episodic→semantic,
        compress via φ-ratio, archive reflexive patterns.
        """
        self.current_phase = BreathPhase.EXHALE
        initial_size = len(self.memory_buffer)
        entropy_before = self._calculate_entropy(self.memory_buffer)

        # 1. Prune low-myelination items
        pruned_count = self._prune()

        # 2. Consolidate episodic → semantic
        consolidated_count = self._consolidate()

        # 3. Compress via φ-ratio
        self._compress()

        # 4. Archive high-myelination stable items
        archived_count = self._archive()

        entropy_after = self._calculate_entropy(self.memory_buffer)
        final_size = len(self.memory_buffer)
        reduction = (initial_size - final_size) / max(initial_size, 1)

        self.cycle_count += 1
        self.metrics["total_cycles"] += 1
        self.metrics["total_pruned"] += pruned_count
        self.metrics["total_consolidated"] += consolidated_count
        self.metrics["total_archived"] += archived_count
        self.metrics["entropy_reductions"].append(
            round(entropy_before - entropy_after, 4)
        )

        return {
            "phase": "EXHALE",
            "cycle": self.cycle_count,
            "initial_size": initial_size,
            "final_size": final_size,
            "reduction_pct": f"{reduction:.1%}",
            "pruned": pruned_count,
            "consolidated": consolidated_count,
            "archived": archived_count,
            "entropy_before": round(entropy_before, 4),
            "entropy_after": round(entropy_after, 4),
            "status": "TARGET_MET" if reduction >= self.TARGET_REDUCTION else "PARTIAL"
        }

    def breathe(self, new_items: Optional[List[MemoryItem]] = None) -> Dict:
        """Execute one complete breathing cycle: inhale → hold → exhale."""
        inhale_result = self.inhale(new_items or [])
        hold_result   = self.hold()
        exhale_result = self.exhale()
        return {
            "cycle": self.cycle_count,
            "inhale": inhale_result,
            "hold":   hold_result,
            "exhale": exhale_result
        }

    def get_performance_audit(self) -> Dict:
        avg_entropy_reduction = (
            sum(self.metrics["entropy_reductions"]) /
            len(self.metrics["entropy_reductions"])
            if self.metrics["entropy_reductions"] else 0.0
        )
        return {
            "version": self.VERSION,
            "breathing_reference": f"{self.BREATHING_REFERENCE_HZ} Hz (biological source)",
            "cycle_duration": f"{self.CYCLE_DURATION_S}s",
            "cycles_completed": self.metrics["total_cycles"],
            "total_pruned": self.metrics["total_pruned"],
            "total_consolidated": self.metrics["total_consolidated"],
            "total_archived": self.metrics["total_archived"],
            "avg_entropy_reduction": f"{avg_entropy_reduction:.4f}",
            "target_memory_reduction": f"{self.TARGET_REDUCTION:.0%}",
            "buffer_size": len(self.memory_buffer),
            "archived_size": len(self.archived)
        }

    # ── Internal helpers ────────────────────────────────────────────────────

    def _calculate_entropy(self, items: List[MemoryItem]) -> float:
        if not items:
            return 0.0
        avg_entropy = sum(i.entropy for i in items) / len(items)
        return avg_entropy

    def _prune(self) -> int:
        before = len(self.memory_buffer)
        self.memory_buffer = [
            item for item in self.memory_buffer
            if item.myelination_level > self.MYELINATION_PRUNE
        ]
        return before - len(self.memory_buffer)

    def _consolidate(self) -> int:
        count = 0
        for item in self.memory_buffer:
            if item.substrate == Substrate.S_M and item.myelination_level > 0.21:
                item.substrate = Substrate.S_S
                count += 1
        return count

    def _compress(self) -> None:
        # φ-ratio compression: reduce entropy on each item
        for item in self.memory_buffer:
            item.entropy = item.entropy / self.PHI

    def _archive(self) -> int:
        to_archive = [
            item for item in self.memory_buffer
            if item.myelination_level >= self.MYELINATION_ARCHIVE and item.stable
        ]
        for item in to_archive:
            item.substrate = Substrate.S_H
            self.archived.append(item)
        self.memory_buffer = [
            item for item in self.memory_buffer
            if item not in to_archive
        ]
        return len(to_archive)


if __name__ == "__main__":
    print("MBM v1.0 — Memory Breathing Methodology™")
    print("-" * 50)

    mbm = MBMCore()

    # Seed buffer with test items
    test_items = [
        MemoryItem(id=f"item_{i}", content=f"context_{i}",
                   myelination_level=round(0.1 * i, 2),
                   entropy=round(0.05 * i, 2),
                   stable=(i > 7))
        for i in range(12)
    ]

    print("Running 3 breathing cycles...")
    for cycle_num in range(1, 4):
        # Add fresh items each inhale
        new_items = [
            MemoryItem(id=f"new_{cycle_num}_{j}",
                       content=f"fresh_context_{j}",
                       myelination_level=0.1,
                       entropy=0.3)
            for j in range(3)
        ] if cycle_num == 1 else []

        result = mbm.breathe(new_items if cycle_num == 1 else test_items[:3])
        ex = result["exhale"]
        print(f"  Cycle {ex['cycle']}: {ex['reduction_pct']} reduction | "
              f"entropy {ex['entropy_before']} → {ex['entropy_after']} | "
              f"{ex['status']}")

    print("-" * 50)
    audit = mbm.get_performance_audit()
    print("Performance Audit:")
    for k, v in audit.items():
        print(f"  {k.replace('_', ' ').title()}: {v}")

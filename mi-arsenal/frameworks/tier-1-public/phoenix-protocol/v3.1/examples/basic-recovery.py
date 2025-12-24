"""
Basic Phoenix Protocol Recovery Example

Demonstrates simple cascade detection and recovery
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.phoenix_base import PhoenixProtocol
from datetime import datetime


def simulate_cascade_scenario():
    """Simulate a typical cascade scenario"""

    print("=" * 70)
    print("PHOENIX PROTOCOL v3.1 - BASIC RECOVERY EXAMPLE")
    print("=" * 70)
    print()

    # Initialize Phoenix Protocol
    phoenix = PhoenixProtocol()

    # Scenario 1: Symbolic Drift Cascade (SDC)
    print("SCENARIO: Symbolic Drift Cascade Detected")
    print("-" * 70)
    print("Symptoms:")
    print("  - Coherence score: 0.68 (below 0.70 threshold)")
    print("  - Memory bloat detected")
    print("  - Response latency increasing")
    print()

    incident = {
        "type": "symbolic_drift_cascade",
        "severity": "high",
        "coherence": 0.68,
        "memory_bloat_factor": 1.85,
        "latency_ms": 450,
        "detection_time": datetime.now(),
    }

    # Execute recovery
    print("Initiating Phoenix Protocol Recovery...")
    print()

    session = phoenix.execute_recovery(incident)

    # Display results
    print()
    print("=" * 70)
    print("RECOVERY SUMMARY")
    print("=" * 70)
    print(f"Session ID: {session.session_id}")
    print(f"Incident Type: {session.incident_type}")
    print(f"Severity: {session.severity}")
    print(
        f"Recovery Status: {'✅ SUCCESS' if session.recovery_successful else '❌ FAILED'}"
    )
    print(
        f"Duration: {session.duration_seconds:.1f}s ({session.duration_seconds/60:.1f} minutes)"
    )
    print(f"Phases Completed: {len(session.phases_completed)}/4")
    print()

    # Show phase breakdown
    print("PHASE BREAKDOWN:")
    print("-" * 70)
    for phase_data in session.phases_completed:
        phase_num = phase_data["phase"]
        phase_name = phase_data["name"].title()
        result = phase_data["result"]
        duration = result.get("duration_minutes", 0)
        print(f"Phase {phase_num}: {phase_name}")
        print(f"  Duration: ~{duration} minutes")

        if phase_num == 1:
            print(f"  Status: {'✅ Contained' if result['contained'] else '❌ Failed'}")
        elif phase_num == 2:
            print(f"  Coherence: {result['identity_coherence']:.2f}")
            print(f"  Damage: {result['damage_percentage']:.1%}")
        elif phase_num == 3:
            print(f"  Recovery Rate: {result['recovery_rate']:.1%}")
        elif phase_num == 4:
            print(f"  Validated: {'✅ Yes' if result['validated'] else '❌ No'}")
        print()

    # Get overall stats
    stats = phoenix.get_recovery_stats()
    print("PHOENIX PROTOCOL STATISTICS:")
    print("-" * 70)
    print(f"Total Recoveries: {stats['total_recoveries']}")
    print(f"Success Rate: {stats['success_rate']:.1%}")
    print(f"Average Duration: {stats['avg_duration_minutes']:.1f} minutes")
    print()


if __name__ == "__main__":
    simulate_cascade_scenario()

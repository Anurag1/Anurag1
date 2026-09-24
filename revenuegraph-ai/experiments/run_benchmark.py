"""Deterministic benchmark harness.

This does not call an LLM. It validates benchmark structure and emits a
machine-readable run manifest so real model runs can be plugged in later.
"""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_problems():
    return json.loads((ROOT / "experiments" / "problems-13.json").read_text())


def build_manifest():
    problems = load_problems()
    return {
        "benchmark": "DISCOVERY-EVAL-001",
        "problem_count": len(problems),
        "problems": [p["problem_id"] for p in problems],
        "systems": ["conventional-baseline", "discovery-oriented"],
        "required_outputs": [
            "hypothesis",
            "evidence_ids",
            "verification_method",
            "verdict",
            "novelty_score",
            "reproducibility_score",
            "latency_ms",
            "estimated_cost",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(build_manifest(), indent=2))

"""Small reproducible benchmark for the evidence-first MVP.

The baseline is intentionally simple: it only counts inputs and emits no
contradiction candidates or follow-up questions. This is a plumbing benchmark,
not a comparison against an LLM or production agent.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from discoveryos.core import analyze_case


def run_benchmark(cases: list[dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for case in cases:
        report = analyze_case(case)
        baseline = {
            "claim_count": len(case.get("claims", [])),
            "candidate_contradiction_count": 0,
            "follow_up_question_count": 0,
        }
        discovery = {
            "claim_count": report["summary"]["claim_count"],
            "candidate_contradiction_count": report["summary"]["candidate_contradiction_count"],
            "follow_up_question_count": len(report["follow_up_questions"]),
        }
        rows.append({
            "case_id": report["case_id"],
            "baseline": baseline,
            "discoveryos": discovery,
            "candidate_contradictions": report["candidate_contradictions"],
            "limitations": report["limitations"],
        })
    return {
        "benchmark": "DiscoveryOS plumbing benchmark v0",
        "interpretation": "Compares the prototype heuristic with a deliberately minimal no-analysis baseline; not an LLM head-to-head.",
        "case_count": len(rows),
        "aggregate": {
            "baseline_candidate_contradictions": sum(row["baseline"]["candidate_contradiction_count"] for row in rows),
            "discoveryos_candidate_contradictions": sum(row["discoveryos"]["candidate_contradiction_count"] for row in rows),
            "baseline_follow_up_questions": sum(row["baseline"]["follow_up_question_count"] for row in rows),
            "discoveryos_follow_up_questions": sum(row["discoveryos"]["follow_up_question_count"] for row in rows),
        },
        "cases": rows,
    }


def run_files(input_path: str | Path, output_path: str | Path) -> dict[str, Any]:
    raw = json.loads(Path(input_path).read_text(encoding="utf-8"))
    cases = raw if isinstance(raw, list) else [raw]
    result = run_benchmark(cases)
    Path(output_path).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result

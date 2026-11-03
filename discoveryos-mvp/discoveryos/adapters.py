"""Adapters for connecting existing research modules to the DiscoveryOS evidence ledger.

Adapters accept JSON-compatible outputs instead of importing unrelated project
internals. This keeps the integration reproducible and avoids pretending that
heterogeneous repositories are one installable Python package.
"""
from __future__ import annotations

from pathlib import Path
import json
from typing import Any


COMPONENT_REGISTRY = {
    "HONet": {
        "role": "continual_learning",
        "repository_path": "HONet-Lifelong-Learning",
        "integration_contract": "Expose task sequence, per-task metrics, and checkpoint metadata as JSON.",
    },
    "Meta-Attention": {
        "role": "meta_reasoning",
        "repository_path": "Generalised-Meta-Attention-Architecture",
        "integration_contract": "Expose critique, confidence, assumptions, and rule candidates as structured JSON.",
    },
    "SUPHAI_MODEL": {
        "role": "multi_agent_orchestration",
        "repository_path": "SUPHAI_MODEL",
        "integration_contract": "Expose agent task, status, output, and evidence references as structured JSON.",
    },
    "Prometheus-AGI": {
        "role": "state_and_hypothesis_loop",
        "repository_path": "Prometheus-AGI",
        "integration_contract": "Expose prior state, observed changes, hypotheses, and persisted result as structured JSON.",
    },
}


def load_json(path: str | Path) -> dict[str, Any]:
    """Load a JSON object from a local component-export file."""
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Component export must be a JSON object")
    return value


def component_export_to_claims(component: str, payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize an explicit component export into source-attributed claims.

    Expected payload shape:
      {"component": "...", "records": [{"id": "...", "text": "...",
       "source": "...", "confidence": 0.8, "tags": ["..."]}]}

    The adapter does not execute the component or infer that a repository is
    operational. It only normalizes records that the component actually emits.
    """
    if component not in COMPONENT_REGISTRY:
        raise ValueError(f"Unknown component: {component}")
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("'records' must be a list")
    claims: list[dict[str, Any]] = []
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Record {index} must be an object")
        text = str(record.get("text", "")).strip()
        source = str(record.get("source", "")).strip()
        if not text or not source:
            raise ValueError(f"Record {index} requires non-empty text and source")
        claims.append({
            "id": f"{component}:{record.get('id', index)}",
            "text": text,
            "source": source,
            "confidence": float(record.get("confidence", 0.5)),
            "tags": [component.lower(), *[str(tag) for tag in record.get("tags", [])]],
        })
    return claims


def build_component_manifest() -> dict[str, Any]:
    """Return the stable component registry and explicit integration contracts."""
    return {
        "schema_version": "0.1",
        "status": "adapter_contracts_defined_not_all_runtime_connected",
        "components": COMPONENT_REGISTRY,
    }

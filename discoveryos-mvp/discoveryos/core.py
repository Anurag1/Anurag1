"""Small, deterministic evidence-first discovery loop.

This module uses transparent heuristics so results are inspectable. It does not
claim semantic understanding or verified scientific discovery.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Any


NEGATIONS = {"not", "never", "no", "cannot", "can't", "fails", "false", "without"}
STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "to", "of", "in", "on", "for", "and", "or", "with", "by", "as", "it",
    "this", "that", "these", "those", "from", "at", "can", "could", "may",
    "might", "will", "would", "should", "not", "never", "no", "cannot",
    "can't", "fails", "false", "true", "does", "do", "did", "has", "have",
    "had", "into", "than", "then", "when", "what", "which", "who",
}


@dataclass(frozen=True)
class Claim:
    id: str
    text: str
    source: str
    confidence: float = 0.5
    tags: tuple[str, ...] = ()


def _tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower())
        if token not in STOPWORDS and len(token) > 2
    }


def _is_negated(text: str) -> bool:
    tokens = set(re.findall(r"[a-z']+", text.lower()))
    return bool(tokens & NEGATIONS)


def _normalise_claim(raw: dict[str, Any]) -> Claim:
    required = ("id", "text", "source")
    missing = [key for key in required if not raw.get(key)]
    if missing:
        raise ValueError(f"Claim missing required field(s): {', '.join(missing)}")
    confidence = float(raw.get("confidence", 0.5))
    if not 0 <= confidence <= 1:
        raise ValueError(f"Claim {raw['id']!r} confidence must be between 0 and 1")
    tags = tuple(str(tag) for tag in raw.get("tags", []))
    return Claim(str(raw["id"]), str(raw["text"]), str(raw["source"]), confidence, tags)


def analyze_case(payload: dict[str, Any]) -> dict[str, Any]:
    """Analyze a JSON-compatible case and return a deterministic report."""
    raw_claims = payload.get("claims", [])
    if not isinstance(raw_claims, list):
        raise ValueError("'claims' must be a list")
    claims = [_normalise_claim(item) for item in raw_claims]
    ids = [claim.id for claim in claims]
    if len(ids) != len(set(ids)):
        raise ValueError("Claim IDs must be unique")

    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, str]] = []
    for claim in claims:
        nodes[f"claim:{claim.id}"] = {
            "type": "claim", "text": claim.text, "source": claim.source,
            "confidence": claim.confidence,
        }
        for concept in sorted(_tokens(claim.text) | set(claim.tags)):
            nodes.setdefault(f"concept:{concept}", {"type": "concept", "label": concept})
            edges.append({"from": f"claim:{claim.id}", "to": f"concept:{concept}", "type": "mentions"})

    contradictions: list[dict[str, Any]] = []
    for index, left in enumerate(claims):
        for right in claims[index + 1:]:
            shared = sorted(_tokens(left.text) & _tokens(right.text))
            if len(shared) >= 2 and _is_negated(left.text) != _is_negated(right.text):
                item = {
                    "claim_ids": [left.id, right.id],
                    "shared_terms": shared,
                    "status": "candidate_requires_review",
                    "reason": "Claims share key terms but differ in explicit negation markers.",
                }
                contradictions.append(item)
                edges.append({"from": f"claim:{left.id}", "to": f"claim:{right.id}", "type": "candidate_contradiction"})

    referenced_terms = set().union(*(_tokens(claim.text) for claim in claims)) if claims else set()
    questions: list[str] = []
    if not claims:
        questions.append("What is the research question, and what observations or sources support it?")
    for contradiction in contradictions:
        a, b = contradiction["claim_ids"]
        questions.append(f"What evidence would distinguish claim {a} from claim {b}?")
    for term in sorted(referenced_terms):
        sources = {claim.source for claim in claims if term in _tokens(claim.text)}
        if len(sources) == 1:
            questions.append(f"Can the claim involving '{term}' be independently checked with a second source?")
            if len(questions) >= 8:
                break

    low_support = [
        {"claim_id": claim.id, "text": claim.text, "source": claim.source,
         "confidence": claim.confidence,
         "next_step": "Seek independent corroboration or record a disconfirming test."}
        for claim in claims if claim.confidence < 0.6
    ]
    hypotheses = [
        {
            "id": f"H{index + 1}",
            "statement": f"If claims {', '.join(item['claim_ids'])} describe the same conditions, at least one may be incomplete or context-dependent.",
            "test": "Define the terms, hold conditions constant, and compare both claims against independently sourced observations.",
            "status": "untested",
        }
        for index, item in enumerate(contradictions)
    ]

    return {
        "schema_version": "0.1",
        "case_id": str(payload.get("case_id", "unnamed-case")),
        "summary": {
            "claim_count": len(claims),
            "source_count": len({claim.source for claim in claims}),
            "graph_node_count": len(nodes),
            "graph_edge_count": len(edges),
            "candidate_contradiction_count": len(contradictions),
            "low_confidence_claim_count": len(low_support),
        },
        "claims": [asdict(claim) for claim in claims],
        "graph": {"nodes": nodes, "edges": edges},
        "candidate_contradictions": contradictions,
        "follow_up_questions": list(dict.fromkeys(questions)),
        "hypotheses_to_test": hypotheses,
        "low_support_claims": low_support,
        "limitations": [
            "Contradictions are lexical candidates and require human review.",
            "Confidence is user-supplied, not calibrated by this prototype.",
            "Hypotheses and questions are suggestions, not verified discoveries.",
        ],
    }

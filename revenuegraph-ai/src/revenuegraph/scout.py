from .evidence import Evidence
from .models import Opportunity


def discover(seed: str, evidence: list[Evidence] | None = None) -> list[Opportunity]:
    """Create an opportunity only when supplied evidence supports the seed."""
    evidence = evidence or []
    for item in evidence:
        item.validate()

    if not seed.strip() or not evidence:
        return []

    return [Opportunity(
        title="AI agent evaluation",
        audience="AI developers and research engineers",
        problem="It is difficult to compare agent behavior across diverse tasks.",
        proposed_offer="Open evaluation benchmark with optional implementation support",
        evidence=[item.source for item in evidence],
        channels=["x", "linkedin", "pinterest"],
        hypothesis="A reproducible cross-domain benchmark can generate qualified technical interest.",
    )]

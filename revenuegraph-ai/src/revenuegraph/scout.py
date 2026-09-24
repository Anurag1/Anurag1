from .models import Opportunity

def discover(seed: str) -> list[Opportunity]:
    """Return deterministic MVP opportunities from a research seed.

    Production Scout will replace this with evidence-backed retrieval.
    """
    return [Opportunity(
        title="AI agent evaluation",
        audience="AI developers and research engineers",
        problem="It is difficult to compare agent behavior across diverse tasks.",
        proposed_offer="Open evaluation benchmark with optional implementation support",
        channels=["x", "linkedin", "pinterest"],
        hypothesis="A reproducible cross-domain benchmark can generate qualified technical interest.",
    )]

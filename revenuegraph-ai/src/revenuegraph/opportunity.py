from .models import Opportunity
from .evidence import Evidence


def score(opportunity: Opportunity, evidence: list[Evidence]) -> float:
    if not evidence:
        return 0.0
    for item in evidence:
        item.validate()
    evidence_quality = sum(x.confidence for x in evidence) / len(evidence)
    monetization_fit = 1.0 if opportunity.proposed_offer.strip() else 0.0
    audience_fit = 1.0 if opportunity.audience.strip() else 0.0
    return round((0.5 * evidence_quality) + (0.3 * monetization_fit) + (0.2 * audience_fit), 4)

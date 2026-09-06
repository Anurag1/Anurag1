from dataclasses import dataclass
from typing import List


@dataclass
class Opportunity:
    topic: str
    demand: float
    commission: float
    competition: float
    content_effort: float
    trust: float = 1.0

    def score(self) -> float:
        """Score an opportunity; higher is better."""
        return round(
            (self.demand * self.commission * self.trust)
            / max(self.competition * self.content_effort, 0.01),
            4,
        )


def rank(opportunities: List[Opportunity]) -> List[Opportunity]:
    return sorted(opportunities, key=Opportunity.score, reverse=True)


def expected_revenue(
    impressions: float,
    ctr: float,
    conversion_rate: float,
    commission: float,
) -> float:
    """Estimate revenue from a traffic/conversion hypothesis."""
    if min(impressions, ctr, conversion_rate, commission) < 0:
        raise ValueError("Inputs must be non-negative")
    return impressions * ctr * conversion_rate * commission


def has_clear_disclosure(text: str) -> bool:
    """Basic pre-publication guard for affiliate disclosures."""
    text = text.lower()
    markers = (
        "affiliate",
        "commission",
        "paid link",
        "sponsored",
        "advertisement",
    )
    return any(marker in text for marker in markers)

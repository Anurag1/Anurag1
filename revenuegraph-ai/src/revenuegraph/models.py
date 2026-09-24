from dataclasses import dataclass, field
from typing import List

@dataclass
class Opportunity:
    title: str
    audience: str
    problem: str
    proposed_offer: str
    evidence: List[str] = field(default_factory=list)
    channels: List[str] = field(default_factory=list)
    hypothesis: str = ""
    status: str = "draft"

@dataclass
class Content:
    opportunity_id: str
    platform: str
    text: str
    cta: str
    tracking_url: str
    publication_status: str = "draft"

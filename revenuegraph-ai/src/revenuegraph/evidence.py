from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    source: str
    claim: str
    confidence: float

    def validate(self) -> None:
        if not self.source.strip():
            raise ValueError("source is required")
        if not self.claim.strip():
            raise ValueError("claim is required")
        if not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")


def rank(evidence: list[Evidence]) -> list[Evidence]:
    for item in evidence:
        item.validate()
    return sorted(evidence, key=lambda item: item.confidence, reverse=True)

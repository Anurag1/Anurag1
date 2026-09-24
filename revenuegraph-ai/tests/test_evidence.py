from revenuegraph.evidence import Evidence, rank
from revenuegraph.models import Opportunity
from revenuegraph.opportunity import score


def test_evidence_ranking_and_score():
    evidence = [Evidence("source-a", "claim-a", 0.6), Evidence("source-b", "claim-b", 0.9)]
    assert rank(evidence)[0].source == "source-b"
    opportunity = Opportunity(
        title="t", audience="a", problem="p", proposed_offer="o", evidence=[], channels=["x"], hypothesis="h"
    )
    assert score(opportunity, evidence) > 0.5

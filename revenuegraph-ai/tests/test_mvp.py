from revenuegraph.analytics import Event, summarize
from revenuegraph.content import generate
from revenuegraph.evidence import Evidence
from revenuegraph.scout import discover


def test_discovery_requires_evidence():
    assert discover("benchmark") == []


def test_discovery_content_and_analytics():
    evidence = [Evidence("source-1", "Agents need reproducible evaluation.", 0.9)]
    opportunity = discover("benchmark", evidence)[0]
    content = generate(opportunity, "x", "https://example.invalid/benchmark")
    assert content.platform == "x"
    assert "utm_source=x" in content.tracking_url
    result = summarize([
        Event("x", "impression"),
        Event("x", "click"),
        Event("x", "lead"),
        Event("x", "purchase", 25),
    ])
    assert result["ctr"] == 1.0
    assert result["lead_rate"] == 1.0
    assert result["revenue"] == 25

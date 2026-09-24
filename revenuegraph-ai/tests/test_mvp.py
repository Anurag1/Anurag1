from revenuegraph.analytics import Event, summarize
from revenuegraph.scout import discover
from revenuegraph.content import generate

def test_discovery_content_and_analytics():
    opportunity = discover("benchmark")[0]
    content = generate(opportunity, "x", "https://example.invalid/benchmark")
    assert content.platform == "x"
    assert "utm_source=x" in content.tracking_url
    result = summarize([Event("x", "impression"), Event("x", "click"), Event("x", "lead"), Event("x", "purchase", 25)])
    assert result["ctr"] == 1.0
    assert result["lead_rate"] == 1.0
    assert result["revenue"] == 25

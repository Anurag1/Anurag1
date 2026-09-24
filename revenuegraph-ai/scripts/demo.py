from revenuegraph.scout import discover
from revenuegraph.content import generate
from revenuegraph.analytics import Event, summarize

opportunity = discover("AI discovery benchmark")[0]
print("OPPORTUNITY:", opportunity.title)
for platform in opportunity.channels:
    content = generate(opportunity, platform, "https://example.invalid/benchmark")
    print(f"\\n[{platform}]\\n{content.text}")

events = [
    Event("x", "impression"), Event("x", "impression"), Event("x", "click"),
    Event("x", "lead"), Event("x", "purchase", 100.0),
]
print("\\nDEMO ANALYTICS:", summarize(events))

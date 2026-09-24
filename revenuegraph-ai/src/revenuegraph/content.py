from .models import Content, Opportunity

def generate(opportunity: Opportunity, platform: str, base_url: str) -> Content:
    tracking_url = f"{base_url}?utm_source={platform}&utm_campaign=discovery-benchmark"
    if platform == "x":
        text = (f"What if AI evaluation tested discovery, not just answers? "
                f"We are testing a reproducible benchmark across 13 cross-domain problems. "
                f"The goal is evidence, not hype. {tracking_url}")
    elif platform == "linkedin":
        text = (f"AI agents are often evaluated on task success, but cross-domain discovery raises a different question: "
                f"can a system find useful relationships that were not explicitly requested? "
                f"We are testing this with 13 reproducible problems. {tracking_url}")
    else:
        text = ("13 cross-domain AI discovery problems. Compare conventional reasoning with a graph/contradiction approach. "
                f"Run the experiment: {tracking_url}")
    return Content(opportunity_id=opportunity.title, platform=platform, text=text,
                   cta="Run the benchmark", tracking_url=tracking_url)

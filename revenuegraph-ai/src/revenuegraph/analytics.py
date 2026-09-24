from dataclasses import dataclass
from typing import Iterable

@dataclass
class Event:
    source: str
    event_type: str
    value: float = 0.0

def summarize(events: Iterable[Event]) -> dict:
    totals = {"impression": 0, "click": 0, "lead": 0, "purchase": 0, "revenue": 0.0}
    for event in events:
        if event.event_type in totals and event.event_type != "purchase":
            totals[event.event_type] += 1
        elif event.event_type == "purchase":
            totals["purchase"] += 1
            totals["revenue"] += event.value
    totals["ctr"] = totals["click"] / totals["impression"] if totals["impression"] else 0.0
    totals["lead_rate"] = totals["lead"] / totals["click"] if totals["click"] else 0.0
    return totals

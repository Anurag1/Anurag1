from __future__ import annotations
import argparse
import json
from pathlib import Path
from .engine import KircherDiscoveryAgent

def main() -> None:
    parser = argparse.ArgumentParser(description="Run Kircher Discovery Agent on structured claims.")
    parser.add_argument("--data", required=True, help="Path to JSON file containing a claims array")
    parser.add_argument("--limit", type=int, default=10, help="Maximum cross-domain candidates")
    parser.add_argument("--output", default="-", help="Output JSON path, or - for stdout")
    args = parser.parse_args()
    agent = KircherDiscoveryAgent.from_json(args.data)
    report = json.dumps(agent.report(limit=args.limit), indent=2, ensure_ascii=False)
    if args.output == "-":
        print(report)
    else:
        Path(args.output).write_text(report + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()

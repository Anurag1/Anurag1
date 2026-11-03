"""Command-line interface for the DiscoveryOS MVP."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from discoveryos.core import analyze_case


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the deterministic DiscoveryOS evidence-first analysis.")
    parser.add_argument("input", help="Path to a case JSON file")
    parser.add_argument("--out", help="Write JSON report to this path; otherwise print to stdout")
    args = parser.parse_args()
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = analyze_case(payload)
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        Path(args.out).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()

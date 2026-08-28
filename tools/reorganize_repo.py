#!/usr/bin/env python3
"""Generate a local monorepo import plan from modules/manifest.yaml.

This script deliberately does not delete, rename, or rewrite source repositories.
It is intended to be run locally where Git is available so repository histories can
be preserved with git subtree/git filter-repo as appropriate.
"""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("Install PyYAML first: python -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "modules" / "manifest.yaml"


def main() -> int:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    print(f"Monorepo: {data['name']}")
    print(f"Strategy: {data['strategy']}")
    print(f"First-party modules: {len(data.get('modules', []))}")
    print(f"Excluded upstream mirrors: {len(data.get('excluded_upstream_mirrors', []))}")
    print()
    for item in data.get("modules", []):
        print(f"{item['source']} -> {item['path']} [{item['role']}]")
    print("\nNo remote repositories were modified by this planner.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

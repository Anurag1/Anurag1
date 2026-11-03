"""CLI entry point for the DiscoveryOS plumbing benchmark."""
import argparse

from discoveryos.benchmark import run_files


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the DiscoveryOS prototype plumbing benchmark.")
    parser.add_argument("input", help="JSON case object or array of cases")
    parser.add_argument("--out", default="benchmark-report.json", help="Output JSON report")
    args = parser.parse_args()
    result = run_files(args.input, args.out)
    print(f"cases={result['case_count']} report={args.out}")


if __name__ == "__main__":
    main()

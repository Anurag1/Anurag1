# DiscoveryOS MVP — Evidence-first discovery loop

A small, runnable Python prototype of the DiscoveryOS idea. It is intentionally an **MVP**, not a claim of general intelligence or superiority over modern models.

## What works today

- Records claims with source, confidence, and tags.
- Builds a lightweight concept/evidence graph (standard library only).
- Flags *candidate* contradictions using explicit polarity markers and shared concepts.
- Generates follow-up questions for unsupported or conflicting claims.
- Produces a deterministic JSON report that can be inspected and benchmarked.
- Runs unit tests in GitHub Actions.

## Quick start

Requires Python 3.11+; no third-party dependencies.

```bash
cd discoveryos-mvp
python -m unittest discover -s tests -v
python -m discoveryos examples/sample_case.json --out report.json
```

## Input format

See `examples/sample_case.json`. Each claim has `id`, `text`, `source`, optional `confidence` (0–1), and optional `tags`.

## Architecture

```text
Claims + sources
      ↓
Evidence ledger → concept graph
      ↓                 ↓
support checks → candidate contradiction checks
      ↓                 ↓
follow-up questions + hypotheses to test
      ↓
reproducible JSON report
```

## Important limitations

- Contradiction detection is a transparent lexical heuristic, not semantic entailment.
- Generated hypotheses/questions are prompts for human review, not verified findings.
- No LLM API, web crawler, or external tool execution is included.
- The included example is a smoke-test fixture, not scientific evidence.
- This repository does not prove DiscoveryOS outperforms a baseline. That requires a controlled, reproducible head-to-head evaluation on identical tasks and budgets.

## Next milestone

Add a benchmark adapter for single-agent and multi-agent baselines, a labelled evaluation set, and metrics for evidence attribution, contradiction precision/recall, task success, latency, and cost.

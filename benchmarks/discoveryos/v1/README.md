# DiscoveryOS Evidence Benchmark v1

A reproducible head-to-head benchmark for testing whether the DiscoveryOS workflow adds measurable value beyond a conventional linear LLM workflow.

## Design

All systems receive the same task fixtures and evidence. The benchmark records task success, evidence attribution, contradiction detection, hypothesis quality, reproducibility, latency, and cost when available.

Systems:

1. `linear` — single-pass baseline.
2. `multi_agent` — independent specialist passes followed by synthesis.
3. `discoveryos` — observation → graph/memory → meta-reasoning → questions/contradictions → hypotheses → evaluation → knowledge update.

This repository version intentionally contains a deterministic harness and task fixtures first. Model adapters can be added without changing the evaluator.

## Pass criteria

DiscoveryOS must beat the strongest baseline on the aggregate score without sacrificing reproducibility, and any claimed advantage must be visible in per-task metrics. No architectural component earns points merely for existing.

## Reproducibility

Run:

```bash
python benchmarks/discoveryos/v1/run_benchmark.py
```

The command writes `results.json` and prints a comparison table. GitHub Actions stores the result as a workflow artifact.

GitHub Actions supports manually triggered workflows and persisted artifacts for test outputs. See the official GitHub Actions documentation.

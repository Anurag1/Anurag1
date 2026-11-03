# DiscoveryOS MVP — Evidence-first discovery loop

A small, runnable Python prototype of the DiscoveryOS idea. It is intentionally an **MVP**, not a claim of general intelligence or superiority over modern models.

## Current capabilities

- Records claims with source, confidence, and tags.
- Builds a lightweight concept/evidence graph (standard library only).
- Flags *candidate* contradictions using explicit polarity markers and shared concepts.
- Generates follow-up questions for unsupported or conflicting claims.
- Normalizes explicit JSON exports from research components through adapter contracts.
- Produces deterministic JSON analysis and benchmark reports.
- Includes unit tests and a GitHub Actions workflow.

## Quick start

Requires Python 3.11+; no third-party dependencies.

```bash
cd discoveryos-mvp
python -m unittest discover -s tests -v
python -m discoveryos.cli examples/sample_case.json --out report.json
python -m discoveryos.benchmark_cli examples/benchmark_cases.json --out benchmark-report.json
```

## Architecture

```text
HONet / Meta-Attention / SUPHAI / Prometheus
         ↓ component-owned JSON exports
     Adapter contracts + provenance
         ↓
Evidence ledger → concept graph
         ↓                 ↓
support checks → candidate contradiction checks
         ↓                 ↓
follow-up questions + hypotheses to test
         ↓
reproducible JSON reports + benchmark output
```

## Benchmark scope

The included baseline is deliberately minimal and only measures pipeline behavior. It is useful for smoke testing, not evidence of superiority over an LLM or multi-agent system. A fair model comparison needs the same labelled tasks, inputs, tools, and budgets for every baseline.

## Important limitations

- Contradiction detection is a transparent lexical heuristic, not semantic entailment.
- Generated hypotheses/questions are prompts for human review, not verified findings.
- The adapter registry defines integration contracts; it does not itself execute HONet, Meta-Attention, SUPHAI, or Prometheus.
- No LLM API, web crawler, or external tool execution is included.
- The included cases are smoke-test fixtures, not scientific evidence.

See [INTEGRATION_STATUS.md](INTEGRATION_STATUS.md) for component-by-component integration status.

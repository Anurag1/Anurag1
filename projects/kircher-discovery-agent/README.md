# Kircher Discovery Agent (KDA)

An experimental, dependency-free Python prototype inspired by Athanasius Kircher's attempts to organize and combine knowledge across disciplines. KDA represents claims as a provenance-aware graph, proposes cross-domain connections, flags possible contradictions, and emits hypotheses with predictions and falsification tests.

> **Research prototype, not an autonomous scientist.** Its rules produce candidates, not validated discoveries. Demo data is synthetic/illustrative and must not be cited as scientific evidence.

## Kircher-to-computation mapping

- Combinatorial knowledge → cross-domain candidate generation from shared entities or relations.
- Symbolic systems → subject–predicate–object claims.
- Visual inquiry → machine-readable knowledge graph.
- Natural-philosophical speculation → candidate hypotheses with predictions and falsification tests.

This is a modern interpretation, not a claim that Kircher invented modern graph AI or that his historical theories were scientifically correct.

## Local Python prototype

Python 3.10+, no third-party dependencies.

```bash
python -m unittest discover -s tests -v
python -m kda.cli --data examples/demo_claims.json --limit 10 --output report.json
```

The current Python project files are available as a ZIP release generated in this conversation; this repository directory documents the project and current release status.

## Public app deployment

- App URL: https://kircher-discovery-agent.lovable.app
- Builder: https://lovable.dev/projects/7efe1bec-4509-47f1-a4ae-421d48610c2a

**Release caveat (2026-10-26):** the hosting platform reported this application as published, but a follow-up source inspection found `src/routes/index.tsx` was still the default blank-page placeholder. The builder workspace subsequently reported it had run out of credits, which blocked the UI repair. Do not treat this URL as a functionally verified release until the homepage is fixed and smoke-tested.

The app code contains a server-only OpenAI adapter and structured analysis functions. Configure `OPENAI_API_KEY` as a server secret and optional `OPENAI_MODEL` (default `gpt-4.1-mini`) in the builder's project settings. No secret should be exposed in browser code or committed to Git. A real model request has not been verified yet.

## Current limitations

- The Python engine uses heuristic symbolic matching, not semantic understanding.
- No web retrieval, vector database, or automatic citation verification in the Python CLI.
- Contradiction detection compares claims with the same subject/predicate and differing values; condition matching is exact string matching.
- No claims of novelty, accuracy advantage, or scientific discovery until benchmarked.

## Validation results

The local Python prototype's automated tests were run on 2026-10-26: 5 tests passed. These tests cover graph structure, candidate generation constraints, duplicate-claim rejection, condition-aware contradiction caution, and invalid limit handling. They do not test the public web app or live model.

## License

MIT.
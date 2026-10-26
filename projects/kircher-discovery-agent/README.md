# Kircher Discovery Agent (KDA)

An experimental, dependency-free Python prototype inspired by Athanasius Kircher's attempts to organize and combine knowledge across disciplines. KDA represents claims as a provenance-aware graph, proposes cross-domain connections, flags possible contradictions, and emits hypotheses with predictions and falsification tests.

> **Research prototype, not an autonomous scientist.** The current rules produce candidates, not validated discoveries. Demo data is synthetic and must not be treated as scientific evidence.

## Kircher-to-computation mapping

- Combinatorial knowledge → cross-domain candidate generation from shared entities or relations.
- Symbolic systems → subject–predicate–object claims.
- Visual inquiry → machine-readable knowledge graph.
- Natural-philosophical speculation → hypotheses with predictions and falsification tests.

This is a modern interpretation, not a claim that Kircher invented modern graph AI or that his historical theories were scientifically correct.

## Local Python prototype

Python 3.10+, no third-party dependencies.

```bash
python -m unittest discover -s tests -v
python -m kda.cli --data examples/demo_claims.json --limit 10 --output report.json
```

The local prototype source is included in this repository directory. A ZIP snapshot can also be downloaded from the conversation where this project was built.

## Web app deployment

- Intended public URL: https://kircher-discovery-agent.lovable.app
- Builder/editor: https://lovable.dev/projects/7efe1bec-4509-47f1-a4ae-421d48610c2a

**Release caveat (2026-10-26):** the hosting platform reported this application as published, but a source inspection found `src/routes/index.tsx` was still the default blank-page placeholder. The builder workspace subsequently reported it had run out of credits, which blocked the UI repair through that service. Therefore, the URL is a deployment endpoint, not a verified functional release.

The builder project has a server-side OpenAI adapter and structured-analysis functions, but a working public UI has not been confirmed. Add `OPENAI_API_KEY` via server-side project secrets; optionally set `OPENAI_MODEL` (default `gpt-4.1-mini`). Never commit the API key. A successful live model call has not been verified.

## Validation

The local Python prototype was tested on 2026-10-26: **5 tests passed**. Coverage includes graph structure, constrained cross-domain candidate generation, duplicate claim rejection, cautious handling of claims with differing conditions, and invalid candidate limits. The CLI smoke run processed 6 illustrative claims and generated 2 cross-domain candidates and 3 potential-conflict flags. These checks do not test the hosted web app or live language-model integration.

## Current limitations

- Heuristic symbolic matching, not semantic understanding.
- No web retrieval, vector database, or automatic citation verification in the Python CLI.
- Contradiction detection compares claims with the same subject and predicate but differing values; conditions use exact string matching.
- No claims of novelty, accuracy advantage, or scientific discovery until benchmarked.

## Next steps

1. Restore builder credits or use a local clone to replace the blank homepage.
2. Run build, lint and automated tests for the web app.
3. Add the OpenAI secret and successfully execute the real-model test.
4. Publish again and verify the public URL.
5. Sync the complete app source to a dedicated GitHub repository such as `Anurag1/kircher-discovery-agent`.

## License

MIT.
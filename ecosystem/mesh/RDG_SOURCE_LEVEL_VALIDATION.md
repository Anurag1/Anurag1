# RDG Source-Level Validation v0.2

## Objective

Upgrade the Repository Discovery Graph from name-based semantic matching to evidence-based repository composition.

GitHub's own dependency graph is useful for declared package dependencies, but RDG targets a broader question: **can two repositories compose into a useful system even when neither declares the other as a dependency?** GitHub documents that its dependency graph is built from manifests/lockfiles and dependency submissions. citeturn0search1turn0search4

## Validation pipeline

```text
portfolio inventory
    ↓
repository metadata + README/code evidence
    ↓
capability extraction
    ↓
semantic candidate edge
    ↓
interface evidence
    ↓
compatibility check
    ↓
minimal adapter/test
    ↓
benchmark
    ↓
validated edge
```

## Evidence classes

| Evidence | Meaning | Weight |
|---|---|---:|
| repository-name overlap | weak semantic signal | 1 |
| README capability match | documented capability overlap | 2 |
| shared language/runtime | implementation compatibility signal | 2 |
| import/API overlap | concrete integration signal | 4 |
| shared data/interface schema | concrete composition signal | 4 |
| existing test passes across adapter | executable evidence | 6 |
| benchmark improvement | outcome evidence | 8 |

A high score is **not** sufficient by itself. An edge becomes `validated` only after an executable test passes and the result is reproducible.

## First validation targets

### A. Geometric Engine → Discovery

Evidence: GEI explicitly describes a graph representation, unexplored-edge selection, and the loop `map → question → contradiction → explore → simulate → discover`. fileciteturn24file0L2-L6

Test hypothesis: expose a machine-readable candidate-edge interface and verify deterministic candidate selection on a fixed fixture.

### B. SUPHAI → Agent execution

Evidence: SUPHAI documents a coordination layer, priority engine, execution layer, and feedback loop for distributing tasks across agents. fileciteturn25file0L2-L6

Test hypothesis: define a minimal task envelope (`task`, `priority`, `capabilities`, `result`, `feedback`) and verify routing plus feedback on a synthetic fixture.

### C. ReasonSynth / Discovery engine → Evaluation

The portfolio registry already categorizes ReasonSynth and Universal-Discovery-Engine as reasoning/discovery capabilities. fileciteturn22file1L14-L24

Test hypothesis: convert a generated discovery candidate into a structured evaluation case and reject malformed or unsupported candidates.

## False-positive controls

RDG must explicitly reject an edge when:

1. only repository names match;
2. claimed APIs are absent;
3. interfaces cannot be adapted without speculative behavior;
4. licensing/provenance is unresolved;
5. an integration test fails;
6. benchmark results do not improve over the baseline.

## Success criteria

A source-level RDG release is successful when it reports:

- candidate edges;
- evidence supporting each edge;
- rejected edges and reasons;
- executable integration tests;
- baseline versus composed-system metrics;
- reproducible commit references.

## Important distinction

GitHub code navigation can expose definitions and references within and across repositories, while the dependency graph captures declared dependencies. RDG is intended to sit above both as a **composition-discovery layer**, not as a replacement for either. citeturn0search11turn0search1

# Repository Discovery Graph — Full Portfolio Test

## What was tested

The current GitHub owner inventory returned **100 repositories**. RDG was extended to include the full accessible inventory rather than only the earlier 46-node semantic seed.

This test is intentionally conservative: repository names are treated as **weak semantic signals**, not as proof of code compatibility or dependency. A real integration must inspect files, APIs, dependencies, tests, provenance and licenses.

## Test pipeline

```text
100 repository inventory
        ↓
name-level capability extraction
        ↓
semantic candidate-edge generation
        ↓
capability coverage check
        ↓
architecture-seed validation
        ↓
ranked candidate connections
```

## Live test result

The local deterministic harness `rdg_portfolio_demo.py` completed with exit code **0**.

```text
nodes=100
capability_counts={'discovery': 1, 'graph': 5, 'validation': 5, 'evaluation': 2}
architecture_seed=ReasonSynth -> Geometric-Engine-Intelligence- -> truthai-universal -> evals
inventory_missing_from_seed=[]
```

The selected seed therefore exists entirely inside the current 100-repository snapshot.

## Top semantic candidates discovered

The strongest name-level overlaps were:

1. `yacy_search_server ↔ findutils` — infrastructure + retrieval + search
2. `opensearch-dashboards ↔ yacy_search_server` — retrieval + search
3. `opensearch-dashboards ↔ open-source-search-engine` — retrieval + search
4. `opensearch-dashboards ↔ findutils` — retrieval + search
5. `opensearch ↔ yacy_search_server` — retrieval + search
6. `opensearch ↔ opensearch-dashboards` — retrieval + search
7. `opensearch ↔ open-source-search-engine` — retrieval + search
8. `opensearch ↔ findutils` — retrieval + search
9. `open-source-search-engine ↔ yacy_search_server` — retrieval + search
10. `open-source-search-engine ↔ findutils` — retrieval + search

## Behavioral showcase

For an AI-discovery task, the system can now distinguish two levels:

### Level A — semantic candidate

```text
Repository A
   ↓
shared capability
   ↓
Repository B
   ↓
candidate edge
```

### Level B — validated composition

```text
candidate edge
   ↓
inspect source
   ↓
check interfaces/dependencies
   ↓
find contradictions
   ↓
write adapter/integration test
   ↓
run benchmark
   ↓
validated / rejected
```

The current test only proves **Level A automation plus inventory coverage**. It does not claim Level B success.

## Important discovery

The full inventory contains both research/AI repositories and substantial infrastructure, documentation, data, search, UI and systems repositories. That means the RDG should not force everything into one AI graph. It should discover **capability boundaries** and use validation to determine whether a cross-domain composition is actually useful.

## Next validation target

Run the same pipeline at source-code level for the highest-value AI cluster:

```text
ReasonSynth
    ↓
Geometric-Engine-Intelligence-
    ↓
truthai-universal
    ↓
evals
```

Success should require executable tests, not semantic similarity alone.

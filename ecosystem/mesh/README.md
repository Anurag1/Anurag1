# Repository Semantic Mesh

This directory models the Anurag1 GitHub profile as a **semantic mesh**, not as a dependency graph.

## Edge rule

Two repositories are connected when they share one or more observable concepts at profile distance:

- repository name / description vocabulary
- AI capability (reasoning, memory, retrieval, agents, discovery, multimodal, simulation, evaluation)
- infrastructure capability (API, CLI, Docker, search, orchestration)
- data / research role
- graph / semantic / attention concepts

An edge therefore means **"there is something common worth investigating"**, not **"repo A imports repo B"**.

## Levels

- `profile`: inventory of repositories
- `semantic`: common concepts inferred from repository metadata
- `evidence`: exact shared files/dependencies/imports discovered by deeper inspection

The current generated mesh is intentionally profile-distance only. Run `build_mesh.py` with a GitHub token to regenerate it from the complete account inventory and repository metadata.

## Output

`mesh.json` contains nodes, semantic edges, shared concepts, and confidence scores.

The script deliberately keeps semantic edges separate from verified dependency edges so hypotheses are not presented as facts.

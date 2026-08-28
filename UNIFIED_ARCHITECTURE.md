# Anurag1 Unified AI Research Monorepo

This repository is the **integration layer** for Anurag1's AI research and engineering projects.

## Design principle

Preserve each project as an independently understandable module while exposing shared interfaces for:

```text
Perception / Inputs
        ↓
Representation
        ↓
Graph + Memory
        ↓
Meta-Attention + Reasoning
        ↓
Questions / Contradictions / Hypotheses
        ↓
Agents + Execution
        ↓
Simulation / Evaluation
        ↓
Discovery / Evidence
```

## Module map

| Module | Source repository | Role |
|---|---|---|
| `research/discovery/geometric-engine` | Geometric-Engine-Intelligence- | Graph-based unexplored-edge discovery |
| `research/reasoning/meta-attention` | Generalised-Meta-Attention-Architecture-4926c17c | Meta-attention, confidence, self-critique |
| `research/reasoning/suphai` | SUPHAI_MODEL | Adaptive inference / uncertainty |
| `research/reasoning/prometheus` | Prometheus-AGI | AGI-oriented orchestration experiments |
| `research/knowledge/aurora` | Aurora-The-Conversational-Knowledge-Lens | Knowledge exploration |
| `research/representation/geosemalign` | GeoSemAlign-Visual-Geometry-Symbol-Meaning-Pipeline | Geometry / symbol / semantic alignment |
| `agents/symbiote` | symbiote-agent-live | Agent execution experiments |
| `agents/nexus` | nexus-executor | Execution/orchestration |
| `agents/collective-reasoning` | Synthetic-Reason-Collective-Intelligence-System | Collective reasoning |
| `research/multimodal` | Awesome-Multimodal-Reasoning | Multimodal reasoning references |
| `research/memory` | Memori | Memory infrastructure/reference |
| `research/evaluation` | evals | Evaluation infrastructure/reference |
| `research/semantics/wave-grammar` | wave-graph-grammar-core | Graph grammar experiments |
| `research/truth` | truthai-universal | Truth/evidence experiments |
| `research/data/symbl` | symbl-data | Symbol/semantic data |
| `systems/ai-living-system` | ai-living-system-phase1 | Living-system architecture experiments |
| `systems/sems` | sems-phase0-monolith | SEMS prototype |
| `systems/sentient-cloud` | hio_sentient_cloud | Cloud/system experiments |
| `systems/codex` | codex2099 | Codex-style research/material |
| `applications/pbd` | PBDRS | Application prototype |
| `applications/simaf` | SIMAF | Application/research prototype |
| `applications/quantum-future` | A-Quantum-Inspired-Call-to-Collective-Action-Unifying-Domains-for-Humanity-s-Future | Cross-domain research |
| `platform/kodekit` | kodekit, kodekit-ui, kodekit-platform | Platform/UI experiments |
| `platform/payment` | payment-mcp-server | MCP/payment integration |
| `platform/open-source-search` | open-source-search-engine | Search infrastructure |
| `deployment/harmoniaflow` | aws-harmoniaflow-deploy | Deployment experiments |
| `security/guardrails` | openai-guardrails-python01 | Guardrail experiments |
| `tools/master-selector` | MasterSelector | Selection/routing utility |
| `tools/chooser` | chooser | Decision/selection utility |
| `tools/list-files` | list-files | File utility |
| `tools/files-gcs` | files_gcs | Storage utility |
| `tools/docker-socket-proxy` | docker-socket-proxy | Container utility |

## Integration contract

Each migrated module should eventually expose:

- `README.md` — purpose and status
- `module.yaml` — metadata, dependencies, source provenance
- `src/` or equivalent implementation
- `tests/` — reproducible tests
- `examples/` — minimal runnable example
- `docs/` — technical notes

## Important boundary

Large upstream mirrors and third-party source trees are **not copied into this monorepo by default**. They should remain separate dependencies/submodules unless a specific experiment requires vendoring them.

Examples include FAISS, LLVM, OpenSearch, Chromium/Brave, Bitcoin, Nginx, Frappe, PythonRobotics, mpv, Inferno OS, and related upstream mirrors.

## Migration policy

1. Snapshot and inventory each repository.
2. Preserve provenance and original repository URL.
3. Classify before moving code.
4. Merge only when ownership, licensing, and build/test boundaries are understood.
5. Keep source projects intact until the monorepo passes validation.
6. Make the monorepo the integration/research hub rather than blindly concatenating unrelated repositories.

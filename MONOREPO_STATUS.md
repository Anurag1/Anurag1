# Unified Repository Status

**Target:** `Anurag1/Anurag1`

This repository is now the canonical **integration hub** for the Anurag1 portfolio. The initial reorganization is intentionally non-destructive: original repositories remain intact.

## Verified GitHub inventory

The account currently exposes **70 repositories** to this connector. They fall into three groups:

### 1. First-party research / product work

These are the primary candidates for consolidation into modules:

`Geometric-Engine-Intelligence-`, `Generalised-Meta-Attention-Architecture-4926c17c`, `SUPHAI_MODEL`, `Prometheus-AGI`, `Aurora-The-Conversational-Knowledge-Lens`, `GeoSemAlign-Visual-Geometry-Symbol-Meaning-Pipeline`, `symbiote-agent-live`, `Synthetic-Reason-Collective-Intelligence-System`, `nexus-executor`, `wave-graph-grammar-core`, `truthai-universal`, `symbl-data`, `sems-phase0-monolith`, `ai-living-system-phase1`, `hio_sentient_cloud`, `codex2099`, `SIMAF`, `PBDRS`, `A-Quantum-Inspired-Call-to-Collective-Action-Unifying-Domains-for-Humanity-s-Future`, `MasterSelector`, `chooser`, `list-files`, `files_gcs`, `openai-guardrails-python01`, `payment-mcp-server`, `kodekit`, `kodekit-ui`, `kodekit-platform`, `Awesome-Multimodal-Reasoning`, `Memori`, `evals`.

### 2. Infrastructure / external-source mirrors

Large upstream or platform source trees should not be blindly copied into the monorepo. Examples verified in the inventory include `faiss`, `llvm-project`, `opensearch`, `opensearch-dashboards`, `bitcoin`, `brave-browser`, `nginx`, `nginx-tests`, `Win32-OpenSSH`, `PythonRobotics`, `mpv`, `inferno-os`, `inferno-1e0`, `inferno-1e1`, `inferno-2e`, `inferno-3e`, `tmux`, `notepad-plus-plus`, `youtube-dl`, `frappe`, `coreutils`, `findutils`, `kagglehub`, `adk-python`, `eth2.0-specs`, `kubernetes-ingress`, `open-source-search-engine`, `copilot-docs`, `creativecommons.org`, and `open4us.org`.

### 3. Profile / organization infrastructure

`Anurag1`, `.github`, and `docs` require separate treatment because they can contain profile, shared community, or documentation infrastructure rather than a single software module.

## Current implementation

- `UNIFIED_ARCHITECTURE.md` defines the target architecture and module map.
- `modules/manifest.yaml` provides machine-readable source-to-module mappings.
- Original repositories have **not** been deleted, renamed, or overwritten.

## Next consolidation rule

Only migrate actual first-party source trees into module directories after inspecting their file trees, licenses, build systems, and tests. Large mirrors remain external dependencies or references unless there is a concrete technical reason to vendor them.

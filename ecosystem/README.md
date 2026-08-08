# Anurag1 Ecosystem Control Plane

This directory defines a protocol-first control plane for connecting the Anurag1 repository ecosystem without forcing repositories into a monorepo.

## Model

```text
Repository -> Manifest -> Capability Registry -> Task/Event Bus -> Shared Evidence
       ^                                      |
       +-------------- Result / Feedback ----+
```

Repositories remain independently deployable. They share **contracts**, not arbitrary filesystem access or circular imports.

## Core concepts

- `repository-registry.json` — discovered repository inventory and initial classification.
- `protocol.yaml` — common manifest and event contract.
- `manifests/` — per-repository declarations as they are progressively onboarded.
- `knowledge/` — future shared evidence/provenance layer.
- `events/` — future event transport configuration.

## Initial priority graph

- `SUPHAI_MODEL` — orchestration / routing.
- `Generalised-Meta-Attention-Architecture` — reasoning / meta-attention.
- `HONET-` — research/model component.
- `ai-living-system-phase1` — adaptive-system research.
- `Synthetic-Reason-Collective-Intelligence-System` — collective reasoning.
- `ReasonSynth` — reasoning/synthesis.
- `symbiote-agent-live` — agent runtime.
- `nexus-executor` — execution.
- `Universal-Discovery-Engine` — discovery.
- `DiscoveryAI` — discovery research.
- `GeoSemAlign-Visual-Geometry-Symbol-Meaning-Pipeline` — multimodal/geometry.
- `Geometric-Engine-Intelligence-` — geometric intelligence.
- `autoresearch-gnn` — graph research/experimentation.
- `MiroFish` — simulation/agent ecosystem.
- `Memori` — memory capability.
- `gitnexus` — repository/code graph capability.
- `evals` — evaluation layer.

## Onboarding rule

Every repository eventually receives an `ecosystem.yaml` with:

`role`, `capabilities`, `inputs`, `outputs`, `publishes`, `consumes`, `dependencies`, and `protocol_version`.

Do not archive, merge, rename, or delete repositories merely because they appear similar. Classification must precede destructive changes.

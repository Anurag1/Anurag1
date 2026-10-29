# Anurag Dongare — AI Research & Engineering

I build experimental AI systems for **structured reasoning, knowledge graphs, agent coordination, and scientific discovery**. I turn ambitious ideas into runnable prototypes, falsifiable hypotheses, and reproducible evaluations.

**Current research question:** Can explicit representations of claims, relationships, assumptions, contradictions, and evidence help AI systems generate and test better hypotheses?

[Explore my flagship experiment](https://github.com/Anurag1/Universal-Discovery-Engine) · [Read the results and limitations](https://github.com/Anurag1/Universal-Discovery-Engine/pull/2) · [Browse all repositories](https://github.com/Anurag1?tab=repositories)

## Start here

### 🔬 Universal Discovery Engine
An experimental system for selecting candidate mathematical explanations and evaluating them against baselines.

- **What has been tested:** synthetic functions not exactly represented by the original candidate library.
- **What the results show:** sparse selection improved on the full-library baseline for three tested function families, but struggled on a mixed-frequency case where the needed basis function was missing.
- **Why this matters:** the failure exposes a concrete limitation—candidate selection cannot recover a useful structure that the library never proposes.
- **Next research step:** adaptive candidate generation, stronger held-out tests, and clean-checkout reproducibility.

**Status:** experimental research, not a claim of general superiority over modern AI.

## Featured projects

| Project | What it explores | Evidence and next step |
|---|---|---|
| [Universal Discovery Engine](https://github.com/Anurag1/Universal-Discovery-Engine) | Candidate explanations, mathematical pattern discovery, and baseline comparison | Synthetic benchmark and documented failure case; extend candidate generation and independent evaluation. |
| [HONet](https://github.com/GALAXYUNIONEORGANIZATION/HONET-) | Continual-learning concepts and an observation-to-hypothesis discovery loop | Research architecture with documented demos and tests; independent benchmark validation remains important. |
| [Aurora / VINCI AI](https://github.com/Anurag1/Aurora-The-Conversational-Knowledge-Lens) | Surfacing assumptions, missing context, contradictions, and links across conversations | Deterministic Python prototype with documented demo and regression-test workflow. |
| [Generalised Meta-Attention Architecture](https://github.com/Anurag1/Generalised-Meta-Attention-Architecture-4926c17c) | Meta-attention, confidence estimation, and self-critique | Experimental architecture; distinguish proposed components from implemented and evaluated ones. |
| [SUPHAI Model](https://github.com/Anurag1/SUPHAI_MODEL) | Multi-agent coordination and adaptive system architecture | Architecture-focused project; compare against simpler single-agent and orchestration baselines. |
| [Synthetic Reason — Collective Intelligence](https://github.com/Anurag1/Synthetic-Reason-Collective-Intelligence-System) | Symbolic memory, agent collaboration, and consensus | Prototype with documented API and optional integrations; deployment reliability requires separate testing. |

## Research workflow

```text
Observe → Represent claims and evidence → Map relationships
       → Find assumptions and contradictions → Generate hypotheses
       → Design discriminating tests → Compare with baselines
       → Publish results, limitations, and reproduction steps
```

## Technical interests

- Applied AI/ML and Python engineering
- Knowledge graphs and structured reasoning
- Agent systems and orchestration
- Evaluation harnesses, ablations, and reproducibility
- Symbolic representation and cross-domain discovery

## Research principles

- Runnable code over unsupported claims.
- Strong baselines and ablations over impressive demos.
- Publish negative results and known failure cases.
- Separate algorithmic novelty, knowledge novelty, and validated scientific discovery.
- Make experiments reproducible by other developers.

## Collaborate

I welcome focused collaboration on graph reasoning, agent systems, evaluation design, and independent replication.

**A useful contribution:** reproduce a benchmark, find a counterexample, challenge an assumption, or propose a stronger baseline. Please open an issue in the relevant repository with the experiment or evidence.

- [Browse all repositories](https://github.com/Anurag1?tab=repositories)

---

<sub>Project descriptions summarize repository documentation and are not independent verification of every advertised capability. Results described here are limited to the stated experiments; broader performance and scientific-discovery claims require controlled, reproducible evaluation.</sub>

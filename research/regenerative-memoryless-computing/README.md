# Regenerative Memoryless Computing (RMC) — Prototype

A small, reproducible experiment testing when a computer can avoid persisting generated data by retaining a recipe and regenerating it.

## What this tests

Three strategies on the same synthetic workloads:

1. **Raw storage** — persist the complete payload.
2. **gzip storage** — persist a losslessly compressed payload.
3. **Recipe storage** — persist a compact deterministic recipe and regenerate the payload.

Workloads:
- `procedural`: deterministic structured data generated from a seed and parameters.
- `repetitive`: highly repetitive text.
- `random`: deterministic pseudorandom bytes generated from a seed (the seed is the compact recipe; this is not a model of arbitrary unknown data).

The experiment reports stored bytes, regeneration time, exact reconstruction, and the break-even storage ratio. Recipe storage is only fair when the recipe is genuinely sufficient to regenerate the target. The random workload deliberately uses a known PRNG seed; arbitrary random data with no known origin cannot be recovered from a seed guessed after the fact.

## Run

Requires Python 3.10+; standard library only.

```bash
python rmc_benchmark.py --size-mib 1 --repeat 3
python -m unittest discover -s tests -v
```

## Interpretation caveats

- File sizes exclude filesystem metadata, interpreter/runtime, and the program/model needed to interpret recipes.
- Generation time is not directly comparable to disk-read time in every environment.
- Recipe storage shifts cost to compute; it does not violate information theory.
- The synthetic generator is not evidence of a general-purpose storage replacement.
- Results depend on machine, Python version, payload size, and workload.

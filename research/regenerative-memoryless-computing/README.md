# Regenerative Memoryless Computing (RMC) — Prototype

A reproducible experiment testing when generated data can be recreated from a compact recipe instead of persisting every output. The benchmark now charges the recipe strategy for the **generator source, Python executable, and on-disk Python standard-library tree** required to run it.

## Strategies compared

1. **Raw storage** — persist the complete payload.
2. **gzip storage** — persist a losslessly compressed payload.
3. **Recipe + deployment** — persist the recipe and account for the generator/runtime footprint. The one-time deployment footprint is then amortized across configurable numbers of artifacts sharing the same runtime.

Workloads:
- `procedural`: deterministic structured data generated from a seed and parameters.
- `repetitive`: highly repetitive text.
- `random`: deterministic pseudorandom bytes generated from a seed. This is not a model of arbitrary unknown data.

## Run locally

Requires Python 3.11+; the benchmark itself uses only the standard library.

```bash
python rmc_benchmark.py --size-mib 1 --repeat 3 --output artifacts/results.json
python -m unittest discover -s tests -v
```

Change the amortization assumptions explicitly:

```bash
python rmc_benchmark.py --amortization-counts 1,10,100,1000 --output results.json
```

## Continuous integration

GitHub Actions runs unit tests and the full-cost benchmark on Python 3.11 and 3.12 for relevant pushes, pull requests, and manual dispatch. Each matrix run uploads a `results.json` artifact with environment-specific storage costs and reconstruction checks.

Workflow: [RMC tests and full-cost benchmark](../../../.github/workflows/rmc-benchmark.yml)

## What the cost means

The reported one-time footprint includes:
- this benchmark/generator source file,
- the active Python interpreter executable,
- files under the Python standard-library tree, excluding third-party `site-packages` and `dist-packages`.

The benchmark reports both the **one-artifact full deployment cost** and per-artifact recipe cost when 1, 10, 100, or 1,000 artifacts share the same generator/runtime. This is more informative than comparing a 48–52 byte recipe to a 1 MiB payload. The exact footprint depends on the CI runner and Python version.

## Limitations

- The footprint is an on-disk approximation; it excludes the operating system/kernel, filesystem metadata, caches, and container/base-image layers.
- A runtime may already be installed or shared with unrelated workloads. Amortization scenarios expose, rather than hide, that assumption.
- Storage break-even alone ignores CPU time, energy, latency, durability, and generator maintenance.
- Recipe regeneration works only when the recipe and generator preserve enough information to reproduce the output exactly. A known pseudorandom seed does not recover arbitrary unknown bytes.
- Synthetic workloads are not evidence of a general-purpose storage replacement or a violation of information theory.

The relevant question is therefore not “is the recipe smaller?” but “does the complete, fairly allocated regeneration system beat a conventional compressor for this workload and deployment model?”

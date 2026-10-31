# Regenerative Memoryless Computing (RMC) — Prototype

A reproducible experiment testing when generated data can be recreated from a compact recipe instead of persisting every output. The benchmark now charges the recipe strategy for the **generator source, Python executable, and on-disk Python standard-library tree** required to run it.

## Strategies compared

1. **Raw storage** — persist the complete payload.
2. **gzip storage** — persist a losslessly compressed payload.
3. **Recipe + deployment** — persist the recipe and account for the generator/runtime footprint. The one-time deployment footprint is then amortized across configurable numbers of artifacts sharing the same runtime.

Workloads are deterministic procedural data, repetitive text, and seeded pseudorandom bytes. The last workload is not a model of arbitrary unknown data.

## Run locally

Requires Python 3.11+; standard library only.

```bash
python rmc_benchmark.py --size-mib 1 --repeat 3 --output artifacts/results.json
python -m unittest discover -s tests -v
python rmc_benchmark.py --amortization-counts 1,10,100,1000 --output results.json
```

## Continuous integration

GitHub Actions runs unit tests and the full-cost benchmark on Python 3.11 and 3.12 for relevant pushes, pull requests, and manual dispatch. Each matrix run uploads an environment-specific `results.json` artifact.

Workflow: [RMC tests and full-cost benchmark](../../../.github/workflows/rmc-benchmark.yml)

## Cost model

The one-time deployment footprint includes this generator source, the active Python executable, and files in the Python standard-library tree (excluding third-party `site-packages` and `dist-packages`). Results report the full cost for one artifact and the per-artifact cost when 1, 10, 100, or 1,000 artifacts share the same runtime. This avoids treating a tiny recipe as a fair comparison against a compressor while ignoring the code needed to interpret it.

## Limitations

- The footprint is an on-disk approximation; it excludes the operating system/kernel, filesystem metadata, caches, and container/base-image layers.
- A runtime may already be installed or shared with other workloads. Amortization scenarios make that assumption explicit.
- Storage break-even alone ignores CPU time, energy, latency, durability, and generator maintenance.
- A known pseudorandom seed cannot recover arbitrary unknown bytes.
- Synthetic workloads are not evidence of general-purpose storage replacement or a violation of information theory.

The key question is whether the complete regeneration system beats conventional compression for a workload and deployment model—not whether the recipe alone is small.

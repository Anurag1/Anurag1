#!/usr/bin/env python3
"""Compare raw, gzip, and recipe storage including the deployed generator/runtime footprint."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import random
import statistics
import sys
import sysconfig
import time
from pathlib import Path


def make_payload(kind: str, size: int, seed: int = 20261031) -> bytes:
    if size < 0:
        raise ValueError("size must be non-negative")
    if kind == "procedural":
        rng = random.Random(seed)
        out = bytearray()
        while len(out) < size:
            n = rng.randrange(0, 1000)
            out.extend(f"node:{n:04d}|edge:{n % 17:02d}|kind:{n % 5}\n".encode())
        return bytes(out[:size])
    if kind == "repetitive":
        unit = b"RMC:reconstructible-data|"
        return (unit * ((size + len(unit) - 1) // len(unit)))[:size]
    if kind == "random":
        # Reproducible PRNG output; not a recipe for arbitrary unknown bytes.
        rng = random.Random(seed)
        return rng.randbytes(size)
    raise ValueError(f"unknown workload: {kind}")


def timed(fn, repeats: int):
    samples, value = [], None
    for _ in range(repeats):
        t0 = time.perf_counter()
        value = fn()
        samples.append(time.perf_counter() - t0)
    return value, statistics.median(samples)


def tree_bytes(root: Path) -> int:
    """Count regular files under a directory, without following symlinked directories."""
    total = 0
    if not root.exists() or not root.is_dir():
        return 0
    for path in root.rglob("*"):
        try:
            if path.is_file() and not path.is_symlink():
                total += path.stat().st_size
        except (OSError, PermissionError):
            continue
    return total


def deployment_footprint() -> dict:
    """Approximate on-disk Python interpreter + stdlib + this generator source."""
    script_bytes = Path(__file__).resolve().stat().st_size
    executable = Path(sys.executable).resolve()
    interpreter_bytes = executable.stat().st_size if executable.exists() else 0
    stdlib = Path(sysconfig.get_path("stdlib")).resolve()
    # Count the standard-library tree, but exclude third-party site-packages if nested.
    stdlib_bytes = 0
    if stdlib.exists():
        for p in stdlib.rglob("*"):
            try:
                if not p.is_file() or p.is_symlink():
                    continue
                if "site-packages" in p.parts or "dist-packages" in p.parts:
                    continue
                stdlib_bytes += p.stat().st_size
            except (OSError, PermissionError):
                continue
    return {
        "generator_source_bytes": script_bytes,
        "python_executable_bytes": interpreter_bytes,
        "standard_library_tree_bytes": stdlib_bytes,
        "deployment_one_time_bytes": script_bytes + interpreter_bytes + stdlib_bytes,
        "measurement_note": "On-disk Python executable and standard-library tree plus this script; excludes OS/kernel, filesystem metadata, caches, and any container/base image. The runtime may already be installed/shared, so both full and amortized views are reported."
    }


def benchmark(kind: str, size: int, repeats: int, footprint: dict,
              amortization_counts: list[int]) -> dict:
    payload, generation_s = timed(lambda: make_payload(kind, size), repeats)
    raw_bytes = len(payload)
    compressed = gzip.compress(payload, compresslevel=6, mtime=0)
    recipe = json.dumps({"kind": kind, "size": size, "seed": 20261031},
                        sort_keys=True, separators=(",", ":")).encode()
    restored, regen_s = timed(lambda: make_payload(kind, size, 20261031), repeats)
    exact = hashlib.sha256(payload).digest() == hashlib.sha256(restored).digest()
    one_time = footprint["deployment_one_time_bytes"]
    full_cost = one_time + len(recipe)
    amortized = []
    for count in amortization_counts:
        per_artifact = (one_time / count) + len(recipe)
        amortized.append({
            "artifacts_sharing_generator_runtime": count,
            "recipe_strategy_bytes_per_artifact_amortized": round(per_artifact, 2),
            "gzip_bytes_per_artifact": len(compressed),
            "recipe_beats_gzip_on_storage": per_artifact < len(compressed),
            "raw_bytes_per_artifact": raw_bytes,
        })
    return {
        "workload": kind,
        "payload_bytes": raw_bytes,
        "raw_stored_bytes": raw_bytes,
        "gzip_stored_bytes": len(compressed),
        "recipe_only_bytes_misleading_without_runtime": len(recipe),
        "recipe_plus_full_deployment_bytes_for_one_artifact": full_cost,
        "gzip_savings_pct": round(100 * (1 - len(compressed) / max(raw_bytes, 1)), 2),
        "recipe_only_savings_pct_not_fair_comparison": round(100 * (1 - len(recipe) / max(raw_bytes, 1)), 2),
        "recipe_reconstruction_exact": exact,
        "median_generation_ms": round(generation_s * 1000, 3),
        "median_recipe_reconstruction_ms": round(regen_s * 1000, 3),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "recipe": json.loads(recipe),
        "storage_break_even_scenarios": amortized,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size-mib", type=float, default=1.0)
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--amortization-counts", default="1,10,100,1000",
                        help="comma-separated number of artifacts sharing one generator/runtime")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.size_mib <= 0 or args.repeat < 1:
        parser.error("--size-mib must be positive and --repeat must be >= 1")
    try:
        counts = sorted(set(int(x) for x in args.amortization_counts.split(",")))
    except ValueError:
        parser.error("--amortization-counts must be comma-separated positive integers")
    if not counts or any(n < 1 for n in counts):
        parser.error("--amortization-counts must contain positive integers")

    size = int(args.size_mib * 1024 * 1024)
    footprint = deployment_footprint()
    results = {
        "title": "Regenerative Memoryless Computing: full deployment-cost benchmark",
        "method": "raw vs gzip vs deterministic recipe, including generator source + Python executable + standard-library tree",
        "size_mib_requested": args.size_mib,
        "repeat": args.repeat,
        "amortization_counts": counts,
        "deployment_footprint": footprint,
        "results": [benchmark(k, size, args.repeat, footprint, counts)
                    for k in ("procedural", "repetitive", "random")],
        "limitations": [
            "Synthetic workloads only; this does not establish general storage elimination.",
            "Deployment footprint is an on-disk approximation and excludes OS/kernel, filesystem metadata, container image layers, and caches.",
            "The Python runtime may already exist or be shared with other workloads; amortization scenarios make this assumption explicit.",
            "The random workload is reproducible because the PRNG seed and algorithm are known; arbitrary unknown bytes cannot be recovered from a seed guessed after the fact.",
            "Storage break-even ignores energy, CPU time, latency, durability, and the cost of maintaining compatible generator code."
        ]
    }
    rendered = json.dumps(results, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

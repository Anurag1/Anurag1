#!/usr/bin/env python3
"""Benchmark raw, gzip, and recipe-based persistence for reproducible synthetic data."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import random
import statistics
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
        # Reproducible PRNG output; this is not a recipe for arbitrary unknown bytes.
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

def benchmark(kind: str, size: int, repeats: int) -> dict:
    payload, generation_s = timed(lambda: make_payload(kind, size), repeats)
    raw_bytes = len(payload)
    compressed = gzip.compress(payload, compresslevel=6, mtime=0)
    recipe = json.dumps({"kind": kind, "size": size, "seed": 20261031},
                        sort_keys=True, separators=(",", ":")).encode()
    restored, regen_s = timed(lambda: make_payload(kind, size, 20261031), repeats)
    exact = hashlib.sha256(payload).digest() == hashlib.sha256(restored).digest()
    return {
        "workload": kind,
        "payload_bytes": raw_bytes,
        "raw_stored_bytes": raw_bytes,
        "gzip_stored_bytes": len(compressed),
        "recipe_stored_bytes": len(recipe),
        "gzip_savings_pct": round(100 * (1 - len(compressed) / max(raw_bytes, 1)), 2),
        "recipe_savings_pct": round(100 * (1 - len(recipe) / max(raw_bytes, 1)), 2),
        "recipe_reconstruction_exact": exact,
        "median_generation_ms": round(generation_s * 1000, 3),
        "median_recipe_reconstruction_ms": round(regen_s * 1000, 3),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "recipe": json.loads(recipe),
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size-mib", type=float, default=1.0)
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.size_mib <= 0 or args.repeat < 1:
        parser.error("--size-mib must be positive and --repeat must be >= 1")
    size = int(args.size_mib * 1024 * 1024)
    results = {
        "title": "Regenerative Memoryless Computing benchmark",
        "method": "raw vs gzip vs deterministic recipe regeneration",
        "size_mib_requested": args.size_mib,
        "repeat": args.repeat,
        "results": [benchmark(k, size, args.repeat)
                    for k in ("procedural", "repetitive", "random")],
        "limitations": [
            "Synthetic workloads only; not a general storage-elimination result.",
            "Recipe size excludes the code/runtime required to interpret the recipe.",
            "Random workload is reproducible because its PRNG seed is known.",
            "Arbitrary unknown information cannot be reconstructed without preserving sufficient information or obtaining it elsewhere."
        ]
    }
    rendered = json.dumps(results, indent=2)
    print(rendered)
    if args.output:
        args.output.write_text(rendered + "\n")

if __name__ == "__main__":
    main()

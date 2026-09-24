import importlib.util
from pathlib import Path


def test_benchmark_has_13_problems_and_two_systems():
    path = Path(__file__).parents[1] / "experiments" / "run_benchmark.py"
    spec = importlib.util.spec_from_file_location("runner", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    manifest = module.build_manifest()
    assert manifest["problem_count"] == 13
    assert manifest["systems"] == ["conventional-baseline", "discovery-oriented"]
    assert len(manifest["problems"]) == 13

#!/usr/bin/env python3
"""Minimal Repository Discovery Graph (RDG) portfolio demo.

This is a semantic-name prototype, not a code dependency analyzer.
It treats repository names as weak signals and ranks candidate compositions.
"""
from itertools import combinations

REPOS = [
    "Anurag1", "Sapient-Ultra", "Synapse-X", "Aurelius", "ENIGMA", "Prometheus-AGI", "SUPHAI_MODEL", "hio_sentient_cloud", "sems-phase0-monolith", "A-Quantum-Inspired-Call-to-Collective-Action-Unifying-Domains-for-Humanity-s-Future", "faiss", "ai-living-system-phase1", "Win32-OpenSSH", "wave-graph-grammar-core", "truthai-universal", "evals", "openai-python-advanced", "PBDRS", "symbiote-agent-live", "ReasonSynth", "codex2099", "openai-guardrails-python01", "alphafold3-2099", "Synthetic-Reason-Collective-Intelligence-System", "aws-harmoniaflow-deploy", "Aurora-The-Conversational-Knowledge-Lens", "UrbanOrbit", "Geometric-Engine-Intelligence-", "nginx-site", "nginx", "nginx-tests", "xslscript", "angie", "bitcoin", "brave-browser", "adk-python", "Memori", "PythonRobotics", "mpv", "inferno-os", "ventivac", "inferno-1e0", "inferno-1e1", "inferno-2e", "inferno-3e", "tmux", "notepad-plus-plus", "youtube-dl", "frappe", "opensearch", "opensearch-dashboards", "open-source-search-engine", "PiBits", "yacy_search_server", "llvm-project", "chooser", "cc-legal-tools-app", "cc-legal-tools-data", "cc-resource-archive", "creativecommons.org", "open4us.org", "taaccct", "sre-wp-pull", "SIMAF", "Awesome-Multimodal-Reasoning", "files_gcs", "cortivox", "docker-socket-proxy", "list-files", "MasterSelector", "hyperglot", "workshop-material", "SpecimenDropper", "DrawBot-Scripts", "symbl-data", "FAI", "Generalised-Meta-Attention-Architecture-4926c17c", "nexus-executor", ".github", "GeoSemAlign-Visual-Geometry-Symbol-Meaning-Pipeline", "kubernetes-ingress", "kagglehub", "docs", "payment-mcp-server", "coreutils", "findutils", "copilot-docs", "code-push-server", "redis-csc", "kodekit-ui", "illusion", "kodekit", "openpolice-intranet", "timble-team", "jekyll-pagination", "kodekit-platform", "openpolice-vagrant", "Countdown", "eth2.0-specs", "Git2Jira2Jenkins"
]

TAGS = {
    "reasoning": ("reason", "reasoning", "attention", "agi", "intelligence", "sapient", "enigma", "aurelius", "pbdrs", "quantum", "synapse", "truthai", "fai"),
    "agents": ("agent", "adk", "masterselector", "symbiote", "executor", "suphai", "prometheus", "codex", "copilot"),
    "discovery": ("discover", "discovery", "enigma", "research"),
    "graphs": ("graph", "geometric", "geometry", "nexus", "semantic", "symbl", "wave"),
    "memory": ("memori", "memory", "context", "living", "sentient"),
    "retrieval": ("search", "faiss", "opensearch", "kaggle", "findutils"),
    "multimodal": ("multimodal", "visual", "drawbot", "mpv"),
    "evaluation": ("eval", "benchmark", "leaderboard", "test"),
    "validation": ("truth", "guardrail", "legal", "integrity", "validator", "eval"),
    "infrastructure": ("docker", "kubernetes", "nginx", "redis", "aws", "ssh", "coreutils", "findutils", "llvm", "tmux", "vagrant", "server", "platform"),
    "science": ("alphafold", "robotics", "quantum"),
    "search": ("search", "opensearch", "yacy", "faiss", "findutils"),
}

def tags(repo):
    s = repo.lower()
    return {tag for tag, words in TAGS.items() if any(w in s for w in words)}

def candidate_edges(min_shared=1):
    tagged = {r: tags(r) for r in REPOS}
    edges = []
    for a, b in combinations(REPOS, 2):
        shared = tagged[a] & tagged[b]
        if len(shared) >= min_shared:
            edges.append((len(shared), a, b, sorted(shared)))
    return sorted(edges, reverse=True)

def showcase():
    required = {
        "discovery": [r for r in REPOS if "discovery" in tags(r)],
        "graph": [r for r in REPOS if "graphs" in tags(r)],
        "validation": [r for r in REPOS if "validation" in tags(r)],
        "evaluation": [r for r in REPOS if "evaluation" in tags(r)],
    }
    print(f"nodes={len(REPOS)}")
    print("capability_counts=" + str({k: len(v) for k, v in required.items()}))
    seed = ["ReasonSynth", "Geometric-Engine-Intelligence-", "truthai-universal", "evals"]
    missing = [r for r in seed if r not in REPOS]
    print("architecture_seed=" + " -> ".join(seed))
    print("inventory_missing_from_seed=" + str(missing))
    print("top_semantic_edges:")
    for score, a, b, shared in candidate_edges(min_shared=2)[:10]:
        print(f"  score={score}  {a} <-> {b}  shared={','.join(shared)}")

if __name__ == "__main__":
    showcase()

#!/usr/bin/env python3
"""Build a profile-distance semantic mesh for all repositories owned by a GitHub user.

This is intentionally NOT a dependency detector. It creates candidate semantic edges
from repository metadata. A later evidence pass can verify imports, package dependencies,
shared workflows, submodules, forks, or direct links.
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

OWNER = os.environ.get("GITHUB_OWNER", "Anurag1")
OUT = Path(os.environ.get("MESH_OUT", "ecosystem/mesh/mesh.json"))
TOKEN = os.environ.get("GITHUB_TOKEN")

CONCEPTS = {
    "reasoning": {"reasoning", "logic", "validator", "intelligence", "cognition", "attention", "compute", "inference", "thought", "knowledge"},
    "agents": {"agent", "agents", "autonomous", "copilot", "claw", "executor", "orchestration", "selector", "workflow", "mcp"},
    "memory": {"memory", "memori", "context", "state", "world", "adaptive", "self", "living"},
    "discovery": {"discovery", "discover", "research", "architecture", "synth", "synthesis", "eureka", "enigma"},
    "retrieval": {"search", "retrieval", "faiss", "opensearch", "index", "latent", "semantic", "library", "arxiv"},
    "graphs": {"graph", "graphical", "geometry", "geometric", "nexus", "network", "node", "symbol", "latent"},
    "multimodal": {"multimodal", "visual", "vision", "image", "video", "draw", "geometry"},
    "evaluation": {"eval", "evals", "benchmark", "leaderboard", "hallucination", "red", "robustness", "validation", "audit"},
    "infrastructure": {"api", "server", "cli", "docker", "kubernetes", "nginx", "terraform", "aws", "azure", "cloudflare", "redis", "rabbitmq", "jenkins", "vercel"},
    "learning": {"learn", "learning", "llm", "transformer", "tensor", "tensorflow", "pytorch", "machine", "neural", "model", "course"},
    "data": {"data", "dataset", "kaggle", "csv", "pdf", "docs", "archive", "openlibrary"},
    "simulation": {"simulation", "simaf", "mirofish", "urban", "robotics", "robot", "iot"},
    "security": {"guardrail", "security", "sentinel", "jailbreak", "adversarial", "red", "robustness"},
}

STOP = {"the", "and", "for", "with", "from", "how", "why", "system", "project", "model", "repo", "anurag1"}

def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 2 and w not in STOP}

def concepts(text: str) -> set[str]:
    ws = words(text)
    return {c for c, terms in CONCEPTS.items() if ws & terms}

def gh(path: str):
    url = "https://api.github.com" + path
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "Anurag1-semantic-mesh"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def get_repos():
    repos = []
    page = 1
    while True:
        batch = gh(f"/users/{urllib.parse.quote(OWNER)}/repos?per_page=100&page={page}&type=all&sort=updated")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos

def similarity(a: dict, b: dict):
    ac = set(a["concepts"])
    bc = set(b["concepts"])
    common = sorted(ac & bc)
    aw = words(a["name"] + " " + (a.get("description") or ""))
    bw = words(b["name"] + " " + (b.get("description") or ""))
    lexical = len(aw & bw)
    score = (len(common) / max(1, len(ac | bc))) + min(0.25, lexical * 0.05)
    return score, common, lexical

def main():
    repos = get_repos()
    nodes = []
    for r in repos:
        text = r["name"] + " " + (r.get("description") or "")
        nodes.append({
            "id": r["full_name"],
            "name": r["name"],
            "url": r["html_url"],
            "visibility": r.get("visibility"),
            "archived": bool(r.get("archived")),
            "description": r.get("description") or "",
            "language": r.get("language"),
            "stars": r.get("stargazers_count", 0),
            "concepts": sorted(concepts(text)),
        })

    edges = []
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            score, common, lexical = similarity(a, b)
            if not common and lexical == 0:
                continue
            # Keep only meaningful candidate links; very weak lexical collisions are noise.
            if score >= 0.20 or len(common) >= 2 or lexical >= 2:
                edges.append({
                    "source": a["id"],
                    "target": b["id"],
                    "type": "semantic_commonality",
                    "shared_concepts": common,
                    "lexical_overlap": lexical,
                    "score": round(score, 4),
                })

    edges.sort(key=lambda e: e["score"], reverse=True)
    degree = Counter()
    for e in edges:
        degree[e["source"]] += 1
        degree[e["target"]] += 1
    for n in nodes:
        n["mesh_degree"] = degree[n["id"]]

    payload = {
        "schema_version": "1.0",
        "owner": OWNER,
        "graph_type": "profile-distance semantic mesh",
        "edge_semantics": "shared observable concept; not verified dependency",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": nodes,
        "edges": edges,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}: {len(nodes)} nodes, {len(edges)} semantic edges")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"mesh build failed: {exc}", file=sys.stderr)
        raise

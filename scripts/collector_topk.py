#!/usr/bin/env python3
"""
Collector topK benchmark (v2.3 scaffold).

Purpose:
- Build a complete raw_results file for 20 benchmark queries.
- Works in two modes:
  1) prepare: generate TODO file per query (for tool/operator run)
  2) assemble: merge filled results into raw_results JSON

Why scaffold:
- In-chat tool execution (memory_search) is not directly callable from standalone Python
  without an external bridge. This script standardizes the handover format so any agent/operator
  can collect topK consistently.
"""

import json
import sys
from pathlib import Path


def prepare(queries_path: Path, out_path: Path, topk: int = 8):
    queries = json.loads(queries_path.read_text())
    rows = []
    for q in queries:
        rows.append({
            "id": q["id"],
            "query": q["query"],
            "maxResults": topk,
            "results": []
        })
    out_path.write_text(json.dumps(rows, indent=2))
    print(f"prepared {len(rows)} query slots -> {out_path}")


def assemble(in_path: Path, out_path: Path):
    rows = json.loads(in_path.read_text())
    out = []
    for r in rows:
        candidates = []
        for x in r.get("results", []):
            candidates.append({
                "path": x.get("path"),
                "score": x.get("score"),
                "snippet": x.get("snippet", "")
            })
        out.append({
            "id": r["id"],
            "query": r["query"],
            "candidates": candidates
        })
    out_path.write_text(json.dumps(out, indent=2))
    print(f"assembled raw_results -> {out_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  collector_topk.py prepare <queries.json> <todo.json> [topk]")
        print("  collector_topk.py assemble <todo_filled.json> <raw_results.json>")
        raise SystemExit(1)

    mode = sys.argv[1]
    if mode == "prepare":
        q = Path(sys.argv[2])
        o = Path(sys.argv[3])
        k = int(sys.argv[4]) if len(sys.argv) > 4 else 8
        prepare(q, o, k)
    elif mode == "assemble":
        i = Path(sys.argv[2])
        o = Path(sys.argv[3])
        assemble(i, o)
    else:
        raise SystemExit(f"Unknown mode: {mode}")


if __name__ == "__main__":
    main()

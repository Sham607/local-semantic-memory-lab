#!/usr/bin/env python3
"""
V2.2 middleware simulator: structured-first rerank for memory retrieval candidates.

Input JSON format:
[
  {
    "id": "Q01",
    "query": "...",
    "candidates": [
      {"path":"memory/2026-03-06.md","score":0.51,"snippet":"..."},
      ...
    ]
  }
]

Output: same entries with `reranked` list + selected `top1`.
"""

from __future__ import annotations
import json
import re
from pathlib import Path
from datetime import datetime


def parse_day(path: str):
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", path)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    except Exception:
        return None


def load_manifest(paths):
    kinds = {}
    for p in paths:
        p = Path(p)
        if not p.exists():
            continue
        data = json.loads(p.read_text())
        for r in data:
            kinds[Path(r["path"]).as_posix()] = r.get("kind", "transcript")
    return kinds


def lexical_overlap(q: str, s: str) -> float:
    qw = set(re.findall(r"[a-zA-Z0-9_]+", q.lower()))
    sw = set(re.findall(r"[a-zA-Z0-9_]+", s.lower()))
    if not qw:
        return 0.0
    return len(qw & sw) / len(qw)


def recency_boost(path: str, ref_date):
    d = parse_day(path)
    if not d:
        return 0.0
    age = (ref_date - d).days
    if age <= 7:
        return 0.05
    if age <= 30:
        return 0.02
    return 0.0


def kind_bonus(kind: str):
    # structured > transcript
    return 0.08 if kind == "structured" else 0.0


def rerank(query, candidates, kinds, ref_date):
    scored = []
    for c in candidates:
        path = Path(c.get("path", "")).as_posix()
        kind = kinds.get(path, "transcript")
        sem = float(c.get("score", 0.0))
        lex = lexical_overlap(query, c.get("snippet", ""))
        final = (0.75 * sem) + (0.15 * lex) + kind_bonus(kind) + recency_boost(path, ref_date)
        x = dict(c)
        x["kind"] = kind
        x["rerank_score"] = round(final, 6)
        scored.append(x)
    return sorted(scored, key=lambda x: x["rerank_score"], reverse=True)


def main(in_path: str, out_path: str):
    data = json.loads(Path(in_path).read_text())
    root = Path(__file__).resolve().parents[1]
    manifests = [
        root / "benchmarks" / "manifest.structured.json",
        root / "benchmarks" / "manifest.transcript.json",
    ]
    kinds = load_manifest(manifests)
    ref_date = datetime.utcnow().date()

    out = []
    for row in data:
        rr = rerank(row["query"], row.get("candidates", []), kinds, ref_date)
        out.append({
            "id": row["id"],
            "query": row["query"],
            "top1": rr[0] if rr else None,
            "reranked": rr,
        })

    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"wrote {out_path} ({len(out)} queries)")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: rerank_structured_first.py <raw_results.json> <out.json>")
        raise SystemExit(1)
    main(sys.argv[1], sys.argv[2])

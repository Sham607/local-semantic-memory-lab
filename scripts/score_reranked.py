#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def norm(s):
    return (s or "").lower()


def main(reranked_path, ground_truth_path):
    rr = json.loads(Path(reranked_path).read_text())
    gt = {x["id"]: x for x in json.loads(Path(ground_truth_path).read_text())}

    counts = {"strong": 0, "partial": 0, "noise": 0}
    details = []

    for row in rr:
        qid = row["id"]
        top1 = row.get("top1") or {}
        blob = norm((top1.get("path", "") + "\n" + top1.get("snippet", "")))
        exp = [norm(x) for x in gt.get(qid, {}).get("expected_contains", [])]
        hit = sum(1 for e in exp if e and e in blob)

        if exp and hit >= max(1, len(exp) // 2 + (len(exp) % 2)):
            label = "strong"
        elif hit > 0:
            label = "partial"
        else:
            label = "noise"
        counts[label] += 1
        details.append({"id": qid, "label": label, "hit": hit, "expected": len(exp), "path": top1.get("path")})

    total = len(rr) or 1
    print(f"strong: {counts['strong']} ({counts['strong']/total:.1%})")
    print(f"partial: {counts['partial']} ({counts['partial']/total:.1%})")
    print(f"noise: {counts['noise']} ({counts['noise']/total:.1%})")

    out = Path(reranked_path).with_suffix(".labels.json")
    out.write_text(json.dumps(details, indent=2))
    print(f"labels saved: {out}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: score_reranked.py <reranked.json> <ground_truth.json>")
        raise SystemExit(1)
    main(sys.argv[1], sys.argv[2])

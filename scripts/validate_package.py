#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def main(raw_path: str, min_candidates: int = 1):
    data = json.loads(Path(raw_path).read_text())
    total = len(data)
    ok = 0
    bad = []
    for row in data:
        n = len(row.get("candidates", []))
        if n >= min_candidates:
            ok += 1
        else:
            bad.append({"id": row.get("id"), "count": n})

    print(f"queries: {total}")
    print(f"valid_queries: {ok}")
    print(f"invalid_queries: {len(bad)}")
    if bad:
        print("invalid_detail:")
        for b in bad:
            print(f"- {b['id']}: {b['count']}")
        raise SystemExit(2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_package.py <raw_results.json> [min_candidates]")
        raise SystemExit(1)
    path = sys.argv[1]
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    main(path, m)

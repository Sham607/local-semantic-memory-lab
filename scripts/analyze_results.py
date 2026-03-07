#!/usr/bin/env python3
"""
Analyze benchmark labels (strong/partial/noise).
Input format (example):
[
  {"id":"Q01","label":"strong"},
  ...
]
"""

import json
import sys
from collections import Counter


def main(path: str):
    data = json.load(open(path))
    c = Counter([x.get("label", "unknown") for x in data])
    total = len(data) or 1
    for k in ["strong", "partial", "noise", "unknown"]:
        v = c.get(k, 0)
        print(f"{k}: {v} ({v/total:.1%})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: analyze_results.py <labels.json>")
        sys.exit(1)
    main(sys.argv[1])

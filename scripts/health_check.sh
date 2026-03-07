#!/usr/bin/env bash
set -euo pipefail

echo "[health] local semantic memory lab"
echo "- check disk usage"
df -h . | tail -n 1

echo "- check benchmark assets"
ls -1 ../benchmarks >/dev/null

echo "OK"

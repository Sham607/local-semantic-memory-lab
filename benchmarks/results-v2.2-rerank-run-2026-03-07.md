# V2.2 Rerank Run — 2026-03-07

## What was added
- Raw benchmark capture file:
  - `benchmarks/raw_results.2026-03-07.v22.json`
- Reranked output:
  - `benchmarks/reranked.2026-03-07.v22.json`
- Auto labels output:
  - `benchmarks/reranked.2026-03-07.v22.labels.json`
- New scorer script:
  - `scripts/score_reranked.py`

## Run command
```bash
python3 scripts/rerank_structured_first.py benchmarks/raw_results.2026-03-07.v22.json benchmarks/reranked.2026-03-07.v22.json
python3 scripts/score_reranked.py benchmarks/reranked.2026-03-07.v22.json benchmarks/ground_truth.v1.json
```

## Score (heuristic)
- Strong: **40%** (8/20)
- Partial: **0%** (0/20)
- Noise: **60%** (12/20)

## Important note
This run used a minimal raw capture (mostly top-1 candidate snapshots), not full topK per query. So reranker impact is under-represented.

## Next action (high impact)
1. Build full collector to capture topK candidates for all 20 queries.
2. Re-run reranker on real topK (8-12 candidates per query).
3. Re-score and compare against baseline/v1/v2-sim.

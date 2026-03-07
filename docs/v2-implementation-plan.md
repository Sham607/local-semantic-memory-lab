# V2 Implementation Plan — Structured-first Retrieval

## Why V2
V1 (minScore only) did not improve quality. Need pipeline-level changes.

## Deliverables
1. Source manifest split (done): structured vs transcript.
2. Retrieval middleware:
   - Pull topK candidates
   - Attach source kind from manifest
   - Re-score with source priority + recency
   - Return topN
3. Benchmark rerun (20 queries) with same protocol.

## Execution Steps
1. Build candidate pool from memory search topK (>=8, target 12).
2. Map candidate file path to `manifest.structured.json` / `manifest.transcript.json`.
3. Apply structured-first priority.
4. Penalize old noisy transcript snippets (time decay).
5. Optional lexical overlap bonus to reduce semantic drift.
6. Output ranked topN and evaluate top-1 label.

### Middleware script (v2.2)
- Script: `scripts/rerank_structured_first.py`
- Input: `benchmarks/raw_results.<date>.json`
- Output: `benchmarks/reranked.<date>.json`
- Example:
  - `python3 scripts/rerank_structured_first.py benchmarks/raw_results.template.json benchmarks/reranked.sample.json`

## Acceptance Criteria
- Strong >= 55%
- Noise <= 25%
- No severe latency regression (>30% from baseline)

## Risks
- Over-bias to structured files may miss valid contextual transcript.
- Need balancing weight tuning.

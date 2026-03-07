# V2.2 Middleware Status

Tanggal: 2026-03-07 (UTC)

## Done
- Implemented structured-first rerank middleware simulator:
  - `scripts/rerank_structured_first.py`
- Added input template:
  - `benchmarks/raw_results.template.json`
- Updated implementation doc:
  - `docs/v2-implementation-plan.md`

## Rerank Logic
`final_score = 0.75*semantic + 0.15*lexical_overlap + kind_bonus + recency_boost`

- `kind_bonus`: +0.08 for structured candidates
- `recency_boost`: +0.05 (<=7 days), +0.02 (<=30 days)

## Pending
- Capture full raw topK results for all 20 queries into one JSON file.
- Run middleware and score Strong/Partial/Noise automatically.

## Why Pending
Current `memory_search` tool interface in-chat is request/response; raw capture pipeline to file needs orchestration wrapper (or manual export) before full automated scoring can run end-to-end.

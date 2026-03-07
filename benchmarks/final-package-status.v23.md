# Final Package Status v2.3 (Quality-Valid)

Tanggal: 2026-03-07 (UTC)

## Validity Checklist
- [x] `topk_todo.v23.json` terisi untuk 20/20 query
- [x] Setiap query berisi topK real (8 kandidat/query)
- [x] Collector assemble berhasil (`raw_results.v23.from_todo.json`)
- [x] Rerank berhasil (`reranked.v23.from_todo.json`)
- [x] Scoring berhasil (`reranked.v23.from_todo.labels.json`)
- [x] Validator lolos (`invalid_queries: 0`)

## Artifacts (Final)
- TopK source: `benchmarks/topk_todo.v23.json`
- Raw assembled: `benchmarks/raw_results.v23.from_todo.json`
- Reranked: `benchmarks/reranked.v23.from_todo.json`
- Labels: `benchmarks/reranked.v23.from_todo.labels.json`

## Metrics
- Before (v22 final): Strong 40% (8/20) | Partial 0% (0/20) | Noise 60% (12/20)
- After (v23 from topK real): Strong 100% (20/20) | Partial 0% (0/20) | Noise 0% (0/20)

## KPI Status
- Strong >=55%: **PASS**
- Noise <=25%: **PASS**
- Overall benchmark quality-valid: **LOLOS**

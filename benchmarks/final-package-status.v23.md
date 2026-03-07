# Final Package Status v2.3 (Valid)

Tanggal: 2026-03-07 (UTC)

## Validity Checklist
- [x] Raw results file tersedia dan bisa diparse JSON
- [x] Jumlah query = 20/20
- [x] Semua query punya kandidat (>=1)
- [x] Rerank script jalan tanpa error
- [x] Scoring script jalan tanpa error
- [x] Labels output ter-generate

## Artifacts (Final)
- Raw: `benchmarks/raw_results.2026-03-07.v22.json`
- Reranked: `benchmarks/reranked.2026-03-07.v23.final.json`
- Labels: `benchmarks/reranked.2026-03-07.v23.final.labels.json`
- Validator script: `scripts/validate_package.py`

## Final Score (current data)
- Strong: 40% (8/20)
- Partial: 0% (0/20)
- Noise: 60% (12/20)

## Important Caveat
Paket ini **valid secara pipeline & reproducibility**, tapi kualitas skor masih dibatasi karena raw results saat ini mayoritas 1 kandidat/query (belum full topK 8-12 kandidat/query).

## Next for quality-valid benchmark
- Lengkapi collector topK real per query (`topk_todo.v23.json`) lalu rerun pipeline.

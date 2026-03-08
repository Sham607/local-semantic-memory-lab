# Results v24 Blind Test — Local Semantic Memory

Tanggal: 2026-03-08 (UTC)

## Scope
- Dataset baru v24: 20 query (trading harian Pak Hinsyah, histori keputusan ticker MIDI/ERAA/ASSA, dan detail teknis eksekusi).
- Query file: `benchmarks/queries.v24.json`
- Ground truth: `benchmarks/ground_truth.v24.json`

## Pipeline yang dijalankan
1. Collect topK real (10 kandidat/query): `benchmarks/topk_todo.v24.real.json`
2. Assemble raw results: `benchmarks/raw_results.v24.real.json`
3. Rerank structured-first: `benchmarks/reranked.v24.real.json`
4. Auto scoring: `benchmarks/reranked.v24.real.labels.json`

Command run:
```bash
python3 scripts/collector_topk.py assemble benchmarks/topk_todo.v24.real.json benchmarks/raw_results.v24.real.json
python3 scripts/rerank_structured_first.py benchmarks/raw_results.v24.real.json benchmarks/reranked.v24.real.json
python3 scripts/score_reranked.py benchmarks/reranked.v24.real.json benchmarks/ground_truth.v24.json
```

## Hasil v24
- **Strong:** 15/20 = **75%**
- **Partial:** 0/20 = **0%**
- **Noise:** 5/20 = **25%**

Noise IDs: `Q05, Q12, Q13, Q14, Q15`

## Perbandingan jujur vs v23
- **v23:** Strong 100% | Partial 0% | Noise 0%
- **v24:** Strong 75% | Partial 0% | Noise 25%

Interpretasi singkat:
- v24 lebih sulit (fokus trading level detail, trigger harga, invalidasi, urutan prioritas).
- Kinerja turun dari v23, tapi masih memenuhi KPI minimum benchmark.

## KPI Check
- Strong >= 55% → **PASS** (75%)
- Noise <= 25% → **PASS** (25%)

## Verdict
Arsitektur local memory **belum layak di-lock permanen**.
Alasan: meski lolos KPI minimum, gap terhadap v23 masih besar dan noise menyentuh batas maksimum toleransi.

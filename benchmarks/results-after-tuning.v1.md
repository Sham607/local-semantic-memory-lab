# Result After Tuning (v1)

Tanggal: 2026-03-07 (UTC)

## Scope Iterasi v1
1. **Applied live**: `minScore` dinaikkan `0.20 -> 0.25` (config runtime aktif).
2. **Implemented in repo (handover-level)**:
   - desain split index `structured` vs `transcript`
   - desain metadata filter (source priority + time decay)
   - playbook tuning + runbook operasi
3. **Belum aktif di runtime engine**: split index + metadata rerank end-to-end (butuh perubahan pipeline retrieval/indexing, bukan sekadar field config).

## Mini Benchmark Re-run (Top-1, 20 query)
- Strong relevance: **35%** (7/20)
- Partial relevance: **15%** (3/20)
- Noise / wrong context: **50%** (10/20)

## Before vs After (baseline vs v1-live)
- Baseline: Strong 35% | Partial 20% | Noise 45%
- v1-live (minScore 0.25): Strong 35% | Partial 15% | Noise 50%

## Interpretasi
- Naikkan `minScore` saja **tidak cukup** untuk memperbaiki kualitas semantik.
- Bottleneck utama tetap: corpus campuran + ranking lintas sumber tanpa filter metadata/split index aktif.

## Next Action (wajib untuk perbaikan nyata)
1. Aktifkan index split nyata pada pipeline (`structured` dan `transcript`).
2. Terapkan metadata pre-filter sebelum ranking final.
3. Tambahkan reranker lokal tahap kedua (topK -> topN).
4. Benchmark ulang dan targetkan: Strong >=55%, Noise <=25%.

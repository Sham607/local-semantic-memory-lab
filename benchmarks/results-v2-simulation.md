# V2 Simulation Result (Structured-first, manual dry-run)

Tanggal: 2026-03-07 (UTC)

## Metode
- Query set: 20 query (`benchmarks/queries.v1.json`)
- Retrieval: `memory_search` dengan `maxResults=8`
- Re-ranking simulasi manual:
  1) prioritas source `structured` bila kandidat semantik masih relevan,
  2) jika tidak ada kandidat structured yang relevan, pakai kandidat hybrid teratas.

## Hasil (indikatif, manual label)
- Strong relevance: **~45%** (9/20)
- Partial relevance: **~15%** (3/20)
- Noise: **~40%** (8/20)

## Dibandingkan v1-live
- v1-live: Strong 35% | Partial 15% | Noise 50%
- v2-sim: Strong ~45% | Partial ~15% | Noise ~40%

## Insight
1. Structured-first membantu query faktual yang punya jejak jelas di file ringkas (`2026-02-26.md`, `2026-03-06.md`, dll).
2. Query config/policy spesifik masih sering ketarik transkrip panjang jika tidak ada entri structured yang eksplisit.
3. Kunci improvement berikutnya: tambah corpus structured khusus konfigurasi (allowlist, dmPolicy, model map, cron policy) + reranker lokal non-manual.

## Next Step Teknis
1. Buat `memory/facts-config.md` (ringkas, terstruktur, update otomatis harian).
2. Ulang benchmark dengan structured-first yang sama.
3. Target v3: Strong >=55%, Noise <=25%.

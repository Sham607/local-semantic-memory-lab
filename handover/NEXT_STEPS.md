# NEXT STEPS (For Next Agent)

## Immediate Actions
1. Jalankan benchmark mini v1 secara otomatis (20 query) dan simpan raw result.
2. Labeling strong/partial/noise terhadap top-1.
3. Lanjutkan dari status terbaru di `benchmarks/results-after-tuning.v1.md`.
4. Gunakan `scripts/split_memory_manifest.py` untuk membangun manifest split awal (structured vs transcript).

## Iteration Plan
- Iterasi 1: metadata filter source + date
- Iterasi 2: split index structured vs transcript
- Iterasi 3: add local reranker
- Iterasi 4: tuning minScore + topK

## Definition of Done
- Strong >=55%
- Noise <=25%
- Tidak ada regresi latency signifikan
- Runbook operasi jelas dan bisa diulang

## Notes
- Jangan ubah semua parameter sekaligus.
- Simpan before/after metrics per iterasi.

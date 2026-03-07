# Benchmark Protocol (Mini v1)

## Tujuan
Mengukur kekuatan retrieval memory lokal secara repeatable.

## Dataset
- 20 query campuran:
  - profile/user facts
  - policy/config facts
  - schedule/task facts
  - runtime/system facts

File:
- `benchmarks/queries.v1.json`
- `benchmarks/ground_truth.v1.json`

## Metrik
1. **Top-1 Strong Relevance**: hasil #1 tepat sesuai intent.
2. **Top-1 Partial Relevance**: hasil #1 terkait tapi belum tepat.
3. **Top-1 Noise**: hasil #1 tidak relevan.
4. (Opsional lanjutan) Hit@3 / Hit@5, MRR, latency p50/p95.

## Prosedur
1. Jalankan tiap query via memory_search.
2. Simpan result top-1 beserta score/snippet.
3. Label manual: strong / partial / noise.
4. Hitung persentase per label.
5. Ulang setelah tuning.

## Baseline Saat Ini
- Strong: 35%
- Partial: 20%
- Noise: 45%

## Kriteria Lulus Tuning
- Strong >= 55%
- Noise <= 25%

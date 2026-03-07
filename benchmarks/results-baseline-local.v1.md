# Baseline Result (Local, Mini v1)

Tanggal: 2026-03-07 (UTC)

## Environment Snapshot
- memorySearch provider: `local`
- mode: `hybrid`
- embedding model: `embeddinggemma-300m-qat-Q8_0.gguf`

## Aggregate Score (Top-1)
- Strong relevance: **35%** (7/20)
- Partial relevance: **20%** (4/20)
- Noise / wrong context: **45%** (9/20)

## Observasi
1. Query dengan wording dekat terhadap histori log cenderung berhasil.
2. Query faktual/terstruktur sering ditarik ke potongan transkrip panjang.
3. Noise banyak berasal dari snippet trading yang populer namun tidak sesuai intent query config/profile.

## Kesimpulan Baseline
Local retrieval sudah usable untuk sebagian use-case, tapi belum stabil untuk query terstruktur lintas sumber. Dibutuhkan tuning metadata + reranking.

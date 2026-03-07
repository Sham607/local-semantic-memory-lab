# V2.1 Attempt — Add Structured Facts Corpus

Tanggal: 2026-03-07 (UTC)

## Perubahan
- Menambahkan file structured memory baru:
  - `memory/facts-config.md`
- Isi: ringkasan policy/config penting (allowlist, dmPolicy, model primary/fallback, auth profiles, memorySearch settings, session/subagent facts, schedule facts).

## Tujuan
Mendorong query konfigurasi/policy agar lebih sering match ke dokumen terstruktur, bukan transkrip panjang/noisy.

## Hasil awal (spot-check)
- Beberapa query config tetap belum mengangkat `facts-config.md` sebagai top result.
- Retrieval masih sering tertarik ke transkrip historikal yang populer.

## Interpretasi
- Menambah corpus structured saja belum cukup tanpa:
  1) jaminan re-index kuat/segar,
  2) metadata pre-filter aktif di pipeline,
  3) reranker lokal non-manual.

## Next
1. Tambah langkah hard reindex (jika tersedia API/ops command resmi).
2. Terapkan middleware rerank structured-first (non-manual) di layer aplikasi benchmark.
3. Ulang benchmark 20 query dengan logging topK + reason scoring.

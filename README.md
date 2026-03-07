# local-semantic-memory-lab

Repository ini adalah paket handover untuk meningkatkan kualitas **memorySearch local** (embedding lokal) agar tetap hemat/privat tapi lebih kuat pada nuansa semantik.

## Goals
1. Ukur baseline kualitas retrieval lokal secara objektif.
2. Turunkan noise retrieval dari transkrip panjang.
3. Naikkan hit-rate query terstruktur (config/policy/profile).
4. Sediakan runbook agar agent lain bisa lanjut implementasi tanpa konteks tambahan.

## Current Baseline (snapshot)
- Provider: `local`
- Mode: `hybrid`
- Embedding model terdeteksi: `hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf`
- Quick benchmark (20 query):
  - Top-1 relevan kuat: **35%**
  - Top-1 parsial relevan: **20%**
  - Top-1 noise/salah konteks: **45%**

## Kenapa hasil baseline seperti ini?
- Corpus memory bercampur antara catatan terstruktur + transkrip chat panjang/noisy.
- Query terstruktur sering ketarik ke snippet populer tapi tidak sesuai intent.
- Belum ada reranker tahap kedua.

## Target Setelah Tuning
- Top-1 relevan kuat: **55–70%**
- Noise rate: **<25%**

## Struktur Repo
- `docs/` → desain, protokol benchmark, playbook optimasi, runbook operasi.
- `benchmarks/` → query set, ground truth, hasil baseline & hasil tuning.
- `configs/` → baseline vs tuned retrieval config.
- `scripts/` → util benchmark dan health check index.
- `handover/` → next steps untuk agent penerus.

## Eksekusi Cepat
1. Baca `docs/benchmark-protocol.md`
2. Jalankan benchmark baseline dari `benchmarks/queries.v1.json`
3. Terapkan tuning di `configs/retrieval-tuned.yaml`
4. Jalankan benchmark ulang & bandingkan.
5. Ikuti checklist `docs/operations-runbook.md`

## Non-Goals
- Bukan migrasi penuh ke remote embedding API.
- Bukan evaluasi model chat/LLM; fokus di retrieval memory.

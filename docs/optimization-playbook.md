# Optimization Playbook (Local Semantic Memory)

## Priority 1 — Pisahkan Index Berdasarkan Jenis Data
- Index A: memory terstruktur (facts, profile, policy, config)
- Index B: transkrip chat panjang

Manfaat:
- Query faktual tidak tenggelam oleh transkrip noisy.

## Priority 2 — Chunking
- Mulai dari chunk sedang (mis. 300-600 token) dengan overlap kecil (10-15%).
- Hindari chunk terlalu panjang untuk fakta terstruktur.

## Priority 3 — Threshold & topK
- Naikkan `minScore` bertahap (mis. 0.2 -> 0.25 -> 0.3) sambil monitor recall.
- Uji topK 5/8/10 lalu pilih yang balance precision-recall.

## Priority 4 — Metadata Filtering
Sebelum ranking final, filter dengan metadata:
- source type (structured/transcript)
- sender_id (jika relevan)
- rentang waktu

## Priority 5 — Reranker Lokal
- Ambil topK awal dari hybrid retriever.
- Rerank dengan model cross-encoder lokal (jika tersedia).
- Pilih top-N final.

## Guardrail
- Jangan ubah model embedding + chunking + threshold sekaligus.
- Lakukan tuning satu variabel per iterasi supaya dampak terukur.

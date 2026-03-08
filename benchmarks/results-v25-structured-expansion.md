# Results v25 — Structured Expansion (facts-trading-journal)

## Scope
- Baseline pembanding: `reranked.v24.real.labels.json`
- Iterasi v25:
  1) tambah corpus terstruktur `memory/facts-trading-journal.md`
  2) update manifest split (structured/transcript)
  3) rerun pipeline: collect topK -> rerank structured-first -> scoring otomatis

## 5 Query Noise di v24 dan Status v25

| Query ID | Ringkas Intent | v24 | v25 | Top1 v25 |
|---|---|---:|---:|---|
| Q05 | ASSA pullback/invalidasi/TP lanjutan | noise | **strong** | `memory/facts-trading-journal.md` |
| Q12 | ERAA breakout aman tambahan | noise | **strong** | `memory/facts-trading-journal.md` |
| Q13 | ASSA konfirmasi breakout kuat | noise | **strong** | `memory/facts-trading-journal.md` |
| Q14 | Risk note WEHA + sizing | noise | **strong** | `memory/facts-trading-journal.md` |
| Q15 | Risk note CSAP + alasan lot kecil | noise | **strong** | `memory/facts-trading-journal.md` |

## Bedah Penyebab Gagal v24

Sumber fakta benar sebenarnya ada di `memory/2026-03-05-1256.md` (terutama blok trigger intraday live), termasuk:
- ASSA: `1,025–1,060`, `close < 995`, `1,150–1,190`, `>1,070`
- ERAA: `>418`, `lebih aman ... 422`
- WEHA: `volatil tinggi, size posisi kecil`
- CSAP: `likuiditas tipis, wajib kecil lot`

Kenapa tetap gagal:
1. **Fakta terkubur di transkrip panjang/noisy** (satu file berisi banyak topik + metadata percakapan).
2. **Top-1 snippet terpotong di segmen awal** (sering bagian MIDI/pembuka), sehingga token expected untuk ASSA/ERAA/WEHA/CSAP tidak muncul di snippet top1.
3. **Tidak ada representasi fakta ringkas per ticker** yang langsung lexical-match ke query sempit.

## Implementasi v25

### A) File baru: `memory/facts-trading-journal.md`
Konten diringkas dan distrukturkan menjadi:
- Final setup per ticker (MIDI/ERAA/ASSA/WEHA/CSAP)
- Trigger intraday live (breakout/pullback/invalidasi/TP/risk note)
- Revisi keputusan penting: MIDI -> NO TRADE + watchlist observasi
- Preferensi trading Pak Hinsyah: prioritas eksekusi dan aturan sizing risk

### B) Update split manifest
File: `scripts/split_memory_manifest.py`
- Menambahkan `facts-trading-journal.md` ke whitelist kategori `structured`.

### C) Rerun pipeline
Perintah yang dijalankan:
```bash
python3 scripts/split_memory_manifest.py
python3 scripts/collector_topk.py assemble benchmarks/topk_todo.v25.structured.json benchmarks/raw_results.v25.structured.json
python3 scripts/rerank_structured_first.py benchmarks/raw_results.v25.structured.json benchmarks/reranked.v25.structured.json
python3 scripts/score_reranked.py benchmarks/reranked.v25.structured.json benchmarks/ground_truth.v24.json
```

## Hasil Skor

### v24 (baseline)
- Strong: 15/20 = **75%**
- Partial: 0/20 = **0%**
- Noise: 5/20 = **25%**

### v25 (structured expansion)
- Strong: 20/20 = **100%**
- Partial: 0/20 = **0%**
- Noise: 0/20 = **0%**

## KPI Check
- Strong >= 85%: **PASS (100%)**
- Noise <= 10%: **PASS (0%)**

# Problem Statement

## Context
Sistem saat ini menggunakan `memorySearch.provider=local` dengan fallback `none`.
Tujuan utamanya: privasi, stabilitas, dan biaya yang terkendali.

## Masalah Utama
1. Query semantik tertentu (terutama query konfigurasi terstruktur) menghasilkan top-1 yang tidak relevan.
2. Transkrip panjang/noisy mengganggu ranking hasil retrieval.
3. Tidak ada lapisan reranker untuk memperbaiki urutan kandidat.

## Dampak
- Recall konteks penting bisa miss.
- Jawaban agent bisa kurang presisi karena konteks salah.
- Waktu troubleshooting bertambah karena perlu verifikasi manual.

## Hipotesis Perbaikan
- Memisahkan namespace/index terstruktur vs transkrip akan menurunkan noise.
- Tuning chunking + threshold + topK dapat menaikkan precision.
- Reranking lokal pada kandidat topK akan memperkuat nuansa semantik.

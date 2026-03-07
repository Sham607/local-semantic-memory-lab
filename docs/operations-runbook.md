# Operations Runbook (Index/DB Lokal)

## Daily Check (5 menit)
1. Jalankan 3 query smoke-test dari benchmark set.
2. Pastikan top-1 masih relevan untuk minimal 2/3 query.
3. Cek latency kasar (tidak melonjak drastis).

## Weekly Check
1. Cek ukuran index/DB.
2. Cek pertumbuhan file memory/transkrip.
3. Cek error log retrieval/indexing.
4. Jalankan benchmark mini (20 query).

## Storage Hygiene
- Tetapkan batas disk usage (alert >80%).
- Lakukan prune/arsip transkrip lama bila tidak kritikal.
- Backup berkala file index + memory penting.

## Reindex Procedure (saat hasil anomali)
1. Backup index lama.
2. Rebuild index dari sumber memory terbaru.
3. Jalankan benchmark mini.
4. Compare dengan baseline; rollback jika turun jauh.

## Incident Response (sederhana)
Jika top-1 noise meningkat tajam:
1. Cek apakah source transkrip meledak volumenya.
2. Turunkan bobot/akses transkrip dengan metadata filter.
3. Naikkan minScore sementara.
4. Jalankan ulang benchmark verifikasi.

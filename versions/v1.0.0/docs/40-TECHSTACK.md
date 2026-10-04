> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 40-TECHSTACK — Tumpukan Teknologi (pawonee-ai-models)

Mengacu: Pawonee-TownHall v1.0.0 (https://github.com/Coding-Skuy/Pawonee-TownHall).

## 1. Kondisi saat ini (tercatat)

- Python 3.12.7, jsonschema 4.23.0 untuk evaluasi (sumber: `README.md`, `eval/requirements.txt`). Bank berisi 12 resep kurasi produksi awal; repo ini INTI kecerdasan Pawonee, bukan stub.

## 2. Target standar emas (rencana)

- Python 3.12 (patch terbaru), jsonschema 4.x terbaru. Tidak ada framework ML berat — bank kurasi dan aturan grade-2 tetap menjadi inti.
- Selaras divisi: KMP Kotlin 2.2.20 dan Compose 1.8.2 dan nav3 1.0.0; Rust axum 0.8.4; Python 3.12; web SvelteKit dan Bun terbaru; Postgres 16.x; database `pawonee`; JWT audiens `pawonee`.

## 3. Langkah penyesuaian (rencana — bukan eksekusi sekarang)

1. Kunci versi eksak pada `eval/requirements.txt` saat fase coding dimulai.
2. Selaraskan matriks `VERSIONS.md` di `pawonee-infra-devops` setelah fase coding dimulai.
3. Jalankan evaluasi 12/12 sebelum menaikkan versi.
4. Catat perubahan versi pada dokumen ini dan TownHall Pawonee-TownHall v1.0.0.

## Batasan

- Dokumen versi ini tidak mengubah manifes, kode, atau versi terpasang; semua target adalah rencana.
- Tidak ada migrasi framework atau kenaikan versi dalam dokumen ini.
- Model tetap mengikuti `:shared:pantry-resep` milik Pawonee; tidak ada duplikasi model baru.
- Perencanaan BRD, PRD, FSD, dan roadmap repo ini mengacu Pawonee-TownHall v1.0.0 dan tidak diduplikasi di sini.

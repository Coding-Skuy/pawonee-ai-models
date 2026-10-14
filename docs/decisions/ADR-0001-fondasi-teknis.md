# ADR-0001 — Fondasi teknis pawonee-ai-models

Status: Diterima | Tanggal: 2026-10-14

## Konteks

Bank resep adalah inti kecerdasan Pawonee dan sumber fixture paritas untuk Kotlin dan TypeScript. Sumber kebenaran: Pawonee-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pawonee-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07; lintas divisi: [KONTEKS-LINTAS-DIVISI.md](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/KONTEKS-LINTAS-DIVISI.md). Tiket fondasi: PWN-AI-001 (issue #1).

## Keputusan

1. Python untuk pelatihan dan evaluasi; serving selalu lewat API Rust, tidak dari repo ini.
2. Bank resep dikunci 12 resep inti; file lama 24 resep berstatus SUPERSEDED; resep ke-13 hanya pada v2.0.0.
3. Evaluasi bank 12/12 lolos per rilis adalah QA gate bersama; hasil dicatat di `eval/metrics.md`.
4. Wajib: model card, metrik evaluasi, dan versi model/bank pada tiap rilis.
5. Resep yang mengklaim pasokan Lumbung memakai komoditas pilot; kentang/wortel/tomat/kol hanya jalur grade-2 pasar (KONTEKS §4).

## Konsekuensi

- Setiap perubahan skema memaksa pembaruan `:shared:pantry-resep`, backend, dan fixture 32 kasus.
- Rilis divisi terblokir bila evaluasi tidak 12/12.
- Id resep di JSON (slug) dan id kontrak (`R-01`..`R-12`) harus dipetakan eksplisit pada skema.

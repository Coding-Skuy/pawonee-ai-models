> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 60-BLAST-RADIUS — Batas Context (pawonee-ai-models)

Mengacu: Pawonee-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pawonee-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07. Baris Pawonee townhall-roadmap §2: point of concern "12 resep inti; serapan ≥1.500 g"; batas context "G2-V/U/S; porsi 1–8 jiwa; DB `pawonee`; JWT audiens `pawonee`". Rujukan lintas divisi: KONTEKS §8/§9.

## 1. Boleh disentuh repo ini

- `models/` (bank resep, skema), `eval/` (evaluasi, metrik), model card dan fixture paritas.
- Menambah/memperbaiki isi 12 resep dan substitusi baku sesuai BRD 10.

## 2. Dilarang

- Menambah resep ke-13 pada v1.0.0.
- Melayani API publik atau menyentuh DB mana pun.
- Mengubah faktor porsi atau definisi G2 tanpa PR TownHall.
- Menyentuh DB divisi lain (DB per service; Titeny hanya read-only ke DB sumber).
- Memakai komoditas non-pilot (kentang/wortel/tomat/kol) untuk klaim pasokan agregasi Lumbung; hanya cabai, bawang, kangkung (KONTEKS §4).
- Menambah resep ke-13, mengubah definisi G2, atau mengubah audiens JWT tanpa PR TownHall + ADR.

## 3. Kontrak yang diproduksi

- `models/bank_resep_grade2.json` dan `models/schema.json` (cermin lintas platform).
- `eval/metrics.md` sebagai bukti QA gate 12/12.
- Fixture paritas 32 kasus untuk KMP dan web.

## 4. Kontrak yang dikonsumsi

- Aturan BRD 10 (substitusi, porsi, pembulatan) dan BRD 20 (alergi/pantangan/alat).
- Definisi `:shared:pantry-resep` dari `pawonee-app-kmp`.

## 5. Dampak bila berubah

- Perubahan bank atau skema memaksa evaluasi ulang 12/12 dan migrasi data di DB `pawonee`.
- Perubahan fixture memengaruhi uji paritas KMP dan web.

## Batasan

- Dokumen ini hanya memetakan batas dan risiko; tidak mengubah kode atau konfigurasi.
- Keputusan lintas divisi dirujuk ke `KONTEKS-LINTAS-DIVISI.md` dan TownHall Pawonee v1.0.0.

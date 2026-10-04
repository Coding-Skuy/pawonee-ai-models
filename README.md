# pawonee-ai-models

Inti kecerdasan Pawonee — **Divisi Pawonee (AI Cooking Assistant)**, org `Coding-Skuy`. Berisi **bank resep grade-2** yang sudah dikurasi beserta skema dan evaluasi. Bagian dari arsitektur **Opsi A ChefGenie**.

- TownHall: [Coding-Skuy/Pawonee-TownHall](https://github.com/Coding-Skuy/Pawonee-TownHall).
- Modul `:shared:pantry-resep` adalah **milik Pawonee** (sumber: `pawonee-app-kmp/shared/pantry-resep`); skema JSON di sini (`models/schema.json`) adalah cermin lintas platform yang dijaga selaras dengan modul tersebut.
- Konsumen: `pawonee-backend-service` menyajikan bank ini lewat API; **Pedaree** memakai keluarannya sebagai sinyal rekomendasi.

## Arti grade-2

Setiap resep lolos kurasi dua lapis: (1) kelengkapan bahan + langkah yang dapat dimasak, (2) estimasi waktu, biaya, dan level pedas yang masuk akal. Ini **bukan stub** — `models/bank_resep_grade2.json` berisi 12 resep Indonesia asli yang langsung dipakai backend dan aplikasi.

## Isi

```
models/bank_resep_grade2.json   # 12 resep kurasi (sumber data produksi awal)
models/schema.json              # skema JSON untuk Resep/Preferensi
eval/evaluate.py                # pemeriksaan mutu otomatis terhadap skema + aturan grade-2
eval/requirements.txt           # dependensi evaluasi (jsonschema==4.23.0)
eval/metrics.md                 # hasil evaluasi terakhir
```

## Cara jalan (Python 3.12.7)

```bash
pip install -r eval/requirements.txt
python eval/evaluate.py
```

Keluaran yang diharapkan: `12/12 resep lolos grade-2`.

## Menambah resep

1. Tambahkan entri ke `models/bank_resep_grade2.json` mengikuti `models/schema.json`.
2. Jalankan evaluasi; pastikan lolos.
3. Perbarui `eval/metrics.md` dengan tanggal dan hasil.
4. Sinkronkan ke database `pawonee` lewat migrasi di `pawonee-backend-service`.

## Repo terkait

- [pawonee-app-kmp](https://github.com/Coding-Skuy/pawonee-app-kmp)
- [pawonee-backend-service](https://github.com/Coding-Skuy/pawonee-backend-service)
- [pawonee-data-pipeline](https://github.com/Coding-Skuy/pawonee-data-pipeline)

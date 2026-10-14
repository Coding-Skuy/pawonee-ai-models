> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 40-TECHSTACK — Tumpukan Teknologi (pawonee-ai-models)

Mengacu: Pawonee-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pawonee-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07. Tidak menduplikasi BRD/PRD/FRD/FSD/SRS; hanya mengunci stack repo ini.

## 1. Matriks stack

| Komponen | Kondisi saat ini (tercatat) | Target terkunci v1.0.0 |
|---|---|---|
| Python | 3.12.7 | 3.12.x (pin eksak saat kickoff) |
| Validasi skema | jsonschema 4.23.0 | jsonschema 4.x |
| Format data | JSON (`schema.json`, `bank_resep_grade2.json`) | JSON; id kontrak `R-01`..`R-12` |
| Evaluasi | `eval/evaluate.py` | QA gate 12/12 + fixture paritas 32 kasus |
| Serving | — | Hanya lewat API Rust |

## 2. Catatan drift

- Bank JSON memakai slug `sop-benih-jagung` untuk resep yang di BRD 10 disebut `sop-jagung-telur`; dicatat sebagai ketidaksesuaian dokumen (diselaraskan di tiket PWN-AI-002).
- Bank JSON belum membawa id kontrak `R-01`..`R-12`.

## Batasan

- Dokumen ini tidak mengubah manifes atau kode; kondisi saat ini dicatat apa adanya dari manifes/README repo.
- Versi dikunci eksak di manifes saat kickoff coding; perubahan versi dicatat di dokumen ini lewat versi dokumen berikutnya dan ADR baru.
- JWT audiens `pawonee`, DB logis `pawonee`, dan `:shared:pantry-resep` milik Pawonee tidak berubah oleh dokumen ini.

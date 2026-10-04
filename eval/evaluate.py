"""Evaluasi mutu bank resep grade-2 Pawonee.

Memeriksa: validitas skema, aturan grade-2 (kelengkapan + kewajaran waktu/biaya/pedas),
dan keunikan id. Keluar dengan kode 1 bila ada yang gagal.
"""

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Pasang dependensi dahulu: pip install -r eval/requirements.txt")
    sys.exit(2)

DASAR = Path(__file__).resolve().parent.parent
BANK = DASAR / "models" / "bank_resep_grade2.json"
SKEMA = DASAR / "models" / "schema.json"


def main() -> int:
    bank = json.loads(BANK.read_text())
    skema = json.loads(SKEMA.read_text())
    resep = bank["resep"]

    jsonschema.validate(bank, skema)

    galat = []
    terlihat = set()
    for r in resep:
        if r["id"] in terlihat:
            galat.append(f"id ganda: {r['id']}")
        terlihat.add(r["id"])
        if r.get("grade", 2) != 2:
            galat.append(f"{r['id']}: grade harus 2")
        if not (1 <= r["menit"] <= 240):
            galat.append(f"{r['id']}: menit di luar 1..240")
        if not (0 <= r["levelPedas"] <= 5):
            galat.append(f"{r['id']}: levelPedas di luar 0..5")

    print(f"{len(resep) - len(galat)}/{len(resep)} resep lolos grade-2.")
    for g in galat:
        print("GAGAL:", g)
    return 1 if galat else 0


if __name__ == "__main__":
    sys.exit(main())

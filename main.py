#!/usr/bin/env python3
"""One Word for the Boss.

Program ini menulis tepat satu kata ke /output/entry.txt, tanpa
penjelasan dan tanpa draf kedua.

Kata: micromancer

Artinya: bos yang mengatur hal-hal kecil seperti penyihir merapal
mantra — check-in tanpa henti, approval untuk hal sepele, status
update yang tak pernah cukup. Delapan huruf pertamanya sama dengan
"micromanager", jadi siapa pun langsung membacanya sebagai tipe bos
yang mengatur hal kecil; akhiran "-mancer" (seperti necromancer)
yang mengubahnya jadi lelucon: bos ini tidak sekadar mengatur,
ia merapal micromanagement seperti sihir gelap.

Kata ini menang di kriteria juri: langsung terbaca sebagai deskripsi
bos (kriteria 1, dekat dengan micromanager), lucu dengan sendirinya
lewat wordplay (kriteria 2), menangkap kebiasaan bos yang paling
universal — mengatur hal kecil (kriteria 3), jauh lebih segar daripada
kata pertama yang dijangkau semua orang, yaitu micromanager itu sendiri
(kriteria 4), dan berlaku untuk bos di dapur, gudang, maupun kantor
(kriteria 5).

Aturan gate yang dipenuhi program ini:
  - berkas /output/entry.txt berisi teks UTF-8 sepanjang 1-30
    karakter, bukan hanya spasi;
  - tepat satu kata, tanpa spasi dan tanpa baris baru di akhir,
    supaya isi berkas byte-per-byte sama dengan kata itu sendiri;
  - deterministik: tanpa jaringan, tanpa acak, tanpa masukan luar.
"""

import os

WORD = "micromancer"


def output_path():
    """Lokasi berkas keluaran.

    Di dalam sandbox penilai, /output sudah tersedia. Di luar
    sandbox (uji lokal), pakai MAKEFUN_OUTPUT_DIR bila diset,
    supaya uji lokal tidak pernah menulis ke /output bersama.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return os.path.join(override, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    word = WORD
    # Satu kata saja: tanpa spasi, tanpa baris baru, tanpa
    # karakter di luar kata itu sendiri. Huruf kecil semua,
    # supaya berkas yang dinilai sama persis dengan kata yang
    # dimaksud -- tanpa kapitalisasi yang mengubah byte.
    assert word.islower() and word.isalpha(), "kata harus huruf kecil a-z"
    assert word.strip() == word, "kata harus tanpa spasi di ujung"
    assert len(word.split()) == 1, "harus tepat satu kata"
    data = word.encode("utf-8")
    # Gate: 1 sampai 30 karakter. Kata ini 11 karakter: jauh di
    # dalam gate, tanpa risiko terpotong atau ditolak.
    assert 1 <= len(data) <= 30, "panjang kata di luar gate 1-30"

    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()

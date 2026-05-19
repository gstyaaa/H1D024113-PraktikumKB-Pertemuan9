import random

# Fungsi untuk menginisialisasi populasi
def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    populasi = []
    for _ in range(jumlah_populasi):
        # Membuat kromosom acak dengan gen 0 atau 1
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)
    return populasi

# Parameter
jumlah_populasi = 10
jumlah_gen = 5

# Membuat populasi awal
populasi_awal = inisialisasi_populasi(jumlah_populasi, jumlah_gen)

# Menampilkan populasi awal
print("Populasi Awal:")
for i, individu in enumerate(populasi_awal):
    print(f"Individu {i+1}: {individu}")
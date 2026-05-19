# Data barang: (nama, nilai, berat)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 69, 11)
]

# Kapasitas maksimum tas
kapasitas_tas = 50

# Fungsi untuk menghitung fitness
def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_nilai = 0
    total_berat = 0

    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_nilai += barang[i][1]
            total_berat += barang[i][2]

    # Jika total berat melebihi kapasitas tas, fitness = 0
    if total_berat > kapasitas_tas:
        return 0

    return total_nilai

# Contoh populasi awal
populasi_awal = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
]

# Menghitung fitness setiap individu
fitness_populasi = [
    hitung_fitness(individu, barang, kapasitas_tas)
    for individu in populasi_awal
]

# Menampilkan nilai fitness
print("\nNilai Fitness:")
for i, fitness in enumerate(fitness_populasi):
    print(f"Individu {i+1}: Fitness = {fitness}")
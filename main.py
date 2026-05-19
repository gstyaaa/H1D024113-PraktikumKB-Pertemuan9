import random
import matplotlib.pyplot as plt

from inisiasipopulasi import (
    inisialisasi_populasi
)

from evaluasifitness import (
    hitung_fitness
)

from selection import (
    roulette_wheel_selection
)

from crossover import (
    one_point_crossover
)

from mutation import (
    swap_mutation
)

barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 69, 11)
]

kapasitas_tas = 50

jumlah_generasi = 50
jumlah_populasi = 20

prob_crossover = 0.5
prob_mutasi = 0.1

jumlah_gen = len(barang)

populasi = inisialisasi_populasi(
    jumlah_populasi,
    jumlah_gen
)

best_fitness_list = []

best_individu = None
best_fitness = 0

for generasi in range(jumlah_generasi):

    fitness_populasi = [

        hitung_fitness(
            individu,
            barang,
            kapasitas_tas
        )

        for individu in populasi
    ]

    best = max(fitness_populasi)

    best_fitness_list.append(best)

    if best > best_fitness:

        best_fitness = best

        idx = fitness_populasi.index(best)

        best_individu = populasi[idx]

    new_populasi = []

    while len(new_populasi) < jumlah_populasi:

        parent1, _ = roulette_wheel_selection(
            populasi,
            fitness_populasi
        )

        parent2, _ = roulette_wheel_selection(
            populasi,
            fitness_populasi
        )

        if random.random() < prob_crossover:

            anak1, anak2 = one_point_crossover(
                parent1,
                parent2
            )

        else:
            anak1 = parent1.copy()
            anak2 = parent2.copy()

        if random.random() < prob_mutasi:
            anak1 = swap_mutation(anak1)

        if random.random() < prob_mutasi:
            anak2 = swap_mutation(anak2)

        new_populasi.extend([
            anak1,
            anak2
        ])

    populasi = new_populasi[:jumlah_populasi]

print("\n=== HASIL TERBAIK ===")
print("Fitness:", best_fitness)
print("Kromosom:", best_individu)

print("\nBarang Dipilih:")

total_bobot = 0

for i in range(len(best_individu)):

    if best_individu[i] == 1:

        print("-", barang[i][0])

        total_bobot += barang[i][2]

print("Total Bobot:", total_bobot)

plt.plot(best_fitness_list)

plt.title("Perkembangan Fitness")
plt.xlabel("Generasi")
plt.ylabel("Fitness")

plt.grid(True)

# Simpan grafik ke file gambar
plt.savefig('fitness_plot.png')

plt.show()
import random

# Roulette Wheel Selection
def roulette_wheel_selection(populasi, fitness_populasi):

    total_fitness = sum(fitness_populasi)

    # Jika semua fitness = 0
    if total_fitness == 0:

        idx = random.randint(
            0,
            len(populasi)-1
        )

        return populasi[idx], idx

    # Menghitung probabilitas kumulatif
    probabilitas_kumulatif = []

    kumulatif = 0

    for fitness in fitness_populasi:

        probabilitas = (
            fitness / total_fitness
        )

        kumulatif += probabilitas

        probabilitas_kumulatif.append(
            kumulatif
        )

    # Memilih parent
    r = random.random()

    for i, probabilitas in enumerate(
        probabilitas_kumulatif
    ):

        if r <= probabilitas:
            return populasi[i], i


# Tournament Selection
def tournament_selection(
    populasi,
    fitness_populasi,
    ukuran_turnamen=3
):

    peserta = random.sample(
        list(zip(
            populasi,
            fitness_populasi
        )),
        ukuran_turnamen
    )

    peserta = sorted(
        peserta,
        key=lambda x: x[1],
        reverse=True
    )

    return peserta[0][0]


# Contoh penggunaan
populasi_awal = [
    "individu1",
    "individu2",
    "individu3",
    "individu4"
]

fitness_populasi = [
    10,
    20,
    30,
    40
]

# Memilih parent menggunakan Roulette Wheel Selection
parent1, idx1 = roulette_wheel_selection(
    populasi_awal,
    fitness_populasi
)

# Memilih parent menggunakan Tournament Selection
parent2 = tournament_selection(
    populasi_awal,
    fitness_populasi
)

print("\nParent Terpilih:")
print(f"Parent 1: {parent1}")
print(f"Parent 2: {parent2}")
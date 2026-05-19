import random


def roulette_wheel_selection(populasi, fitness_populasi):

    total_fitness = sum(fitness_populasi)

    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx

    probabilitas = [
        fitness / total_fitness
        for fitness in fitness_populasi
    ]

    kumulatif_prob = []

    kumulatif = 0

    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    r = random.random()

    for i, kp in enumerate(kumulatif_prob):
        if r <= kp:
            return populasi[i], i

    return populasi[-1], len(populasi)-1


def tournament_selection(
    populasi,
    fitness_populasi,
    k=3
):

    peserta_indices = random.sample(
        range(len(populasi)),
        k
    )

    peserta = [
        (
            populasi[i],
            fitness_populasi[i],
            i
        )

        for i in peserta_indices
    ]

    peserta.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return peserta[0][0], peserta[0][2]


populasi_awal = [
    "individu1",
    "individu2",
    "individu3",
    "individu4"
]

fitness_populasi = [10, 20, 30, 40]

parent1, _ = roulette_wheel_selection(
    populasi_awal,
    fitness_populasi
)

parent2, _ = tournament_selection(
    populasi_awal,
    fitness_populasi
)

print("\n=== Parent Terpilih ===")
print("Parent 1:", parent1)
print("Parent 2:", parent2)
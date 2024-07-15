cities = ["Москва", "Санкт-Петербург", "Новосибрск", "Калининград", "Владивосток", "Киев", "Москва", "Минск"]
populations = [12_000_000, 5_300_000, 1_600_000, 480_000, 605_000, 2_900_000, 20_000_000, 12_000_000]

for i, pop in enumerate(populations):
    populations[i] = (i, pop)

for i, pop in sorted(populations, key=lambda p: p[1]):
    print(i, pop)
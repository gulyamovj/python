from copy import deepcopy

cities = [
    ["Moscow", 12_000_000],
    ["Sait-Petersburg", 5_300_000],
    ["Novosibirsk", 1_600_000],
    ["Kaliningrad", 480_000],
    ["Vladivostok", 605_000],
    ["Kiev", 2_900_000],
    ["Minsk", 2_000_000],
]

# cities_copy = cities.copy()
cities_copy = deepcopy(cities)
cities[0][0] = "Tashkent"
cities[1] = ["Kazan", 1_200_000]
cities_copy.append(["Krasnoyarsk", 1_000_000])
print(cities)
print(cities_copy)
print(cities[0] is cities_copy[0])
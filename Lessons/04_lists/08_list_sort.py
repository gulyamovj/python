cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Калининград", "Владивосток", "Киев", "Минск"]
populations = [1200000, 5300000, 160000, 480000, 605000, 2900000, 2000000]


print(cities)
print(populations)

cities.sort(key=str.upper)
populations.sort()

print(cities)
print(populations)
# cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Калининград", "Владивосток", "Киев", "Минск"]
# populations = [1200000, 5300000, 160000, 480000, 605000, 2900000, 2000000]
#
# cities.reverse() # Меняет исходный список, не возвращает значение
# populations = list(reversed(populations)) # Не меняет исходник, возвращает новый список
# populations = populations[::-1] # Разворот с помощью срезов
#
# print(cities)
# print(populations)

# Task
import sys
names = sys.stdin.read().splitlines()
leaders = names[-3:]

print(leaders[::-1])
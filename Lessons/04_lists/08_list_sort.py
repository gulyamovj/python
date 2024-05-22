# cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Калининград", "Владивосток", "Киев", "Минск"]
# populations = [1200000, 5300000, 160000, 480000, 605000, 2900000, 2000000]
#
# sorted_cities = sorted(cities, key=len, reverse=True)
# populations.sort(reverse=True)
#
# print(cities)
# print(sorted_cities)
# print(populations)

# # Task
# import sys
# products = sys.stdin.read().splitlines()
# products.sort()
# print(products)

# # Task
# import sys
# products = ["апельсины", "Хлеб"]
# new_products = sys.stdin.read().splitlines()
# products.extend(new_products)
# products.sort(key=str.upper)
# print(products)

# Task

import sys
numbs = sys.stdin.read().splitlines()
numbs.sort(key=str.int)
print(numbs)
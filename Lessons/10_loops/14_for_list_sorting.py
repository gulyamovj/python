# # Lesson
# cities = ["Москва", "Санкт-Петербург", "Новосибрск", "Калининград", "Владивосток", "Киев", "Москва", "Минск"]
# populations = [12_000_000, 5_300_000, 1_600_000, 480_000, 605_000, 2_900_000, 12_000_000, 2_000_000]
#
#
# for i, pop in enumerate(sorted(populations, reverse=True), start=1):
#     print(i, pop)
#
# print(populations)

# Task
import sys

customers = sys.stdin.read().splitlines()
new_customers = []

for i, name in enumerate(customers):
    if name not in new_customers:
        new_customers.append(name)

print(", ".join(new_customers))


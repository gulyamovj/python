# cars = ["Toyota", "Mercedes", "Hyundai", "BMW", None, "Skoda", "Lexus"]
#
# for car in cars:
#     if car is None:
#         continue
#     car = car.upper()
#     print(car)
#
# print(cars)
# print(car)

# # Task
# products = ["Молоко", "Апельсины", "ХЛЕБ", "виноград"]
#
# for prod in products:
#     print(prod.lower())

# # Task
# import sys
# last_names = sys.stdin.read().splitlines()
#
# for name in last_names:
#     print(name.title())

# # Task
# names = input()
# names = names.split(",")
#
# for name in names:
#     space_index = name.index(" ")
#     print(f"{name[space_index + 1:]} {name[:1]}.")

# # Task
# names = input()
# names = names.split(",")
# result = []
#
# for name in names:
#     if name.startswith("И"):
#         result.append(name)
#
# print(",".join(result))

# # Task
# import sys
# num = sys.stdin.read().splitlines()
#
# for n in num:
#     if int(n) <= 0:
#         break
#     print(n)

# # Task
# numbers = [41, 5, 83, 4, 16, 14, 59]
# result = 0
#
# for n in numbers:
#     result += n
#
# print(result)

# import sys
#
# numbers = sys.stdin.read().splitlines()
# income, expenditure = 0, 0
#
# for n in numbers:
#     if int(n) > 0:
#         income += int(n)
#     else:
#         expenditure += int(n)
#
# print(f'Доходы: {income} руб.\n'
#       f'Расходы: {abs(expenditure)} руб.')

# Task

import sys
names = sys.stdin.read().splitlines()

i = 1
for name in names:
    print(f"{i}. {name}")
    i += 1

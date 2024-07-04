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


# # Task
# import sys
# names = sys.stdin.read().splitlines()
#
# i = 1
# for name in names:
#     print(f"{i}. {name}")
#     i += 1

# # Task
#
# population = [
#     144_963_650,  # 2003
#     144_168_205,
#     143_474_219,
#     142_753_551,
#     142_220_968,
#     142_008_838,
#     141_903_979,
#     142_856_536,
#     142_865_433,
#     143_056_383,
#     143_347_059,
#     143_666_931,
#     146_267_288,
#     146_544_710,
#     146_804_372,
#     146_880_432,
#     146_780_720,
#     146_748_590  # 2020
# ]
#
# # Получаем год
# year = int(input())
#
# # Вычисляем индекс года
# year_index = year - 2003
#
# # Получаем значение
# year_population = population[year_index]
#
# # Список для хранения результатов
# result = []
#
# # Создаем переменную, в которой будем хранить текущий год.
# current_year = 2003
#
# # Перебираем значение в цикле
# for p in population:
#     # Если значение очередного года больше или ровно переданному,
#     # то добавляем результат в список result
#     if p >= year_population:
#         result.append(str(current_year))
#
#     # Увеличиваем год
#     current_year += 1
#
# # Вывод данных
# print(", ".join(result))
#
#
#
# year = int(input())
#
# year_index = year - 2003
# year_population = population[year_index]
#
# result = []
# current_year = 2003
#
# for p in population:
#     if p >= year_population:
#         result.append(str(current_year))
#
#     current_year += 1
#
# print(", ".join(result))

# # Task
# import sys
# incomes = sys.stdin.read().splitlines()
#
# sum = []
# count = 0
#
# for i in incomes:
#     count += int(i)
#     sum.append(str(count))
#
# print(" ".join(sum))

# # Task
# import sys
# num = sys.stdin.read().splitlines()
# numbers = []
#
# for i in num:
#     numbers.append(int(i))
#
# maximum = max(numbers)
#
# count = 0
# result = []
#
# for n in numbers:
#     count = n - maximum
#     result.append(str(count))
#
# print(" ".join(result))

# # Task
#
# import sys
# values = sys.stdin.read().splitlines()
#
# last_word = values[0]
# result = []
#
# for value in values:
#     if value != "null":
#         last_word = value
#         result.append(last_word)
#
#     elif value == "null":
#         result.append(last_word)
#
# print(" ".join(result))

# Task
products = [
    {"name": "Гречка", "price": 69},
    {"name": "Хлеб", "price": 34},
    {"name": "Молоко", "price": 57},
    {"name": "Яйца", "price": 78},
    {"name": "Рис", "price": 88},
    {"name": "Макароны", "price": 49},
    {"name": "Сахар", "price": 22},
    {"name": "Яблоки", "price": 79},
    {"name": "Картофель", "price": 18},
    {"name": "Свинина", "price": 120},
    {"name": "Масло", "price": 66},
    {"name": "Помидоры", "price": 64}
]

# amount = int(input())
res = 0
for i in products:
    res = int(i["price"])
    print(res)

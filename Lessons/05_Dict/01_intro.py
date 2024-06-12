# # Словари - контейнеры данных
# # Элементы словаря – "ключ":значение
# user = {
#     "age": 18,
#     "first_name": "Nikita",
#     "is_active": True,
#     "roles": [17,48],
#     "address": {"city":"Moscow",
#                 "street":"Gagarina",
#                 "house":22
#                 }
# }
#
# print(user["address"]["house"])

# # Task
# rainbow = {
#     "red":"красный",
#     "orange":"оранжевый",
#     "yellow":"желтый",
#     "green":"зеленый",
#     "blue":"голубой",
#     "indigo":"синий",
#     "violet":"фиолетовый"
# }

# # Task 2
# color = input()
# rainbow = {
#     "red":"красный",
#     "orange":"оранжевый",
#     "yellow":"желтый",
#     "green":"зеленый",
#     "blue":"голубой",
#     "indigo":"синий",
#     "violet":"фиолетовый"
# }
#
# print(rainbow[color])

# # Task
# numb = input()
# quarters = {
#     "quarter_1": [137, 565, 145],
#     "quarter_2": [145, 738, 1145],
#     "quarter_3": [1345, 1141, 879],
#     "quarter_4": [784, 689, 543]
# }
#
# total = sum(quarters[f"quarter_{numb}"])
#
# print(total)

# # Task
# numb = int(input())
# lang = input()
#
# digits = {
#     1: {"ru": "один", "en": "one"},
#     2: {"ru": "два", "en": "two"},
#     3: {"ru": "три", "en": "three"},
#     4: {"ru": "четыре", "en": "four"},
#     5: {"ru": "пять", "en": "five"},
#     6: {"ru": "шесть", "en": "six"},
#     7: {"ru": "семь", "en": "seven"},
#     8: {"ru": "восемь", "en": "eight"},
#     9: {"ru": "девять", "en": "nine"},
#     0: {"ru": "ноль", "en": "zero"}
# }
#
# print(digits[numb][lang])

# Task
year = int(input())
month = int(input())

finance = {
    2019: {
        1: {"income": 987, "expenses": 345},
        2: {"income": 1987, "expenses": 1247},
        3: {"income": 3011, "expenses": 2098},
        4: {"income": 3400, "expenses": 2798},
        5: {"income": 1987, "expenses": 1783},
        6: {"income": 2684, "expenses": 2004},
        7: {"income": 2008, "expenses": 1555},
        8: {"income": 2498, "expenses": 2210},
        9: {"income": 1714, "expenses": 789},
        10: {"income": 6971, "expenses": 6971},
        11: {"income": 345, "expenses": 147},
        12: {"income": 2487, "expenses": 2101}
    },
    2020: {
        1: {"income": 1487, "expenses": 578},
        2: {"income": 2654, "expenses": 1743},
        3: {"income": 3654, "expenses": 2478},
        4: {"income": 3614, "expenses": 6971},
        5: {"income": 2971, "expenses": 3240},
        6: {"income": 2876, "expenses": 2147},
        7: {"income": 3456, "expenses": 3047},
        8: {"income": 3129, "expenses": 3017},
        9: {"income": 1998, "expenses": 1149},
        10: {"income": 2478, "expenses": 2014},
        11: {"income": 2649, "expenses": 2970},
        12: {"income": 3001, "expenses": 1345}
    }
}

income = finance[year][month]["income"]
expense = finance[year][month]["expenses"]
result = (income - expense) / income * 100

print(f"{result:.0f}%")
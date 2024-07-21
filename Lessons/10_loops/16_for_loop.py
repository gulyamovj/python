# revenues = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
# prev_revenue = 0
# for idx, revenue in enumerate(revenues):
#     next_revenue = revenues[idx + 1] if idx < len(revenues) - 1 else 0
#     prev_revenue = revenues[idx - 1] if idx > 0 else 0
#     print(prev_revenue, revenue, next_revenue)


# # Task
# import sys
# revenue = sys.stdin.read().splitlines()
# prev_rev = 0
# result = []
#
# for i in revenue:
#     result.append(int(i) - prev_rev)
#     prev_rev = int(i)
#
# final = []
#
# for en in result:
#     final.append(str(en))
#
# print(" ".join(final))

# # Task
# input_str = input()
#
# chars = list(input_str)
#
# for i in range(0, len(chars) - 1, 2):
#     chars[i], chars[i + 1] = chars[i + 1], chars[i]
#
# print("".join(chars))

# # Task
# import sys
# input_num = sys.stdin.read().splitlines()
# input_num = list(map(int, input_num))
#
# result = []
#
# for i, n in enumerate(input_num):
#     prev_n = input_num[i - 1] if i > 0 else 0
#     if n > prev_n:
#         result.append("green")
#     elif n < prev_n:
#         result.append("red")
#     else:
#         result.append(result[i-1] if i > 0 else "green")
#
# print(" ".join(result))


cities_t = [
    ("Каир", 16_925_000),
    ("Токио", 38_505_000),
    ("Дакка", 18_595_000),
    ("Шанхай", 22_125_000),
    ("Мехико", 20_395_000),
    ("Пекин", 19_430_000),
    ("Мумбаи", 23_645_000),
    ("Дели", 28_125_000),
    ("Осака", 19_281_000),
    ("Сан-Паулу", 20_935_000)
]

cities_d = [
    {"name": "Каир", "population": 16_925_000},
    {"name": "Токио", "population": 38_505_000},
    {"name": "Дакка", "population": 18_595_000},
    {"name": "Шанхай", "population": 22_125_000},
    {"name": "Мехико", "population": 20_395_000},
    {"name": "Пекин", "population": 19_430_000},
    {"name": "Мумбаи", "population": 23_645_000},
    {"name": "Дели", "population": 28_125_000},
    {"name": "Осака", "population": 19_281_000},
    {"name": "Сан-Паулу", "population": 20_935_000}
]

employees = [
    {"name": "Иван Иванов",    "job": {"role": "Программист", "salary": 150_000}},
    {"name": "Дмитрий Петров", "job": {"role": "Менеджер",    "salary": 120_000}},
    {"name": "Олег Осипов",    "job": {"role": "Дизайнер",    "salary": 140_000}},
    {"name": "Ирина Смирнова", "job": {"role": "Программист", "salary": 160_000}},
    {"name": "Юлия Соколова",  "job": {"role": "Дизайнер",    "salary": 150_000}},
    {"name": "Семен Сорокин",  "job": {"role": "Архитектор",  "salary": 130_000}}
]

for employee in sorted(employees, key=lambda e: e["job"]["salary"]):
    name = employee["name"]
    salary = employee["job"]["salary"]
    print(f"{name:<20}{salary:>12,}")
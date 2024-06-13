# Lesson
# user = {
#     "age": 18,
#     "first_name": "Nikita",
#     "is_active": True,
#     }
#
# user.update(AGE = None)
# # print(user["Age"]) # Если в запросе несуществующее значение то программа закроется с ошибками
# print("AGE" in user)
# print("age" in user)
# print(user.get("age"))
# print(user.get("AGE", 0) or "Nothing")

# # Task
# car = {
#     "mark": "Nissan",
#     "model": "Qashqai",
#     "year": 2018,
#     "price": 1_200_000,
#     'volume': 2.0
# }
#
# arg = input()
#
# print(car.get(arg, 0) or "неизвестно")

# # Task
# revenue = {
#     2017: 123_000,
#     2018: 127_000,
#     2019: 134_000,
#     2020: 201_000,
#     2021: 289_000
# }
#
# first_year = int(input())
# second_year = int(input())
#
# first = revenue.get(first_year) or 0
# second = revenue.get(second_year) or 0
# resul = first - second
#
# print(resul)

# # Task
# revenue = {
#     2017: 123_000,
#     2018: 127_000,
#     2019: 134_000,
#     2020: 201_000,
#     2021: 289_000
# }
#
# year_1 = int(input())
# year_2 = int(input())
#
# year_max = max(year_1, year_2)
# year_min = min(year_1, year_2)
#
# first = revenue.get(year_max) or 0
# second = revenue.get(year_min) or 0
#
# print(first - second)

# Task

sizes = {
    "44": "xs",
    "46": "s",
    "48": "m",
    "50": "l",
    "52": "xl"
}

sex = {
    "m": "m",
    "f": "w",
    "w": "w"
}

name = input()
size = input()
gender = input()

name = name.lower()
size = sizes.get(size) or "all"
gender = sex.get(gender) or "unisex"

print(f'{name} {size} {gender}'.replace(" ", "-"))
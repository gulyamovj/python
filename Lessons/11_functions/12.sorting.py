# # Lesson
#
# countries = ["Франция", "Япония", "Россия", "Казахстан",
#              "Китай", "Польша", "Украина", "Беларусь"]
# # Что должна возвращать функция?
# # 1. Значения, которые можно сравнить: числа, строки, кортежи
# # 2. Значения одного типа
# # def country_sort(country):
# #     return {
# #         "Россия" : "1",
# #         "Украина" : "2",
# #         "Казахстан" : "3",
# #         "Беларусь" : "4"
# #     }.get(country, country).lower()
#
# def country_sort(country):
#     country = country.lower()
#     if country in {"россия", "казахстан", "украина", "беларусь"}:
#         return 0, country
#     return 1, country
#
# countries = sorted(countries, key=country_sort)
#
# print(countries)

# # Task
# import sys
# num = sys.stdin.read().splitlines()
# numbers = sorted(num, key=float)
# print(", ".join(numbers))

# Task
import re, sys
cars = sys.stdin.read().splitlines()
def cyrilic(text):
    if bool(re.match(r'[\u0400-\u04FF]', text)):
        return 0, text
    return 1, text

sorted_cars = sorted(cars, key=cyrilic)
print(", ".join(sorted_cars))
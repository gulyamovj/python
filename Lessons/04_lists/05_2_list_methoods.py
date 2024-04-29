# # Lesson
# cities = ["Москва", "Санкт-Петербург", "Новосибрск",
#           "Калининград", "Владивосток", "Киев",
#           "Москва", "Минск"]
# populations = [12_000_000, 5_300_000, 1_600_000,
#                480_000, 605_000, 2_900_000,
#                12_000_000, 2_000_000]
#
# moscow_i = cities.index("Москва", 1)
#
# city = cities.pop(moscow_i).upper()
# print(city)
#
# population = populations.pop(moscow_i) / 1e6
# print(population)
#
# print(cities)

# # Task - Двойное извлечение
# el = int(input())
# values = [7, 9, 4, 8, 1, 5, 3, 6, 2]
# value = values.pop(el)
# values.pop(value)
#
# print(values)

# # Task
# name = input()
# biathletes = ["Йоханнес Тиннес Бё", "Яков Фак", "Доминик Ландертингер",
#              "Себастьян Самуэльссон", "Мартен Фуркад", "Беньямин Вегер",
#              "Михал Крчмарж", "Фредрик Линдстрём", "Эрик Лессер",
#              "Эмиль Хегле Свеннсен"]
#
# athlet_i = biathletes.index(name)
# print(athlet_i + 1)

# # Task
# brand = input()
# model = input()
#
# cars = ["Ford Focus", "Skoda Octavia", "Toyota Prius",
#         "Hyundai Solaris", "Volkswagen Polo", "Skoda Rapid"]
#
# car = "{} {}".format(brand, model)
#
# print(car in cars)

# # Task - Количество оценок
# numb = int(input())
# school_marks = [3, 4, 4, 5, 3, 3, 5, 5, 5, 4, 3, 2, 4, 5, 2, 4, 5]
# print(school_marks.count(numb))

# Task - Процент от числа оценок
# numb = int(input())
numb = 2
school_marks = [3, 4, 4, 5, 3, 3, 5, 5, 5, 4, 3, 2, 4, 5, 2, 4, 5]
col = school_marks.count(numb)
marks = len(school_marks)
result = col/marks * 100

print("{:2%}".format(result))

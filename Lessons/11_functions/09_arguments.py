# # Lesson
#
# rus_president_fn = "Владимир"
# rus_president_ln = "Путин"
# rus_president_p = "Владимирович"
# usa_president = ["Барак", "Обама", "Иванович"]
# first_rus_president = {"last_name":"Ельцин", "first_name":"Борис"}
#
# def print_full_name(first_name, last_name, patronymic=""):
#     print(first_name, patronymic, last_name)
#
# print_full_name(rus_president_fn, rus_president_ln, rus_president_p)
# print_full_name(usa_president[0], usa_president[1])
# print_full_name(*usa_president) # * Расспаковка последовательности
# print_full_name(**first_rus_president) # * Расспаковка словаря, key должен совподать с аргументами

# # Task
# def line(fill, length=10):
#     return fill * length
#
# print(line("-", 15))
# print(line("-"))

# # Task
# def pace_to_speed(minutes, seconds=0):
#     total_hours = (minutes * 60 + seconds) / 3600
#     speed_kph = 1 / total_hours
#     speed_rounded = round(speed_kph, 1)
#     return speed_rounded
#
# print(pace_to_speed(4, 48))

# Task
cities = [
    # Клд  Мск   СПб,  Каз   Врж,  Тверь
    [0,    1337, 1103, 2192, 1855, 1255],  # Калининград
    [1337, 0,    712,  825,  522,  192],   # Москва
    [1103, 712,  0,    1526, 1337, 531],   # Санкт-Петербург
    [2192, 825,  1526, 0,    1080, 1006],  # Казань
    [1855, 522,  1337, 1080, 0,    815],   # Воронеж
    [1255, 192,  531,  1006, 815,  0]      # Тверь
]


def calc_distance(path):

    total = 0
    for i in range(len(path) - 1):
        total += cities[path[i]][path[i + 1]]
    return total

print(calc_distance([3, 0, 5]))
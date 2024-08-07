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

# # Task
# cities = [
#     # Клд  Мск   СПб,  Каз   Врж,  Тверь
#     [0,    1337, 1103, 2192, 1855, 1255],  # Калининград
#     [1337, 0,    712,  825,  522,  192],   # Москва
#     [1103, 712,  0,    1526, 1337, 531],   # Санкт-Петербург
#     [2192, 825,  1526, 0,    1080, 1006],  # Казань
#     [1855, 522,  1337, 1080, 0,    815],   # Воронеж
#     [1255, 192,  531,  1006, 815,  0]      # Тверь
# ]
#
#
# def calc_distance(path):
#
#     total = 0
#     for i in range(len(path) - 1):
#         total += cities[path[i]][path[i + 1]]
#     return total
#
# print(calc_distance([3, 0, 5]))

# # Task
# def resize_disk(size, lst):
#     sum_of_list = sum(lst)
#     each_sum = 0
#     new_lst = []
#
#     for i in range(len(lst)):
#         each_sum = lst[i] / sum_of_list * size
#         new_lst.append(int(each_sum))
#
#     ost = size % sum(new_lst)
#
#     if ost > 0:
#         new_lst[-1] += ost
#
#     return new_lst
#
# print(resize_disk(150, [15, 15, 20, 10, 40]))

# # Task
# def get_dict(arg):
#     arg = arg.split(";")
#     new_dict = {}
#     for i in range(len(arg)):
#         key, value = arg[i].split(":")
#         new_dict[key] = value
#
#     return new_dict
#
# print(get_dict("a:10;b:20;c:30"))

# Task
def replace_all(text, replacements):

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text

result = replace_all(
    "one, two, three, four",
    {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'}
)

print(result)
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

# Task
def pace_to_speed(minutes, seconds=0):

    minutes = 60 / minutes
    seconds = str(seconds / 60)
    seconds = seconds.split(".")

    result = f'{minutes:.0f}.{seconds[1][:1]}'
    return result

print(pace_to_speed(4))
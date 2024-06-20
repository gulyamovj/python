# # Lesson
# names_list =      ["Oleg", "Nikita", "Yan", "Oleg", "Sofia", "Yan", "Oleg", "Viktor"]
# names_uniq_list = ["Oleg", "Nikita", "Yan", "Sofia", "Viktor"]
# names_set =       {"Oleg", "Nikita", "Yan", "Sofia", "Viktor"}
#
# name = "Oleg"
#
# print(name in names_list)
# print(name in names_uniq_list)
# print(name in names_set)

# # Task
# import sys
#
# schedule = {
#     "04.01.2023 10:00",
#     "04.01.2023 12:00",
#     "04.01.2023 14:00",
#     "04.01.2023 16:00",
#     "05.01.2023 10:00",
#     "05.01.2023 14:00",
# }
#
# check_date = sys.stdin.read().splitlines()
# date_time = check_date[0] + " " + check_date[1]
#
# print(date_time in schedule)

# Task

clients = {
    ("Дмитрий", "Петров"),
    ("Василий", "Филиппов"),
    ("Светлана", "Нестерова"),
    ("Василий", "Филиппов"),
    ("Евгения", "Карпова")
}

name = input()
last_name = input()

full_name = (name, last_name)

print(full_name not in clients)
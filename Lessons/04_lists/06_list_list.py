# # Lesson
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# matrix[2][1] = 8.5
# matrix[2][1] = [8.6, 8.7, 8.8]
# print(matrix[1][-1])
# print(12 in matrix[3]) # оператор in
# print(matrix)

# # Task - Add letter
# letter = "c"
# L = [
#     [1, 2],
#     ['a', 'b'],
#     [5, 6]
# ]
# L[1].append(letter)
# print(L)

# # Task - Monthly budget
# year = int(input()) - 2019
# month = int(input()) - 1
# budget = [
#     [176, 148, 245, 378, 451, 568, 135, 146, 761, 414, 135, 171],  # 2019
#     [211, 175, 301, 474, 569, 721, 158, 172, 972, 521, 158, 205],  # 2020
#     [257, 210, 374, 599, 722, 920, 188, 206, 1246, 660, 188, 249]  # 2021
# ]
# print(budget[year][month])

# # Task
# year = int(input())
# month = int(input())
# value = int(input())
# start_year = 2019
#
# budget = [
#     [176, 148, 245, 378, 451, 568, 135, 146, 761, 414, 135, 171],  # 2019
#     [211, 175, 301, 474, 569, 721, 158, 172, 972, 521, 158, 205],  # 2020
#     [257, 210, 374, 599, 722, 920, 188, 206, 1246, 660, 188, 249]  # 2021
# ]
#
# budget[year-start_year][month-1] = value
# result = "{0:,}".format(sum(budget[year-start_year] * 1000)).replace(",", " ")
# print(result)

# # Task
# fio = [
#     ["Иванов", "Юдашкин", "Петров", "Королева", "Коваленко"],  # Фамилии
#     ["Юрий", "Андрей", "Никита", "Вероника", "Игнат", "Пётр", "Валерий"],  # Имена
#     ["Александрович", "Анатольевна", "Викторовна", "Иванович"]   # Отчества
# ]
#
# name = int(input())
# family_name = int(input())
# surname = int(input())
#
# name = fio[0][name]
# family_name = fio[1][family_name]
# surname = fio[2][surname]
#
# print("{} {} {}".format(name, family_name, surname))

# # Task
# import sys
#
# value = sys.stdin.read().splitlines()
#
# products = [
#     ["молоко", "кефир"],  # молочка
#     ["котлеты", "курица", "говядина"]  # мясо
# ]
#
# products.append(value)
# print(products)

# # Task
# import sys
#
# indx, *goods = sys.stdin.read().splitlines()
#
# products = [
#     ["молоко", "кефир"],  # молочка
#     ["котлеты", "курица", "говядина"]  # мясо
# ]
#
# products[int(indx)].extend(goods)
#
# print(products)
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


# # ОСНОВНОЕ НАЗНАЧЕНИЕ
# # 1. Повторение частей кода
# # 2. Перебор последовательностей
#
# # While - Выполнять код до тех пор ПОКА условие верно или ПОКА условие верно, выполнять код
#
# i = 5 # Счетчик / Начальное значение
# while i >= -5:
#     print(i)
#     i -= 1 # ШАГ / Инкремент

# Task
# numbers = []
# i = 11
# while i <= 27:
#     numbers.append(i)
#     i += 2

# # Task
# numbers = []
# i = 30
# while i >= 18:
#     numbers.append(i)
#     i -= 2

# # Task
# num = int(input())
# i = 1
# res = []
# while i <= 9:
#     res.append(str(num * i))
#     i += 1
#
# print(" ".join(res))

# # Task
# numbers = []
#
# i = 0
# while i <= 10:
#     numbers.append(2 ** i)
#     i += 1
#
# print(numbers)

# # Task
# N = int(input())
# factorial = 1
# i = 1
#
# while i <= N:
#     factorial = factorial * i
#     i += 1
#
# print(factorial)

# Task
numbers = [1, 7, 8, 34, 56, 14, 9]

total_sum = 0

i = 0
while i <= (len(numbers) - 1):
    total_sum = total_sum + numbers[i]
    i += 1

print(total_sum)
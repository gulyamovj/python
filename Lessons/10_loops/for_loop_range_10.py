names = ["Ivan", "Nikita", "Ilya", "Viktor", "Alena", "Svetlana"]

# for num in range(5, -6, -1): # начало, конец, шаг
#     print(num)

# for i in range(len(names)): # Неправильный подход для питона
#     name = names[i]
#     print(name)

# for name in names: # Правильный перебор последовательностей в питоне
#     print(name)

# for num in range(10):
#     num = num / 10
#     print(num)

# # Task
# numbers = list(range(10, 1, -2))
# print(numbers)

# # Task
# N = int(input())
# factorial = 1
#
# for i in range(1, N + 1):
#     factorial *= i
#
# print(factorial)

# # Task
# start = int(float(input()) * 10)
# end = int(float(input()) * 10)
#
# result = []
#
# for i in range(start, end + 1):
#     result.append(str(i / 10))
#
# print(" ".join(result))

# # Task
# start = int(float(input()) * 10)
# end = int(float(input()) * 10)
#
# result = []
#
# if start < end:
#     for i in range(start, end + 1):
#         result.append(str(i / 10))
# elif start > end:
#     for i in range(start, end - 1, - 1):
#         result.append(str(i / 10))
#
# print(" ".join(result))

# # Task
# input_data = input()
# pages = input_data.split(",")
#
# result = set()
#
# for page in pages:
#     if "-" in page:
#         start, end = page.split("-")
#         for page in range(int(start), int(end) + 1):
#             result.add(page)
#     else:
#         result.add(int(page))
#
# sorted_pages = sorted(result)
#
# print(",".join(map(str, sorted_pages)))

# Task

n = int(input()) + 1

for i in range(1, n):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    if i % 5 != 0 and i % 3 != 0:
        print(i)
        continue
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")

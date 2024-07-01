# i = 5
# while i >= -5:
#     print(i)
#     i -= 1

# Task
# rooms_per_floor = int(input())
# number_of_floors = int(input())
#
# floor = 1
# result = []
#
# while floor <= number_of_floors:
#     room = 1
#     while room <= rooms_per_floor:
#         result.append(f"{floor}{room}")
#         room += 1
#     floor += 1
#
# print(' '.join(result))

# rooms = int(input())
# floors = int(input())
#
# result = []
# floor = 1
#
# while floor <= floors:
#     room = 1
#     while room <= rooms:
#         result.append(f"{floor}{room}")
#         room += 1
#     floor += 1
#
# print(' '.join(result))

# # Task
# max_value = int(input())
# separator = int(input())
#
# result = []
# i = 1
# count = 0
#
# while i <= max_value:
#     result.append(str(i))
#     count += 1
#     if count == separator:
#         result.append("\n")
#         count = 0
#     i += 1
#
# print(" ".join(result).replace(" \n ", "\n").rstrip())

# Task
num = ["111", "2", "33", "41"]

result = 0
list = []
counter = 1

while counter <= len(num):
    result = result + int(num[counter - 1])
    if counter == len(num):
        list.append(result)
    counter += 1

print(list)
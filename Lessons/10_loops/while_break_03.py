# i = 0
#
# while True:
#
#     i += 1
#
#     if not i % 2:
#         continue
#     print(i)
#
#     if i == 13:
#         break

# # Task
# import sys
#
# num = sys.stdin.read().splitlines()
#
# stop = 0
# i = 0
#
# while i < len(num):
#     if int(num[i]) != stop:
#         print(num[i])
#     else:
#         break
#     i += 1

# # Task
#
# numbers = input().split()
#
# result = 0
# i = 0
#
# while i <= len(numbers) - 1:
#
#     if numbers[i] == '0':
#         break
#
#     result += int(numbers[i])
#     i += 1
#
# print(result)

# # Task
# user_id = int(input())
#
# users = [
#     {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов"},
#     {"id": 156, "first_name": "Виктор", "last_name": "Осипов"},
#     {"id": 23, "first_name": "Алёна", "last_name": "Гордеева"},
#     {"id": 84, "first_name": "Семён", "last_name": "Васильев"},
#     {"id": 21, "first_name": "София", "last_name": "Зинько"},
#     {"id": 55, "first_name": "Антон", "last_name": "Ватутин"},
#     {"id": 287, "first_name": "Виталий", "last_name": "Новиков"}
# ]
#
# i = 0
#
# while i < len(users):
#
#     if users[i]["id"] == user_id:
#         print(users[i]["first_name"], users[i]["last_name"] )
#
#     i += 1

# Task
users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов", "lang": "python"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов", "lang": "php"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева", "lang": "java"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев", "lang": "python"},
    {"id": 21, "first_name": "София", "last_name": "Зинько", "lang": "java"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин", "lang": "python"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков", "lang": "c++"}
]

language = input()

i = 0
while i < len(users):

    if users[i]["lang"] == language:
        print(users[i]["first_name"], users[i]["last_name"])
        break
    i += 1
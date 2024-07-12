# # Task
# file_name = input()
#
# balance_file = open(file_name, "r", encoding="utf-8")
# result = 0
#
# for line in balance_file.readlines():
#     name, count = line.split(";")
#     result = result + int(count)
#
# print(result)

# # Task
# card_num = input()
# file = open("bank.txt", "r", encoding="utf-8")
#
# total = 0
#
# for line in file.read().splitlines():
#     outcome, income, amount = line.split(";")
#     if income == card_num:
#         total += int(amount)
#     if outcome == card_num:
#         total -= int(amount)
#
# print(total)

# # Task
# file_name = input()
#
# file = open(file_name, "r", encoding="utf-8")
# file_read = file.read().splitlines()
#
# sales = {}
#
# for line in file_read:
#     manager, amount = line.split("\t")
#     amount = int(amount)
#
#     if manager in sales:
#         sales[manager] += amount
#     else:
#         sales[manager] = amount
#
# top_manager = None
# max_sales = 0
#
# for manager, total_sales in sales.items():
#     if total_sales > max_sales:
#         max_sales = total_sales
#         top_manager = manager
#
# print(f"{top_manager}, {max_sales}")

# # Task
# search = input().lower()
# file = open("films.txt", "r")
#
# result = ""
#
# for line in file.read().splitlines():
#
#     num, ru, en = line.split(",")
#
#     if search in ru.lower():
#         print(ru)
#     elif search in en.lower():
#         print(en)
#
# print(result)

# # Task
# file_name = "spar.txt"
# file = open(file_name, "r")
#
# word_en = "spar"
# word_ru = "спар"
# result = ""
#
# for line in file.read().splitlines():
#     if word_ru in line.lower():
#         line = line.lower()
#         result = line.replace(word_ru, word_en.upper())
#         print(result)

# # Task
#
# import sys
# prefix, quantity, chars = sys.stdin.read().splitlines()
# quantity = int(quantity)
# chars = int(chars)
#
# file_content = []
#
# for count in range(1, quantity + 1):
#     file = open(f"{prefix}-{count}.txt", "r", encoding="utf-8")
#     file_content.append(file.read())
#
# result = []
# for i in range(chars):
#     file_index = i % quantity
#     char_index = i // quantity
#
#     if char_index < len(file_content[file_index]):
#         result.append(file_content[file_index][char_index])
#
# print("".join(result))

# Lesson
employees = [
    [
        {"name" : "Ivanov I. I.", "busy" : True},
        {"name" : "Petrov P. P.", "busy" : True},
        {"name" : "Sidorov S. S.", "busy" : True}
    ],
    [
        {"name": "Sokolov A. A.", "busy": True},
        {"name": "Utkin B. B.", "busy": False},
        {"name": "Lebedev A. T.", "busy": False}
    ],
    [
        {"name": "Medvedev D. A.", "busy": False},
        {"name": "Volkov A. E.", "busy": True},
        {"name": "Kozlov A. C.", "busy": False}
    ]
]

candidate = None

for dep in employees:
    for emp in dep:
        if not candidate and not emp["busy"]:
            candidate = emp["name"]

print(candidate)
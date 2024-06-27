# # Скоринговая программа
#
# age = 21
# sex = "f"
# credit = True
# has_military_id = False
#
# if age >= 18 and age < 65:
#     if sex == "m" and age < 27 and not has_military_id:
#         credit = False
#     if sex == "f" and (age <= 22 or has_military_id):
#         credit = False
# else:
#     credit = False
#
# if credit:
#     print("Кредит одобрен")
# else:
#     print("Кредит НЕ одобрен")

# Task

age = int(input())
time = int(input())
can_sold = True

if age >= 18 and (time >= 7 and time < 22):
    can_sold = True
else:
    can_sold = False

if can_sold:
    print("Разрешено")
else:
    print("Запрещено")
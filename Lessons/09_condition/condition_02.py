# age = 18
#
# if age >= 14:
#     if age >= 18:
#         print("Доступ разрешен")
#     else:
#         print("Доступ разрешен с согласия родителей")
# else:
#     print("Доступ запрещен")
#
# # Улучшиенный вариант
# if age >= 18:
#     print("Доступ разрешен")
# elif age > 13:
#     print("Доступ разрешен с согласия родителей")
# else:
#     print("Доступ запрещен")

# # Task
# users = {
#     "user1": "password1",
#     "user2": "abcde",
#     "user3": "123456",
#     "user4": "lovelove",
#     "user5": "kdmUdmk84M",
# }
#
# name = input()
# password = input()
#
# if name in users:
#     if users[name] == password:
#         print("Доступ открыт")
#     else:
#         print("Доступ закрыт")
# else:
#     print("Пользователь не найден")

# # Task
# password = input()
#
# if len(password) >= 6:
#     if len(password) <= 8:
#         print("Хорошо, но можно и лучше")
#     elif len(password) >= 9:
#         print("Пароль подходит")
# else:
#     print("Пароль слишком короткий")

# Вариант автора
# if len(password) < 6:
#     print("Пароль слишком короткий")
# elif password.__len__() <= 8:
#     print("Хорошо, но можно и лучше")
# else:
#     print("Пароль подходит")

# Task
numb = int(input())
result = 0
prefix = ""

if numb >= 1_000_000:
    result = round(numb / 1_000_000, 2)
    prefix = "M"

    if result.is_integer():
        result = int(result)
    else:
        result = round(result, 2)

elif numb >= 1000:
    result = round(numb / 1000, 2)
    prefix = "K"

    if len(str(result)) >= 4:
        result = str(result)[:4]
        if result.endswith(".0"):
            result = result.strip(".0")
        if result.endswith("."):
            result = result.strip(".")
    elif len(str(result)) <= 3:
        result = str(result)[:3]
        if result.endswith(".0"):
            result = result.strip(".0")

else:
    result = str(numb)

print(str(result) + prefix)
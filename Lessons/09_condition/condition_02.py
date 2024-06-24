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

Task
numb = int(input())
result = 0

if numb >= 1_000_000:
    result = round(numb / 1_000_000, 2)
    if result.is_integer():
        result = int(result)
    print(f"{result}M")

elif numb >= 1000:
    result = numb / 1000

    if result.is_integer():
        print(f"{result}K")

else:
    print(f"{numb}")
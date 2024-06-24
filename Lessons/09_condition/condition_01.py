# age = 24
#
# if age >= 18:
#     full_name = " petrov ivan ivanovich  "
#     full_name = full_name.title()
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")
#
# print("end")

# # Task
# password = "idY*49amd6z"
# pas_in = input()
#
# if pas_in == password:
#     print("Доступ открыт")
# else:
#     print("Доступ закрыт")

# # Task
# import hashlib
#
# hash_password = 'c8b667f4e6953d59b6ae9b9659772333'
#
# raw_password = input()
#
# raw_password = raw_password.encode()
# hash_password2 = hashlib.md5(raw_password)
# hash_password2 = hash_password2.hexdigest()
#
# if hash_password == hash_password2:
#     print("Доступ открыт")
# else:
#     print("Доступ закрыт")

# # Task
# user_input = int(input())
#
# if user_input % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# # Task
# numb1 = int(input())
# numb2 = int(input())
#
# if numb1 > numb2:
#     print(numb1)
# elif numb2 > numb1:
#     print(numb2)
# else:
#     print(numb1)

# Task
#
# price = input()
#
# if price[-2:] == "99":
#     price = int(price)
#     price += 1
#
# print(price)

# # Task
# password = input()
#
# if len(password) < 6:
#     print("Пароль слишком короткий")
# else:
#     print("Пароль подходит")

# # Task
# products = ["Молоко", "Масло", "Хлеб", "Овсянка", "Яйца"]
#
# new_product = input()
#
# if new_product not in products:
#     products.append(new_product)
#
# products.sort()
# print(", ".join(products))
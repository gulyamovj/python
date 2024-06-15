# # Получение значение
#
# contacts = {
#     "email": "user@domain.com",
#     "facebook": "username",
#     "instagram": "@account",
# }
#
# contacts.update({
#     "phone1": "+7 891 555-55-55",
#     "phone2": "+7 891 555-55-55",
# })
#
# print(contacts)
# print(contacts.pop("facebook")) # pop() возвращает значение и удаляет из словаря
# print(contacts.popitem())
# print(contacts.popitem())
# print(contacts)

# # Task
# colors = {
#    "black": "черный",
#    "white": "белый",
#    "blue": "синий",
#    "red": "красный",
#    "yellow": "желтый"
# }
#
# color = input()
#
# print(colors.pop(color), colors)

# # Task
# game = {
#    "name": "Cyberpunk 2077",
#    "price": 3900,
#    "genre": "action"
# }
#
# f1 = input()
# value = game.pop(f1)
# game.update({f1.upper():value})
# print(game)

# Task

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}

key = input()

value = colors.pop(key)
colors.update({value:key})

print(colors)
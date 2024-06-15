# # Lesson
#
# user = {
#     "age": 18,
#     "first_name": "Nikita",
#     "is_active": True,
#     "role": "manager"
# }
#
# print(list(user))
# print(list(user.values()))
# print(list(user.items()))

# Task
colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}

en = input()
ru = input()

colors.update({en:ru})
k = list(colors.keys())

print(f"{k[0]}, {k[1]}, {k[2]}, {k[3]}" )
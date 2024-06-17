# # Lesson
#
# user = {
#     "age": 18,
#     "first_name": "Nikita",
#     "is_active": True,
#     "role": "manager"
# }
#
# print(list(user.keys()))
# print(list(user.values()))
# print(list(user.items()))

# # Task
# colors = {
#    "black": "черный",
#    "white": "белый",
#    "blue": "синий"
# }
#
# en = input()
# ru = input()
#
# colors.update({en:ru})
# k = list(colors.keys())
#
# print(", ".join(k))

# # Task
# colors = {
#    "black": "черный",
#    "white": "белый",
#    "blue": "синий"
# }
#
# en = input()
# ru = input()
#
# colors.update({en:ru})
# k = list(colors.values())
#
# print(", ".join(k))

# # Task
# colors = {
#    "black": "черный",
#    "white": "белый",
#    "blue": "синий"
# }
#
# en = input()
# ru = input()
#
# colors.update({en:ru})
# k = list(colors.keys())
# k.sort()
# print(", ".join(k))

# # Task
# revenue2023 = {
#    "q1": 50,
#    "q2": 200,
#    "q3": 400,
#    "q4": 300
# }
#
# new_update = input()
#
# quarter = new_update[:1]
# value = int(new_update[2:])
#
# revenue2023.update({f"q{quarter}":value})
# total = sum(list(revenue2023.values()))
# procent = (value / total) * 100
# print(f"{procent:.1f}%")

# Task

users = {
   "user1@domain.com": "nikitos",
   "user2@domain.com": "black adam",
   "user3@domain.com": "minion",
   "user4@domain.com": "lovey",
   "user5@domain.com": "barbie",
   "user6@domain.com": "comedy central",
   "user7@domain.com": "bro",
   "user8@domain.com": "rapunzel"
}

name = input().lower()

user_name = list(users.values())

print(name in user_name)
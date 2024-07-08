# NEW LINE
# # Task
# users = [
#     {"id": 17,  "lang": "python", "active": False},
#     {"id": 156, "lang": "php",    "active": True},
#     {"id": 23,  "lang": "java",   "active": True},
#     {"id": 84,  "lang": "python", "active": True},
#     {"id": 28,  "lang": "java",   "active": False},
#     {"id": 21,  "lang": "java",   "active": True},
#     {"id": 55,  "lang": "python", "active": True},
#     {"id": 88,  "lang": "python", "active": True},
#     {"id": 287, "lang": "c++",    "active": False},
#     {"id": 481, "lang": "php",    "active": False},
#     {"id": 134, "lang": "c++",    "active": True},
#     {"id": 65,  "lang": "php",    "active": True},
# ]
#
# input_lang = input()
# user_id = []
#
#
# for user in users:
#     if user["lang"] == input_lang and user["active"] == True:
#         user_id.append(user["id"])
#
# user_id.sort()
# id_str = []
#
# for id in user_id:
#     id_str.append(str(id))
#
# print(", ".join(id_str))


# # Task
# users = [
#     {"id": 17,  "active": False, "langs": ["python", "javascript"]},
#     {"id": 156, "active": True,  "langs": ["php"]},
#     {"id": 23,  "active": True,  "langs": ["java", "c++"]},
#     {"id": 84,  "active": True,  "langs": ["python", "c++"]},
#     {"id": 28,  "active": False, "langs": ["java", "php"]},
#     {"id": 21,  "active": True,  "langs": ["java", "javascript"]},
#     {"id": 55,  "active": True,  "langs": ["python", "c#"]},
#     {"id": 88,  "active": True,  "langs": []},
#     {"id": 287, "active": False, "langs": ["c++", "c#", "java"]},
#     {"id": 481, "active": False, "langs": ["php", "javascript", "python"]},
#     {"id": 134, "active": True,  "langs": ["c++", "python"]},
#     {"id": 65,  "active": True,  "langs": ["php", "python"]},
#     {"id": 7,  "active": False,  "langs": ["javascript", "c#"]}
# ]
#
# input_lang = input()
# user_id = []
#
# for user in users:
#     for langs in user["langs"]:
#         if input_lang == langs and user["active"] == False:
#             user_id.append(user["id"])
#
#
# users_id = []
#
# i = 0
# while i <= len(user_id) - 1:
#     users_id.append(str(user_id[i]))
#     i += 1
#
# print(", ".join(users_id))

# # Task
# import sys
#
# num = sys.stdin.read().splitlines()
# numbers = []
#
# for n in num:
#     numbers.append(int(n))
#
# max_value = None
# result = []
#
# for number in numbers:
#     if max_value is None or number > max_value:
#         max_value = number
#         result.append(str(max_value))
#
# print(", ".join(result))

# Teacher variant
import sys
values = ['34', '56', '12', '55', '74', '58', '59', '74', '75']
print(values)
max_values = []
max_value = float("-inf")

for value in values:
    value = int(value)
    if value > max_value:
        max_value = value
        max_values.append(str(max_value))

print(", ".join(max_values))
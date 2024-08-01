# # Lesson
# def mult(x, y):
#     if type(x) == str and x.isdigit():
#         x = int(x)
#
#     if type(y) == str and y.isdigit():
#         x = int(y)
#
#     if type(x) not in [int, float] or type(y) not in [int, float]:
#         raise TypeError
#     return x * y
#
# print(mult(2, 7))
# print(mult(2.5, 7.12))
# print(mult("5", "3"))

# # Task
# def calc_money(price, hours):
#     hour, minute = hours
#     total = (hour + (minute / 60)) * price
#
#     return f"{total:.0f}"

# # Task
# def check_access(card_number, floor):
#
#     file = open('db.txt', 'r', encoding='utf-8')
#     lines = file.readlines()
#     file.close()
#
#     for line in lines:
#         card, room = line.strip().split(";")
#         if card == card_number:
#             room_floor = room[0]
#             if floor == room_floor:
#                 return True
#             else:
#                 return False
#
#     return None
#
# print(check_access("123056", "2"))

# # Task
# def separate(data):
#     number = "0"
#     text = ""
#     key = True
#     for i in data:
#         if i.isdigit() and key:
#             number += str(i)
#         elif i.isalpha():
#             text += i
#             key = False
#
#     return int(number), text
#
# print(separate("75, Python"))
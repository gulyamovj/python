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

# Task
def calc_money(price, hours):
    hour, minute = hours
    total = (hour + (minute / 60)) * price

    return f"{total:.0f}"
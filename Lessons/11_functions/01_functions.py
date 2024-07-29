
# # Lesson
# def get_min_item(items):
#     min_item = items[0]
#     for item in items[1:]:
#         if item < min_item:
#             min_item = item
#
#     return min_item
#
#
# items1 = [23, 4, 7, 12, 6, 8, 41, 20]
# items2 = [5, 4, -12, 5, 6, 7, 8, 1]
# items3 = [54, 14, 12, 15, 60, 7, 8, 19]
#
# min_items1 = get_min_item(items1)
# min_items2 = get_min_item(items2)
# min_items3 = get_min_item(items3)
#
# print(min_items1)
# print(min_items2)
# print(min_items3)

# # Task
# x = int(input())
# def sum_num(x):
#     result = 0
#     i = 0
#     while i <= x:
#         result += i
#         i += 1
#     return result
#
# print(sum_num(x))

# # Task
# def line(x):
#     result = ""
#     for i in range(x):
#         result += "-"
#     return result

# # Task
# def strip(text):
#     text = text.strip()
#
#     message = []
#
#     for char in text:
#         message.append(char)
#
#     next_char = ""
#     prev_char = ""
#     new_message = []
#
#     for idx, sym in enumerate(message):
#
#         next_char = message[idx + 1] if idx < len(message) - 1 else sym
#         prev_char = message[idx - 1] if idx > 0 else sym
#
#         if sym == " " and next_char == " ":
#             del message[idx]
#         if sym == " " and prev_char == " ":
#             del message[idx]
#
#     message = "".join(message)
#     return message
#
# print(strip("   Hello how   do you    feel?   "))

# # Task
# def c_to_f(c):
#     result = (c * (9/5)) + 32
#     return f'{result:.1f}'
#
# print(c_to_f(5))

# Task
def speed_to_pace(speed):
    pace_minutes = 60 / speed
    minutes = int(pace_minutes)
    seconds = round((pace_minutes - minutes) * 60)

    return f"{minutes}:{seconds:02d}"
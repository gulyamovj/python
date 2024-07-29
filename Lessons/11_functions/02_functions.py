# # Lesson
# def get_min_item(items):
#     if not items:
#         return None
#
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
# items3 = []
#
#
# print(get_min_item(items1))
# print(get_min_item(items2))
# print(get_min_item(items3))

# # Task
# def sum_mult_index(nums):
#     result = 0
#     for idx, num in enumerate(nums):
#         result += idx * num
#
#     return result
#
# print(sum_mult_index([11, 22, 33, 44, 55]))

# Task
def wellcome(name):

    woman_names = []
    man_names = []

    for i in open("woman.txt", "r", encoding='utf-8'):
        woman_names.append(i.strip())

    for i in open("man.txt", "r", encoding='utf-8'):
        man_names.append(i.strip())

    if name in woman_names:
        return f"Уважаемая {name}!"
    elif name in man_names:
        return f"Уважаемый {name}!"
    else:
        return f"Здравствуйте, {name}!"
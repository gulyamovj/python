# # Lesson
# print("a", "b", "c", "d")
#
# def mult(*digits):
#     result = 1
#     for i in digits:
#         result *= i
#     return result
#
# print(mult(5, 20))

# # Task
# def series_connection(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# r = series_connection(1, 1.2, 1.4, 1.6)
# print(r)

# # Task
# def parallel_connection(*arg):
#     result = 0
#     for a in arg:
#         result += 1 / a
#     return round(1 / result, 3)
#
# print(parallel_connection(2, 6))

# # Task
# def sm(*digits):
#     if len(digits) == 0:
#         return 0
#     return sum(digits)
#
# print(sm())

# # Task
# def path(*args):
#     text = ""
#     for i in args:
#         text += "/" + i
#     return text
#
# print(path("var", "www", "marg"))

# # Task
# def usm(*args):
#
#     first_arg = args[0]
#
#     if isinstance(first_arg, (int, float)):
#         total = 0
#         for el in args:
#             total += int(el)
#     else:
#         total = ""
#         for el in args:
#             total = str(total) + str(el)
#
#     return total
#
# print(usm("4", 1, 5, 9))

# Task
def get_chars(*args):

    text = args[0]
    result = []
    for i in args[1:]:
        result.append(text[i])

    return "".join(result)

print(get_chars("I am Programmer", 0, 2, 4, 6))
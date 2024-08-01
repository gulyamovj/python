# # Lesson
# def func(arg1, arg2):
#     arg1 = 20
#     arg2 = arg2[:]
#     arg2[0] = 100
#     print(arg1)
#     print(arg2)
#
# ten = 10
# l = [1, 2, 3, 4, 5]
#
# func(ten, l)
# print(ten)
# print(l)

# Task
def products_range(products_on_page, page):
    products = products_on_page * page
    start_page = products - products_on_page
    return start_page, products
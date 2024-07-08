# revenues = [
#     [500, 500, 600, 600, 450, 500, 700, 600, 650, 700, 750, 700],
#     [600, 650, 300, 700, 750, 500, 800, 850, 900, 900, 750, 800],
#     [900, 800, 700, 600, 750, 850, 950, 900, 900, 700, 700, 600]
# ]
#
#
# min_month_revenue = float("inf")
#
# for year_revenue in revenues:
#     for month_revenue in year_revenue:
#         min_month_revenue = min(min(year_revenue), min_month_revenue)
# print(min_month_revenue)

# # Task
# users = [
#     {"email": "user1@domain.com", "password": "password1"},
#     {"email": "user2@domain.com", "password": "abcde"},
#     {"email": "user3@domain.com", "password": "123456"},
#     {"email": "user4@domain.com", "password": "lovelove"},
#     {"email": "user5@domain.com", "password": "kdmUdmk84M"},
#     {"email": "user7@domain.com", "password": "123456"},
#     {"email": "user8@domain.com", "password": "123456"},
#     {"email": "user9@mail.com.ru", "password": "password9"}
# ]
#
# in_email = input().lower()
# in_pass = input()
#
# result = "Пользователь не найден"
#
# for user in users:
#     if in_email == user["email"]:
#         if in_pass == user["password"]:
#             result = "Доступ открыт"
#             break
#         elif in_pass != user["password"]:
#             result = "Доступ закрыт"
#             break
#
# print(result)

# # Task
# products = [
#     {"name": "Гречка", "price": 69},
#     {"name": "Хлеб", "price": 34},
#     {"name": "Молоко", "price": 57},
#     {"name": "Яйца", "price": 78},
#     {"name": "Рис", "price": 88},
#     {"name": "Макароны", "price": 49},
#     {"name": "Сахар", "price": 22},
#     {"name": "Яблоки", "price": 79},
#     {"name": "Картофель", "price": 18},
#     {"name": "Свинина", "price": 120},
#     {"name": "Масло", "price": 66},
#     {"name": "Помидоры", "price": 64}
# ]
#
# amount = int(input())
#
# my_products = []
#
# for product in products:
#
#     if amount >= product['price']:
#         amount = amount - product['price']
#         my_products.append(product['name'])
#     elif amount < product['price']:
#         continue
#     else:
#         break
#
# print(', '.join(my_products))

# Task
users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 28,  "lang": "java",   "active": False},
    {"id": 21,  "lang": "java",   "active": True},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True},
    {"id": 65,  "lang": "php",    "active": True},
]



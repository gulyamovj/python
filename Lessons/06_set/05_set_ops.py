# # Lesson Диаграмма Венна
# names1 = {"Ivanov", "Lunin", "Varlamov", "Orlov"}
# names2 = {"Lunin", "Varlamov", "Ivanov", "Grekov", "Rossum"}
#
# # РАЗНОСТЬ
# # Метод 1
# print(names1 - names2)
#
# # Метод 2
# uniq_names = names1.difference(names2)
# print(uniq_names)
#
# # ПЕРЕСЕЧЕНИЕ
# # Метод 1
# print(names1 & names2)
#
# # Метод 2
# common_names = names1.intersection(names2)
# print(common_names)
#
# # ОБЪЕДИНЕНИЕ
# # Метод 1
# print(names1 | names2)
#
# # Метод 2
# all_names = names1.union(names2)
# print(all_names)
#
# # СИММЕТРИЧНАЯ РАЗНОСТЬ (УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ, НЕ В ОБОИХ СРАЗУ)
# # Метод 1
# print(names1 - names2 | names2 - names1)
# print(names2 ^ names1) # Симметричная разность (Возвращает уникальные элементы)
#
# # Метод 2
# all_names = names1.symmetric_difference(names2)
# print(all_names)

# # Task
# import sys
# my_card = {17, 29, 1, 56, 83}
#
# game_numbers = sys.stdin.read().splitlines()
# game_numbers = list(map(int, game_numbers))
# game_numbers = set(game_numbers)
#
# print(my_card == game_numbers)

# # Task
# import sys
# products_list = {
#     "Молоко",
#     "Яйца",
#     "Хлеб"
# }
#
# purchased = set(sys.stdin.read().splitlines())
# result = list(products_list - purchased)
# result.sort()
#
# print(", ".join(result))

# # Task
# GUEST = {"Иванов", "Петр", "Сергеевич"}
# new_date = input()
# new_date = set(new_date.split())
# print(new_date == GUEST)

# # Task
# import sys
# my_list = ["Бананы", "Хлеб", "Молоко"]
# new_products = sys.stdin.read().splitlines()
#
# my_list = set(my_list)
# new_products = set(new_products)
#
# to_buy = my_list.union(new_products)
# to_buy = list(to_buy)
# to_buy.sort()
#
# print("\n".join(to_buy))

# # Task
# import sys
# # Мой список игр
# my_games = ["It Takes Two", "Overcooked", "Unravel Two", "Halo"]
#
# friend_games = set(sys.stdin.read().splitlines())
# final_games = list(set(my_games).intersection(friend_games))
# final_games.sort()
# print("\n".join(final_games))

# # Task
# pl1 = input()
# pl2 = input()
#
# pl1_file = set(open(pl1).read().splitlines())
# pl2_file = set(open(pl2).read().splitlines())
#
# result = list(pl1_file & pl2_file)
# result.sort()
#
# print("\n".join(result))

# # Task
# g1 = input()
# g2 = input()
#
# g1_f = set(open(g1).read().splitlines())
# g2_f = set(open(g2).read().splitlines())
#
# result =  list(g1_f | g2_f)
# result.sort()
#
# print("\n".join(result))

# # Task
# books_1 = input()
# books_2 = input()
#
# b1_file = open(books_1).read().splitlines()
# b2_file = open(books_2).read().splitlines()
#
# b1_file = set(b1_file)
# b2_file = set(b2_file)
#
# restult = list(b1_file - b2_file | b2_file - b1_file)
# restult.sort()
#
# print("\n".join(restult))

# # Task
# new_books = {"Мастер и Маргарита", "Отцы и дети", "Ревизор"}
# cafe = "c1.txt"
# cafe_file = set(open(cafe).read().splitlines())
# result = list(new_books - cafe_file)
# result.sort()
#
# print("\n".join(result))

# Task
FOR_SWIMMING = {"Шапочка", "Очки", "Плавки", "Сланцы", "Мочалка", "Мыло", "Полотенце"}
import sys

my_stuff = set(sys.stdin.read().splitlines())

if my_stuff == FOR_SWIMMING:
    print("Вы готовы!")
else:
    result = list(FOR_SWIMMING - my_stuff)
    result.sort()
    print(", ".join(result))

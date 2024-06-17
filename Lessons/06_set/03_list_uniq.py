# names = ["Oleg", "Nikita", "Yan", "Oleg", "Sofia", "Yan", "Oleg", "Victor"]
#
# names = list(set(names))
# names.sort()
#
# print(", ".join(names))

# # Task
# import sys
# songs = sys.stdin.read().splitlines()
# songs = list(set(songs))
# songs.sort()
# print(", ".join(songs))

# # Task
# fruits = ["Яблоки", "Бананы", "Ананасы", "Киви"]
# new_fruit = input()
# fruits.append(new_fruit)
# fruits = list(set(fruits))
# fruits.sort()
# print(fruits)

# Task
import sys

# Получаем новый список фруктов
new_fruits = sys.stdin.read().splitlines()

# Список фруктов
fruits = ["Яблоки", "Бананы", "Ананасы", "Киви"]

# Добавляем новые фрукты в список
fruits.extend(new_fruits)

# Убираем дубли
fruits = list(set(fruits))

# Сортируем
fruits.sort()

# Выводим
print(fruits)
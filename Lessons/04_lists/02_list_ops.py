# europe = ["Франция", "Англия", "Украина", "Германия", "Польша", "Россия"]
# asia = ["Китай", "Россия", "Япония", "Сингапур", "Казахстан"]
#
# world = europe + asia
# print(world)
#
# revenue = [0] * 12
# revenue[0] = 180000
# print(revenue)

# # Task_01 - Default value
# blank = input()
# numb = int(input())
# new_list = [blank] * numb
# print(new_list)

import sys

params = sys.stdin.read().splitlines()

print(len(params))
print(params)
# i = 5
# while i >= -5:
#     print(i)
#     i -= 1

# Task
# rooms_per_floor = int(input())
# number_of_floors = int(input())
#
# floor = 1
# result = []
#
# while floor <= number_of_floors:
#     room = 1
#     while room <= rooms_per_floor:
#         result.append(f"{floor}{room}")
#         room += 1
#     floor += 1
#
# print(' '.join(result))

# rooms = int(input())
# floors = int(input())
#
# result = []
# floor = 1
#
# while floor <= floors:
#     room = 1
#     while room <= rooms:
#         result.append(f"{floor}{room}")
#         room += 1
#     floor += 1
#
# print(' '.join(result))

# # Task
# max_value = int(input())
# separator = int(input())
#
# result = []
# i = 1
# count = 0
#
# while i <= max_value:
#     result.append(str(i))
#     count += 1
#     if count == separator:
#         result.append("\n")
#         count = 0
#     i += 1
#
# print(" ".join(result).replace(" \n ", "\n").rstrip())

# # Task
# num = ["111", "2", "33", "24"]
#
# elements = 0
#
# while elements <= (len(num) - 1):
#     print(num[elements])
#     elements += 1

import random

def get_choices():
    player_choice = input("Enter a choise (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    if player == computer:
        return "It's a tie!"

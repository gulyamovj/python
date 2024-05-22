# users_file = open('users.txt')
# users = users_file.read().split("\n")
# print(users)

# # Task
# year = int(input())
# population_file = open("population.txt")
# population = population_file.readlines()
# print(population[year - 2003])

# Task
import sys
info = sys.stdin.read().splitlines()

population_file = open("{}".format(info[0]))
population = population_file.readlines()

index = int(info[1]) - int(population[0]) + 1

print(population[index])
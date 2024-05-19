# cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Калининград", "Владивосток", "Киев", "Минск"]
# populations = [1200000, 5300000, 160000, 480000, 605000, 2900000, 2000000]
#
# cities_copy = cities # This is not a copy of the list. This method creates an Alias to the same element in a ram
# cities_copy = cities.copy() # This is a copy of the list
# cities_copy = cities[:] # And this a copy to
#
# print(cities_copy == cities, cities_copy is cities)
#
# print(cities)
# print(cities_copy)

# Task
import sys
assessment = sys.stdin.read().splitlines()
assessment = list(map(int, assessment))
original = assessment[:]
assessment.sort()
new_assessment = assessment[1:len(assessment)-1]
total = sum(new_assessment)
count = len(new_assessment)
average = total / count
print("{} {:.2f}".format(original, average))
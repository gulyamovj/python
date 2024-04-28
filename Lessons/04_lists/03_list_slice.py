# # Особенности срезов в списке
#
# fruits = ["Банан", "Яблоко", "Апельсин", "Ананас", "Груша", "Мандарин", "Киви"]
# fruits[3:5] = ["Лимон", "Грейпфрут", "Лайм", "Персик",]
#
# # Удаление элементов
# fruits[3:5] = []
# del fruits[3:5]
# print(fruits) # Срезы возвращают копии исходного списка и тоже являются списком
#
# # Добавление элементов
# fruits[4:4] = ["Лимон", "Лайм"]
# print(fruits) # Срезы возвращают копии исходного списка и тоже являются списком
#

# # Task List first 3
# import sys
# athletes = sys.stdin.read().splitlines()
# print(athletes[:3])

# # Task List last 3
# import sys
# athletes = sys.stdin.read().splitlines()
# print(athletes[-3:])

# # Task - Change value
# import sys
# new_athlets = sys.stdin.read().splitlines()
# athletes = ['Иванов', 'Ильин', 'Петров', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']
#
# athletes[0:3] = new_athlets
# print(athletes)

# # Task - Del element
# athlet = int(input())
# athletes = ['Иванов', 'Ильин', 'Петров', 'Зинько', 'Сидоров', 'Васильев', 'Литвинов']
# del athletes[athlet]
# print(athletes)

# Task
population = [
    144_963_650,  # 2003
    144_168_205,
    143_474_219,
    142_753_551,
    142_220_968,
    142_008_838,
    141_903_979,
    142_856_536,
    142_865_433,
    143_056_383,
    143_347_059,
    143_666_931,
    146_267_288,
    146_544_710,
    146_804_372,
    146_880_432,
    146_780_720,
    146_748_590  # 2020
]
start = int(input()) - 2003
end = int(input()) - 2002

print(population[start:end])

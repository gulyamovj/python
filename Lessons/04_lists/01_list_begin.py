# # Lesson
# l = [7, "string", 3.14, 7, [12], True]
# l[2] = 3.13159
# l[3] = "Sofie"
# del l[4]
# print(l)

# # Task_1 - Create colors of rainbow
# colors = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]
#
# # Task_2 - Name generator
# first_names = ['Иван', 'Пётр', 'Дмитрий', 'Василий']
# last_names = ['Антонов', 'Шмидт', 'Лебедев', 'Васильев', 'Шиков']
#
# name_index = int(input()) - 1
# last_name_index = int(input()) - 1
#
# result = "{} {}".format(first_names[name_index], last_names[last_name_index])
#
# print(result.upper())

# # Task_3 - Change value by index
# languages = ['Python', 'C++', 'JavaScript', 'Java']
# index = int(input())
# value = input()
# languages[index] = value
# print(languages)

# # Task_3 - Value exchange
# languages = ['Python', 'C++', 'JavaScript', 'Java']
#
# first = int(input())
# second = int(input())
#
# temp = languages[first] # временная переменная для хранения
# languages[first] = languages[second]
# languages[second] = temp
#
# print(languages)

# Task_4 - Value exchange
employees = [
    "Иван Иванов",
    "Василий Смирнов",
    "Ярослав Сидоров",
    "Алексей Федьков",
    "Валерий Алтушев",
    "Дмитрий Петров",
    "Семен Альтов"
]

index = int(input()) - 1001
print(employees[index])

# Тут новый коммент
# # Lesson
# cities = ["Москва", "Санкт-Петербург", "Калининград"]
# populations = [1200000, 5300000, 480000]
#
# # Метод append() добавляет данные в конец и не возвращает значение а только присваивает
# cities.insert(2, "Новосибирск")
# populations.insert(2, 1600000)
#
# new_cities = ["Vladivostok", "Kiev", "Moscow", "Minsk"]
# new_population = [605000, 2900000, 12000000, 2000000]
#
# # Метод extend() склеивает два списка
# cities.extend(new_cities)
# populations.extend(new_population)
#
# cities.extend(["Perm"])
#
# # Remove
# cities.remove("Москва")
#
# # Clear
# populations.clear()
#
# print(cities)
# print(populations)

# # Task
# marks = ["BMW", "Toyota", "Mercedes"]
# new_mark = input()
# marks.append(new_mark)
# print(marks)

# # Task
# val = int(input())
# marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]
# del marks[val]
#
# print(marks)

# # Task
# val = input()
# marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]
# marks.remove(val)
# print(marks)

# Task
index = int(input())
new_country = input()

countries = ["Россия", "Украина", "Беларусь"]
countries.insert(index, new_country)

print(countries)

# There is new comment
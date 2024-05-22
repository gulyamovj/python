first_name = ["Max"]
names = ["Ivan", "Alena", first_name, "Sergey", "Liza"]

names[2] = "Alex"
print(names)
print(first_name)

# Task
q1 = int(input())
q2 = int(input())
q3 = int(input())
q4 = int(input())

# Помещаем значения в список.
year = [q1, q2, q3, q4]

# Вычисляем среднее.
avg = sum(year) / len(year)

# Выводим результат.
print("Средний доход: {0:} руб.".format(avg))
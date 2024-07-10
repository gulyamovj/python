# Task
file_name = input()

balance_file = open(file_name, "r", encoding="utf-8")
result = 0

for line in balance_file.readlines():
    name, count = line.split(";")
    result = result + int(count)

print(result)
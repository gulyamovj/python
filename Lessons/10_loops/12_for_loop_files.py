# # Task
# file_name = input()
#
# balance_file = open(file_name, "r", encoding="utf-8")
# result = 0
#
# for line in balance_file.readlines():
#     name, count = line.split(";")
#     result = result + int(count)
#
# print(result)

# Task
file_name = input()

balance_file = open(file_name, "r", encoding="utf-8")
result = 0

for line in balance_file.readlines():
    product, type, amount = line.split(";")
    if type == "income":
        result += int(amount)
    else:
        result -= int(amount)

print(result)
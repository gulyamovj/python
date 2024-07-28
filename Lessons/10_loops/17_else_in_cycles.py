90  # pupils = [
#     ('Иванов', 'Петр', True),
#     ('Васильвева', 'Мария', True),
#     ('Антонов', 'Леонид', True),
#     ('Смирнов', 'Денис', True),
#     ('Лебедева', 'Алиса', True),
#     ('Никитина', 'Вероника', True),
#     ('Широков', 'Виктор', True)
# ]
#
# for last_name, first_name, duty in pupils:
#     if not duty:
#         new_duty = f'{last_name} {first_name}'
#         break
# else:
#     new_duty = 'Дежурный не найден'
#
# print(new_duty)

# Task

# import sys
#
# numbers = sys.stdin.read().splitlines()
# numbers = list(map(int, numbers))
# result = 0
#
# for i in numbers:
#     if i < 0:
#         result += i
#
# print(result)

# # Task
# text = input().split()
# result = []
#
# for idx, t in enumerate(text):
#     result.append(text[idx][::-1])
#
# print(" ".join(result))

# # Task
# num = int(input())
# i = 1
# while i < 10:
#     # print(f'{num} x {i} = {num * i}')
#     print('{:,} x {} = {:,}'.format(num, i, num * i))
#     i += 1

# # Task
# fn = input()
#
# file = open(fn, 'r')
# lines = file.readlines()
#
# matrix = []
# for line in lines:
#     row = list(map(int, line.split()))
#     matrix.append(row)
#
# trace = 0
# for i in range(len(matrix)):
#     trace += matrix[i][i]
#
# print(trace)

# Task
# word = input()
# vowels = "aeiouy"
# result = []
# for w in word:
#     if w.lower() in vowels.lower():
#         result.append(w)
# print("".join(result))

# # Task
# text = input()
# brackets = []
#
# for char in text:
#     if char == "(":
#         brackets.append(char)
#     elif char == ")":
#         if not brackets:
#             print(0)
#             exit()
#         brackets.pop()
#
# if not brackets:
#     print(1)
# else:
#     print(0)

## Task
# text = input()
# brackets = 0
#
# for i in text:
#     if i == "(":
#         brackets += 1
#         print(brackets)
#     elif i == ")":
#         brackets -= 1
#         print(brackets)
#
#     if brackets < 0:
#         break
#
# if not brackets:
#     print("1")
# else:
#     print("0")

# # Task
# import sys
#
# num = sys.stdin.read().splitlines()
# num = list(map(int, num))
# prev_num = 0
# key = True
#
# for i in num:
#     if i > prev_num:
#         key = True
#     elif i < prev_num or i == prev_num:
#         key = False
#
#     if key == False:
#         break
#
#     prev_num = i
#
# if key:
#     print(1)
# elif not key:
#     print(0)

# # Task
# import sys
#
# nums = sys.stdin.read().splitlines()
# nums = list(map(int, nums))
#
# path = []
# visited = set()
#
# current_index = 0
#
# for _ in range(len(nums)):
#     if current_index in visited:
#         path.append(current_index)
#         break
#     path.append(current_index)
#     visited.add(current_index)
#     current_index = nums[current_index]
#
# print(" ".join(map(str, path)))

# # Task
# n = int(input())
# current_numb = 1
# i = 1
#
# while current_numb <= n:
#     row = []
#     for _ in range(i):
#         if current_numb > n:
#             break
#         row.append(str(current_numb))
#         current_numb += 1
#     print(" ".join(row))
#     i += 1
#
# # Task
#
# custumers_ages = input().split()
# custumers_ages = list(map(int, custumers_ages))
#
# max_value = max(custumers_ages)
# max_value_index = custumers_ages.index(max_value)
#
# del custumers_ages[max_value_index]
#
# custumers_ages.insert(0, max_value)
#
# print(" ".join(map(str, custumers_ages)))

# revenues = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
#
# prev_revenue = 0
#
# for idx, revenue in enumerate(revenues):
#     next_revenue = revenues[idx+1] if idx < len(revenues) - 1 else 0
#     prev_revenue = revenues[idx-1] if idx > 0 else 0
#     print(prev_revenue, revenue, next_revenue)

# # Task
#
# nums = [2, 5, 4, 0, 1, 6, 3]
#
# path = []
# visited = set()
#
# current_index = nums[0]
#
# for _ in range(len(nums)):
#     if current_index in visited:
#         break
#     path.append(current_index)
#     visited.add(current_index)
#     current_index = nums[current_index]
#
# print(" ".join(map(str, path)))



# # Task
#
# fn = "bank.txt"
#
# balances = {}
#
# for line in open(fn):
#     from_account, to_account, amount = line.split(";")
#     amount = int(amount)
#
#     if from_account != '000':
#         if from_account in balances:
#             balances[from_account] -= amount
#         else:
#             balances[from_account] = -amount
#
#     if to_account != '000':
#         if to_account in balances:
#             balances[to_account] += amount
#         else:
#             balances[to_account] = amount
#
#
# if '000' in balances:
#     del balances['000']
#
# sorted_accounts = sorted(balances.items(), key=lambda x: x[1])
#
# result = ";".join(f'{account} {balance}' for account, balance in sorted_accounts)
#
# print(result)


# Task
import sys
nums = sys.stdin.read().splitlines()
nums = list(map(int, nums))

current = nums[0]
values = []

for i in range(len(nums)):
    if current in values:
        values.append(current)
        break
    if nums[0] == 0:
        values.append(current)
        break
    values.append(current)
    current = nums[current]

print(" ".join(map(str, values)))






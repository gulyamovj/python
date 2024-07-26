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

# Task
n = int(input())
current_numb = 1
i = 1

while current_numb <= n:
    row = []
    for _ in range(i):
        if current_numb > n:
            break
        row.append(str(current_numb))
        current_numb += 1
    print(" ".join(row))
    i += 1

# Task

custumers_ages = input().split()
custumers_ages = list(map(int, custumers_ages))

max_value = max(custumers_ages)
max_value_index = custumers_ages.index(max_value)

del custumers_ages[max_value_index]

custumers_ages.insert(0, max_value)

print(" ".join(map(str, custumers_ages)))


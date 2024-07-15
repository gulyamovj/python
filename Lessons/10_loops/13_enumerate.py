# months = ["январь", "февраль", "март", "апрель", "май", "июнь",
#          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь",]
#
#
# # Классический вариант
# counter = 0
# for month in months:
#     print(counter, month)
#     counter += 1
#
# # Вариант через range
# for month_idx in range(len(months)):
#     month = months[month_idx]
#     print(month_idx + 1, month)
#
# # Вариант через enumerate
# for counter, month in enumerate(months):
#     print(counter, month)
#
#
# # Вывод кварталов
# for counter, month in enumerate(months, start=1):
#     if counter % 3 == 1:
#         print("Квартал", counter // 3 + 1)
#     print("    {}".format(month))

# # Task
# text = input()
#
# result = []
# i = 0
# while i < len(text):
#     if text[i] in '.!?':
#         if i > 0 and text[i-1] == ' ' and (i == 1 or text[i-2] != ' '):
#             result.pop()
#         result.append(text[i])
#     else:
#         result.append(text[i])
#     i += 1
#
# print(''.join(result))

# Task
files_count = 3
text = "Программирование"
text = list(text)
a = []
x = 0
i = 0

while x < files_count:
    while i < len(text):
        a.append(text[i])
        i += files_count
    x += 1
    i = x
    b = open("data-{}.txt".format(i),  "w", encoding="utf-8")
    b.write("".join(a))
    a = []
    b.close()
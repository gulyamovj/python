# age = 18
#
# if age > 18:
#     credit = True
# else:
#     credit = False
#
# print(credit)
#
# # Упрощенная версия
# credit = True if age > 18 else False

# # Task
# text = input().upper()
# text_rotated = text[::-1]
# result = 1 if text == text_rotated else 0
# print(result)

# # Task
# start_day = int(input())
# year_day = int(input())
#
# week = ((year_day - start_day) // 7) + 1
#
# if start_day <= year_day:
#     print(week)
# else:
#     print(-1)

# Task
sec = int(input())

hours = sec // 3600
minutes = sec % 3600 // 60
seconds = sec % 60

if hours > 0:
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

elif hours <= 0 and minutes > 1:
    print(f"{minutes:02d}:{seconds:02d}")

elif minutes <= 0:
    print(f"{seconds:02d}")
else:
    print(f"{minutes:02d}:{seconds:02d}")
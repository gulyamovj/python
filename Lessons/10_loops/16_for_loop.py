# revenues = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
# prev_revenue = 0
# for idx, revenue in enumerate(revenues):
#     next_revenue = revenues[idx + 1] if idx < len(revenues) - 1 else 0
#     prev_revenue = revenues[idx - 1] if idx > 0 else 0
#     print(prev_revenue, revenue, next_revenue)


# # Task
# import sys
# revenue = sys.stdin.read().splitlines()
# prev_rev = 0
# result = []
#
# for i in revenue:
#     result.append(int(i) - prev_rev)
#     prev_rev = int(i)
#
# final = []
#
# for en in result:
#     final.append(str(en))
#
# print(" ".join(final))

# # Task
# input_str = input()
#
# chars = list(input_str)
#
# for i in range(0, len(chars) - 1, 2):
#     chars[i], chars[i + 1] = chars[i + 1], chars[i]
#
# print("".join(chars))

# Task
import sys
input_num = sys.stdin.read().splitlines()
input_num = list(map(int, input_num))

result = []

for i, n in enumerate(input_num):
    prev_n = input_num[i - 1] if i > 0 else 0
    if n > prev_n:
        result.append("green")
    elif n < prev_n:
        result.append("red")
    else:
        result.append(result[i-1] if i > 0 else "green")

print(" ".join(result))
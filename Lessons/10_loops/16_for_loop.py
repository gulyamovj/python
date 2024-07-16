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

# Task

chars = ["A", "B", "C", "D", "E", "F"]
prev_char = chars[0]
result = []

for idx, char in enumerate(chars):
    prev_char = chars[idx-1] if idx > 0 else chars[idx]

    print(idx, char, prev_char)

print(result)
# # Lesson
# reveue = [211_000, 135_000, 155_000, 120_000, 78_000, 160_000,
#           209_000, 164_000, 169_000, 236_000, 188_000, 193_000]
#
# print(len(reveue))
# print(min(reveue))
# print(max(reveue))
# print(sum(reveue[6:]))

# # Task
# import sys
# list = sys.stdin.read().splitlines()
# print(len(list))

# # Task - Tax for the year
# revenue = [178, 351, 145, 764, 514, 456,
#            411, 145, 275, 245, 441, 716]
#
# tax = int(input())
# print(sum(revenue) * tax / 100)

# # Task - quarterly revenue
# import sys
# revenue = [178, 351, 0, 764, 514, 0,
#            411, 145, 0, 245, 441, 0]
#
# values = sys.stdin.read().splitlines()
# revenue[2] = int(values[0])
# revenue[5] = int(values[1])
# revenue[8] = int(values[2])
# revenue[11] = int(values[3])
#
# print(sum(revenue[:3]),\
#       sum(revenue[3:6]),\
#       sum(revenue[6:9]),\
#       sum(revenue[9:]))

# # Task Average value
# values = [184.414, 174.12, 581, 145.98, 159.1, 824.24]
# new_value = float(input())
# values += [new_value]
# result = sum(values) / len(values)
# print("{:.3f}".format(result))

# Task
import sys
values = sys.stdin.read().splitlines()
values_list = list(map(int, values))
print(max(values_list))
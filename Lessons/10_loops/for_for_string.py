# word = "программа"
#
# syllables = 0
# for char in word:
#     syllables += char in "аоиыеэяёую"
#
# print(syllables)

# # Task
# message = input()
# numbers = ""
#
# for m in message:
#     if m in "1234567890":
#         numbers += m
#
# print(numbers)


# # Task
# symbolls = input()
#
# alphabet = "abcdefghiklmnopqrstuvwxyz"
# alphabet_upper = alphabet.upper()
#
# sorted_small = ""
# sorted_upper = ""
#
# for symbol in symbolls:
#     if symbol in alphabet:
#         sorted_small += symbol
#     elif symbol in alphabet_upper:
#         sorted_upper += symbol
#
# print(sorted_small + sorted_upper)

#
# # Task
# import sys
# digits = sys.stdin.read().splitlines()
#
# negative, positive = [], []
#
# for digit in digits:
#
#     if int(digit) < 0:
#         negative.append(digit)
#
#     elif int(digit) >= 0:
#         positive.append(digit)
#
# print(" ".join(negative + positive))
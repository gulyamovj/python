# # Lesson
# from datetime import date
# today = date.today()
#
# data = ["ОЛ-17.12", 12000, today]
# sale = 0.1
# final_price = round(data[1] * (1 - sale))
#
# product_template = f"Schet: {data[0].lower()}\n"+\
#                    f"Summ: {final_price:,} rub\n".replace(","," ")+\
#                    f"Date: {data[2]}"
#
# print(product_template)
#
# # Task
# import sys
#
# # Список транзакций
# transactions = sys.stdin.read().splitlines()
#
# # Выводим информацию о последней операции
# print(f"Последняя операция: {float(transactions[-1]):.2f} руб.")


# # Расчет стоимости товара
# current_price = 6000000
# inflation = 0.0877
# years = 10
#
# price = current_price * ((1 + inflation) ** years)
# print(f"Товар на ${current_price:,} через {years} года (лет) будет: ${price:,.0f}")

# # Task
# import sys
#
# # Список транзакций
# transactions = sys.stdin.read().splitlines()
#
# # Вычесляем последнюю инфориацию
# last_operation = transactions[-1]
#
# number, amount = last_operation.split(":")
#
# # Выводим информацию о последней операции
# print(f'Последняя операция {number} на {float(amount):.2f} руб.')

# ------------
# Extra tasks
# ------------

# # Task 1
# text = input()
# text = list(text)
# text.sort(key=str.lower)
# text = "".join(text)
# print(text)

# # Task 2
# word = input()
# word = list(set(word))
# word.sort(key=str.lower)
# word = ''.join(word)
# print(word)

# # Task 3
# f1 = input()
# f2 = input()
# f3 = input()
#
# file_1 = open(f1).read().splitlines()
# file_2 = open(f2).read().splitlines()
# file_3 = open(f3).read().splitlines()
#
# all_products = file_1 + file_2 + file_3
#
# dublicates_removed_list = list(set(all_products))
# dublicates_removed_list.sort()
#
# my_list = "\n".join(dublicates_removed_list)
#
# print(my_list)

# Task 4
words = input()
words = words.\
    replace('.', "").\
    replace(',', "").\
    replace('!', "").\
    replace('?', "")

words = words.split()

print(len(words))
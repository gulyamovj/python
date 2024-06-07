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

# Task
import sys

# Список транзакций
transactions = sys.stdin.read().splitlines()

# Выводим информацию о последней операции
print(f"Последняя операция: {float(transactions[-1]):.2f} руб.")
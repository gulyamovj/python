# # Lesson
# user = {
#     "name": {"first":"Anton"},
#     "price": [3000, "rub"],
#     "sale": .3
# }
#
# hello_template = "Zdravstvuyte, {name[first]}!\n" \
#                  "Stoimost tovara: {price[0]} {price[1]}.\n" \
#                 "Vasha skidka: {sale:.0%}."
#
# print(hello_template.format(**user))

# Task
# Формируем словарь.
mountain = {
   "name": input(),
   "high": {
      "m":  int(input()),
      "ft": int(input())
      }
}

# Сформируйте шаблон ниже.
m_template = "{name} - {high[0]} м ({high[1]} ф)"

# Форматируем строку данными из словаря.
print(m_template.format(**mountain))
# # Lesson
# phone = "89513658483"
# full_name = "Ivanov Andrey Petrov"
# ip = "127.0.0.1"
#
# phone_list = list(phone)
# print(phone_list)
#
# fio = full_name.split(" ")
# print(fio)
#
# ip = ip.split(".")
# print(ip)
#
# last_name, first_name, patronymic = full_name.split() # Распаковка списка
#
# print(last_name)
# print(first_name)
# print(patronymic)

# # Task 01
# # Напишите программу, которая принимает фамилию,
# # имя и отчество записанные в одну строку, а затем
# # выводит данные в формате: Фамилия И. О.
#
# # Учитывайте следующие особенности получаемых данных:
# # между словами может быть любое количество пробелов,
# # а сами слова могут быть набраны в разных регистрах.
# # При этом выводить их нужно в формате, описанном выше.
#
# # Simple inpute
# # Иванов Дмитрий Петрович
#
# # Sample Output:
# # Иванов Д. П.
#
# user = input()
# last_name, name, patronymic = user.split()
# print(f"{last_name.capitalize()} {name[0].capitalize()}. {patronymic[0].capitalize()}.")
#################################

# # Task 02
# # Самое длинное слово
# # Напишите программу, которая через stdin принимает строку
# # со списком слов, разделенных пробелом, а после выводит самое
# # длинное из этих слов.
#
# # Sample Input:
# # кошки собаки пингвины зебры
#
# # Sample Output:
# # пингвины
#
# words = input()
# words = words.split()
# words.sort(key=len)
# print(words[-1])
#################################

# # Task 02
# # Новые товары
# # Ниже в редакторе кода содержится список товаров — products.
# # Напишите программу, которая принимает из stdin один параметр —
# # строку продуктов разделенных запятой с пробелом. Эти продукты
# # нужно добавить в исходный список, а затем отсортировать его и вывести.
#
# # Sample Input:
# # апельсины, ватрушки
#
# # Sample Output:
# # ['ананас', 'апельсины', 'ватрушки', 'макароны', 'помидоры', 'яблоки']
#
# new_products = input()
# products = ["ананас", "макароны", "помидоры", "яблоки"]
# products.extend(new_products.split(", "))
# products.sort()
# print(products)

# Task 03
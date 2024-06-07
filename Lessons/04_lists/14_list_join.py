# # Lesson
# product = ["moloko", "maslo", "smetana", "slivki", "kefir", "sir"]
# name = "products"
# name = list(name)
# name[0] = "P"
# name = "".join(name)
# print(name)
#
# s_products = "\n".join(product)
# print(s_products)

# # Task
# file_name = input()
# file_name = file_name.split()
# file_name = "_".join(file_name)
# print(file_name)

# # Task
# pets = input()
# pets = pets.split(", ")
# pets.reverse()
# pets = ", ".join(pets)
# print(pets)

# # Task Человекопонятный URL
# url = input()
# url = url.split()
# url = "-".join(url)
# url = url.replace(":","")
# url = url.strip("?")
# print(url.lower())

# # Task
# ing = "булочки,  пирожки,печенье"
# ing = ing.split(",")
# ing = ", ".join(ing)
# ing = ing.capitalize()
# index = ing.index(",", ing.index(",")) + 1
# new_ing = ing[:index] + ing[index:].replace(",", " и") + "."
# print(new_ing)

# Task
fn = 'products-1.txt'

# Открываем файл
products_file = open(fn)

# Читаем файл
products = products_file.read().splitlines()

# Сортируем файл
sorted_product = sorted(products)

# Преобразовываем в текст и сохраняем в оперативке
sorted_product = "\n".join(sorted_product)

# Закрываем файл в режиме чтения
products_file.close()

# Открываем файл в режиме записи (Все удалится)
products_file = open(fn, "w")

# Записываем соритрованный список продуктов
products_file.write(sorted_product)

# Закрываем файл
products_file.close()
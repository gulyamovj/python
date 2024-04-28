# source_fn = "source.txt"
# destination_fn = "destination.txt"
#
# source = open(source_fn, "r", encoding="koi8-r")
# source_readed = source.read()
#
# destination = open(destination_fn, "a", encoding="cp1251")
# destination.write(source_readed)
#
# source.close()
# destination.close()

# # Rewriting files KEY => r+
# products_file = open("shopping_list.txt", encoding="utf-8")
# products = products_file.read().strip()
# products = products.replace("масло", "").title()
# # print(products)
# products_file.close()
#
# new_product_files = open("shopping_list.txt", "w")
# new_product_files.write(products)
# new_product_files.close()

# # Creat a document
# html = open("index.html", "w")
# html.write("<html><head></head><body></body></html>")
# html.close()

# fn = "template-1.txt"
# name = "Никита"
#
# file = open(fn)
# file_content = file.read().replace("{{ name }}", name)
# file.close()
#
# file = open(fn, "w")
# file.write(file_content)
# file.close()

# file = open("index.html", "w")
# file.close()

# year = "2023"
#
# q1 = f"q1-{year}.txt"
# q2 = f"q2-{year}.txt"
# q3 = f"q3-{year}.txt"
# q4 = f"q4-{year}.txt"
#
# quarter_1 = open(q1)
# q1_r = quarter_1.read()
#
# quarter_2 = open(q2)
# q2_r = quarter_2.read()
#
# quarter_3 = open(q3)
# q3_r = quarter_3.read()
#
# quarter_4 = open(q4)
# q4_r = quarter_4.read()
#
# new_year = open(f"year-{year}.txt", "w")
# new_year.write(str(int(q1_r) + int(q2_r) + int(q3_r) + int(q4_r)))
# new_year.close()

# fn = "products.txt"
#
# file = open(fn, "r", encoding="cp1251")
# values = file.read()
# file.close()
#
# file = open(fn, "w", encoding="utf8")
# file.write(values)
# file.close()
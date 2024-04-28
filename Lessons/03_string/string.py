# # Строки записываются в ковычках
# text = "Programming its good!"
#
# print(text)
#
# # вычесление длины строки
# print(len(text))
#
# # получение символа по индексу
# print(text[0])
#
# # обратный порядок по индексу (идем в минус)
# print(text[-1])
#
# # ЗАДАЧА - Вывести первую и последнюю букву из слово
#
# my_str = "Python"
#
# print(my_str[0], my_str[-1])
#
# # ЗАДАЧА - Вывести среднюю букву
#
# text = "Maftuna"
# middle = (len(text) - 1) // 2
# print(text[middle])
#
#
# # 2.6 Склейка строк и функция print
# lang1 = "python"
# lang2 = "javascript"
# lang3 = "php"
#
# langs = lang1 + ', ' + lang2 + ', ' + lang3
# print(langs)
# print(lang1, lang2, lang3, sep=", ", end=".\n")
# print("-" * len(langs))
#
# # Срезы –> [:]dd
# card_number = "1211344443554467"
# print(card_number[1 : 4]) # Срез
# print(card_number[-4:len(card_number)]) #-4 - обратная индексация
# print(card_number[-4:]) #если не писать второе значение то срез будет браться до конца
# print(card_number[:4]) #если не писать первое значение то срез начнется с нулевого индекса
#
# # Получаем первую четверку
# print(card_number[:4])
#
# # Получаем вторую четверку
# print(card_number[4:8])
#
# # Получаем третью четверку
# print(card_number[8:-4])
#
# # Получаем последнюю четверку
# print(card_number[-4:])
#
# # Вывод со звезчоками
# print(("*" * 12) + card_number[-4:])
#
# # Task
# car_numb = "c064mk78"
# print(car_numb[1:4])
#
# text = "I'm good programmer"
# print(text[:10] + "...")
#
# file_format = "my_car.png"
# print(file_format[-3:])
#
# file_name = "my_car.png"
# print(file_name[:-4])
#
# phone = "+71112223344"
# phone_hidden = phone[:6] +("?" * 5) + phone[-2:]
# print(phone_hidden)
#
# number = "81112223344"
# print("+7 " + "(" + number[1:4] + ") " + number[4:7] + "-" + number[7:9] + "-" + number[9:12])
#
# print("-" * 40)
#
# phone = "leefmu lmunlee mun."
# phone = phone.replace("lee", "8")
# phone = (phone.
#          replace("lee","8").
#          replace("a","0").
#          replace(" ", "1").
#          replace("b","2").
#          replace("x","3").
#          replace("l","4").
#          replace("mu","5").
#          replace("n","6").
#          replace("o","7").
#          replace("f","9"))
#
# print(phone)
#
# 89514568156

#
# html = input()
# new_text = input()
# open = html.find("<h1>")
# close = html.find("</h1>")
# result = html[:open + 4] + new_text + html[close:]
#
# print(result)

# file_name = "my_car.png"
# file_extansion = file_name.rfind(".")
# result = file_name[file_extansion + 1:]
# print(result.lower())


# domain1 = "www.yandex.ru"
# domain2 = "www.youtube.com"
# domain3 = "www.rutracker.org"
# domain4 = "yandex.ua"
#
# print(domain1.islower())
# print(domain2.islower())
# print(domain3.isupper())
# print(domain4.isupper())

# number = "+79511234455"
# result = not number.startswith("+7")
# print(result)
#
# file_name = "photo.png"
# result = file_name.lower().endswith(".png")
# print(result)


# file_name = "photo.jpeg"
# print(file_name.lower().endswith(".png") or \
#       file_name.lower().endswith(".jpeg") or \
#       file_name.lower().endswith(".jpg") or \
#       file_name.lower().endswith(".gif"))
#
# lang1 = "Языки: \n\tpython \n\tjavascript \n\tsql"
# lang2 = "javascript"
# lang3 = "sql"
#
# print(lang1)
#
# html = "Leading growth:<br>why strategy matters"
# html = html.replace("<br>", "\n")
# print(html)
#
# lang = "python"
# some_text = ("this is some "
#              "here is "
#              "text".upper())
# some_text2 = ("and " +
#               "this is some " +
#               "text too ".upper())
#
# print(some_text)
# print(some_text2)
#
# text = ".Понимание strip... .?!"
# text = text.strip("!. ?") # Каждый знак работает индивидуально!!!!
# print(text)
#
# domain = "www.weekend.moscow"
# print(domain.strip("w . "))

# car_num = "AC8761BCA"
# car_num = car_num.strip("E T O P A H K C B M Y X")
# print(car_num)

# numb = "78.4500"
# numb = numb.rstrip("0")
# print(numb)

# salary = "50000"
# year_salary = float(salary) * 12
# print("Ваша годовая зарплата: " + str(year_salary))

# numb = int("81")
# sqrt = int(numb ** 0.5)
# square = int(numb ** 2)
# print(sqrt, numb, square, sep=",")

# m = int("10")
# h = int("10")
# g = 9.8
# result = m * h * g
# print(int(result))


# rubl = "64,66"
# usd = "12"
# rubl = float(rubl.replace(",", "."))
# print(usd + " долларов в рублях = " + str(int(usd) * rubl) + " руб.")


# amount = "mmwmwwmwwwmmw"
# m = amount.count("m")
# w = amount.count("w")
# print("m " + "(" + str(m) + ") " + str("*" * m) )
# print("w " + "(" + str(w) + ") " + str("*" * w) )

# age = 18
# name = "Jack"
# text = "Hi my name is %s I'm %d years old" % (name, age) # Форматирование строк (%d - спецификатор)
# print(text)

# distance = float("60.2")
# time = float("1.5")
# speed = distance / time
# print("%.2f" % speed)

# A = float("17.3")
# B = float("22.6")
# C = float("7.34")
#
# print("%+d°...%+d°, %.1f м/с" % (A, B, C))

# price = "1250"
# print("Итого: %7d руб." % int(price))

# naming = "Бампер передний"
# quantity = float("1")
# price = float("12000")
# amount = int(price * quantity)
#
# print("| %-30s | %-6d | %-10d | %12d |" % (naming, quantity, price, amount))

# age = 18.54
# name = "James"
# age_str = "Hi my name is {}. I'm {:.1f} years old".format(name, age)
# print(age_str)
#
# last_name = "Иванов"
# name = "Ivan"
# year = "1994"
#
# print("| {last_name:<8s} | {name:<8s} | {year:>6s} |".format(last_name = last_name, name = name, year = year))


# text = "Основной заголовок"
# print("{line}\n| {text:^27s} |".format(text=text, line="+{}+".format("-" * len(text))))

# text = "| {:^27} |".format(text)
# print("+" + "-" * (len(text) - 2) + "+")
# print(text)
# print("+" + "-" * (len(text) - 2) + "+")


# text = "I'm good programmer"
# print("{:.10s}{}".format(text, "..."))

# grade1 = float("8.741")
# grade2 = float("8.85")
# print("{last_grade:.2f} ({difference:+.2f})".format(last_grade=grade2, difference = grade2 - grade1))

# num = float("178.451")
# result = "{:0>9.2f}".format(num)
# print("{:.>16}".format(result))

# from datetime import datetime
# now = datetime.now()
# print(now)
#
# print("{:%d.%m.%Y}".format(now))

# numb = 10
# print("{1:d} {0:b} {0:o} {0:x}".format(numb, numb))

# # Цена со скидкой
# product = input()
# price = float(input())
# discount = float(input())
# new_price = price - price * discount
# print(f"{product}: {price:.2f} - {discount * 100:.0f}% = {new_price:.2f}")

# # Корреспондентский счет
# number = "30101810100000000634"
# input(f"{number[0:5]} {number[5:8]} {number[8:9]} {number[9:13]}")
# Последовательность произвольных объектов. Отличие от списков, кортежи нельзя изменять

animals = ("xomyak", ("koshka", ), "xoryok", "krisa")

animals[1][0] = "sobaka"
print(animals[1][0])
print(animals)
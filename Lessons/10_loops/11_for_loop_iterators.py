names = ["Ivan", "Nikita", "Ilya", "Viktor", "Alena", "Svetlana"]

for name in names:
    print(name)

print()

# names_iter = names.__iter__() # Объект итератор
# print(names_iter.__next__())
# print(names_iter.__next__())
# print(names_iter.__next__())
# print(names_iter.__next__())
# print(names_iter.__next__())
# print(names_iter.__next__())

digits = range(5)
digits_iter = iter(digits)
print(next(digits_iter))
print(next(digits_iter))
print(next(digits_iter))
print(next(digits_iter))
print(next(digits_iter))
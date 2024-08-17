# Lesson
class Auto:
    # Функции внутри класса называются Методами класса
    def __init__(self):
        self.number = []

    def get_number(self):
        return "".join(self.number)
    def set_number(self, number):
        if number.__len__() != 6:
            print('Номер должен состоять из 6 символов')
        else:
            self.number = []
            for i in number:
                self.number.append(i)

auto1 = Auto()

auto1.set_number("a111aa")

print("a1:", auto1.get_number())

# Task
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.upper()

per = Person("Viktor")
print(per.get_name())
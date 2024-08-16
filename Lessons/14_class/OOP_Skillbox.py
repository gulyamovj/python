# class Cat():
#     def __init__(self, breed, color, age):
#         self._breed = breed
#         self._color = color
#         self._age = age
#
#     @property
#     def breed(self):
#         return self._breed
#
#     @property
#     def color(self):
#         return self._color
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, new_age):
#         if new_age > self._age:
#             self._age = new_age
#         return self._age
#
#     def meow(self):
#         print('Мяу!')
#
#     def purr(self):
#         print('Мрррр')
#
#
# class HomeCat(Cat):
#     def __init__(self, breed, color, age, owner, name):
#         super().__init__(breed, color, age)
#         self._owner = owner
#         self._name = name
#
#     @property
#     def owner(self):
#         return self._owner
#
#     @property
#     def name(self):
#         return self._name
#
#     def getTreat(self):
#         print('Мяу-мяу')
#
# my_cat = HomeCat('Сиамская', 'Белая', 3, 'Иван', 'Роза')
#
# print(my_cat.owner)
# print(my_cat.breed)
# my_cat.getTreat() # Мяу-мяу
# my_cat.purr() # Мрррр

# ### Полиморфизм
# class Cat:
#   def sleep(self):
#     print('Свернулся в клубок и сладко спит.')
#
# class Parrot:
#   def sleep(self):
#     print('Сел на жёрдочку и уснул.')
#
# def homeSleep(animal):
#   animal.sleep()
#
# cat = Cat()
# parrot = Parrot()
# homeSleep(cat) # Свернулся в клубок и сладко спит.
# homeSleep(parrot) # Сел на жёрдочку и уснул.

#####################################################

class Drink:
    # Определяем статический атрибут.
    _volume = 200

    # Вызываем инициализатор класса и определяем динамические атрибуты.
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._remains = self._volume

    # Просим друга сообщить информацию о напитке.
    def drink_info(self):
        print(
            f'Название: {self.name}. Стоимость: {self.price}. Начальный объём: {self._volume}. Осталось: {self._remains}')

    # Служебный метод, позволяющий узнать, достаточно ли напитка.
    def _is_enough(self, need):
        if self._remains >= need and self._remains > 0:
            return True
        print('Осталось недостаточно напитка')
        return False

    # Говорим другу сделать глоток.
    def sip(self):
        if self._is_enough(20) == True:
            self._remains -= 20
            print('Друг сделал глоток')

    # Говорим другу сделать маленький глоток.
    def small_sip(self):
        if self._is_enough(10) == True:
            self._remains -= 10
            print('Друг сделал маленький глоток')

    # Говорим другу выпить напиток залпом.
    def drink_all(self):
        if self._is_enough(0) == True:
            self._remains = 0
            print('Друг выпил напиток залпом')

class Juice(Drink):

    _juice_name = 'сок'

    def __init__(self, price, taste):
        super().__init__(self._juice_name, price)
        self.taste = taste

apple_juice = Juice(250, "яблочный")

apple_juice.small_sip()
apple_juice.sip()
apple_juice.drink_info()

print(__name__)
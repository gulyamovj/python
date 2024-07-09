# numbers = input()
#
# result = []
# i = 0
#
# while i < len(numbers):
#
#     result.append(int(numbers[i:i + 1]))
#
#     i += 1
#
# maximum = max(result)
# minimum = min(result)
#
# print(f"Максимальная цифра равна: {maximum} \n"
#       f"Минимальная цифра равна: {minimum}")


cars = ["Toyota", "Mercedes", "Hyundai", "BMW", "Skoda", "Lexus"]

i = 0
while cars:
    car = cars.pop(0)
    print(car)

print(cars)
result = 0
while True:
    number = input("Input number: ")
    if number == "0":
        break
    else:
        number = int(number)
        result += number

print(result)
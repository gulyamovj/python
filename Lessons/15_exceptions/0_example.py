# l = [1, 3, 5, 7]
#
# print(l[4])

import traceback
while True:
    x = input("Введите число: ")

    try:
        x = float(x)
        if x == 1:
            x = None
        y = 100 / x
        break
    except (ValueError, NameError):
        print("Ошибка. Введите число")
    except TypeError:
        print("Ошибка, не вводите 1")
    except ZeroDivisionError:
        y = "бесконечность"
        break
    except Exception:
        f = open("log.txt", "a+")
        traceback.print_exc(file=f)
        f.close()
        print("Неверное значение")

print(y)

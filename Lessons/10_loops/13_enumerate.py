months = ["январь", "февраль", "март", "апрель", "май", "июнь",
         "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь",]


for counter, month in enumerate(months, start=1):
    if counter % 3 == 1:
        print("Квартал", counter // 4)
    print(counter, month)
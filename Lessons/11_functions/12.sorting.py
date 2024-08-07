countries = ["Франция", "Япония", "Россия", "Казахстан",
             "Китай", "Польша", "Украина", "Беларусь"]

def country_sort(country):
    return len(country)

countries = sorted(countries, key=country_sort)

print(countries)
# Lesson
user = {
    "first_name": "Anton",
    "price": 3000,
    "sale": .3
}

price_f = "price"

currencies = {643: "RUB", 840: "USD", 978: "UER"}

hello = f"Zdravstvuyte, {user['first_name']}!\n" \
        f"Stoimost tovara: {user[price_f]} {currencies[643]}.\n" \
        f"Vasha skidka: {user['sale']:.0%}."

print(hello)
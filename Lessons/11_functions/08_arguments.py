rus_president_fn = "Владимир"
rus_president_ln = "Путин"
rus_president_p = "Владимирович"

def print_full_name(first_name, last_name, patronymic):
    print(first_name, patronymic, last_name)

print_full_name(rus_president_fn, rus_president_ln, rus_president_p)
print_full_name(
    last_name=rus_president_ln,
    patronymic=rus_president_p,
    first_name=rus_president_fn
)

print_full_name(rus_president_fn,
                patronymic=rus_president_p,
                last_name=rus_president_ln)
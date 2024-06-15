# Python не различает в именах ключей
# 1, 1.0, True
# 0, False

# d = {
#     "name": "Nazvanie 1"
# }

# # Task
# plans = {
#     2017: [False, False, False, False, False, False, False, False, False, False, False, False],
#     2018: [True, True, False, False, True, False, True, True, False, True, True, True],
#     2019: [True, True, True, True, True, False, True, True, False, True, True, True],
#     2020: [True, True, True, True, True, False, True, True, False, False, False, False],
#     2021: [True, True, True, True, True, True, True, True, True, True, True, True]
# }
#
# year = int(input())
# result = plans[year].count(True) / len(plans[year]) * 100
#
# print(f'{result:.0f}%')

# Task

born = {
    (2017, 'Jan'): 136544,
    (2017, 'Feb'): 126828,
    (2017, 'Mar'): 148329,
    (2017, 'Apr'): 125534,
    (2017, 'May'): 141947,
    (2017, 'Jun'): 141846,
    (2017, 'Jul'): 148329,
    (2017, 'Aug'): 162223,
    (2017, 'Sep'): 140038,
    (2017, 'Oct'): 146472,
    (2017, 'Nov'): 138108,
    (2017, 'Dec'): 133686,

    (2018, 'Jan'): 135528,
    (2018, 'Feb'): 122425,
    (2018, 'Mar'): 132937,
    (2018, 'Apr'): 123297,
    (2018, 'May'): 136867,
    (2018, 'Jun'): 131697,
    (2018, 'Jul'): 146142,
    (2018, 'Aug'): 149233,
    (2018, 'Sep'): 131897,
    (2018, 'Oct'): 142492,
    (2018, 'Nov'): 126668,
    (2018, 'Dec'): 120133,
}

death = {
    2017: {
        1: 179410,
        2: 146802,
        3: 161610,
        4: 142226,
        5: 161000,
        6: 149314,
        7: 143413,
        8: 152367,
        9: 141652,
        10: 155161,
        11: 145248,
        12: 146137
    },

    2018: {
        1: 165836,
        2: 142931,
        3: 169408,
        4: 157368,
        5: 162805,
        6: 148590,
        7: 152478,
        8: 147822,
        9: 136140,
        10: 150143,
        11: 138749,
        12: 145440
    }
}

year = int(input())
month = int(input())

monthes = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

born_data = born[year, monthes[month - 1]]
death_data = death[year][month]

print(born_data - death_data)
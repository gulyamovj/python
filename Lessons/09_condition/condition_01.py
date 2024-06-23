# age = 24
#
# if age >= 18:
#     full_name = " petrov ivan ivanovich  "
#     full_name = full_name.title()
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")
#
# print("end")

# # Task
# password = "idY*49amd6z"
# pas_in = input()
#
# if pas_in == password:
#     print("Доступ открыт")
# else:
#     print("Доступ закрыт")

# Task
import hashlib
new_password = input()
new_password = new_password.encode()
hash_new_password = hashlib.md5(new_password)
hash_new_password = hash_password.hexdigest()
print(hash_new_password)

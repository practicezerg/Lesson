"""Суть в создании и заполнении словаря. С возможным хранением данных"""
dir_users = {}
# какой-то результат типа логина пароля
# нужно приводить в такое состояние
# Carter10@gmail.com: 69XoKBxnAUNO
# Turner43@gmail.com: 94BivyUom9Mz

# сюда будут приходить данные
open_file = open("for_check.txt", "r", encoding="utf-8")
slovo_test = open_file.readlines()
n = 0
while n < len(slovo_test):
    user_number = "user" + str(n+1)
    dir_users[user_number] = {}
    l = slovo_test[n].split()
    login = l[0].replace(":", "").replace(" ", "")
    psw = l[1].replace(" ", "")
    dir_users[user_number] = {login: psw}
    n += 1
# Пользователь в словаре
print(dir_users)


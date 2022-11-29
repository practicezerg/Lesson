"""Суть в создании и заполнении словаря. С возможным хранением данных"""
import json
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
    l = slovo_test[n].split()
    login = l[0].replace(":", "").replace(" ", "")
    psw = l[1].replace(" ", "")
    dir_users[login] = psw
    n += 1
# Пользователь в словаре
print(dir_users)
open_file.close()
open_file = open("users.txt", "a", encoding="utf-8")
open_file.write(str(dir_users)+"\n")
open_file.close()
with open("users.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(type(data))
data = data | dir_users
print(data)
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

# a = {1: "one", 2: "two", 3: "three"}
# a[5] = 35
# a[4] = "solo"
# print(a)
# a.popitem()
# print(a)
# b = {1: 12, 55: 43, 14: 11,  900: 838}
# a.update(b)
# print(a)
# ==================
# school = {"1a": 12, "1b": 5, "2a": 15, "3a": 12, "3b": 10, "4a": 6, "5a": 8}
# # в одном из классов изменилось количество учащихся допустим в 3а
# school["3a"] = 15
# print(school)
# # в школе появился новый класс
# school["5b"] = 10
# print(school)
# # в школе был раформирован 1b
# print(school.pop("1b"))
# print(school)
# final = 0
# # вычислить всего учащихся
# for i in school:
#     final = final + school[i]
# print(final)
# ============================
a = {}
a[1] = "test"
a[2] = "abc"
a[3] = "kfgkf"
a[4] = 14


def swap_dict(a):
    print(a, "передал ли список а в функцию")
    a2 = a.copy()
    a2.clear()
    for i, z in a.items():
        print(i, "должно быть в индексах")
        print(z)
        a2[z] = i
    return a2


a2 = swap_dict(a)
print(a)
print(a2)

# ==========================
dir_users = {}
login = "edyard02@mail.ru"
psw = "fu83jsp"
login2 = "edyard0233@mail.ru"
psw2 = "fu83j332g234g2sp"


dir_users["user"] = {login: psw}
dir_users["user2"] = {login2: psw2}
dir_users["user2"]["asdasdasd@mail.ru"] = "dji3jij32"
dir_users["user3"] = {"test@mail.ru": ["dasda", "asdasd"]}
print(dir_users)
print(dir_users["user3"])
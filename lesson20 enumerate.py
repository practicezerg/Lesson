spisok = [9, 100, 90, 91, -82, 99, 32, -98, 3, 3, -17, 15, 72, 39, 89]
for i in enumerate(spisok):
    print(i)
b = "hellow"
for i in enumerate(b):
    print(i)
# иная запись
for id, val in enumerate(spisok):
    print(id, val)
#=====================================
r_obj = range(len(spisok))
e_obj = enumerate(spisok)
for i in r_obj:
    if i == 1:
        break
# print(r_obj)
# print(len(spisok))
for i in e_obj:
    if i[0] == 1:
        break
for i in r_obj:
    print(i)
for i in e_obj:
    print(i)
# print(e_obj)


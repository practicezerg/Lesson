spisok = [9, 100, 90, 91, -82, 99, 32, -98, 3, 3, -17, 15, 72, 39, 89]
spisok2 = []
for id, item in enumerate(spisok):
    e = str(item)
    g = ("{0} {1} {2}".format(e, id, item))
    spisok2.append(g)
print(spisok2)

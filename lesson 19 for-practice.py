import random
x = []
for a in range(15):
    a = x.append(random.randint(-100, 100))
print(x)

# =============================
spisok = [*range(0, 100, 17)]
print(spisok)

spisok2 = []
start, end = 0, 100
if start < end:
    spisok2.extend(range(start, end, 17))
print(spisok2)
# =================================
spisok3 = [9, 100, 90, 91, -82, 99, 32, -98, 3, 3, -17, 15, 72, 39, 89]
spisok4 = []
for i in spisok3:
    if i < 0:
        spisok4.append(i)
print(spisok4)
# =================================
spisok5 = []
spisok6 = []
g5 = len(spisok5)
while g5 < 5:
    z5 = str(input("input word=  "))
    print(z5)
    spisok5.append(z5)
    spisok6.append(len(z5))
    g5 += 1
print(spisok5)
print(spisok6)

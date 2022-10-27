from random import randint, random
y = []
for i in range(100):
    y.append(randint(-999, 999))
print(len(y))
print(y)


def spisok(y):
    for i2 in range(90):
        print(y[i2:(i2+10)])


spisok(y)


def spisok_sort(y):
    y.sort()
    for i2 in range(90):
        print(y[i2:(i2 + 10)])


spisok_sort(y)
# x = []
# i = 0
# while i < 8:
#     x.append(int(input("input number")))
#     i += 1
# print(sum(x))
# print(min(x))
# print(max(x))

#==========================================
# import random, randint
from random import randint, random
y = []
i2 = 0
while i2 < 100:
    y.append(randint(-999, 999))
    i2 += 1
print(len(y))
print(y)


def spisok(y):
    a = 0
    while a < 90:
        print(y[a:(a+10)])
        a += 10


spisok(y)


def spisok_sort(y):
    y.sort()
    a = 0
    while a < 90:
        print(y[a:a+10])
        a += 10


spisok_sort(y)






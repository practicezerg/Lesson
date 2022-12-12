import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# import readchar
# k = readchar.readkey()
# if k == "a":
#     print("sssssssss")
# if k == readchar.key.ENTER:
#     print("testt")
# =========================
# a = "\u0421\u0430\u043d\u044f, \u0438\u0434\u0438 \u043d\u0430\u0445\u0443\u0439"
# b = a.encode()
# c = b.decode()
# print(c)


# import time
# ts = time.time()
# print(ts)
# print(str(time.time()).split('.')[0])
# print(int(ts))


def countPoints(rings):
    d = {}
    res = 0
    for i in range(10):
        d[i] = [0,0,0]
    for i in range(0, len(rings), 2):
        j = int(rings[i+1])
        if rings[i] == "R":
            d[j][0] += 1
        elif rings[i] == "G":
            d[j][1] += 1
        else:
            d[j][2] += 1
    for v in d.values():
        if min(v) > 0:
            res += 1
    return res





rings = "B0B6G0R6R0R6G9"
#18 так как всего 9 стержней
res = countPoints(rings)
print(res)
"""Нужно найти количество общего вхождения символов из одной строки в другую"""


def numJewelsInStones(jewels, stones):
    res = 0
    for i in jewels:
        y = stones.count(i)
        print(y, "y")
        res = res + y
    return res



jewels = "aA"
stones = "aAAbbbb"

res = numJewelsInStones(jewels, stones)
print(res)

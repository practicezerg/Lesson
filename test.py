import random
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

strings = ["a","b","c"]
for i in strings:
    print(strings[-1])
    i, strings[-1] = strings[-1], i
    print(i, "==i")
    print(strings)
print(strings)

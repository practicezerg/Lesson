# g = open("data.txt")
# g1 = open("dataRu.txt", "w")
# list = ["один", "два", "три", "четыре", "пять"]
# x = 0
# for i in g:
#     print(i, "= что перебирает i")
#     a = i.split(" - ")
#     a.pop(0)
#     a.insert(0, list[x])
#     a2 = " - ".join(a)
#     print(a2)
#     x += 1
#     g1.writelines(a2)
# ================================================
a = open("nums.txt")
print(a)
b = 0
for i in a:
    print(i)
    a = i.split(" ")
    print(a)
    for i2 in a:
        print(i2)
        i2 = int(i2)
        b += i2
print(b)








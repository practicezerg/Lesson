# ближе к сердцу
# text = input("Input words")
# small = []
# big = []
# n = len(text)
# print(n)
# for i in text:
#     if "a" <= i <= "z":
#         small.append(i)
# for i in text:
#     if "A" <= i <= "Z":
#         big.append(i)
# if len(small) >= len(big):
#     print(text.lower())
# else:
#     print(text.upper())

# у верхнего недоработка потому что рассматривается тольк  английский вариант
# ==================================
# второй вариант как надо по заданию
# text = input("=  ")
# big = []
# small = []
# a = 0
# for i in text:
#     print(text[a : a + 1].isupper())
#     xz = text[a : a + 1].isupper()
#     a += 1
#     if xz == True:
#         big.append(i)
#         print(big)
#     else:
#         small.append(i)
#         print(small)
# print(len(small))
# print(len(big))
# if len(small) >= len(big):
#     print(text.lower())
# else:
#     print(text.upper())


# ==================================
def try_unput():
    test = input("Input 2 numbers with . =")
    return test

def telo(vvod):
    for i in vvod:
        number_ornot = vvod.isdigit()
        if number_ornot == True:
            a, b = vvod.split(".")
            a = int(a)
            b = int(b)
            print(a + b)
        else:
            try_unput()



vvod = try_unput()
print(vvod)
telo(vvod)
# ==================================
text = "4e"
while text.isdigit() == False:
    text = input("Input 2 numbers=        ")
a = int(text[0])
b = int(text[1])
print(a + b)

# ==================================
# text = "45"
# a = int(text[0])     само суммирование
# b = int(text[1])
# print(a + b)
#
# ============
# print(text.isdigit())   проверка на цифры
# ++++++++++++
def test1():
    qq = input("")
    return qq


def test2(text):
    if text.isdigit() == True:
        a = int(text[0])
        b = int(text[1])
        print(a + b)
    else:
        test2()

text = test1()
test2(text)
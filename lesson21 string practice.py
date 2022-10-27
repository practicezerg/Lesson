# ближе к сердцу
text = input("Input words")
small = []
big = []
n = len(text)
print(n)
for i in text:
    if "a" <= i <= "z":
        small.append(i)
for i in text:
    if "A" <= i <= "Z":
        big.append(i)
if len(small) >= len(big):
    print(text.lower())
else:
    print(text.upper())

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




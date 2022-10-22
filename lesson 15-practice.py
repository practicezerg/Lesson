# a = chr(int(input("input unicode=     ")))
# print(a)
#=====================================
# a = 1
# while a > 0:
#     try:
#         a = int(input("input unicode=     "))
#         # a = chr(int(input("input unicode=     ")))
#         # a = int(chr(input("input unicode=     ")))
#         # print(a)
#         print(chr(a))
#     except:
#         print("work is end")
# print("work is end")
#=====================================
# stroka = input("input string=       ")
# # c = print(len(stroka))
# if len(stroka) > 10:
#     print("String must be 10 symbol!")
# else:
#     c1 = 10 - len(stroka)
#     print(c1)
#     while 0 < c1 < 10:
#         stroka = stroka + "*"
#         c1 = 10 - len(stroka)
#     print(stroka)

#=====================================
# так завещал толик
# stroka = input("input string=       ")
# # c = print(len(stroka))
# if len(stroka) > 10:
#     print("String must be 10 symbol!")
# else:
#     c1 = 10 - len(stroka)
#     print(c1)
#     while 1 <= c1:
#         stroka += "*"  # так же можно записать +=  = stroka + "*"
#         c1 -= 1
#     print(stroka)
#=====================================
a3 = input("Input numbers=       ")
b3 = input("Input numbers=       ")
c3 = input("Input numbers=       ")
d3 = input("Input numbers=       ")
e3 = input("Input numbers=       ")
f3 = input("Input numbers=       ")
# возможно через лен считать сколько символов ?
if a3 > b3:
    print("a3 > b3")
elif c3 > d3:
    print("c3 > d3")
elif e3 > f3:
    print("e3 > f3")



print(round(max(a3, b3, c3, d3, e3, f3), 2))
print(min(a3, b3, c3, d3, e3, f3))





#Пользователь вводит один символ.Проверить один ли символ? Если символ 1 англиского алфовита.
# первый вариант если пользователь сознательный и вводит только числа

def test_eng(a):
#     if ord("a") <= a <= ord("Z"):
#         print(chr(a))
#         return True
#     else:
#         return False
    return ord("a") <= a <= ord("Z")


a = input("Input number>>> ")
if len(a) == 1:
    a = int(a)
    test_eng(a)
    print(chr(a), "This symbol")
else:
    a = int(a)
    print(" Need only one number")
    print("But you symbol is =      ", chr(a))


#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#print(ord("a"))
# print(ord("A"))
# print(ord("Z"))
# print(ord("z"))
# print(chr(123))
#65-122 включительно

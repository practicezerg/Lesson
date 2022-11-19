# print("This is {1}, He so {3} in {2}. I think him number {0}!".format(1,"Tolik", "Poe","fucking good"))

# a, b = input("Enter two numbers").split("")
# a, b = int(a),int(b)
# print(a+b)

# a1,b1,c1 = "mama mila ramy".split()
# print(a1,b1,c1,sep="\n")   # sep по сути разделение.      \n - дает нам разделение на каждую строчку

# try:
#     a = input("Введите ваш ip (формат записи должен быть ***.***.***.***)  ")  # для теста 192.168.1.1
#         #if "0.0.0.0" < a < "255.255.255.255":
#     a = (a).split(".")
#     b, c, d, f =print(a, sep=f"{b}")
# except ValueError:
#     print("Введите пожалуйста через точку (для примера ***.***.***.***) ")
# print(a)

# a = input("Введите ваш ip (формат записи должен быть ***.***.***.***)  ")
# result = a.split('.')
# if len(result) < 4:
#     elif 0 < {0} < 256:
#     elif 0 < {1} < 256:
#     elif 0 < {2} < 256:
#     elif 0 < {3} < 256:
#     print("Спасибо, ожидайте ответа")
# else:
#     print("Введите пожалуйста через точку (для примера ***.***.***.***) ")

# try:
#     a = input("Введите пожалуйста через точку (для примера ***.***.***.***) ")
#     result = user_input.split('.')
#     if len(result) < 4:
#     else
# except ValueError, IndentationError:
# print("Введите пожалуйста через точку (для примера ***.***.***.***) ")
#
a = input("Введите ваш ip (формат записи должен быть ***.***.***.***)  ")
try:
    # a = "192.168.1.1"
    a1, b1, c1, d1 = a.split('.')
    print(a1,b1,c1,d1,sep="\n")
    a1, b1, c1, d1 = int(a1,b1,c1,d1)
    if 0 > a1 > 255:
        0 > b1 > 255
        0 > c1 > 255
        0 > d1 > 255

        print("Вы ввели неверный ip или ошиблись в написании")
    else:
        print("Спасибо, ожидайте ответа")
except:
    print("Вы ввели неверный ip или ошиблись в написании")



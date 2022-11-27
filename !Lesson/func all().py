# функция all выводит если все значения True/ Выводит False если есть не True /типа None или False
#  так же 0 и NoneType
l = [True, False, True]
l2 = [True, True, True]
l3 = [False, False, False]
# так же работает с картежами + словарями
print(all(l))
print(all(l2))
print(all(l3))

a = [15, 15, 15, 15, 15, 4, False]
print(all(a))
# print(all(l))
# print(all(l))
a = [12, 38.45, "wait", -4, "Alex"]
my_list = ["test", "job", "relax", "python", "boobs",14, 44,]
print(a)
print(my_list)
print(a[2])
print(my_list[0])  #  нумерация с лева на права
print(my_list[-1])  #тут нумерация с конца и первая позиция -1
print(my_list[0:2])# часто надо взять кусок листа.В этом случае указывается индекс первого элемента среза и индекс следующего за последним элементом среза
print(my_list[:3])
print(my_list[2:])
print(my_list[:])
print(my_list[5])
my_list[5] = 14.55
print(my_list)
print(my_list[5])
my_list.append("wood")    # добавить в конец списка
print(my_list)
my_list.insert(1, "Tolik")  #добавить в конкретную позицию конкретное значение
print(my_list)
my_list.remove("Tolik")  #убрать конкретную позицию
print(my_list)
my_list.pop(3)   #убирает конретную позицию по счету
print(my_list)
my_list.pop()   #убирает последний аргумент из списка
print(my_list)
b = [15, 16, 17, 18, 19, 20, 21, 22]
b = b[0:2] + b[3:]
print(b)
b[0:2] = [15.5, 16.5]
print(b)

import random
c = []
i = 0
while i < 10:
    c.append(random.randint(0,100))
    i += 1
print(c)

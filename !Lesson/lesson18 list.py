a = [12, 38.45, "wait", -4, "Alex", 12]
my_list = ["test", "job", "relax", "python", "boobs",14, 44,]
print(a)
print(my_list)
print(a[2])
print(my_list[0])  #  нумерация с лева на права
print(my_list[-1])  #тут нумерация с конца и первая позиция -1
print(my_list[0:2]) #Часто надо взять кусок листа. В этом случае указывается индекс первого элемента среза и индекс следующего за последним элементом среза
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
my_list.pop(3)   #убирает конкретную позицию по счету
print(my_list)
my_list.pop()   #убирает последний аргумент из списка
print(my_list)
b = [15, 16, 17, 18, 19, 20, 21, 22]
b = b[0:2] + b[3:]
print(b)
b[0:2] = [15.5, 16.5]
print(b)
print(a.count(12), "count ведет подсчет в листе сколько встречается аргумент")
print(a.index(-4), "возвращает индекс элемента")
a.extend(b)
print(a, "метод extend объединяет 2 списка в один")

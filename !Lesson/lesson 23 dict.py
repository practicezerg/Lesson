a = {1: "one", 2: "two", 3: "three"}
b = {
    dom: ""
}
print(a)
print(a[1], "обращаемся по ключу присвоенному в словаре выдает значение")
"""ключ может быть любой 
переменной или булевым значением или строкой или картежом
списком не может быть!!!!!"""
a[1] = "Noone"
print(a)
del a[2]
print(a)
a[2] = "two"
print(a)
for i,v in a.items():
    print(i, v)
    print(i, "is", v)
for i in a:
    print(i) #перебирает по ключам
    print(a[i]) #перебирает по объектам
#print(a.clear()) удаляет все значения, но не сам словарь(будет пустым)
a2 = a.copy()
print(dict.fromkeys(a2, "test"))  # заменяет объекты на значение
print(a.get(2), "Демонстрация get")
print(a.pop(2)) #удаляет по ключа
# popitem() # удаляет последний добавленый объект
# a.setdefault(15, "Tratata")  то же самое что и a[15, "tatatata"]
"""только a[] перезапишет значение, если оно есть. А вот setdefault нет
update() добавляет другой словарь и если смиежные перезаписывает"""


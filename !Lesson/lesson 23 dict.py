from pprint import pprint
a = {1: "one", 2: "two", 3: "three"}
b = {
    "code": "RU",
    "name": "Russian",
    "population": "human",
    3: "sdfs"
}

for i, value in b.items():
    print(i, " - ", value)
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
a2 = a.copy()  # делает копию словаря без сылок(самостоятельный объект)
print(dict.fromkeys(a2, "test"))  # заменяет объекты на значение
print(a.get(2), "Демонстрация get Метод get запрашивает ключ, и если его нет, вместо ошибки возвращает None. "
                "Без гета будет ошибка если такого ключа нет. Гет позволяет писать другое значение если ключа не нашлось")
print(a.get(500, "nety takogo key"))
print(a.pop(2)) #удаляет по ключа
# popitem() # удаляет последний добавленый объект
# a.setdefault(15, "Tratata")  то же самое что и a[15, "tatatata"]
"""только a[] перезапишет значение, если оно есть. А вот setdefault нет
update() добавляет другой словарь и если смиежные перезаписывает"""
print(a.values(), "возвращает  все значения списком")  #возвращает  все значения списком
print(a.keys(),"возвращеат все ключи списком") #возвращеат все ключи списком
print(a.items())
a.update(b)
print(a, "Если нужно обединить словари, если будут одинаковые ключи то внедряемое значение перепишет старое")
# Метод setdefault ищет ключ, и если его нет, вместо ошибки создает ключ со значением None.

#
a = [10,20,30,40]
b = ["topol", "sosna", "barga", "korabl"]
s = dict(zip(a,b))
print(s)

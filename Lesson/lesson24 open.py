gg = open("test24.txt")
"""r - в режиме чтения
w - в режиме записи. Все данные до этого момента стираются
a - режим дозаписи
x - всегда создается новый файл
b - если нужно байтовый
t - если нужно текстовый"""
# print(gg)
# print(gg.read(7))  #в скобках количество символов
# print(gg.read())
gg = open("test24.txt")
print(gg.readline())  # одну строку
print(gg.readlines())  # все строки

for i in open("test24.txt"):
    print(i)

list = ["Радиус", "Разлив", "Ракита", "Распря", "Реветь", "Резкий", "Ресурс", "Робкий"]
gg1 = open("lesson24.txt", "w")
print(gg1.write("Забияка"))
print(gg1.write("test"))
print(gg1.writelines(list))
gg1.close()   # лучше закрывать файл послеработы что бы освободить память
gg.close()
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
open('file.txt', 'w+', encoding='utf-8', errors='ignore')  # игнорирование ошибки
with open('log.txt', 'a', encoding='utf-8') as file:
    string = f"Клиенту на свитче  на  порту был применен тариф \n"
    file.write(string)
with open('r1.txt') as src, open('result.txt', 'w') as dest: # открытие 2 файлов одновременно
    print("!")
    # src.seek(0)   обозначает переход на начало фалй так как задан 0
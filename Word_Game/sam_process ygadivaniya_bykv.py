def input_char(l_temp,l_all):
    char = input(str("Напишите букву=  "))
    char = char.lower()
    if char in l_all:
        print("Есть такая буква")
        print(l_all.count(char), "сколько вхождений в строку")
        if l_all.count(char) == 1:
            print(l_all.index(char), "индекс в слове")  # показывает, где лежит буква по индексу
            l_temp.pop(l_all.index(char))
            l_temp.insert(l_all.index(char), char)
            return l_temp
        if l_all.count(char) >= 2:
            print(l_all.index(char), "индекс в слове")
            l_count = []  #для индексов
            count =0
            for i in l_all:
                if i == char:
                    l_count.append(count)
                count += 1
            print(l_count, "это индексы повторений")
            n = 0
            while n <= l_all.count(char) - 1:
                l_temp.pop(l_count[n])
                l_temp.insert(l_count[n], char)
                n += 1
    else:
        print("Нет такой буквы")



slovo = "ананас"
l_all = []
for i in slovo:
    l_all.append(i)
print(l_all,"l_all  все буквы показаны")
slovo2 = slovo
l_hidden = []

slovo3 = len(slovo)* "*"

for i in slovo3:
    l_hidden.append(i)
print(l_hidden,"l_hidden  все буквы показаны")
l_temp = l_hidden
print(l_temp,"l_temp  все буквы показаны")
print(slovo3)
input_try = 10
while input_try >= 0:
    if "*" in l_temp:
        input_char(l_temp,l_all)
        print(l_temp, "l_temp  после добавления")
        print("".join(l_temp))
        print("Ещё можешь попробовать {} раз!".format(input_try))
        input_try -= 1
    else:
        print("Поздравляю.Вы угадали все слово!!!!")
        break
if input_try < 0:
    print("У вас закончились попытки. Сыграете ещё раз?")






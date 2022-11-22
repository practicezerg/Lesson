def input_char(l_temp,l_all):
    char = input(str("Напишите букву=  "))
    char = char.lower()
    if char in l_all:
        print("Есть такая буква!!Ты молодец!!")
        if l_all.count(char) == 1:
            l_temp.pop(l_all.index(char))
            l_temp.insert(l_all.index(char), char)
            return l_temp
        if l_all.count(char) >= 2:
            print("И их несколько!!")
            l_count = []  #для индексов
            count = 0
            for i in l_all:
                if i == char:
                    l_count.append(count)
                count += 1
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
slovo2 = slovo
l_hidden = []
slovo3 = len(slovo) * "*"
for i in slovo3:
    l_hidden.append(i)
l_temp = l_hidden
print("Вот такое слово я задумал")
print(slovo3)
input_try = 10
while input_try > 0:
    if "*" in l_temp:
        print("Ещё можешь попробовать {} раз!".format(input_try))
        input_char(l_temp, l_all)
        print("".join(l_temp))
        input_try -= 1
    else:
        print("Поздравляю.Вы угадали все слово!!!!")
        break
if input_try == 0:
    print("У вас закончились попытки. Сыграете ещё раз?")

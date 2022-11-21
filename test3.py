slovo = "дракон"
l = []
for i in slovo:
    l.append(i)
print(l)
slovo2 = slovo
l5 = []
l2 = []
test = len(slovo)* "*"
for i in test:
    l2.append(i)
print(l2)
print(test)
char = input(str("char="))
char = char.lower()
if char in l:
    print("Есть такая буква")
    l5.append(char)
    print(l.count(char), "сколько вхождений в строку")
    if l.count(char) == 1:
        print(l.index(char), "индекс в слове")  # показывает, где лежит буква по индексу
    elif l.count(char) > 2:
        print(l.index(char), "индекс в слове")

        # print(slovo2.replace("*", char))
        #
        # print(slovo)
        # print(slovo2)

else:
    print("Нет такой буквы")



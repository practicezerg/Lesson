import random


"""Ниже выбираем версию игры."""
def ver():
    print("Введите 1, если хотите легкий режим(2 подсказки).В виде открытых 2 случайных букв.")
    print("Введите 2, если хотите сложный режим.В сложной версии подсказок нет!")
    print("Что же ты выбираешь?")
    version_game = input("Жми цифру!  ===>>")  # выбор версии игры
    """Версия игры.Для новичка(ребенка) - 2 подсказки. В виде открытых 2 случайных букв. 
    То Хард версии подсказок нет."""
    if version_game == "1":
        print("Хорошо, ты выбрал легкий вариант")
        return 1
    else:
        print("Толя тобой доволен!")
        return 2


def input_char(l_temp,l_all):
    char = input("Напишите букву=  ")
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


"""ниже хранится список слов. в txt формате.для теста пока 6 слов"""
def slova():
    open_file = open("slova.txt", "r", encoding="utf-8")
    num_string_all = len(open('slova.txt').readlines())  # тут количество слов в списке.
    ran_num = random.randint(0, num_string_all - 1)  # случайное число для выбора строки со словом
    slovo_test = open_file.readlines()
    slovo = slovo_test[ran_num]
    slovo = slovo.replace("\n", "")
    return slovo


def slovo_for_game_easy(slovo):
    b1 = random.randint(0, len(slovo)-1)
    b2 = random.randint(0, len(slovo)-1)
    while slovo[b1] == slovo[b2]:
        b2 = random.randint(0, len(slovo)-1)
    # print(slovo[b1], slovo[b2])
    show_user_easy = ""
    for i in slovo:
        if i != slovo[b1] and i != slovo[b2]:
            show_user_easy = show_user_easy + "*"
        else:
            show_user_easy = show_user_easy + i
    return show_user_easy


def game_hard(slovo):
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
    input_try = 15
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
        print("Загаданное слово было {} ".format(slovo))


def game_easy(slovo, show_user_easy):
    l_all = []
    for i in slovo:
        l_all.append(i)
    l_hidden = []
    slovo3 = show_user_easy
    for i in slovo3:
        l_hidden.append(i)
    l_temp = l_hidden
    print("Вот такое слово я задумал и две подсказки, как я и обещал!")
    print(slovo3)
    input_try = 15
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
        print("Загаданное слово было {} ".format(slovo))


print("Привет, малыш или любопытный взрослый! Я робот Толик!")
print("Я загадаю тебе слово, а ты попробуй отгадай!")
print("У вас будет 15 попыток. Не спеши и у тебя получится! ")
slovo = slova()
show_user_easy = slovo_for_game_easy(slovo)
print(show_user_easy)
print(slovo)
if ver() == 2:
    game_hard(slovo)
else:
    game_easy(slovo, show_user_easy)

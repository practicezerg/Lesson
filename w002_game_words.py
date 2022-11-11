import random
""""список из 500 слов. Слово должно быть больше или меньше 6 букв"""

"""Ниже выбираем версию игры."""
def ver():
    print("Введите 1, если хотите легкий режим(2 подсказки).В виде открытых 2 случайных букв.")
    print("Введите 2, если хотите сложный режим.В сложной версии подсказок нет!")
    print("Что же ты выбираешь?")
    version_game = input("Жми цифру!  ===>>")  # выбор версии игры
    """Версия игры.Для новичка(ребенка) - 2 подсказки. В виде открытых 2 случайных букв. 
    То Хард версии подсказок нет."""
    if version_game == "1":
        return 1
    else:
        return 2


"""ниже хранится список слов. в txt формате.для теста пока предоставлено одно слово."""
def slova():
    import random
    open_file = open("slova.txt", "r", encoding="utf-8")
    num_string_all = len(open('slova.txt').readlines())  # тут количество слов в списке.
    ran_num = random.randint(0, num_string_all - 1)  # случайное число для выбора строки со словом
    slovo_test = open_file.readlines()
    slovo = slovo_test[ran_num]
    slovo = slovo.replace("\n", "")
    return slovo


"""ниже слово переделываем в **** для 2 режимов"""
def game1(slovo):
    # print(slovo, "= slovo_test")
    """1 easy режим 2 подсказки"""
    b1 = random.randint(0, len(slovo)-1)
    b2 = random.randint(0, len(slovo)-1)
    while b2 == b1:
        b2 = random.randint(0, len(slovo)-1)
    # print(slovo[b1], slovo[b2])
    show_user_hard = len(slovo) * "*"
    show_user_easy = ""
    for i in slovo:
        if i != slovo[b1] and i != slovo[b2]:
            show_user_easy = show_user_easy + "*"
        else:
            show_user_easy = show_user_easy + i
    # print(show_user_easy, "= show_user_easy")
    return show_user_hard, show_user_easy


"""ниже пользователь гадает само слово"""
def game2(slovo):
    pass
    # try_input = 10
    # print("Вы угадали слово!!")
    # print("Вы были близки")
    # print("У вас осталось 9 попыток!")
    # print("У вас осталось 8 попыток!")
    # print("У вас осталось 7 попыток!")
    # print("У вас осталось 6 попыток!")
    # print("У вас осталось 5 попыток!")
    # print("У вас осталось 4 попыток!")
    # print("У вас осталось 3 попыток!")
    # print("У вас осталось 2 попыток!")
    # print("У вас осталось 1 попыток!")


print("Привет, малыш или любопытный взрослый! Я робот Толик!")
print("Я загадаю тебе слово, а ты попробуй отгадай!")
print("У вас будет 10 попыток. Не спеши и у тебя получится! ")

ver = ver()
# print(ver, "вывод функции ver()")
slovo = slova()
# print(slovo, "вывод функции slova()")
show_user_hard,show_user_easy = game1(slovo)



if ver == 1:
    print("Я загадал слово и вот тебе 2 буквы подсказки, как я и обещал = ", show_user_easy)
else:
    print(show_user_hard)









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
        print("Хорошо, ты выбрал легкий вариант")
        return 1
    else:
        print("Толя тобой доволен!")
        return 2


"""ниже хранится список слов. в txt формате.для теста пока 6 слов"""
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
def game2(slovo, show_user_easy):
    input_type = 10
    # print(slovo, "== test game2 slovo")
    print("Я загадал слово и вот тебе 2 буквы подсказки, как я и обещал = ", show_user_easy)
    try:

        while input_type > 0:
            test_char = char()
            if test_char in slovo:
                print(test_char, "==test_char")
                print("Есть такая буква!У вас осталось {} попыток!".format(input_type))
                x = (slovo.find(test_char))
                slovo2 = show_user_easy[0:x] + test_char + show_user_easy[x:]
                print(slovo2)
                input_type -= 1
            else:
                print("В задуманном мною слове нет такой буквы")
                print("У вас осталось {} попыток!".format(input_type))
                input_type -= 1
    except TypeError:
        print("Друг, ты ввел неверный символ!")
        print("Вводи русские буквы.Попробуй ещё разок")






"""обработка ошибки"""
# def error():
#     print("Друг, ты ввел неверный символ!")
#     print("Вводи русские буквы.Попробуй ещё разок")
#     char()





"""проверка буквы на кириллицу"""
def char():
    print("Подумай, назови букву.")
    char_ideal = "йцукенгшщзхъфывапролджэячсмитьбюё"
    res_char = input("Введи букву, а я проверю есть она или нет ==  ")
    # print(char)
    if res_char in char_ideal:
        return res_char
    else:
        print("Друг, ты ввел неверный символ!")
        print("Вводи русские буквы.Попробуй ещё разок")



"""для Хард"""
def game3(slovo):
    pass
    """для hard"""


print("Привет, малыш или любопытный взрослый! Я робот Толик!")
print("Я загадаю тебе слово, а ты попробуй отгадай!")
print("У вас будет 10 попыток. Не спеши и у тебя получится! ")

ver = ver()
# print(ver, "вывод функции ver()")
slovo = slova()
# print(slovo, "вывод функции slova()")
show_user_hard, show_user_easy = game1(slovo)
# res_char = char()
if ver == 1:
    game2(slovo, show_user_easy)

else:
    print(show_user_hard)
    game3(slovo)




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


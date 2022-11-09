import random
""""список из 500 слов. Слово должно быть больше или меньше 6 букв"""

"""Ниже выбираем версию игры."""
def ver():
    version_game = input("Введите 1, если хотите легкий режим(2 подсказки)\n"
                         "Введите 2, если хотите сложный режим                     >>>  ")  # выбор версии игры
    """Версия игры.Для новичка(ребенка) - 2 подсказки. В виде открытых 2 случайных букв. 
    То Хард версии подсказок нет."""
    if version_game == 1:
        return 1
    else:
        return 2


"""ниже хранится список слов. в txt формате.для теста пока предоставлено одно слово."""
def slova():
    slovo_test = "Аристократия"
    return slovo_test


"""ниже слово переделываем в **** для 2 режимов"""
def game1(slovo_test):
    print(slovo_test, "= slovo_test")
    """1 easy режим 2 подсказки"""
    b1 = random.randint(0, len(slovo_test)-1)
    b2 = random.randint(0, len(slovo_test)-1)
    while b2 == b1:
        b2 = random.randint(0, len(slovo_test)-1)
    print(slovo_test[b1], slovo_test[b2])
    show_user_hard = len(slovo_test) * "*"
    show_user_easy = ""
    for i in slovo_test:
        if i != slovo_test[b1] and i != slovo_test[b2]:
            show_user_easy = show_user_easy + "*"
        else:
            show_user_easy = show_user_easy + i
    print(show_user_easy, "= show_user_easy")
    return show_user_hard, show_user_easy


"""ниже пользователь гадает само слово"""
def game2(slovo_test):
    slovo_test = "Аристократия"




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


step1 = ver()
# slova()


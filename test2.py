import random
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

slovo = game1("Гавань")
print(slovo)
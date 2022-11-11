"""какое то задание"""
# my_str = '01234567890'
# print(my_str.endswith('0123', 0,4))
# print(my_str.endswith("0"))

# lst = ([1,2,3,4,5])
# lst2 = []
# x = 0
# print(lst2)
# print(lst[0], ",take carteg")
# for i in lst:
#     i = -i
#     lst.replace(lst[x],i)
#     lst2.append(i)
#     x += 1
# print(lst2)

# list = ([1,2,3,4,5])
# print(list[2])
# x = 0
# for i in list:
#     list[x] = -i
#     x += 1
#     print(i)
# print(list)

"""гадание самой карты"""

"""ниже слово переделываем в **** для 2 режимов"""

import random
def game1(slovo):
    """1 easy режим 2 подсказки"""
    b1 = random.randint(0, len(slovo)-1)
    b2 = random.randint(0, len(slovo)-1)
    while b2 == b1:
        b2 = random.randint(0, len(slovo)-1)
    show_user_hard = len(slovo) * "*"
    show_user_easy = ""
    for i in slovo:
        if i != slovo[b1] and i != slovo[b2]:
            show_user_easy = show_user_easy + "*"
        else:
            show_user_easy = show_user_easy + i
    return show_user_hard, show_user_easy


"""ниже пользователь гадает само слово"""
def game2(slovo):
    pass



slovo = "Елочка"
show_user_hard,show_user_easy = game1(slovo)
print(show_user_hard)
print(show_user_easy)
game2 = game2(slovo)
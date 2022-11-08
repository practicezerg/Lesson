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



import random

def game1(slovo_test):
    print(slovo_test)
    """1 easy режим 2 подсказки"""
    print(len(slovo_test))
    b1 = random.randint(0, len(slovo_test)-1)
    b2 = random.randint(0, len(slovo_test)-1)
    while b2 == b1:
        b2 = random.randint(0, len(slovo_test)-1)
    print(slovo_test[b1], slovo_test[b2])
    show_user = len(slovo_test) * "*"
    print(show_user)
    show_user.replace(show_user[b1], slovo_test[b1])
    print(show_user[b1])
    print(slovo_test[b1])
    show_user.replace(show_user[b2], slovo_test[b2])
    print(show_user)
    # for i in slovo_test:






slovo_test = "Аристократия"
game1(slovo_test)

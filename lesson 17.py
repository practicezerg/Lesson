from random import random, randrange, randint
print(random())   # от 0 до 1
print(random()*5)   #  от 0 до 5
print(random()*(10-6)+6)   #от 6 до 10
print(round(random()*(10-6)+6))  # окуругление до целого
print(random()*(2- -2)+ -2)   #от -2 до 2
print(randint(3, 10) )  #второй аргумент диапозон входит
print(randrange(3,10))  #второй аргумент не входит в диапозон
print(randrange(3,50, 2))  #третий аргумент это шаг

#Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12. Также получите число кратное пяти в пределах от 5 до 100.
from random import randrange
print(randrange(6, 13, 2))
print(randrange(5, 101, 5))
#Напишите программу, которая запрашивает у пользователя границы диапазона и какое (целое или вещественное) число он хочет получить. Выводит на экран подходящее случайное число.

from random import random, randrange, randint

print("если вы хотите целое число введите 1")
print("если вы хотите вещественное число введите 2")
c = int(input("Ваш выбор"))
if c == 1:
    a = int(input('Нижняя граница диапозона ='))
    b = int(input('Верхняя граница диапозона ='))
    print(randint(a, b))
else:
    print("test")
    a = float(input('Нижняя граница диапозона ='))
    b = float(input('Верхняя граница диапозона ='))
    print(random()*(b-a)+a)
"""
В Python истинными и ложными значениями считаются не только True и False.

истинное значение:
любое ненулевое число
любая непустая строка
любой непустой объект

ложное значение:
0
None
пустая строка
пустой объект"""

l = []
l1 = ["test"]
print(bool(1))
print(bool(0))
print(bool(l))
print(bool(l1))
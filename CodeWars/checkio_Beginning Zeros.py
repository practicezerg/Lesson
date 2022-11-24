"""Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0")
 находится в начале строки.

Входные данные: Строка, состоящая только из цифр.
Выходные данные: Целое число.
Пример:
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2

Строка может иметь цифры: 0-9"""

def beginning_zeros(a: str) -> int:
    num = 0
    for i in a:
        if i == "0":
            num += 1
        else:
            break
    return num
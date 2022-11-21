"""Проверка - является ли число произведением одинаковых чисел"""
def is_square(n):
    sqrt = (n**(0.5))
    print(sqrt)
    if sqrt**2 == n:
        return True
    else:
        return False # fix me


n = -1
x = is_square(n)
print(x)
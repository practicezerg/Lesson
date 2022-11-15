"""Функция any() в Python, хотя бы один элемент True.
Проверяет, что хотя бы один элемент в последовательности True."""

w = "asdadadadadasdasdadada4"
q = any(map(str.isdigit, w))
print(q)


b = any([True, False, True])
print(b)
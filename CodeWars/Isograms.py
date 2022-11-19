"""Проверка на повторения в строке"""
def is_isogram(string):
    test = []
    for i in string:
        test.append(i.lower())
    for i in test:
        num = test.count(i)
        if num >= 2:
            return False
    return True


string = "aba"
# string = "moOse"
# string = "aba"
result = is_isogram(string)
print(result)
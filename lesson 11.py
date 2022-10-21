def test():
    a = input("Введите целое число")
    a = int(a)
    if a >= 0:
        positive()
    else:
        negative()

def positive():
    print("Положительное")
def negative():
    print("Отрицательное")

test()




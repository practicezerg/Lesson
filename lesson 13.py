# def fafafa():
#     a = (input("put something   "))
#     b = (input("put something   "))
#     c = a + b
#     return c
#
#
# print(fafafa())


def wewet():
    a = int(input("put any number   "))
    b = int(input("put any number   "))
    c = a * b
    while a != 0 and b != 0:
        b = int(input("put any number   "))
        if b == 0:
            return c
        c = c * b
    return c


print(wewet())


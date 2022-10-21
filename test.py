def wewet():
    a = int(input("put any number   "))
    b = int(input("put any number   "))
    c = a
    while a != 0 and b != 0:
        c = c * b
        try:
            b = int(input("put any number   "))
        except ValueError:
            print("cancel repeat it")


    return c


print(wewet())
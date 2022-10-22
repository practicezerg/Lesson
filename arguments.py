def getinput():
    a = input("input something=     ")
    print(type(a))
    return a


def testinput(a):
    try:
        type(a) != int
        print("False")
        return False
    except:
        print("True")
        return True
    # try:
    #     a = int(a)
    #     print("true")
    #     return True
    # except ValueError:
    #     print("false")
    #     return False


def strToInt(a):
    a = int(a)
    return a


def printInt(a):
    print(a)


a = getinput()
# if True:
#     a = strToInt(a)
#     a = printInt(a)
# else:
#     print("wrong dude")
if testinput(a):
    a = strToInt(a)
    a = printInt(a)
else:
    print("wrong dude")





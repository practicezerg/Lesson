"""Given an array of integers, return a new array with each value doubled."""
def maps(a):
    l = []
    for i in a:
        i = i * 2
        l.append(i)
    return l


a = [1, 2, 3]
print(maps(a))

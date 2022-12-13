def max_digit(value):
    l = []
    value = str(value)
    for i in value:
        l.append(i)
    print(l)
    return int(max(l))


value = 0
res = max_digit(value)
print(res)
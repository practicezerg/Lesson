# a = [15, -3.2, 2.2, 151, -36363, 11123]
# for item in a:
#     print(item+2)
# print(a)

# если нужно прибавть и перезаписать лист
a = [15, -3.2, 2.2, 151, -36363, 11123]
for i in [0, 1, 2, 3, 4, 5]:  #если чисел много можго через len   range(len(a))
    a[i] = a[i] + 2

print(a)


r = range(10)
print(r)
for i in r:
    print(i)

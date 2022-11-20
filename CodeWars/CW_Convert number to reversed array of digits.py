"""35231 => [1,3,2,5,3]
0 => [0]  развернуть в обратном порядке"""


num = 35231
len(str(num))
l = []
x = -1
l_revers = []
for i in str(num):
    l.append(i)
print(l)
for i in l:
    l_revers.insert(x, int(i))
    x -= 1
print(l_revers)


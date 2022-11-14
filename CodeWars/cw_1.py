p0 = 1000

percent = 2
print(percent / 100)
aug = 50
p = 1200
n = 0
l = aug + int(p0 * (percent / 100))
print(l)
while p0 < p:
    l = int(aug + p0 * (percent / 100))
    p0 = p0 + l
    print(p0)
    n += 1
print(n)
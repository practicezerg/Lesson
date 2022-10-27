
text = input("=  ")
big = []
small = []
a = 0
for i in text:
    print(text[a : a + 1].isupper())
    xz = text[a : a + 1].isupper()
    a += 1
    if xz == True:
        big.append(i)
        print(big)
    else:
        small.append(i)
        print(small)
print(len(small))
print(len(big))
if len(small) >= len(big):
    print(text.lower())
else:
    print(text.upper())




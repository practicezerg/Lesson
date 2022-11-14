"""a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"""

def longest(a1, a2):
    a = ""
    for i in a1:
        if i not in a:
            a = a[0:] + i
    for i in a2:
        if i not in a:
            a = a[0:] + i
    a = sorted(a)
    a = "".join(a)
    return a

a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"
print(longest(a1, a2))
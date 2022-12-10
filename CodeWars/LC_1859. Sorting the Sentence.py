def sortSentence(s):
    l = s.split()
    print(l)
    print(len(l))
    n = 0
    s_res = ""
    while n < len(l):
        for i in l:
            x = i[-1]
            if int(x) == len(l):
                i = i.replace(i[-1], "")
            else:
                i = i.replace(i[-1], " ")
            if int(x) == n + 1:
                s_res = s_res + i
                n += 1
    return s_res

s = "is2 sentence4 This1 a3"
s = sortSentence(s)
print(s)
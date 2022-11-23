def no_space(x):
    x2 = ""
    for i in x:
        if i != " ":
            x2 = x2 + i
    return x2
def no_space2(x):
    return x.replace(" ", "")

x = '8 j 8   mBliB8g  imjB8B8  jl  B'
print(no_space(x))
print(no_space2(x))



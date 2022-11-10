
def sum_numbers(text):
    b = text.split(" ")
    g = 0
    print(b)
    for i in b:
        try:
            i = int(i)
            g += i
        except:
            pass
    return g


text = "This picture is an oil on canvas painting by Danish artist Anna Petersen between "
g = sum_numbers(text)
print(g)

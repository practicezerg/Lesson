def descending_order(num):
    num1 = str(num)
    list_num = []
    for i in num1:
        list_num.append(i)
    b = sorted(list_num, reverse=True)
    c = "".join(b)
    num = int(c)
    return num



num = 42145
num_final = descending_order(num)
print(num_final)
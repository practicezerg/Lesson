# my_str = '01234567890'
# print(my_str.endswith('0123', 0,4))
# print(my_str.endswith("0"))

# lst = ([1,2,3,4,5])
# lst2 = []
# x = 0
# print(lst2)
# print(lst[0], ",take carteg")
# for i in lst:
#     i = -i
#     lst.replace(lst[x],i)
#     lst2.append(i)
#     x += 1
# print(lst2)

list = ([1,2,3,4,5])
print(list[2])
x = 0
for i in list:
    list[x] = -i
    x += 1
    print(i)
print(list)

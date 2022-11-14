# list = [10, 2.13, 'square', 89, 'C', 'xerase', 'stepa']
# list2 = list.copy()
# list3 = list[:]
# list2.append("milk")
# list3.pop(2)
# print(list)
# print(list2)
# print(list3)
# =====================================
import random
def make_list():
    a = []
    b = []
    i = 0
    while i <= 10:
        a.append(random.randint(0, 5))
        b.append(random.randint(-5, 0))
        i += 1
    return a + b


sp = make_list()
sp = tuple(sp)
print(sp.count(0))
print(sp)

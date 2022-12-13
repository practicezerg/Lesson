"""You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city."""

def destCity(l):
    l2 = []
    l3 = []
    for i in l:
        l2.append(i[1])
        l3.append(i[0])
    for i in l2:
        count = l3.count(i)
        if count == 0:
            return i



l = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
res = destCity(l)
print(res)
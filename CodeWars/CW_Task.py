"""Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
Mind the input validation."""

def sum_array(arr):
    print(arr)
    l = list(arr)
    print(l)
    # a = arr.index(max(arr))
    a = max(arr)
    print(l.index(a))
    # l.remove(l.index(a))
    print(a)
    # b = min(arr)
    # l.remove(l.index(b))
    # print(b)
    print(l)
    # print(sum(l))

arr = {1, 1, 11, 2, 3}
arr = [arr]
print(arr)

print(arr2)
sum_array(arr)
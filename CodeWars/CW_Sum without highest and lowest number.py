"""Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
Mind the input validation."""


def sum_array(arr):
    pos = 0
    if arr == None:
        return 0
    for i in arr:
        pos += 1
    if pos <= 1:
        return 0
    low = min(arr)
    high = max(arr)
    for i in arr:
        if i == low:
            index = arr.index(i)
            arr.pop(index)
    for i in arr:
        if i == high:
            index2 = arr.index(i)
            arr.pop(index2)
    return sum(arr)

# arr =  [6, 2, 1, 8, 10]
# arr =  [1, 1, 11, 2, 3]
arr = [15, 66]
a = sum_array(arr)
print(a)
# ==========================================================

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


# arr =  [6, 2, 1, 8, 10]
# arr =  [1, 1, 11, 2, 3]
arr = [15, 66]
a = sum_array(arr)
print(a)
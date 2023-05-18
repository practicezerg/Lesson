def updateSubrectangle(row1, col1, row2, col2, newValue):
    for i in range(row1, row2 + 1):
        for j in range(col1, col2 + 1):
            rectangle[i][j] = newValue



rectangle = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row1 = 1
col1 = 1
row2 = 2
col2 = 1
newValue = 5

res = updateSubrectangle(0, 0, 1, 1, 10)
print(res)
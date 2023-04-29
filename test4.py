def cellsInRange(s) :
    leftLetter = s.split(':')[0][0]
    leftDigit = int(s.split(':')[0][1])
    rightLetter = s.split(':')[1][0]
    rightDigit = int(s.split(':')[1][1])
    rowNumber = rightDigit - leftDigit + 1
    columnNumber = ord(rightLetter) - ord(leftLetter) + 1
    res = []
    for i in range(columnNumber):
        for j in range(rowNumber):
            res.append(chr(ord(leftLetter) + i) + str(leftDigit + j))
    return res


s = "U7:X9"
res = cellsInRange(s)
print(res)
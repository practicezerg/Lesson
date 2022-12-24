"""Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain."""

def balancedStringSplit(s):
    count_R = 0
    count_L = 0
    res = 0
    for i in s:
        if i == "R":
            count_R += 1
            if count_R == count_L:
                res += 1
        else:
            count_L += 1
            if count_R == count_L:
                res += 1
    if res == 0:
        res += 1
    return res



s = "RLLLLRRRLR"
res = balancedStringSplit(s)
print(res)
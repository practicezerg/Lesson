"""
Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36."""


def getLucky(self, s: str, k: int) -> int:
    alfa = "abcdefghijklmnopqrstuvwxyz"
    str_num = ""
    for i in s:
        str_num = str_num + str(alfa.index(i) + 1)
    l = []
    for i in str_num:
        l.append(i)
    while 1 <= k <= 10:
        sum = 0
        for i in l:
            sum = sum + int(i)
        k -= 1
        l.clear()
        for i in str(sum):
            l.append(i)
    return sum
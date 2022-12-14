"""The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise."""

def isSumEqual(firstWord, secondWord, targetWord):
    string_ideal = "abcdefghij"
    num2 = ""
    print(string_ideal.find("a"))
    num1 = ""
    num3 = ""
    for i in firstWord:
        num1 = num1 + str(string_ideal.find(i))
    for i in secondWord:
        num2 = num2 + str(string_ideal.find(i))
    for i in targetWord:
        num3 = num3 + str(string_ideal.find(i))
    print(num1, num2, num3)
    if int(num1) + int(num2) == int(num3):
        return True
    else:
        return False



firstWord, secondWord, targetWord = "j", "j", "bi"
res = isSumEqual(firstWord, secondWord, targetWord)
print(res)


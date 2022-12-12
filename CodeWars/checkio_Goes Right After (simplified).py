"""This is the simplified version of Goes Right After mission.
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same - your function should return False.
Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.
Output: A boolean."""


def goes_after(str, first, second):
    num_first = str.find(first)
    num_second = str.find(second)
    if num_first + 1 == num_second:
        return True
    else:
        return False


str = "world"
first =  "w"
second = "o"
res = goes_after(str, first, second)
print(res)
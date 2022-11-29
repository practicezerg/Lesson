"""Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between."""


def number(lines):
    n = 0
    l2 = []
    for i in lines:
        # n = str(n + 1)
        l2.append(("{}: ").format(str(n + 1)) + i)
        n += 1
    return l2


lines = ["a", "b", "c"]
a = number(lines)
print(a)

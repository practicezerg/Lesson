# my_str = '01234567890'
# print(my_str.endswith('0123', 0,4))
# print(my_str.endswith("0"))

string_ = ("What are you, a communist?")
string_ = list(string_)
print(string_)
#a i o e u
for qq in string_:
    if qq == "i" or qq == "a" or qq == "o" or qq == "e" or qq == "u" or qq == "I" or qq == "A" or qq == "O" or qq == "E" or qq == "U":
        string_.remove(qq)
    else:
        continue
string_ = "".join(string_)
print(string_)
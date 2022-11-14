# text = "greetings, friends"
text = "Greetings, friends."
print(text[0])
if text[0].isupper() == True:
    if text[-1] == ".":
        print(text)
    else:
        text = text + "."
        print(text)
else:
    big_str = text[0].title()
    print(big_str)
    text = big_str + text[1:]
    print(text)
    if text[-1] == ".":
        print(text)
    else:
        text = text + "."
        print(text)
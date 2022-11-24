a = "Wha3343t is >apple<фывфы чячя фыфывфы ййцуйцу цу?%*№ВАЫв  ав123ААФ333"
b = ""
for i in a:
    if i.isalpha() == False:
        if i == " ":
            b = b + i
    else:
        b = b + i


print(b)
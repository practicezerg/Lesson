# уйти от интер в качестве подтверждения ввода
# цветной вывод
# чистка экрана
def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

text = "stop SPAM"
colored_text = colored(255, 0, 0, text)
print(colored_text)

a = colored(0, 127, 255, input(colored(0, 255, 0, "Введите символ ==    ")))
b = colored(0, 0, 255, " param pam pam ")
c = colored(255, 237, 0, "tratatata")
g = a + b + c
print(a, "Тут будет цветной вывод")
print(b,"Тут будет цветной вывод2")
print(c,"Тут будет цветной вывод3")
print(g,"Тут будет цветной вывод3")


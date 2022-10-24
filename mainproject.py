import random
psw = '' # предварительно создаем переменную psw
for x in range(18):
    psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
print(psw)

# from random import random
print(random())


# Понадобится рандомный день месяц год
# случайная страна страна
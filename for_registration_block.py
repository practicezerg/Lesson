"""цель шаблонизировать и дергать от сюда данные которые нужны при всяких регистрациях"""
import random
import names

def password():
    random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    random_string2 = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+'
    psw = ''  # предварительно создаем переменную psw
    for x in range(18):
        psw = psw + random.choice(list(random_string))
        psw2 = psw + random.choice(list(random_string2))
    return psw, psw2


def name():
    name = names.get_full_name().split()
    first_name = name[0]
    second_name = name[1]
    return first_name, second_name


def mail(second_name):
    random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    suffix = ""
    for x in range(4):
        suffix = suffix + random.choice(list(random_string))
    email = second_name + suffix +  "@gmail.com"
    login = second_name + suffix
    return email, login

def bithday():
    BirthDay = random.randint(1, 29)
    BirthMonth = random.randint(1, 12)
    BirthYear = random.randint(1980, 2003)
    return BirthDay, BirthMonth, BirthYear

def main():
    psw, psw2 = password()
    BirthDay, BirthMonth, BirthYear = bithday()
    first_name, second_name = name()
    email, login = mail(second_name)
    print(f"login = {login}")
    print(f"psw = {psw}\n"
          f"psw2 = {psw2}")
    print(f"login = {email}")

main()

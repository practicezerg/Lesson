import requests
import random
import names

def registration():
    random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    psw = '' # предварительно создаем переменную psw
    for x in range(18):
        psw = psw + random.choice(list(random_string))
    name = names.get_full_name().split()
    first_name = name[0]
    second_name = name[1]
    email_add = ""
    for i in range(5):
        email_add = email_add + random.choice(list(random_string))
    email = second_name + email_add + "@gmail.com"
    username = second_name + email_add
    return first_name, second_name, psw, email, username

first_name, second_name, psw, email, username = registration()
print(first_name)
print(second_name)
print(psw)
print(email)
print(username)
confirm_psw = psw
# data = requests.get("https://www.upperdeckepack.com/Registration")
# if data.status_code == 200:
#     print('Success!')
# elif data.status_code == 404:
#     print('Not Found.')
# print(data.text)
# param = {}
# try1 = requests.post("", param)
# print(try1.text)
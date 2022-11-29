import time
import random
import requests
import fake_useragent


def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


login, password = pass_txt()
user = fake_useragent.UserAgent().random
# data = requests.get("https://www.upperdeckepack.com/Collection")
# if data.status_code == 200:
#     print('Success!')
# elif data.status_code == 404:
#     print('Not Found.')
param = {
    "email": login,
    "password": password,
    "rememberMe": "true",
    "twoFactorCode": "",
    "site": "https://www.upperdeckepack.com/",
    "platform": "ePack"
}
try1 = requests.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", param)
print(try1.text)
num1 = try1.text.find("Token\":")
num2 = try1.text.find("Remember")
user_token = (try1.text[20:54])
print(user_token)
param2 = {
    "token": user_token,
    "rememberMe": "true"
}
headers = {
    "user-agent" : user
}
"""добвить хеадерсы и userAgent and cookies"""
try2 = requests.post("https://www.upperdeckepack.com/api/User/LoginWithToken", param2)
print(try2.text)

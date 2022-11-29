import time
import random
import requests
import useragent as useragent



def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


session = requests.Session()
login, password = pass_txt()
user = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
headers = {
    "User-Agent": user

}
param = {
    "email": login,
    "password": password,
    "rememberMe": "true",
    "twoFactorCode": "",
    "site": "https://www.upperdeckepack.com/",
    "platform": "ePack"
}

res = session.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", data=param, headers=headers).text

profile_info = "https://www.upperdeckepack.com/Dashboard"
profile_res = session.get(profile_info).text
print(res, "res")

cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
    for key in session.cookies
]
session2 = requests.Session()
for cookies in cookies_dict:
    session2.cookies.set(**cookies)

res1 = session.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", data=param)
print(res1.text, "res1")
num1 = res1.text.find("Token\":")
num2 = res1.text.find("Remember")
user_token = (res1.text[20:54])
print(user_token)
headers = {
    "User-Agent": user,
    "Token": user_token
}

try2 = session2.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", data=param, headers=headers)
print(try2.text)
try3 = session2.get(profile_info, data=param, headers=headers)
print(try3.text)




#
# # data = requests.get("https://www.upperdeckepack.com/Collection")
# # if data.status_code == 200:
# #     print('Success!')
# # elif data.status_code == 404:
# #     print('Not Found.')
#
# try1 = requests.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", param)
# print(try1.text)

# param2 = {
#     "token": user_token,
#     "rememberMe": "true"
# }
#
# """добвить хеадерсы и userAgent and cookies"""
# try2 = requests.post("https://www.upperdeckepack.com/api/User/LoginWithToken", param2)
# print(try2.text)